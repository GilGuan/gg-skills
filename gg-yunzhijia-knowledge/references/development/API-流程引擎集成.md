---
domain: development
module: 流程引擎
keywords: [accessToken, appId, token, 任务, 回调]
---

## 流程引擎集成

统一流程中心-流程引擎集成

简介

流程引擎集成方案适用于中小型或没有流程引擎的业务系统，如企业拥有一套采购系统，可通过链接或纯数据集成的方式将采购系统与智能审批实现无缝集成。其中链接集成方式开发工作量较小，直接嵌入业务系统的单据地址即可完成工作流集成，适用于大规模集成；纯数据集成方式可以保证用户一致的用户体验，用户查看的单据及流程都是智能审批原生的界面，该种开发工作量较大，一般适用于重要业务单据的集成。

流程引擎集成的方式由智能审批负责流程运转，业务系统负责发起流程和接收审批结果回调。业务系统与智能审批进行流程级别的集成，需要建立表单字段映射关系，映射关系统一在云之家进行维护，云之家提供查询映射关系的接口，业务系统先自行根据映射关系将数据映射为智能审批标准格式然后调用接口发起流程。

集成流程图:

集成流程

集成方式-流程引擎集成

链接集成

链接集成方式：单据完全引用业务系统中的表单，流程在智能审批中。业务系统可根据实际业务选择不同的展示方式，如网页端优先展示业务系统单据，移动端优先展示智能审批瀑布流原生布局格式。

链接集成

数据集成

纯数据集成方式：将业务系统的字段完全映射至智能审批模板字段，单据及流程都在智能审批中，适用于没有流程引擎的业务系统。

数据集成

全局事件管理

集中管理开发者选项，模板可直接引用全局事件，免去通用事件类型需要重复设置的烦恼。

模板引用全局事件

accessToken

点击此处查看如何获取accessToken

接口定义

查询映射关系

>http请求方法：post<br/>

请求头部：application/json<br/>

请求地址：https://www.yunzhijia.com/gateway/flowcenter/cloudflow/mapping/query?accessToken={accessToken}<br/>

请求参数说明：

请求参数示例：

{
	"typeId": "xxx"
}

返回结果示例：

{
	"success": true,
	"errorCode": 0,
	"error": null,
	"data": {
		"formCodeId": "xxx",
		"templateTitle": "请假测试模板",
		"mapping": [{
			"type": "textWidget",
			"subType": null,
			"codeId": "Te_0",
			"parentCodeId":null,
			"target": "form.reason"
		}]
	}
}

返回字段说明：

mapping字段说明：

创建流程实例

>http请求方法：post<br/>

请求头部：application/json<br/>

请求地址：https://www.yunzhijia.com/gateway/flowcenter/cloudflow/instance/create?accessToken={accessToken}<br/>

请求参数说明：

请求参数示例：

{
	"appId": "50011234",
	"mobileLink": "https://dev.kdweibo.cn/cloudflow/home/manage/approval-detail/5f0c0307fa10cc000154373c/5f0c03e9445de100011558c7/5f0c03e985fb520001784a23?appId=10104&from=approval-approved",
	"webLink": "https://dev.kdweibo.cn/cloudflow/home/manage/approval-detail/5f0c0307fa10cc000154373c/5f0c03e9445de100011558c7/5f0c03e985fb520001784a23?appId=10104&from=approval-approved",
	"mobileViewPreference": "native",
	"webViewPreference: "link",
	"formCodeId": "28296a3a98714090850f9e7fd4a41281",
	"creator": "5efac2fae4b04c5998b19859",
	"widgetValue": {
		"_S_TITLE": "请假流程测试"
	}
}

返回结果示例：

{
	"success": true,
	"errorCode": 0,
	"error": null,
	"data": {
		"formDefId":"xxx", // 这次发起的表单模版唯一id
		"formInstId":"xxx", // 这次发起的表单实例唯一id
		"flowInstId":"xxx" // 这次发起的流程实例唯一id
	}
}

获取指定用户的已办任务总数

>http请求方法：post<br/>

请求头部：application/json<br/>

请求地址：https://www.yunzhijia.com/gateway/flowcenter/cloudflow/task/done/count?accessToken={accessToken}<br/>

请求参数说明：

请求参数示例：

{
	"owner": "xxx",
    "appId": "xxx"
}

返回结果示例：

{
	"success": true,
	"errorCode": 0,
	"error": null,
	"data": 200 // 已办任务总数
}

获取指定用户的待办任务总数

>http请求方法：post<br/>

请求头部：application/json<br/>

