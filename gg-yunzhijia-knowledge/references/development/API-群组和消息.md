---
domain: development
module: IM消息
keywords: [IM, accessToken, appId, person, secret]
---

# 群组和消息

> 来源：开放平台线上文档 (https://open.yunzhijia.com/opendocs/docs/server-api/im/index.md)

# 群组和消息

点击此处查看[视频教程](https://vip.kingdee.com/school/208231333511333120)

## 接口授权

> 本页的接口使用 `resGroupSecret` 级别的 `AccessToken`。

请在 `管理中心-系统设置-系统集成-资源授权` 中找到 `IM服务` 的授权码， 然后调用系统接口换取 `AccessToken`。

如果您还不了解如何获取AccessToken，请<a href="docs.html#/server-api/auth/oauth" target="_blank">点击此处</a>

## 创建群组

**URL：** `https://www.yunzhijia.com/gateway/xtinterface/group/createGroup?accessToken=xxx`

**请求方法：**  `POST`

**内容类型：** `Content-Type: application/json`

**输入参数说明：**

| 字段            | 类型       |  必须      | 说明                          |
|----------------|------------|-----------|------------------------------ |
| currentUid     | String     | 是        | 创建者的用户openId                  |
| groupName      | String     | 否        | 组名称 如果不指定会以参与人作为组名 |
| userIds        | Array      | 是        | 除了创建者的其它组员openId            |

**json示例：**

```json
{
    "groupName": "讨论组",
    "currentUid":"5b503ee9e4b02abb5318b23e", //用户openId
    "userIds":[
        "5b6cea82e4b05df05b3efc2b", //用户openId
        "5bee6706e4b073e587c144ae",
        "5b50428ce4b091389c3b3777"
    ]
}
```

**返回结果示例：**

```json
{
    "data": {
        "groupId": "5bee7172e4b0f6bbaa32b4bf",
        "groupName": "讨论组",
        "groupType": 2,
        "status": 1059
    },
    "error": null,
    "errorCode": 0,
    "success": true
}
```

## 群组中增加成员

**URL：** `https://www.yunzhijia.com/gateway/xtinterface/group/addGroupUser?accessToken=xxx`

**请求方法：**  `POST`

**内容类型：** `Content-Type: application/json`

**输入参数说明：**

| 字段            | 类型       |  必须       | 说明               |
|----------------|------------|------------|------------------- |
| currentUid     | String     | 是          | 当前操作者的用户openId   |
| groupId        | String     | 是          | 群组id             |
| userIds        | Array      | 是          | 需要添加的组员openId     |

**json示例：**
```json
{
    "currentUid": "5b503ee9e4b02abb5318b23e", //用户openId
    "groupId": "5bee7172e4b0f6bbaa32b4bf",
    "userIds": [
        "5b90c663e4b0216ee04a768c" //用户openId
    ]
}
```

**返回结果示例：**

```json
{
    "data": {
        "groupId": "5bee7172e4b0f6bbaa32b4bf",
        "groupName": "讨论组",
        "groupType": 2,
        "status": 1059
    },
    "error": null,
    "errorCode": 0,
    "success": true
}
```

## 群组中删除成员

**URL：** `https://www.yunzhijia.com/gateway/xtinterface/group/delGroupUser?accessToken=xxx`

**请求方法：**  `POST`

**内容类型：** `Content-Type: application/json`

**输入参数说明：**

| 字段            | 类型       |  必须       | 说明               |
|----------------|------------|------------|------------------- |
| currentUid     | String     | 是          | 当前操作者的用户openId   |
| groupId        | String     | 是          | 群组id             |
| userIds        | Array      | 是          | 被删除的组员openId     |

**json示例：**
```json
{
    "currentUid": "5b503ee9e4b02abb5318b23e", //用户openId
    "groupId": "5bee7172e4b0f6bbaa32b4bf",
    "userIds": [
        "5b90c663e4b0216ee04a768c" //用户openId
    ]
}
```

**返回结果示例：**

```json
{
    "data": {
        "groupId": "5bee7172e4b0f6bbaa32b4bf",
        "groupName": "讨论组",
        "groupType": 2
    },
    "error": null,
    "errorCode": 0,
    "success": true
}
```

## 创建群组公告

**URL：** `https://www.yunzhijia.com/gateway/xtinterface/notice/create?accessToken=xxx`

**请求方法：**  `POST`

**内容类型：** `Content-Type: application/json`

**输入参数说明：**

| 字段            | 类型       |  必须      | 说明                         |
|----------------|------------|------------|-----------------------------|
| currentUid     | String     | 是         | 当前操作者的用户openId             |
| groupId        | String     | 是         | 群组id                       |
| title          | String     | 是         | 群公告标题(字数为1-40个字符)    |
| content        | String     | 是         | 群公告内容(字数为1-2000个字符)  |

**json示例：**
```json
{
    "currentUid": "5b503ee9e4b02abb5318b23e",//用户openId
    "groupId": "5bee7172e4b0f6bbaa32b4bf",
    "title": "群公告标题",
    "content": "群公告内容"
}
```

**返回结果示例：**

```json
{
    "success": true,
    "error": null,
    "data": {
        "noticeId": "5bee684de4b090102edd7509", //公告ID
        "creator": "张三",
        "title": "群公告标题",
        "content": "群公告内容",
        "createTime": 1542350925132
    },
    "errorCode": 0
}
```

## 设置群组主题

**URL：** `https://www.yunzhijia.com/gateway/xtinterface/banner/create?accessToken=xxx`

**请求方法：**  `POST`

**内容类型：** `Content-Type: application/json`

**输入参数说明：**

| 字段            | 类型       |  必须      |  说明                          |
|----------------|------------|-----------|-------------------------------|
| currentUid     | String     | 是         | 当前操作者的用户openId             |
| groupId        | String     | 是         | 群组id                      |
| lightAppId     | String     | 否         | 轻应用id(不传的话，点击跳转时不会生成ticket，无法对接单点登录逻辑)                      |
| thumbUrl       | String     | 否         | 缩略图url                     |
| webpageUrl     | String     | 否         | 点击打开的url，支持所有通用Schema|
| primaryContent | String     | 否         | 主要内容                      |
| contentUrl     | String     | 否         | 内容图表url，有此值时优先显示图表 |

**json示例：**
```json
{
    "currentUid":"5b46b09be4b08bc0c5646ff7",
    "groupId": "5bece07d84ae7a938d0dba5f",
    "params":{
        "content":"string",
        "title":"string",
        "lightAppId":"string",
        "thumbUrl":"string",
        "webpageUrl":"string",  
        "primaryContent":"string",
        "contentUrl":"string"
    }
}
```

**返回结果示例：**

```json
{
    "success": true,
    "error": null,
    "data":{
        "bannerId": "5befb02060b2c390d28d6cdb"
    },
    "errorCode": 0
}
```

## 获取群成员

**URL：** `https://www.yunzhijia.com/gateway/xtinterface/group/groupUsers?accessToken=xxx`

**请求方法：**  `POST`

**内容类型：** `Content-Type: application/json`

**json示例：**
```json
{
  "currentUid":"5b6bf2a7e4b0fbba1110125c",//当前操作者的用户openId
  "groupId": "5c11fb86e4b03461235eef6f"  //群组id
}
```

**返回结果示例：**

```json
{
    "data": {
        "managerIds": [
            "5b6bf2a7e4b0fbba1110125c" //群组管理员用户openId
        ],
        "participantIds": [
            "5b6bf2a7e4b0fbba1110125c", //群组成员用户openId
            "5b90bd35e4b0aaccb6c1ce2d",
            "5b8ce9bae4b0aaccb6c0e55e"
        ]
    },
    "success": true,
    "errorCode": 0
}
```

**返回值参数说明：**

| 字段            | 说明               |
|----------------|--------------------|
| managerIds     |群组管理员的用户openId    |
| participantIds |群组所有成员用户openId    |


## 获取群信息

**URL：** `https://www.yunzhijia.com/gateway/xtinterface/group/groupInfo?accessToken=xxx`

**请求方法：**  `POST`

**内容类型：** `Content-Type: application/json`

**json示例：**
```json
{
  "currentUid":"5b6bf2a7e4b0fbba1110125c", //当前操作者的用户openId
  "groupId": "5c11fb86e4b03461235eef6f" //群组id
}
```

**返回结果示例：**

```json
{
    "data": {
        "5c11fb86e4b03461235eef6f": {
            "banner":{//群组主题信息

            },
            "groupInfo":{
                "groupName":"0708号方案沟通讨论",  //群组名称
                "groupType":2, //群组类型，1:双人组,2:多人组
                "managerIds":[
                    "5be3a5dee4b04e93d781ff99" //群组管理员用户openId
                ],
                "participantCount":4,           //群成员数量
                "groupId":"5c11fb86e4b03461235eef6f",
                "headerUrl":"https://www.yunzhijia.com/image/5eb3b487e4b0545e0babeebf"  //群组图像地址url
            },
            "notice":{   //群公告信息
                "sourceId":"5eb3b4a2e4b0584a6e09440d",
                "createTime":1588835490996,
                "personId":"5be3a5dee4b04e93d781ff99",
                "params":{
                    "title":"公告标题",
                    "content":"这周的任务进度在这里查看哟"
                }
            }
        }
    },
    "success": true,
    "errorCode": 0
}
```

| 字段               | 说明                          |
|--------------------|-------------------------------|
| banner             |群组的主题                     |
| groupInfo          |群组信息                       |
| groupName          |群组名称                       |
| groupType          |群组类型，1:双人组,2:多人组    |
| managerIds         |群组管理员的用户id             |
| participantCount   |群组用户数量                   |
| headerUrl          |群组图像url地址                |
| notice             |群组的公告                     |



<a href="docs.html#/client-document/index/bridge-message" target="_blank">相关：客户端消息API</a>

## 群组机器人

在调用机器人接口之前，请您先阅读以下文档：

<a href="docs.html#/tutorial/index/robot" target="_blank">了解如何创建群组机器人</a>

<a href="docs.html#/tutorial/index/robot?id=通知型机器人调试控制台" target="_blank">在线测试机器人接口</a>


###  接口地址和授权码

Webhook在群组设置的机器人设置中复制而来（仅管理员可见），其中的 `yzjtoken` 即是授权码，请妥善保管勿随意泄露。

<a href="docs.html#/tutorial/index/robot?id=如何获得webhook" target="_blank">如何获得Webhook？</a>

```
https://www.yunzhijia.com/gateway/robot/webhook/send?yzjtype=0&yzjtoken=963cb89c6eb6487fa5d333685b801bs1
```

提示：若怀疑Webhook已泄露，请删除该机器人再重建，并使用新的Webhook地址。

####  限制

> `content` 字段长度限制：字符数最大3000。


**命令行调用方式 **

因为是 http 协议的接口， 所以与发起 `post` 的语言无关， 无论是通过后端发起、通过命令行发起，还是通过ajax发起都可以。

```
curl -X POST -H "Content-Type: application/json" -d '{"content": "大家好，我是天气预报机器人，我将每天为大家推送天气信息。"}' 'https://www.yunzhijia.com/gateway/robot/webhook/send?yzjtype=0&yzjtoken=xxxxxxxxxxxxxxx'
```

**前端调用方式 **

出于安全考虑，不建议通过ajax发起，因为把授权码暴露在前端是非常危险的，有泄露的可能。

若怀疑Webhook已泄露，请删除该机器人再重建，并使用新的Webhook地址。

```javascript
$.ajax({
  url: 'https://www.yunzhijia.com/gateway/robot/webhook/send?yzjtype=0&yzjtoken=xxxxxxxxxxxxxxx',
  method: 'POST',
  headers: {
    'Content-Type': 'application/json;charset=utf-8'
  },
  data: JSON.stringify({
    'content': '大家好，我是天气预报机器人，我将每天为大家推送天气信息。@ALL'
  })
})
```

### 1.发送文本类消息

通过向Webhook地址post以下json，可以让机器人在群组中发送文本类消息：

```json
{
  "content": "大家好，我是天气预报机器人，我将每天为大家推送天气信息。@ALL"  
}
```

> `content` 是必填字段；

> `@ALL` 为可选内容，如有则提醒所有人；

**效果：** 机器人文本类消息

![机器人文本类消息](/opendocs/file/image/527c7e7970052ba8b17bc8e252042f62)


### 2.发送应用类消息

**2.1.应用类消息-默认样式 **

```json
{
    "content": "张姝的周报。本周完成：群组机器人在线DEMO",
    "msgType": 1, //应用类消息
    "param": {
        "appName": "工作汇报", //应用名称
        "title": "张姝的工作汇报",
        "content": "标题：周报\r\n本周完成：群组机器人在线DEMO；\r\n下周计划：同名@及高亮功能优化；", 
        "lightAppId": "10619", //应用id
        "thumbUrl": "https://www.yunzhijia.com/mcloud/download.action?filename=101091429.png&type=1&t=1524560759000_4027",//缩略图地址
        "webpageUrl": "https://www.yunzhijia.com", //点击跳转地址
        "customStyle": 0  //应用类消息样式。0：默认样式，1：主次内容样式，2：内嵌图表样式
    }
}
```

**2.2.应用类消息-主次内容样式 **

```json
{
    "content": "张姝的周报。本周完成：群组机器人在线DEMO",
    "msgType": 1,
    "param": {
        "appName": "工作汇报",
        "title": "张姝的工作汇报",
        "lightAppId": "10619",
        "thumbUrl": "https://www.yunzhijia.com/mcloud/download.action?filename=101091429.png&type=1&t=1524560759000_4027",
        "webpageUrl": "https://www.yunzhijia.com",
        "customStyle": 1,
        "primaryContent": "主要完成：群组机器人在线DEMO", //主要内容
        "content": "本周完成：群组机器人在线DEMO；\r\n下周计划：同名@及高亮功能优化；" //次要内容
    }
}
```

**2.3.应用类消息-内嵌图表样式 **

```json
{
    "content": "累计完成收款率",
    "msgType": 1,
    "param": {
        "appName": "报表秀秀",
        "title": "累计完成收款率",
        "lightAppId": "10619",
        "thumbUrl": "https://www.yunzhijia.com/mcloud/download.action?filename=101091429.png&type=1&t=1524560759000_4027",
        "webpageUrl": "https://www.yunzhijia.com",
        "customStyle": 2,
        "contentUrl": "https://www.yunzhijia.com/connecterp-lapp/public/img/photo-example2.png"  //内嵌图片的地址
    }
}
```


### 3.发送消息卡片类型消息
<a href="https://open.yunzhijia.com/opendocs/docs.html#/server-api/cardmsg?id=通过机器人发送卡片消息" target="_blank">如何发送消息卡片</a>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>






### -可选的通知参数(@效果)

**通知全员 **

在发送的文本消息内容中增加 `@All` 即可

> @ALL 不区分大小写，因此写作 @all 也是可以的

**通知部分人员 **

当前 (2020.10.19) 支持通知的方式为通过手机号码或 openId，请求的参数格式为：

```json
{
    "content": "早啊~喝点热水心情好",
    "notifyParams": [
        {
            "type": "mobiles",
            "values": [
                "1368*******",//此处为手机号码，为保护隐私，进行了处理
                "1376*******",
                "1324*******",
                "1861*******"
            ]
        },
        {
            "type": "openIds",
            "values": [
                "5b6527cee***************",
                "5b65280ae***************",
                "5b652863e***************",
                "5b652885e***************"
            ]
        }
    ]
}
```

##### 通知部分人员的注意事项

* 手机号码目前只支持中国的 11 位号码
* 通过手机号或者 openId 通知的人员会自动去重
* 通过这 2 种方式通知的总人数 不能超过 **100** ，建议当人数过多时，使用 `@ALL`
* 由于是针对一个群组内的人员发送消息，因此若被通知的人不在群组内，则无法收到

## 企业自建对话机器人
<a href="docs.html#/server-api/im/chatbot" target="_blank">对话型机器人</a>