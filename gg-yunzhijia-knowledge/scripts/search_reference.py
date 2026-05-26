#!/usr/bin/env python3
"""
云之家知识检索脚本（三域划分 + metadata + 多关键词 + 排除 + 智能模块提示）

支持：
  --domain    按知识域过滤（product/development/implementation）
  --module    按业务模块过滤（智能审批、智能考勤...）
  --mode and  多关键词AND搜索（默认）
  --mode or   多关键词OR搜索
  --exclude   排除包含指定关键词的文件
"""

import os
import re
import sys
import argparse
from pathlib import Path
from collections import defaultdict

SKILL_DIR = Path(__file__).parent.parent
REFERENCES_DIR = SKILL_DIR / "references"

DOMAINS = {
    "product": "产品知识（功能使用、FAQ、版本更新）",
    "development": "开发知识（API文档、SDK、客户端开发）",
    "implementation": "实施知识（配置指南、部署文档、数据迁移）",
}

# 关键词→模块优先级映射（搜索时自动提示）
KEYWORD_MODULE_HINTS = {
    "回调": ["流程引擎", "IM消息"],
    "callback": ["流程引擎", "客户端开发"],
    "accessToken": ["OAuth授权"],
    "token": ["OAuth授权"],
    "审批": ["智能审批", "流程引擎"],
    "考勤": ["智能考勤"],
    "打卡": ["智能考勤"],
    "门户": ["智能门户"],
    "IM": ["IM消息", "融合通讯"],
    "消息": ["IM消息"],
    "会议": ["智能会议", "文事会"],
    "公文": ["文事会"],
    "轻云": ["轻云"],
    "知识": ["知识中心"],
    "组织": ["组织人员"],
    "人员": ["组织人员"],
    "部门": ["组织人员"],
    "JSAPI": ["客户端开发"],
    "JS桥接": ["客户端开发"],
    "客户端": ["客户端开发"],
    "配置": ["智能审批", "智能考勤"],
}

def parse_frontmatter(content):
    """解析文件头的 YAML frontmatter"""
    if not content.startswith("---"):
        return {}
    
    end = content.find("---", 3)
    if end == -1:
        return {}
    
    fm_text = content[3:end].strip()
    meta = {}
    for line in fm_text.split("\n"):
        line = line.strip()
        if ":" in line:
            key, _, val = line.partition(":")
            key = key.strip()
            val = val.strip()
            # 解析 keywords: [a, b, c]
            if val.startswith("[") and val.endswith("]"):
                val = [v.strip() for v in val[1:-1].split(",")]
            meta[key] = val
    return meta

def matches_keywords(content_lower, keywords, mode):
    """
    检查内容是否匹配关键词
    keywords: list of str
    mode: "and" 或 "or"
    """
    if mode == "and":
        return all(kw.lower() in content_lower for kw in keywords)
    else:  # or
        return any(kw.lower() in content_lower for kw in keywords)

def matches_exclude(content_lower, exclude_keywords):
    """检查内容是否包含任何排除关键词"""
    return any(ex.lower() in content_lower for ex in exclude_keywords)

def get_module_hints(keywords):
    """根据搜索关键词推荐可能匹配的模块"""
    hints = []
    seen = set()
    for kw in keywords:
        kw_lower = kw.lower()
        for hint_kw, modules in KEYWORD_MODULE_HINTS.items():
            if hint_kw.lower() in kw_lower or kw_lower in hint_kw.lower():
                for m in modules:
                    if m not in seen:
                        hints.append(m)
                        seen.add(m)
    return hints

def search_references(keywords, domain="all", module=None, mode="and",
                      exclude=None, max_results=10, context_lines=5):
    """
    在指定知识域中搜索关键词
    
    Args:
        keywords: 搜索关键词列表（空格分隔的多个词）
        domain: 知识域过滤
        module: 业务模块过滤（匹配 metadata.module）
        mode: "and"（所有关键词都匹配）或 "or"（任一关键词匹配）
        exclude: 排除关键词列表（文件包含这些词则跳过）
        max_results: 最大返回结果数
        context_lines: 上下文行数
    """
    results = []
    excluded_files = []
    
    # 确定搜索目录
    if domain == "all":
        search_dirs = ["product", "development", "implementation"]
    else:
        search_dirs = [domain]
    
    for search_dir in search_dirs:
        target_dir = REFERENCES_DIR / search_dir
        if not target_dir.exists():
            continue
        
        for md_file in target_dir.glob("*.md"):
            try:
                content = md_file.read_text(encoding="utf-8")
            except Exception:
                continue
            
            # 解析 metadata
            meta = parse_frontmatter(content)
            
            # 模块过滤（基于 metadata）
            if module:
                file_module = meta.get("module", "")
                if module.lower() not in file_module.lower():
                    continue
            
            # 关键词匹配（跳过 frontmatter 区域）
            body_start = content.find("---", 3)
            if body_start != -1 and content.startswith("---"):
                body = content[body_start + 3:]
            else:
                body = content
            
            body_lower = body.lower()
            
            if not matches_keywords(body_lower, keywords, mode):
                continue
            
            # 排除关键词过滤
            if exclude and matches_exclude(body_lower, exclude):
                excluded_files.append(f"{md_file.name} ({meta.get('module', '')})")
                continue
            
            # 计算匹配数
            match_count = 0
            for kw in keywords:
                match_count += body_lower.count(kw.lower())
            
            # 提取匹配片段
            snippets = extract_snippets(body.split("\n"), keywords, context_lines)
            
            file_title = meta.get("module", md_file.stem)
            file_domain = meta.get("domain", search_dir)
            
            for snippet in snippets[:3]:
                results.append({
                    "domain": file_domain,
                    "module": meta.get("module", ""),
                    "file": md_file.name,
                    "title": file_title,
                    "snippet": snippet,
                    "match_count": match_count,
                })
    
    # 按匹配数排序
    results.sort(key=lambda x: x["match_count"], reverse=True)
    return results[:max_results], excluded_files