请求地址：https://www.yunzhijia.com/gateway/flowcenter/cloudflow/task/todo/count?accessToken={accessToken}<br/>

请求参数说明：

请求参数示例：

{
	"owner": "xxx",
    "appId": "xxx"
}

返回结果示例：

{
	"success": true,
	"errorCode": 0,
	"error": null,
	"data": 200 // 待办任务总数
}

获取指定用户的已办列表

>http请求方法：post<br/>

请求头部：application/json<br/>

请求地址：https://www.yunzhijia.com/gateway/flowcenter/cloudflow/task/done/list?accessToken={accessToken}<br/>

请求参数说明：

请求参数示例：

{
	"appId": "xx",
    "owner": "xxx",
    "pageNumber": 1,
    "pageSize": 20
}

返回结果示例：

{
	"success": true,
	"errorCode": 0,
	"error": null,
	"data": {
        "total": "300",
        "list": [
        	{
            	"flowInstId": "xxx",
                "title": "xxx",
                "formInstId": "xxx",
                "formCodeId": "xxx"
            }
        ]
    }
}

data字段说明：

list字段说明：

获取指定用户的待办列表

>http请求方法：post<br/>

请求头部：application/json<br/>

请求地址：https://www.yunzhijia.com/gateway/flowcenter/cloudflow/task/todo/list?accessToken={accessToken}<br/>

请求参数说明：

请求参数示例：

{
	"appId": "xx",
    "owner": "xxx",
    "pageNumber": 1,
    "pageSize": 20
}

返回结果示例：

{
	"success": true,
	"errorCode": 0,
	"error": null,
	"data": {
        "total": "300",
        "list": [
        	{
            	"flowInstId": "xxx",
                "title": "xxx",
                "formInstId": "xxx",
                "formCodeId": "xxx"
            }
        ]
    }
}

data字段说明：

list字段说明：

获取指定用户的已阅总数

>http请求方法：post<br/>

请求头部：application/json<br/>

请求地址：https://www.yunzhijia.com/gateway/flowcenter/cloudflow/carboncopy/read/count?accessToken={accessToken}<br/>

请求参数说明：

请求参数示例：

{
	"owner": "xxx",
    "appId": "xxx"
}

返回结果示例：

{
	"success": true,
	"errorCode": 0,
	"error": null,
	"data": 200 // 已阅总数
}

获取指定用户的待阅总数

>http请求方法：post<br/>

请求头部：application/json<br/>

请求地址：https://www.yunzhijia.com/gateway/flowcenter/cloudflow/carboncopy/unread/count?accessToken={accessToken}<br/>

请求参数说明：

请求参数示例：

{
	"owner": "xxx",
    "appId": "xxx"
}

返回结果示例：

{
	"success": true,
	"errorCode": 0,
	"error": null,
	"data": 200 // 待阅总数
}

获取指定用户的已阅列表

>http请求方法：post<br/>

请求头部：application/json<br/>

请求地址：https://www.yunzhijia.com/gateway/flowcenter/cloudflow/carboncopy/read/list?accessToken={accessToken}<br/>

请求参数说明：

请求参数示例：

{
	"appId": "xx",
    "owner": "xxx",
    "pageNumber": 1,
    "pageSize": 20
}

返回结果示例：

{
	"success": true,
	"errorCode": 0,
	"error": null,
	"data": {
        "total": "300",
        "list": [
        	{
            	"flowInstId": "xxx",
                "title": "xxx",
                "formInstId": "xxx",
                "formCodeId": "xxx"
            }
        ]
    }
}

data字段说明：

list字段说明：

获取指定用户的待阅列表

>http请求方法：post<br/>

请求头部：application/json<br/>

请求地址：https://www.yunzhijia.com/gateway/flowcenter/cloudflow/carboncopy/unread/list?accessToken={accessToken}<br/>

请求参数说明：

请求参数示例：

{
	"appId": "xx",
    "owner": "xxx",
    "pageNumber": 1,
    "pageSize": 20
}

返回结果示例：

{
	"success": true,
	"errorCode": 0,
	"error": null,
	"data": {
        "total": "300",
        "list": [
        	{
            	"flowInstId": "xxx",
                "title": "xxx",
                "formInstId": "xxx",
                "formCodeId": "xxx"
            }
        ]
    }
}

data字段说明：

list字段说明：

--- 文档抓取完成 ---

参数 | 类型 | 是否必须 | 说明

typeId | String | 是 | 业务系统模板id

参数 | 类型 | 说明

formCodeId | String | 审批模板codeId

templateTitle | String | 审批模板标题

mapping | Array | 字段映射关系

