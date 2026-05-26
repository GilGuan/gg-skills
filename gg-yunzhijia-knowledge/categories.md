# 问题分类与知识域路由表

> 知识已按三域划分：product（产品）、development（开发）、implementation（实施）
> 使用检索脚本时指定 `--domain` 参数可精准定位

## product 域 — 产品知识

适用角色：CSM、客户、产品运营

关键词：功能使用、怎么用、如何操作、FAQ、版本更新、新功能

检索命令：
```bash
python3 {skill_dir}/scripts/search_reference.py "关键词" --domain product
```

### 智能审批

关键词：审批、流程、表单、审批流、抄送、转办、加签

检索范围：
- `product/功能-智能审批-*.md`
- `product/FAQ-产品常见问题.md`（搜索"审批"）

### 智能考勤

关键词：考勤、打卡、排班、请假、外出、加班

检索范围：
- `product/功能-智能考勤-*.md`
- `product/FAQ-产品常见问题.md`（搜索"考勤"）

### 智能门户

关键词：门户、首页、工作台、自定义、应用

检索范围：
- `product/功能-智能门户-*.md`

### 融合通讯（IM）

关键词：聊天、消息、群聊、单聊、语音、视频、会议

检索范围：
- `product/功能-融合通讯-*.md`

### 轻云

关键词：轻云、低代码、表单、应用搭建

检索范围：
- `product/功能-轻云-*.md`

### 文事会

关键词：公文、会议、纪要、文书

检索范围：
- `product/功能-文事会-*.md`

### 版本更新

关键词：版本、更新、新功能、2025、2026

检索范围：
- `product/更新-2025年*.md`
- `product/更新-2026年*.md`

---

## development 域 — 开发知识

适用角色：技术支持、开发人员、集成工程师

关键词：API、接口、开发、SDK、回调、Webhook、鉴权、Token、OAuth

检索命令：
```bash
python3 {skill_dir}/scripts/search_reference.py "关键词" --domain development
```

### OAuth授权

关键词：accessToken、token、鉴权、授权、OAuth2

检索范围：
- `development/API-获取accessToken.md`
- `development/API-线上-server-api_auth_oauth.md`

### 组织人员API

关键词：人员、部门、角色、组织架构、通讯录

检索范围：
- `development/API-人员.md`
- `development/API-部门.md`
- `development/API-角色.md`
- `development/API-获取人员组织数据.md`
- `development/API-线上-server-api_org_*.md`

### 消息API

关键词：消息、群组、聊天、推送、通知、订阅号

检索范围：
- `development/API-群组和消息.md`
- `development/API-消息发送.md`
- `development/API-消息卡片.md`
- `development/API-线上-server-api_im_*.md`

### 智能审批API

关键词：审批API、流程API、表单API、发起审批

检索范围：
- `development/API-智能审批API.md`
- `development/API-流程中心.md`

### 考勤API

关键词：考勤API、打卡API、排班API

检索范围：
- `development/API-新版智能考勤.md`
- `development/API-旧版智能签到.md`

### 客户端开发

关键词：JSAPI、JS桥接、H5、小程序、客户端

检索范围：
- `development/开发-客户端文档.md`
- `development/开发-门户卡片.md`
- `development/API-线上-client-*.md`

### 开发入门

关键词：开发入门、轻应用、机器人

检索范围：
- `development/开发-入门指南.md`
- `development/API-线上-tutorial_*.md`

---

## implementation 域 — 实施知识

适用角色：实施顾问、CSM、项目经理

关键词：配置、部署、实施、安装、初始化、上线、迁移、融合中心

检索命令：
```bash
python3 {skill_dir}/scripts/search_reference.py "关键词" --domain implementation
```

### 智能审批配置

关键词：审批配置、流程配置、表单配置

检索范围：
- `implementation/配置-智能审批.md`

### 智能考勤配置

关键词：考勤配置、考勤规则、排班配置

检索范围：
- `implementation/配置-智能考勤.md`
- `implementation/配置-智能考勤(新).md`

### 其他模块配置

关键词：会议配置、云邮配置、合同配置、工资条配置

检索范围：
- `implementation/配置-会议管理.md`
- `implementation/配置-云邮.md`
- `implementation/配置-合同管理.md`
- `implementation/配置-工资条.md`

### 部署与迁移

关键词：部署、实施、迁移、上线、融合中心

检索范围：
- `implementation/部署-实施交付.md`

---

## 跨域问题处理

部分问题需要跨域检索：

| 问题示例 | 检索策略 |
|---------|---------|
| "审批流程报错了" | 先搜 development（API报错），再搜 product（使用FAQ） |
| "考勤配置后客户用不了" | 先搜 implementation（配置），再搜 product（使用FAQ） |
| "审批功能有哪些新API" | 先搜 product（更新），再搜 development（API） |

全域搜索命令：
```bash
python3 {skill_dir}/scripts/search_reference.py "关键词" --domain all
```

---

## 本地无结果时的提示

当本地检索未找到答案时，提示用户自行访问以下网站：

| 网站 | URL | 适用场景 |
|-----|-----|---------|
| 开放平台文档 | https://open.yunzhijia.com/opendocs/#/ | API最新文档 |
| 产品手册（语雀） | https://yunzhijia.yuque.com/qhigp7/sat4a4/znsp | 功能使用指南 |
| 问题合集（语雀） | https://yunzhijia.yuque.com/qhigp7/kfcpqh/znspqa | 常见问题排查 |
| 金蝶社区 | https://vip.kingdee.com/?productLineId=12 | 社区问答 |