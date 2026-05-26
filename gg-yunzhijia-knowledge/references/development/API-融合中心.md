---
domain: development
module: 融合中心
keywords: [accessToken, secret, token, 任务, 融合]
---

## 融合中心

融合中心接口

融合中心接口

> 本页的接口使用 resGroupSecret 级别的 AccessToken。

请在 管理中心-系统设置-系统集成-资源授权 中找到 融合中心 的授权码， 然后调用系统接口换取 AccessToken。

如果您还不了解如何获取AccessToken，请点击此处

触发高级业务连接动作：星空企业版

URL：https://www.yunzhijia.com/gateway/linkcenter/linkrule/extapi/xingkong/trigger?accessToken=xxx

http请求方法：post

http内容类型：Content-Type:application/x-www-form-urlencoded

输入参数：

示例curl：

curl --location --request POST 'https://www.yunzhijia.com/gateway/linkcenter/linkrule/extapi/xingkong/trigger?accessToken=7xoew0nuv7r4kSlVUqmIj5jKI0eV22qv' \
--data-urlencode 'ruleId=67288ac11903da6d1a77f763' \
--data-urlencode 'billNo=cust001'

返回结果成功示例：

{
    "data": {
        "logId":"xxxxx",       // 异步执行日志id
        "taskStatus":"running" // 任务状态
    },
    "error": null,
    "errorCode": 0,
    "success": true
}

--- 文档抓取完成 ---

参数 | 类型 | 是否必须 | 注释

ruleId | String | 是 | 高级业务连接的动作id

billNo | String | 是 | 单据或基础资料的编码

---