---
domain: development
module: IM消息
keywords: [IM, accessToken, appId, token, 推送]
---

# 公共号订阅管理

> 来源：开放平台线上文档 (https://open.yunzhijia.com/opendocs/docs/server-api/im/pubacc.md)

# 公共号订阅管理

点击此处查看[视频教程](https://vip.kingdee.com/school/208171466029303040)

请注意：公共号接口的授权并非使用 `AccessToken` 而是 `pubtoken`，了解详情请<a href="docs.html#/server-api/im/pubToken" target="_blank">点击此处</a>。

### 设置企业订阅

**请求URL：** `https://www.yunzhijia.com/pubacc/api/pubssb`

**请求方法：** `POST`

**内容类型：** `Content-Type: application/x-www-form-urlencoded`

**输入参数：**

参数|说明
--|--
pubid|公共号id
mid|团队号eid
ssb|1是订阅；0是取消
time|10位unix时间戳
pubtoken|pubtoken=sha(mid,pubid,pubsercet,time)[注意没有nonce参数],请参考<a href="docs.html#/server-api/im/pubToken.md" target="_blank">公共号密钥验证规则</a>

**请求示例：**
```text
https://www.yunzhijia.com/pubacc/api/pubssb

pubid:XT-eda5205f-45ec-4e64-9037-3dcd7768df95
mid:17951708
ssb:1
time:1575986071
pubtoken:d70d2c38640bdb4be8549e5bf5b5a9204553a237
```

**返回结果:**

```json
{
    "success": true
}

```

### 查询企业是否订阅

**请求URL:** `https://www.yunzhijia.com/pubacc/api/pubssb`

**请求方法:** `POST/GET`

**内容类型:** `Content-Type: application/x-www-form-urlencoded`

**输入参数:**

参数|说明
--|--
pubid|公共号id
mid|团队号eid

**请求示例：**
```text
https://www.yunzhijia.com/pubacc/api/pubssb

pubid:XT-eda5205f-45ec-4e64-9037-3dcd7768df95
mid:17951708
```

**返回结果:**

```JSON
{
    "ssb": "1" //1是订阅；0是没有订阅
}
```

### 设置用户订阅

**请求URL:** `https://www.yunzhijia.com/pubacc/api/pubssb`

**请求方法:** `POST`

**内容类型:** `Content-Type: application/x-www-form-urlencoded`

**输入参数:**

参数|说明
--|--
pubid|公共号id
mid|团队号eid
userid|用户openid
ssb|1是订阅；0是取消；没有参数，表示查询是否订阅
time|10位unix时间戳
pubtoken|pubtoken=sha(mid,pubid,pubsercet,time)[注意没有nonce参数],请参考<a href="docs.html#/server-api/im/pubToken.md" target="_blank">公共号密钥验证规则</a>

**请求示例：**
```text
https://www.yunzhijia.com/pubacc/api/pubssb

pubid:XT-eda5205f-45ec-4e64-9037-3dcd7768df95
mid:17951708
userid:5df870e6e4b0b7058a9f8aef
ssb:1
time:1575986071
pubtoken:d70d2c38640bdb4be8549e5bf5b5a9204553a237
```

**返回结果:**

```json
{
    "success": true
}

```

### 设置发言人

**请求URL:** `https://www.yunzhijia.com/pubacc/api/pubssb`

**请求方法:** `POST`

**内容类型:** `Content-Type: application/x-www-form-urlencoded`

**输入参数:**

参数|说明
--|--
pubid|公共号id
mid|团队号eid
sayid|用户openid
ssb|1是订阅；0是取消；没有参数，表示查询是否订阅
time|10位unix时间戳
pubtoken|pubtoken=sha(mid,pubid,pubsercet,time)[注意没有nonce参数],请参考<a href="docs.html#/server-api/im/pubToken.md" target="_blank">公共号密钥验证规则</a>

**请求示例：**
```text
https://www.yunzhijia.com/pubacc/api/pubssb

pubid:XT-eda5205f-45ec-4e64-9037-3dcd7768df95
mid:17951708
sayid:5df870e6e4b0b7058a9f8aef
ssb:1
time:1575986071
pubtoken:d70d2c38640bdb4be8549e5bf5b5a9204553a237
```

**返回结果:**

```json
{
    "success": true
}

```

### 查询订阅用户列表

**请求URL：** `https://www.yunzhijia.com/pubacc/api/pubssbusers`

**请求方法:** `GET`

**内容类型:** `Content-Type: application/x-www-form-urlencoded`

**输入参数:**

参数|说明
--|--
pubid|自主订阅类型公共号id
page|页码(0是第一页)
count|每页记录数(默认10)
time|10位unix时间戳
pubtoken|pubtoken=sha(pubid,pubsercet,time)[注意没有nonce参数],请参考<a href="docs.html#/server-api/im/pubToken.md" target="_blank">公共号密钥验证规则</a>

**请求示例：**
```text
https://www.yunzhijia.com/pubacc/api/pubssbusers

pubid:XT-eda5205f-45ec-4e64-9037-3dcd7768df95
page:0
count:10
time:1575986071
pubtoken:c0e68c260c02eb9fdb6be3d61978fbfd9f87af3c
```

**返回结果:**

```json
[
    {
        "active": "1",
        "activeTime": "2019-12-17 14:08:38",
        "birthday": "2012-12-12",
        "city": "",
        "companyName": "印想测试团队2",
        "contact": [
            {
                "name": "邮箱",
                "permission": "R",
                "publicid": "VIRTUAL",
                "type": "E",
                "value": "15***54@163.com"
            },
            {
                "inputType": "date",
                "name": "生日",
                "permission": "W",
                "publicid": "VIRTUAL",
                "type": "O",
                "value": "2012-12-12"
            },
            {
                "name": "手机",
                "permission": "R",
                "publicid": "VIRTUAL",
                "type": "P",
                "value": "13024***321"
            }
        ],
        "createTime": "2019-12-17 14:08:38",
        "department": "移动平台产品部",
        "eid": "17951708",
        "email": "1587554@163.com",
        "fullPinyin": "zhu xiu cai",
        "gender": "2",
        "hide": false,
        "hireDate": "",
        "id": "5df870e6e4b0b7***a9f8aed",
        "identityId": "",
        "isAdmin": 0,
        "isHidePhone": 0,
        "jobNo": "6667",
        "jobTitle": "开发工程师",
        "leaveDate": "",
        "name": "朱**",
        "oId": "5df870e6e***b7058a9f8aef",
        "openId": "5df870e***b0b7058a9f8ae1",
        "orgId": "58b62641-84bf-406b-a94b-d3bfffae22aa",
        "orgInfoId": "5de50017e4b0b2767b87041b",
        "phone": "1302***5321",
        "phones": "13***125321",
        "photoUrl": "http://static.yunzhijia.com/space/c/photo/load?id=5df870e690144e5959d6a521",
        "positiveDate": "",
        "provice": "",
        "registerDate": "2019-12-17 14:08:38",
        "status": 1,
        "tid": "17951708",
        "uid": "125154606",
        "updateTime": "2019-12-18 16:13:57",
        "userName": "朱**",
        "userType": 20,
        "wbNetworkId": "5de50017e4b0b2767b87041b",
        "wbUserId": "5df870e6e4b0b7058a9f8ae1",
        "weights": 0
    },
     ...
]
```

### 查询公共号列表

**请求URL:** `https://www.yunzhijia.com/pubacc/api/xtpubs`

**请求方法:** `GET`

**内容类型:** `Content-Type: application/x-www-form-urlencoded`

**输入参数:**

参数|说明
--|--
mid|团队号eid


**请求示例：**
```text
https://www.yunzhijia.com/pubacc/api/xtpubs

mid:17951708
```

**返回结果:**

```json
[
    {
        "pid": "XT-249ec086-7c52-4194-984f-15f54f346a52",
        "name": "一起乐队吧",
        "time": 1574147747807,
        "photourl": "https://www.yunzhijia.com/pubacc/public/data/19/11/19/umSeJHWf.png",
        "note": "一起嗨",
        "mid": "17861633",
        "midname": "印*的测试团队",
        "account": "",
        "reply": true,
        "cssb": false,
        "allssb": true,
        "mssb": false,
        "selfssb": false,
        "orgId": "",
        "orgName": "",
        "fold": false,
        "remind": false,
        "tmpl": false,
        "share": false,
        "app": "0",
        "type": 2,
        "state": 2,
        "states": "修改",
        "auto": true,
        "sendMsgByPubPlatform": false,
        "sendMsg2AllByApi": false,
        "sendMsg2SomeByApi": true,
        "replyType": false,
        "grayType": false,
        "safeShare": true,
        "openAd": false,
        "ecosphere": false
    },    
    ...
]
```

### 查询公共号历史消息

**请求URL:** `https://www.yunzhijia.com/pubacc/api/xtBriefMsgs`

**请求方法:** `GET`

**内容类型:** `Content-Type: application/x-www-form-urlencoded`

**输入参数:**

参数|说明
--|--
pid|公共号id
time|10位unix时间戳
pubtoken|pubtoken=sha(pubid,pubsercet,time)[注意没有nonce参数]，请参考<a href="docs.html#/server-api/im/pubToken.md" target="_blank">公共号密钥验证规则</a>
page|页码(0是第一页,默认查询50条)


**请求示例：**
```text
https://www.yunzhijia.com/pubacc/api/xtBriefMsgs

pid:XT-941957a5-2f36-404b-a514-19427c8a5246
time:1701309579
pubtoken:68f9e4efc7d791ca386c58add49a531d0b9221b5
page:0
```

**返回字段:**

字段|说明
--|--
msgId|消息id
msgType| 消息类型（2：纯文本、6：图文）
groupName| 分组名称（0：全部订阅用户）
articleInfos|文章信息
articleInfos.id|文章id
articleInfos.title|文章标题
articleInfos.fileName|文章文件名
articleInfos.thumbUrl|文章封面图
articleInfos.url|文章地址

**返回结果:**

```json
[
    {
        "msgId": "XT-6567ec34e4b0e25877023e99",
        "msgType": 6,
        "groupName": "0",
        "sendTime": 1701309492100,
        "articleInfos": [
            {
                "id": "43ea76a6-8641-402b-a773-7ae5ff33df38",
                "title": "消息B",
                "fileName": "QKqaJwjZ",
                "thumbUrl": "https://www.yunzhijia.com/space/c/photo/load?id=6567ec1a91f4a800013ec9b6",
                "url": "https://www.yunzhijia.com/pubacc-front/article?id=43ea76a6-8641-402b-a773-7ae5ff33df38&p=XT-941957a5-2f36-404b-a514-19427c8a5246&f=QKqaJwjZ"
            }
        ]
    },
    {
        "msgId": "XT-6567ec29e4b0d96596a67b66",
        "msgType": 6,
        "groupName": "0",
        "sendTime": 1701309481778,
        "articleInfos": [
            {
                "id": "7f9a3529-f31c-451a-8d4c-7e1b14c317d7",
                "title": "消息A",
                "fileName": "fpRRpiJL",
                "thumbUrl": "https://www.yunzhijia.com/space/c/photo/load?id=6567ec1a91f4a800013ec9b6",
                "url": "https://www.yunzhijia.com/pubacc-front/article?id=7f9a3529-f31c-451a-8d4c-7e1b14c317d7&p=XT-941957a5-2f36-404b-a514-19427c8a5246&f=fpRRpiJL"
            }
        ]
    }
]

```



### 查询公共号分组信息

通过分组名称查询用户id及类型

**请求URL:** `https://www.yunzhijia.com/pubacc/api/getGroupInfo`

**请求方法:** `GET`

**内容类型:** `Content-Type: application/x-www-form-urlencoded`

**输入参数:**

参数|说明
--|--
pid|公共号id
time|10位unix时间戳
pubtoken|pubtoken=sha(pubid,pubsercet,time)[注意没有nonce参数],请参考<a href="docs.html#/server-api/im/pubToken.md" target="_blank">公共号密钥验证规则</a>
group|分组名称
page|页码(0是第一页,默认查询50条)


**请求示例：**
```text
https://www.yunzhijia.com/pubacc/api/getGroupInfo

pid:XT-794df24f-981f-4b7e-9589-c7f3a4eec3a1
time:1665555174
pubtoken:2d9e3367001a52145809780c6281544ce46059ee
group:分组1
page:1
```

**返回字段:**

字段|说明
--|--
groupUserId|分组用户id
type|分组用户类型（5：部门id、6：角色id、7、人员id）

**返回结果:**

```json
[
	{
        "groupUserId": "4a56ffa8-71a7-40e4-ad6d-e1d69de08a27",
        "type": 6
    },
	{
        "groupUserId": "60c9cc93e4b08b828bd5486e",
        "type": 7
    },
	 {
        "groupUserId": "c9380b44-1668-47a4-b8bc-eb4e676f68ed",
        "type": 5
    }
]
```



### 查询文章已读人员id

通过文章文件名查询文章已读用户id

**请求URL:** `https://www.yunzhijia.com/pubacc/api/getReadUsersPage`

**请求方法:** `GET`

**内容类型:** `Content-Type: application/x-www-form-urlencoded`

**输入参数:**

参数|说明
--|--
pid|公共号id
time|10位unix时间戳
pubtoken|pubtoken=sha(pubid,pubsercet,time)[注意没有nonce参数],请参考<a href="docs.html#/server-api/im/pubToken.md" target="_blank">公共号密钥验证规则</a>
mid|团队号eid
fileName|文章文件名
page|页码(0是第一页,默认查询50条)


**请求示例：**
```text
https://www.yunzhijia.com/pubacc/api/getReadUsersPage

pid:XT-794df24f-981f-4b7e-9589-c7f3a4eec3a1
time:1665555174
pubtoken:2d9e3367001a52145809780c6281544ce46059ee
mid:2701576
fileName:pxrldrPN
page:1
```

**返回字段:**

字段|说明
--|--
oId|已读用户id

**返回结果:**

```json
[
	"60cae7b4e4b0730f11a0cc9f",
	"60cae79ae4b08b828bd5533d",
	"60c9cc93e4b08b828bd5486e",
]
```


### 创建公共号

**请求URL:** `https://www.yunzhijia.com/pubacc/api/pubcreate`

**请求方法:** `POST`

**内容类型:** `Content-Type: application/x-www-form-urlencoded`

**输入参数:**

参数|说明
--|--
sign|在mid企业管理中心->系统集成->资源授权，用资源授权密钥对"name公共号名称"签名后,BASE64编码字符串
mid|团队号eid
midname|企业名称
name|公共号名称
photoname|图标名称
photo64|图标base64
cssb|可订阅[1是、0否]
allssb|全部订阅[1是、0否]
reply|可回复[1是、0否]
remind|可选, 不传默认为false, 为不需要消息推送； 传true为需要消息推送

**请求示例：**
```text
https://www.yunzhijia.com/pubacc/api/pubcreate

sign:BwvklVHVPDyVlAH9CLelZ1PhS9M2qPkn
mid:17951708
midname:印想测试团队2
name:yincy的歌迷会
photoname:vip
cssb:1
allssb:1
reply:1
```

**返回结果:**

```text
    XT-9aac403f-83e8-4888-9ee4-da78d224c22b //公共号pubid
```

### 创建公共号菜单

**请求URL:** `https://www.yunzhijia.com/pubacc/api/pubmenu`

**请求方法:** `POST`

**内容类型:** `Content-Type: application/x-www-form-urlencoded`

**输入参数:**

参数|说明
--|--
sign|用mid企业密钥对"pid"签名后,BASE64编码字符串
mid|团队号eid
pid|公共号pubid
menu|菜单JSON字符串,可参考[查询公共号列表](#查询公共号列表)接口返回的属性menu

**menu属性参数说明如下：**
```json
{
      "id": "menu1489391911113", //id
      "android": "", //Android 应用:安装地址或本地调用协议
      "ios": "", //IOS 应用 :安装地址或本地调用协议
      "name": "我要吐槽", //菜单名称
      "appid": "", //应用id
      "type": "view",  //类型：menu:菜单,click:按钮,url:链接,view:轻应用,app:移动原生应用
      "url": "https://www.baidu.com/",  //跳转地址
      "key": "" //键值:用于唯一识别此菜单项的标识符
 }

```

**请求示例：**
```text
https://www.yunzhijia.com/pubacc/api/pubmenu`

sign:K2R6VjBPOW0xQzE2N0JmZ2U1cHJsNmtJWHRBPQ==
mid:17951708
pid:XT-eda5205f-45ec-4e64-9037-3dcd7768df95
menu:[
    {
        "id": "menu1489391911114", 
        "android": "", 
        "ios": "", 
        "name": "我要吐槽", 
        "appid": "", 
        "type": "view", 
        "url": "https://www.baidu.com/", 
        "key": ""
    }
]
```
**返回结果：**
```json
{
    "success": true
}
```

### 状态返回值规范

**成功** 

当消息发送请求被成功执行时，HTTP状态码返回200。

**失败**

参考<a href="docs.html#/server-api/im/pubSend.md" target="_blank">公共号消息发送API</a>