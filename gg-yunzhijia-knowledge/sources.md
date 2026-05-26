# 资料源清单

## 内置资料结构（三域划分）

知识已按三域组织，匹配用户角色和问题类型：

### product 域 — 产品知识

| 类型 | 文件数 | 大小 |
|-----|-------|------|
| 功能使用指南 | 427 | ~587 KB |
| 版本更新记录 | 40 | ~396 KB |
| FAQ | 1 | ~39 KB |

**目录**：`references/product/`

**文件命名**：
- `功能-{模块名}-{功能名}.md` — 功能使用指南
- `更新-{年份}年{月份}月产品更新.md` — 版本更新
- `FAQ-产品常见问题.md` — 高频QA

### development 域 — 开发知识

| 类型 | 文件数 | 大小 |
|-----|-------|------|
| 服务端API | 37 | ~735 KB |
| Docsify线上API | 16 | ~215 KB |
| 开发指南 | 3 | ~137 KB |

**目录**：`references/development/`

**文件命名**：
- `API-{接口名}.md` — 服务端API文档
- `API-线上-{docsify路径}.md` — Docsify线上文档
- `开发-{类型}.md` — 开发指南（客户端、入门、门户卡片）

### implementation 域 — 实施知识

| 类型 | 文件数 | 大小 |
|-----|-------|------|
| 配置指南 | 38 | ~480 KB |
| 部署文档 | 1 | ~81 KB |

**目录**：`references/implementation/`

**文件命名**：
- `配置-{模块名}.md` — 模块配置指南
- `部署-{文档名}.md` — 部署实施文档

---

## 检索脚本

使用检索脚本按域精准搜索（仅本地检索，不访问外部网站）：

```bash
# product 域（产品功能）
python3 {skill_dir}/scripts/search_reference.py "关键词" --domain product

# development 域（API开发）
python3 {skill_dir}/scripts/search_reference.py "关键词" --domain development

# implementation 域（配置部署）
python3 {skill_dir}/scripts/search_reference.py "关键词" --domain implementation

# 全域搜索
python3 {skill_dir}/scripts/search_reference.py "关键词" --domain all
```

参数说明：
- `-d/--domain` — 知识域（product/development/implementation/all）
- `-n/--max` — 最大返回结果数（默认10）
- `-c/--context` — 上下文行数（默认5）

---

## 线上查阅入口（仅人工访问）

当本地资料未覆盖问题时，可提示用户自行访问：

| 网站 | URL | 适用场景 |
|-----|-----|---------|
| 开放平台文档 | https://open.yunzhijia.com/opendocs/#/ | API最新文档 |
| 产品手册（语雀） | https://yunzhijia.yuque.com/qhigp7/sat4a4/znsp | 功能使用指南 |
| 问题合集（语雀） | https://yunzhijia.yuque.com/qhigp7/kfcpqh/znspqa | 常见问题排查 |
| 金蝶社区 | https://vip.kingdee.com/?productLineId=12 | 社区问答 |