def extract_snippets(lines, keywords, context_lines):
    """提取匹配关键词的上下文片段"""
    kw_lowers = [kw.lower() for kw in keywords]
    
    match_positions = []
    for i, line in enumerate(lines):
        line_lower = line.lower()
        if any(kw in line_lower for kw in kw_lowers):
            match_positions.append(i)
    
    if not match_positions:
        return []
    
    # 合并相邻范围
    merged = []
    cur_start = match_positions[0] - context_lines
    cur_end = match_positions[0] + context_lines
    
    for pos in match_positions[1:]:
        r_start = max(0, pos - context_lines)
        r_end = min(len(lines) - 1, pos + context_lines)
        
        if r_start <= cur_end + 1:
            cur_end = max(cur_end, r_end)
        else:
            merged.append((max(0, cur_start), min(len(lines) - 1, cur_end)))
            cur_start = r_start
            cur_end = r_end
    
    merged.append((max(0, cur_start), min(len(lines) - 1, cur_end)))
    
    snippets = []
    for start, end in merged[:3]:
        snippets.append("\n".join(lines[start:end + 1]))
    
    return snippets

def format_results(results, excluded_files=None):
    output = []
    for i, r in enumerate(results, 1):
        module_tag = f" [{r['module']}]" if r['module'] else ""
        output.append(f"\n【结果 {i}】[{r['domain']}]{module_tag}")
        output.append(f"文件: {r['file']}")
        output.append(f"匹配数: {r['match_count']}")
        output.append("-" * 40)
        output.append(r["snippet"])
        output.append("-" * 40)
    
    if excluded_files:
        output.append(f"\n[已排除 {len(excluded_files)} 个文件]")
        for ef in excluded_files[:5]:
            output.append(f"  - {ef}")
        if len(excluded_files) > 5:
            output.append(f"  ... 还有 {len(excluded_files) - 5} 个")
    
    return "\n".join(output)

def main():
    parser = argparse.ArgumentParser(
        description="云之家知识检索（三域 + 多关键词 + 排除）",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
示例:
  # AND搜索（默认，所有关键词都要匹配）
  %(prog)s "审批 回调"
  %(prog)s "审批 回调" --domain development
  
  # OR搜索（任一关键词匹配）
  %(prog)s "审批 审批流" --mode or
  
  # 排除噪音关键词
  %(prog)s "回调" --domain development --exclude JSAPI qing.call
  
  # 按模块过滤
  %(prog)s "accessToken" --module OAuth授权
  %(prog)s "审批" --domain product --module 智能审批

知识域:
  product        产品知识
  development    开发知识
  implementation 实施知识
  all            全域（默认）
"""
    )
    
    parser.add_argument("query", help="搜索关键词（空格分隔多个词）")
    parser.add_argument("-d", "--domain",
                        choices=["product", "development", "implementation", "all"],
                        default="all", help="知识域 (默认: all)")
    parser.add_argument("-m", "--module", default=None, help="业务模块过滤（如：智能审批、OAuth授权）")
    parser.add_argument("--mode", choices=["and", "or"], default="and",
                        help="多关键词模式：and=全部匹配 or=任一匹配 (默认: and)")
    parser.add_argument("-e", "--exclude", nargs="+", default=None,
                        help="排除包含指定关键词的文件（如：--exclude JSAPI qing.call）")
    parser.add_argument("-n", "--max", type=int, default=10, help="最大返回结果数")
    parser.add_argument("-c", "--context", type=int, default=5, help="上下文行数")
    
    args = parser.parse_args()
    
    keywords = args.query.split()
    
    # 智能模块提示
    if not args.module:
        hints = get_module_hints(keywords)
        if hints:
            hint_str = ", ".join(hints[:3])
            print(f"[提示] 关键词可能与以下模块相关：{hint_str}")
            print(f"[提示] 使用 --module <模块名> 可精准过滤\n")
    
    results, excluded_files = search_references(
        keywords,
        domain=args.domain,
        module=args.module,
        mode=args.mode,
        exclude=args.exclude,
        max_results=args.max,
        context_lines=args.context,
    )
    
    if not results:
        mode_hint = "（AND模式：所有关键词都要匹配，可加 --mode or 放宽）" if args.mode == "and" and len(keywords) > 1 else ""
        domain_hint = f"（已限定 {args.domain} 域）" if args.domain != "all" else ""
        module_hint = f"（已限定模块：{args.module}）" if args.module else ""
        exclude_hint = f"（已排除：{', '.join(args.exclude)}）" if args.exclude else ""
        print(f"本地资料未找到匹配 '{args.query}' 的内容{domain_hint}{module_hint}{exclude_hint}{mode_hint}")
        
        # 给出模块建议
        if not args.module:
            hints = get_module_hints(keywords)
            if hints:
                print(f"\n建议尝试以下模块过滤：")
                for h in hints[:3]:
                    print(f"  --module {h}")
        
        print("\n可自行访问以下网站查阅：")
        print("  - 开放平台文档：https://open.yunzhijia.com/opendocs/#/")
        print("  - 产品手册（语雀）：https://yunzhijia.yuque.com/qhigp7/sat4a4/znsp")
        print("  - 问题合集（语雀）：https://yunzhijia.yuque.com/qhigp7/kfcpqh/znspqa")
        print("  - 金蝶社区：https://vip.kingdee.com/?productLineId=12")
        return
    
    print(format_results(results, excluded_files))

if __name__ == "__main__":
    main()