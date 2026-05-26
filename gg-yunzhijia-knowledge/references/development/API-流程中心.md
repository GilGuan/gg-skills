---
domain: development
module: 流程引擎
keywords: [accessToken, appId, callback, token, 任务]
---

## 流程中心

流程中心

流程中心（**<font color="red">如未购买统一流程中心，请使用 通知中心+待审批 接口</font>**）

点击此处查看视频教程

概述

与待办通知的对比

必读

业务系统完成集成并正式上线后请勿再修改集成参数，尤其是AppId，否则可能导致统一流程中心的待办无法正常处理。

业务系统必须兼容云之家待办集成和统一流程中心集成的数据。比如业务系统原先集成了云之家待办，并且仍有一些待办数据未处理，此时业务系统从云之家待办集成切换为了流程中心集成，那么业务系统需要确保此时仍能正常处理切换流程中心以前已经产生的待办数据。如果不做此种兼容的话，将导致切换之前产生的待办数据在云之家无法成功转成已办（即使业务系统已经将此种待办转为了已办）。建议业务系统记录每条待办数据对应的集成方式(云之家待办还是统一流程中心)以及对应的appId，在处理待办时根据待办对应的集成方式进行相应处理。

业务系统必须兼容云之家待办集成和统一流程中心集成这两种方式的快捷审批。因为这两种集成方式下的快捷审批处理逻辑有一些差异，为确保兼容性，业务系统必须兼容这两种快捷审批方式。

考虑到接口和网络环境的稳定性，建议业务系统在调用统一流程中心的接口时做好容错处理，针对调用失败的情况做一定次数的重试，避免因为短暂的网络或接口故障导致业务系统与云之家的数据出现不一致的情况。

集成过程

初始化。业务系统首次接入统一流程中心时，调用"统一流程中心_初始化"接口执行初始化

业务系统发起流程。发起流程时，调用"统一流程中心_发送待办"接口给审批人发送待办

业务系统内部流程。流程运转时，根据审批、撤回、退回等操作调用相应接口更新统一流程中心数据状态

业务系统处理完毕。调用"统一流程中心_标记已完成"接口更新统一流程中心状态

业务系统集成过程：

业务系统发送待办过程：

业务系统处理待办过程：

统一流程中心SDK

戳我下载统一流程中心SDK

目前统一流程中心SDK(cloudflow-sdk)仅提供java版本，最低支持jdk1.5

下载cloudflow-sdk

添加jar包依赖到工程

添加fastjson依赖(groupId com.alibaba, artifact fastjson, version 1.2.9)

添加commons-codec依赖(groupId commons-codec, artiface commons-codec, version 1.10)

开始使用

SDK用法示例

// 配置
Configuration configuration = new Configuration();
configuration.setCloudflowAppId(xxx);
... // 初始化各种配置

// 获取FlowCenter实例，后续各种请求都依赖该实例
FlowCenter flowCenter = new FlowCenter(configuration);

// 发送待办
flowCenter.getSendTodoRequest()
                .addField(new SendTodoRequest.Field("金额", "100"))
                .addTodo(new SendTodoRequest.Todo(oid", bizId"))
               ... // 一系列参数设置
               .request(); // 触发请求
               
// 初始化模板
flowCenter.getInitRequest()
                .addField(new InitRequest.Field("姓名", InitRequest.Field.Type.TEXT_WIDGET))
                ... // 一系列参数设置
                .withWebUrl("https://w.com")
                .request(); // 触发请求

接口授权

原生集成accesstoken的scope为team。

点击此处查看如何获取accessToken

统一流程中心_初始化

