# gg-skills

Hermes Agent 自定义 Skill 合集。

## 命名规范

- `gg-*` — 原创skill
- `third-party/` — 第三方skill

## Skills

| Skill | 说明 |
|-------|------|
| [gg-yunzhijia-knowledge](./gg-yunzhijia-knowledge/) | 云之家知识问答。覆盖产品功能、API开发、实施交付三域，294个知识文件，支持多维度检索。 |

## 安装

```bash
# 单个skill安装
cp -r gg-yunzhijia-knowledge ~/.hermes/skills/

# 或用 hermes CLI（如已支持）
hermes skill install https://github.com/<username>/gg-skills/tree/main/gg-yunzhijia-knowledge
```