参数 | 类型 | 说明

type | String | 审批字段类型

subType | String | 审批字段子类型(比如选人字段有单选和多选的区别)

codeId | String | 审批字段codeId

parentCodeId | String | 审批父控件codeId，只有明细表字段才有值

target | String | 用户配置字段映射规则

参数 | 类型 | 是否必须 | 说明

appId | String | 否 | 业务系统对应的轻应用appId，用于按业务系统区分流程实例数据

mobileLink | String | 否 | 移动端表单详情页面链接地址

webLink | String | 否 | 网页端表单详情页面链接地址

mobileViewPreference | String | 否 | 移动端表单详情页面优先展示模式，native=优先展示审批原生页面，link=优先展示链接地址

webViewPreference | String | 否 | 移动端表单详情页面优先展示模式，native=优先展示审批原生页面，link=优先展示链接地址

skipWidgetAuthorityCheck | boolean | 否 | 是否跳过节点字段权限校验，默认为false

justDraft | boolean | 否 | 是否仅存为草稿，默认为false

useAlias | boolean | 否 | 是否使用别名(字段中文名)，默认为false

resubmit | boolean | 否 | 退回或撤回到发起节点后是否允许在审批中重新发起，默认为false

formCodeId | String | 是 | 审批表单模板codeId

creator | String | 是 | 流程发起人openid

widgetValue | Object | 是 | 主表单字段键值对，key为字段codeId，value为字段值

details | Object | 是 | 明细表，key为明细表字段codeId，value为明细表键值对数组

参数 | 类型 | 是否必须 | 说明

owner | String | 是 | 指定用户的openid

appId | String | 否 | 如果指定了appId则表示查询指定业务系统的已办总数

参数 | 类型 | 是否必须 | 说明

owner | String | 是 | 指定用户的openid

appId | String | 否 | 如果指定了appId则表示查询指定业务系统的已办总数

参数 | 类型 | 是否必须 | 说明

appId | String | 否 | 如果指定了appId则表示获取指定业务系统的已办任务列表

owner | String | 是 | 指定用户的openid

pageNumber | int | 是 | 页码，从1开始，必须为正整数

pageSize | int | 否 | 每页数据量，必须为正整数，默认为50

参数 | 类型 | 说明

total | int | 数据总量

list | Array | 数据列表

参数 | 类型 | 说明

flowInstId | String | 流程实例id

title | String | 流程标题

formInstId | String | 表单实例id

formCodeId | String | 表单模板codeId

参数 | 类型 | 是否必须 | 说明

appId | String | 否 | 如果指定了appId则表示获取指定业务系统的已办任务列表

owner | String | 是 | 指定用户的openid

pageNumber | int | 是 | 页码，从1开始，必须为正整数

pageSize | int | 否 | 每页数据量，必须为正整数，默认为50

参数 | 类型 | 说明

total | int | 数据总量

list | Array | 数据列表

参数 | 类型 | 说明

flowInstId | String | 流程实例id

title | String | 流程标题

formInstId | String | 表单实例id

formCodeId | String | 表单模板codeId

参数 | 类型 | 是否必须 | 说明

owner | String | 是 | 指定用户的openid

appId | String | 否 | 如果指定了appId则表示查询指定业务系统的已阅总数

参数 | 类型 | 是否必须 | 说明

owner | String | 是 | 指定用户的openid

appId | String | 否 | 如果指定了appId则表示查询指定业务系统的待阅总数

参数 | 类型 | 是否必须 | 说明

appId | String | 否 | 如果指定了appId则表示获取指定业务系统的已办列表

owner | String | 是 | 指定用户的openid

pageNumber | int | 是 | 页码，从1开始，必须为正整数

pageSize | int | 否 | 每页数据量，必须为正整数，默认为50

参数 | 类型 | 说明

total | int | 数据总量

list | Array | 数据列表

参数 | 类型 | 说明

flowInstId | String | 流程实例id

title | String | 流程标题

formInstId | String | 表单实例id

formCodeId | String | 表单模板codeId

参数 | 类型 | 是否必须 | 说明

appId | String | 否 | 如果指定了appId则表示获取指定业务系统的待阅列表

owner | String | 是 | 指定用户的openid

pageNumber | int | 是 | 页码，从1开始，必须为正整数

pageSize | int | 否 | 每页数据量，必须为正整数，默认为50

参数 | 类型 | 说明

total | int | 数据总量

list | Array | 数据列表

参数 | 类型 | 说明

flowInstId | String | 流程实例id

title | String | 流程标题

formInstId | String | 表单实例id

formCodeId | String | 表单模板codeId

---