说明：<font color="red">业务系统首次接入统一流程中心前一定要先执行初始化</font>。初始化过程首先根据appId和appName创建一个智能审批模板分类（如果该appId对应分类已经存在则不创建），然后使用typeName创建一个智能审批模板(模板图标随机），重复调用该接口将会对现有模板进行更新。该模板是一个原生集成模板，符合第三方模板的发起规则，用户点击模板发起审批时会跳转到对应的业务系统发起页面。如果一个业务系统需要创建多个模板分类，可以通过将集成模板转换为标准模板，然后在智能审批网页端手动调整分类。

>http请求方法：post<br/>

请求头部：application/json<br/>

请求地址：https://www.yunzhijia.com/gateway/flowcenter/native/init?accessToken={accessToken}<br/>

请求参数说明：

field字段说明：

注意：field字段在初始化接口里面以去重累加形式创建。即如果针对同一个typeId执行了多次初始化，那么该typeId对应的模板的字段是多次初始化所指定的字段去重后的累加。假设针对typeId=123的模板先执行初始化，指定了字段A、B，然后再执行初始化A、B、C，那么typeId=123对应的模板的字段为A、B、C。

请求参数示例：

{
    "buid": "xxxx",
    "typeId": "0a1ab",
    "typeName": "费用报销",
    "appId: "50001234",
    "appName": "EAS"
    "mobileUrl": "http://www.xxx.com",
    "webUrl": "https://www.xxx.com",
    "field": [
        {
            "title": "报销类型"
        },
        {
            "title": "报销金额",
            "type": "moneyWidget"
        },
        {
            "title": "报销时间"
        }
    ],
    "creator": "xxxx",
    "description": "这里是模板描述信息，可以填写一些简短描述性文字用以描述模板的用途"
}

返回结果示例：

{
	"success": true,
	"errorCode": 0,
	"error": null,
	"data": null
}

重要字段展示效果图：

模板注册效果图：

统一流程中心_发送待办

说明：集成核心接口，通过该接口能将业务系统流程数据集成到统一流程中心。系统首先会判断flowId是否已经存在对应的智能审批流程实例，若不存在则创建一个新的智能审批流程实例；然后根据activityId和activityName创建审批节点，并给approver指定的人员创建审批任务；同时针对该审批节点启动审批超时定时器（如果设置了超时规则的话）。

建议同一个节点审批人在同一个请求里面发送，不要分开请求调用，若同一个节点代办较多，分开发送代办有可能因并发太大未抢占到锁返回失败；当前接口是同步接口，若返回失败建议重试一到两次。

>http请求方法：post<br/>

请求头部：application/json<br/>

请求地址：https://www.yunzhijia.com/gateway/flowcenter/native/todo/send?accessToken={accessToken}<br/>

请求参数说明：

todo参数说明：

flowId、activityId、bizId三者之间的关系示意图（一个流程包含多个节点，一个节点包含多个任务）

field参数说明：

请求参数示例：

{
	"webLink": "https://dev.kdweibo.cn/cloudflow-mobile/approval/5edef8d74624080001cbb5fe/5edef93af13cfe000170fe83/5edef93a788d4a000151d662?opentype=111&from=approveNotice",
    "mobileLink": "https://dev.kdweibo.cn/cloudflow-mobile/approval/5edef8d74624080001cbb5fe/5edef93af13cfe000170fe83/5edef93a788d4a000151d662?opentype=111&from=approveNotice",
    "webFlowLink": "https://dev.kdweibo.cn/cloudflow-mobile/approval/5edef8d74624080001cbb5fe/5edef93af13cfe000170fe83/5edef93a788d4a000151d662?opentype=111&from=approveNotice",
    "appId": "10104",
    "todo":[
        {
        "bizId": "5edef94a788d4a000151d698",
        "approver": "5edef94a2eb8a00001b0607e"
        }
    ]
    "typeId": "5edef94a2eb8a00001b062ce",
    "urgency": 1,
    "processUrl": "https://dev.kdweibo.cn/cloudflow/quick-deal?id=5edef93a788d4a000151d662",
    "flowId": "5edef94a2eb8a00001b998ce",
    "title": "请假审批测试",
    "serialNo": "QJ-20200506-001",
    "creator": "5edef94a2eb8a00001b060de",
    "creatorOrgId": "5edef94a2eb8a00001b06881",
    "activityName": "直接主管审批",
    "activityId": "xxx",
    "ttl": 7200,
    "field": [
        {
        "name": "报销金额",
        "value": "9000"
        },
        {
        "name": "报销类型",
        "value": "项目出差"
        },
        {
        "name": "出差时间",
        "value": "2020-08-31"
        }
    ]
}

返回结果示例：

{
	"success": true,
	"errorCode": 0,
	"error": null,
	"data": 
}

快捷同意说明

快捷同意：只有指定了processUrl参数才可以在待办列表快捷处理该待办。处理逻辑为当用户点击快捷处理时将触发访问processUrl接口，业务系统在响应该接口后应当及时调用标记待办为已办接口将对应待办转为已办。processUrl接口调用说明：

url: http://www.xx.com/flow/deal?id=abcdefg
method: post
head: Content-Type: application/json
参数: 
{
    "param": {
        "eid": "xxx", // 企业eid
        "appId": "xxx", // 轻应用appId
        "openId": "xxx", // 当前操作人的openid
        "bizIds": [ // 待处理的任务bizId
            "bizId"
        ]
    },
    "sign": "xxx" // 签名，具体参考下方签名计算逻辑
}
超时: 5秒
返回: application/json
{
    "success": true, // true表示处理成功，false表示处理失败，必填
    "data":{
        "failed": [ // 处理失败的bizId列表，选填
            "bizId1",
            ...
        ]
    }
}

sign计算逻辑

将oid、appId，bizId全部放到一个list中

针对list进行字典序升序排序

将排序后的list的各元素按顺序用&符号拼接成一个字符串

对拼接字符串计算哈希值，算法为HmacSHA1，密钥为signKey。其中signKey在轻应用管理中心可以查到，每个轻应用都有对应的signKey。

链接跳转：当用户在待办列表、已办列表、我发起的、抄送我的、流程监控这几个列表点击流程时，系统将跳转到相应的链接地址，并会携带标识用户身份信息的参数(ticket)。比如webLink=https://www.xx.com?bizId=xxxx&appId=xxx，当用户在网页端待办列表点击该条待办时，系统将跳转到https://www.xx.com?bizId=xxx&appId=xxx&ticket=xxx，其中，ticket参数为系统拼接参数。

统一流程中心_发送抄送

说明：集成核心接口，通过该接口能将业务系统流程数据集成到统一流程中心。系统首先会判断flowId是否已经存在对应的智能审批流程实例，若不存在则创建一个新的智能审批流程实例；然后根据activityId和activityName创建审批节点，并给copyTo指定的人员创建抄送数据。

>http请求方法：post<br/>

请求头部：application/json<br/>

请求地址：https://www.yunzhijia.com/gateway/flowcenter/native/carboncopy/send?accessToken={accessToken}<br/>

请求参数说明：

copy参数说明：

field参数说明：

请求参数示例：

{
	"webLink": "https://dev.kdweibo.cn/cloudflow-mobile/approval/5edef8d74624080001cbb5fe/5edef93af13cfe000170fe83/5edef93a788d4a000151d662?opentype=111&from=approveNotice",
    "mobileLink": "https://dev.kdweibo.cn/cloudflow-mobile/approval/5edef8d74624080001cbb5fe/5edef93af13cfe000170fe83/5edef93a788d4a000151d662?opentype=111&from=approveNotice",
    "webFlowLink": "https://dev.kdweibo.cn/cloudflow-mobile/approval/5edef8d74624080001cbb5fe/5edef93af13cfe000170fe83/5edef93a788d4a000151d662?opentype=111&from=approveNotice",
    "appId": "10104",
    "copy":[
        {
        "bizId": "5edef94a788d4a000151d698",
        "copyTo": "5edef94a2eb8a00001b0607e",
        "manualConfirm":0
        }
    ]
    "typeId": "5edef94a2eb8a00001b062ce",
    "urgency": 1,
    "processUrl": "https://dev.kdweibo.cn/cloudflow/quick-deal?id=5edef93a788d4a000151d662",
    "flowId": "5edef94a2eb8a00001b998ce",
    "title": "请假审批测试",
    "serialNo": "QJ-20200506-001",
    "creator": "5edef94a2eb8a00001b060de",
    "creatorOrgId": "5edef94a2eb8a00001b06881",
    "activityName": "直接主管审批",
    "activityId": "xxx",
    "ttl": 7200,
    "field": [
        {
        "name": "报销金额",
        "value": "9000"
        },
        {
        "name": "报销类型",
        "value": "项目出差"
        },
        {
        "name": "出差时间",
        "value": "2020-08-31"
        }
    ]
}

返回结果示例：

{
	"success": true,
	"errorCode": 0,
	"error": null,
	"data": 
}

统一流程中心_删除待办

说明：删除指定待办。比如审批人执行了撤回操作，那下个审批人的待办可以调该接口进行删除。

>http请求方法：post<br/>

请求头部：application/json<br/>

请求地址：https://www.yunzhijia.com/gateway/flowcenter/native/todo/delete?accessToken={accessToken}<br/>

请求参数说明：

请求参数示例：

{
	"appId": "xxx",
    "bizId": [xxx]
}

返回结果示例：

{
	"success": true,
	"errorCode": 0,
	"error": null,
	"data": 
}

统一流程中心_标记待办为已办

说明：用于已处理场景。比如审批人已经在业务系统执行了审批同意操作，可以调用该接口将待办标记为已办。

*注意：当调用该接口将某待办标记为已办时，如果流程已经成功流转到下个节点，则应及时调用发送待办接口生成下个节点的待办任务*

>http请求方法：post<br/>

请求头部：application/json<br/>

请求地址：https://www.yunzhijia.com/gateway/flowcenter/native/todo/done?accessToken={accessToken}<br/>

请求参数说明：

请求参数示例：

{
	"appId": xxx,
    "bizId": [xxx]
}

返回结果示例：

{
	"success": true,
	"errorCode": 0,
	"error": null,
	"data": 
}

统一流程中心_标记抄送为已读

说明：当用户访问过对应的界面进行调用。

>http请求方法：post<br/>

请求头部：application/json<br/>

请求地址：https://www.yunzhijia.com/gateway/flowcenter/native/carboncopy/read?accessToken={accessToken}<br/>

请求参数说明：

请求参数示例：

{
	"appId": xxx,
    "bizId": [xxx]
}

返回结果示例：

{
	"success": true,
	"errorCode": 0,
	"error": null,
	"data": 
}

统一流程中心_删除流程

说明：当业务系统删除流程时触发调用。删除流程后将删除流程对应的待办和抄送。

>http请求方法：post<br/>

请求头部：application/json<br/>

请求地址：https://www.yunzhijia.com/gateway/flowcenter/native/instance/delete?accessToken={accessToken}<br/>

请求参数说明：

请求参数示例：

{
	"appId": xxx,
    "flowId": [xxx]
}

返回结果示例：

{
	"success": true,
	"errorCode": 0,
	"error": null,
	"data": 
}

统一流程中心_标记流程为已完成

说明：当业务系统流程完成时需要调用该接口将统一流程中心的流程也标记为已完成。

>http请求方法：post<br/>

请求头部：application/json<br/>

请求地址：https://www.yunzhijia.com/gateway/flowcenter/native/instance/finish?accessToken={accessToken}<br/>

请求参数说明：

请求参数示例：

{
	"appId": xxx,
    "flowId": [xxx]
}

返回结果示例：

{
	"success": true,
	"errorCode": 0,
	"error": null,
	"data": 
}

统一流程中心_标记流程为待发起

说明：当业务系统流程回到发起节点时，需要调用该接口将统一流程中心的流程也标记为待发起。

>http请求方法：post<br/>

请求头部：application/json<br/>

请求地址：https://www.yunzhijia.com/gateway/flowcenter/native/instance/reset?accessToken={accessToken}<br/>

请求参数说明：

请求参数示例：

{
	"appId": xxx,
    "flowId": [xxx]
}

返回结果示例：

{
	"success": true,
	"errorCode": 0,
	"error": null,
	"data": 
}

统一流程中心_注册待阅已读通知

说明：注册待阅已读通知接口，当标记全部为已读时将触发通知接口通知业务系统。待阅已读通知接口用于实现状态同步，将已读状态同步至业务系统。

>http请求方法：post<br/>

请求头部：application/json<br/>

请求地址：https://www.yunzhijia.com/gateway/flowcenter/native/carboncopy/addcallback?accessToken={accessToken}<br/>

请求参数说明：

请求参数示例：

{
	"appId": xxx,
    "callback": "http://xxx"
}

返回结果示例：

{
	"success": true,
	"errorCode": 0,
	"error": null,
	"data": 
}

待阅已读回调接口调用说明：

url: callback url
method: post
head: Content-Type: application/json
参数：
{
    "param": {
        "eid": "xxx", // 企业eid
   	 "appId": "xxx", // 轻应用appId
        "openId": "xxx", // 当前操作人的openid
        "bizId": [ // 抄送数据bizId
            "bizId"
        ]
    },
    "sign": "xxx" // 签名计算规则参考待办快捷同意
}
参数的含义为将指定appId下面的指定bizId的待阅标记为已读。
超时：5秒
返回：application/json
{
	"success": true
}

该通知接口的作用就是用来将已读状态通知到业务系统，只要正常接收到了通知业务系统就应该立即返回成功，业务系统内部的处理逻辑不应该影响回调接口的结果。

统一流程中心_存为草稿

说明：将流程存为草稿，存为草稿之后数据会出现在草稿箱。针对同一个流程(appId、flowId)可以多次调用存为草稿接口，多次调用存为草稿接口会更新单据字段，一旦某条草稿流程被发起之后则不允许再对该条流程调用存为草稿接口。

>http请求方法：post<br/>

请求头部：application/json<br/>

请求地址：https://www.yunzhijia.com/gateway/flowcenter/native/draft/save?accessToken={accessToken}<br/>

请求参数说明：

field参数说明：

请求参数示例：

{
    "webFlowLink": "https://dev.kdweibo.cn/cloudflow-mobile/approval/5edef8d74624080001cbb5fe/5edef93af13cfe000170fe83/5edef93a788d4a000151d662?opentype=111&from=approveNotice",
   "appId": "10104",
    "typeId": "5edef94a2eb8a00001b062ce",
	"urgency": 1,
	"flowId": "5edef94a2eb8a00001b998ce",
	"title": "请假审批测试",
	"serialNo": "QJ-20200506-001",
	"creator": "5edef94a2eb8a00001b060de",
	"creatorOrgId": "5edef94a2eb8a00001b06881",
    "field": [
    {
        "name": "报销金额",
        "value": "9000"
    }
    ]
}

返回结果示例：

{
	"success": true,
	"errorCode": 0,
	"error": null,
	"data": 
}

统一发起

如果只是要实现统一发起，需要满足如下3个条件

已经集成了云之家轻应用的单点登录

业务系统具有WEB端发起页面或移动端发起页面

已经购买了统一流程中心

满足上述3个条件后，简单配置即可实现统一发起入口的效果。配置步骤如下：

新建一个模板，并开启集成模式

切换到"从第三方模板接入"页签

配置appId、网页端、移动端的发起地址。这里appId是业务系统对应云之家轻应用的appId，发起地址填业务系统对应的web端、移动端发起页面的地址。

发布模板

配置效果图：

配置成功后，用户在智能审批的发起界面将看到这个模板，点击该模板时将跳转到对应的地址（从web端点击则打开web端发起地址，从移动端点击则打开移动端发起地址），同时会在地址后面携带一个ticket，业务系统通过解析该ticket可以获得当前操作的用户身份信息，解析过程请参考

根据ticket解析用户身份（单点登录）

注意，配置统一发起只是给业务系统提供一个统一的发起入口，用户直接从云之家智能审批发起审批的界面即可快捷进入各业务系统进行发起，但所有审批数据仍旧在业务系统。统一流程中心我发起的、待办、待阅里面并不能看到这些数据，如果需要在这些地方看到业务系统的数据，请按照统一流程中心-原生流程集成的方式进行接口级别的集成

错误码（errorCode）说明

1301001：代办任务不存在或已删除 （删除代办、标记代办为已办 若未找到代办会提示这个错误）

1301002：抄送不存在或已删除

1301003：流程不存在或已删除

1301004：同一个bizId代办已发送，不可以重复发送（当前存在同样的bizId的代办时会提示该错误）

1301005：同一个bizId抄送已发送，不可以重复发送 （当前存在同样的bizId的待阅时会提示该错误）

1301006：流程节点处理超时时间(ttl)不合法

FAQ

问：为什么我在业务系统看到这条任务显示已处理，在云之家却还显示待审批？

答：这种问题一般是因为业务系统没有成功调用标记待办为已办接口导致的，正常情况下用户审批了待办后，业务系统会主动调用云之家标记待办为已办的接口来将云之家的待办标记为已办。建议业务系统增加异常重试机制，在发现调用标记待办为已办接口失败后进行一定次数的重试。

问： 为什么在云之家没有看到对应的待办？

答：这种情况一般有2个原因：1是因为对接BUG，业务系统未向云之家用户发送对应待办，2是因为业务系统尝试调用发送待办的接口但没成功。第1种情况需要由业务系统梳理对接逻辑，确保在适当的时机要给对应用户发送待办，第2种情况需要由业务系统增加异常重试机制，在发现调用发送待办接口失败后进行一定次数的重试，尽可能地确保将待办送达云之家。

--- 文档抓取完成 ---

统一流程中心 | 待办通知

流程待办及通知 | API级调用推送待办通知，与应用类型无关 | 仅支持通知类或流程类中的一种待办

公共号 | 用户体验统一，一个公共号可覆盖所有流程系统 | 一个流程系统对应一个公共号，体验不一致

附加信息 | 附加标准原生流程数据 | 仅待办基础信息

业务分类审批 | 支持按多重业务维度筛选分类 | 仅支持按appId分类

搜索 | 支持多重维度搜索 | 仅支持标题搜索

应用 | 智能审批轻应用统一所有流程系统 | 一个流程对应一个轻应用，体验不一致

统一发起 | 支持在流程中心直接发起各个业务系统单据和流程 | 不支持

统一监控 | 支持在流程中心监控所有流程过程和流程结果 | 不支持

统一时效分析 | 支持对所有流程进行审批效率分析 | 不支持

参数 | 类型 | 是否必须 | 说明

buid | String | 否 | 业务系统模板所属业务单元，如有启用权限中心则该字段可用来对模板做业务单元隔离。这里应填云之家部门id（orgId），填其他无效值将导致在模板管理界面看不见该模板。不填则默认属于根组织

typeId | String | 是 | 业务系统模板标识，可以是任意值，用于表示一个特定的流程模板，后续发待办时将根据该id确定流程的类型。在同一个业务系统内不同模板应当使用不同的typeId。比如付款申请流程的typeId可以是FQSK，请假申请的typeId可以是QJSQ

typeName | String | 是 | 业务系统模板名称，可以是任意值，用于标识一个特定的流程模板名称。在同一个业务系统内不同模板应当使用不同的typeName。比如付款申请的typeName可以是付款申请流程，请假申请的typeName可以是请假申请流程

appId | String | 是 | 业务系统对应的云之家轻应用id，具体可用云之家轻应用管理员身份登录WEB端后在轻应用管理中心查询获得

appName | String | 是 | 流程中心对应模板所属分类的名称，一般可以填业务系统对应的云之家轻应用名称。对应分类创建后可以手动调整模板所属分类或分类名称

mobileUrl | String | 否 | 业务系统的发起页面链接地址（移动端），不填则表示该模板不支持从移动端发起且该模板在移动端不可见

webUrl | String | 否 | 业务系统的发起页面链接地址（网页端），不填则表示该模板不支持从web端发起且该模板在网页端不可见

field | Array | 否 | 自定义表单字段。将取前3个字段作为重要字段，最多支持50个自定义字段

creator | String | 是 | 模板创建人id，这里应填云之家openid

description | String | 否 | 模板描述信息，最多200个字

参数 | 类型 | 是否必填 | 说明

title | String | 是 | 字段标题，同一个typeId下面的字段title不应重复

type | String | 否 | 字段类型，目前支持：textWidget=单行文本字段，numberWidget=数字字段，moneyWidget=金额字段，textAreaWidget=多行文本字段，默认为textWidget

参数 | 类型 | 是否必须 | 说明

webLink | String | 是 | 点击该条待办后的跳转地址（web端）

mobileLink | String | 否 | 点击该条待办后的跳转地址（移动端），不传的话则移动端待办列表该条数据将被置灰不能点击

webFlowLink | String | 是 | 流程监控页面点击流程后的跳转地址(web端)

mobileFlowLink | String | 否 | 我发起的列表点击流程后的跳转地址（移动端），不传的话则移动端我发起的列表该条数据将被置灰不能点击

appId | String | 是 | 业务系统对应的云之家轻应用id

todo | Array | 是 | 审批信息

typeId | String | 是 | 业务系统模板id，对于同一个流程，每次发送待办都应该使用相同的typeId

urgency | int | 是 | 紧急程度，从1到5

processUrl | String | 否 | 快捷同意url，设置了该url后将出现快捷同意按钮，如果不设置则表示该条待办不支持快捷同意。必须确保该url能通过外网正常访问

flowId | String | 是 | 业务系统流程实例id，能唯一标识一条流程

title | String | 是 | 流程标题

serialNo | String | 否 | 流水号

field | Array | 否 | 字段值。针对针对同一个流程，首次发送待办时可以通过field字段指定表单字段的值，同一个流程实例后续发待办不需要传field参数

ignoreUnknownFields | boolean | 否 | 是否忽略并丢弃不存在的表单字段。值为true时，field数组里面传的表单字段若不存在，会自动忽略并丢弃；值为false时，若表单不存在会提示xx别名不存在 的异常。默认值为false

creator | String | 是 | 流程发起人openid

creatorOrgId | String | 否 | 流程发起人所属部门id，不填则默认为发起人主职部门

ttlType | String | 否 | 流程节点处理超时类型。传standard表示使用系统标准超时设置（排除非工作时间），传natural表示使用自然时间超时设，默认为空，即不启用超时。更多解释请参考智能审批节点超时设置。流程效率信息分析，依赖[统一流程中心]及[大数据流程效率门户]，购买后本选项方可生效。

ttl | int | 否 | 流程节点处理超时时间，单位为分钟。传值说明：-1：使用系统默认时间段作为超时时间段；>0：使用指定的时间作为超时时间；0：不启用超时

activityId | String | 是 | 业务系统流程节点id

activityName | String | 是 | 业务系统流程节点名称

参数 | 类型 | 是否必须 | 说明

approver | String | 是 | 审批人openid

bizId | String | 是 | 业务系统的待办id，用于唯一标识一条待办。针对一个特定的业务系统（appId），调用方应确保bizId的唯一性

messageMode | String | 否 | 任务消息模型，MODE_TITLE:仅标题（待办列表只显示标题），MODE_MESSAGE:仅消息（待办列表只显示消息），MODE_TITLE_MESSAGE:标题+消息（都显示，但标题优先）。未传值默认为：MODE_TITLE

messageContent | String | 否 | 审批任务消息内容，messageMode值为MODE_MESSAGE或MODE_TITLE_MESSAGE时生效，若消息内容为空默认显示标题

参数 | 类型 | 是否必须 | 说明

name | String | 是 | 字段名，即/gateway/flowcenter/native/init接口中的field参数的title字段

value | String | 是 | 字段值，数字、金额控件也传字符串格式的数字，比如"1000"

参数 | 类型 | 是否必须 | 说明

webLink | String | 是 | 点击该条待办后的跳转地址（web端）

mobileLink | String | 否 | 点击该条待办后的跳转地址（移动端）,不传的话则移动端待阅列表该条数据将被置灰不能点击

webFlowLink | String | 是 | 流程监控页面点击流程后的跳转地址(web端)

mobileFlowLink | String | 否 | 我发起的列表点击流程后的跳转地址（移动端），不传的话则移动端我发起的列表该条数据将被置灰不能点击

appId | String | 是 | 业务系统对应的云之家轻应用id

copy | Array | 是 | 抄送信息

typeId | String | 是 | 业务系统模板id，对于同一个流程，每次发送抄送都应该使用相同的typeId

urgency | int | 是 | 紧急程度，从1到5

flowId | String | 是 | 业务系统流程实例id，能唯一标识一条流程

title | String | 是 | 流程标题

serialNo | String | 否 | 流水号

field | Array | 否 | 字段值。针对针对同一个流程，首次发送待办时可以通过field字段指定表单字段的值，同一个流程实例后续发待办不需要传field参数

ignoreUnknownFields | boolean | 否 | 是否忽略并丢弃不存在的表单字段。值为true时，field数组里面传的表单字段若不存在，会自动忽略并丢弃；值为false时，若表单不存在会提示xx别名不存在 的异常。默认值为false

creator | String | 是 | 流程发起人openid

creatorOrgId | String | 否 | 流程发起人所属部门id，不填则默认为发起人主职部门

ttlType | String | 否 | 流程节点处理超时类型。传standard表示使用系统标准超时设置（排除非工作时间），传natural表示使用自然时间超时设，默认为空，即不启用超。具体解释请参考智能审批节点超时设置。流程效率信息分析，依赖[统一流程中心]及[大数据流程效率门户]，购买后本选项方可生效。

ttl | int | 否 | 流程节点处理超时时间，单位为分钟。当ttlType为standard时：-1：使用系统默认时间段作为超时时间段，>0：使用指定的时间作为超时时间。当ttlType为natural时：参数必须大于0，传0会进行业务报错。

activityId | String | 是 | 业务系统流程节点id

activityName | String | 是 | 业务系统流程节点名称

参数 | 类型 | 是否必须 | 说明

copyTo | String | 是 | 抄送人openid

bizId | String | 是 | 业务系统的抄送id，用于唯一标识一条抄送。针对一个特定的业务系统（appId），调用方应确保bizId的唯一性

messageMode | String | 否 | 任务消息模型，MODE_TITLE:仅标题（待阅列表只显示标题），MODE_MESSAGE:仅消息（待阅列表只显示消息），MODE_TITLE_MESSAGE:标题+消息（都显示，但标题优先）。未传值默认为：MODE_TITLE

messageContent | String | 否 | 待阅消息内容，messageMode值为MODE_MESSAGE或MODE_TITLE_MESSAGE时生效，若消息内容为空默认显示标题

manualConfirm | int | 否 | 是否手动确认标记已读？从云之家待阅列表查看单据详情时是自动标记为已读还是手动确认后标记为已读，1：手动确认标记已读，0：自动标记已读，默认值：0（未传该字段或填其他非定义内的值都取默认值）, 若是需在业务系统手动点确认才标记为已读，值传1（需业务系统调标记抄送为已读接口更新抄送状态）

参数 | 类型 | 是否必须 | 说明

name | String | 是 | 字段名，即/gateway/flowcenter/native/init接口中的field参数的title字段

value | String | 是 | 字段值，数字、金额控件也传字符串格式的数字，比如"1000"

参数 | 类型 | 是否必须 | 说明

appId | String | 是 | 业务系统对应的轻应用id

bizId | Array | 是 | 业务系统待办id

参数 | 类型 | 是否必须 | 说明

appId | String | 是 | 业务系统对应轻应用id

bizId | Array | 是 | 业务系统待办唯一id

参数 | 类型 | 是否必须 | 说明

appId | String | 是 | 业务系统对应轻应用id

bizId | Array | 是 | 业务系统待办唯一id

参数 | 类型 | 是否必须 | 说明

appId | String | 是 | 业务系统对应轻应用id

flowId | Array | 是 | 业务系统流程id

参数 | 类型 | 是否必须 | 说明

appId | String | 是 | 业务系统对应轻应用id

flowId | Array | 是 | 业务系统流程id

参数 | 类型 | 是否必须 | 说明

appId | String | 是 | 业务系统对应轻应用id

flowId | Array | 是 | 业务系统流程id

参数 | 类型 | 是否必须 | 说明

appId | String | 是 | 业务系统对应的轻应用id

callback | String | 否 | 待阅已读回调地址(必须是一个有效的http接口地址)。值为空时表示清除该回调。清除回调后将导致该应用的待阅已读状态无法在统一流程中心与业务系统之间同步

参数 | 类型 | 是否必须 | 说明

webFlowLink | String | 是 | 草稿列表中将使用该地址做跳转（web端）

mobileFlowLink | String | 否 | 草稿列表中将使用该地址做跳转（移动端）

appId | String | 是 | 业务系统对应的云之家轻应用id

typeId | String | 是 | 业务系统模板id

urgency | int | 是 | 紧急程度，从1到5

flowId | String | 是 | 业务系统流程id

title | String | 是 | 流程标题

serialNo | String | 是 | 流水号

field | Array | 否 | 字段值

ignoreUnknownFields | boolean | 否 | 是否忽略并丢弃不存在的表单字段。值为true时，field数组里面传的表单字段若不存在，会自动忽略并丢弃；值为false时，若表单不存在会提示xx别名不存在 的异常。默认值为false

creator | String | 是 | 草稿发起人openid

creatorOrgId | String | 是 | 草稿发起人部门id

参数 | 类型 | 是否必须 | 说明

name | String | 是 | 字段名，即/gateway/flowcenter/native/init接口中的field参数的title字段

value | String | 是 | 字段值，数字、金额控件也传字符串格式的数字，比如"1000"

---