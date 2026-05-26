---
domain: development
module: 智能会议
keywords: [IM, accessToken, person, secret, token]
---

## 智能会议

智能会议接口

智能会议接口

点击此处查看视频教程

会议新增和编辑接口

> 本页的接口使用 resGroupSecret 级别的 AccessToken。

请在 管理中心-系统设置-系统集成-资源授权 中找到 时间助手管理 的授权码， 然后调用系统接口换取 AccessToken。

如果您还不了解如何获取AccessToken，请点击此处

新增单个会议接口

URL：https://www.yunzhijia.com/gateway/cloudwork/meeting/create?accessToken=xxx

http请求方法：post

http内容类型：Content-Type:application/json

输入参数：

json示例：

{
    "openid": "5a67e08d00b0e8dfe4aab4fa",
    "title": "测试会议",
    "content":"新增会议测试",
    "meetingPlace":"云8会议室",
    "startDate":1522729800000,
    "endDate":1522737000000,
    "roomId":"xxxxx",
    "noticeTimes": [5,15,60],
    "actors": ["xxxxxx","xxxxxx"],
    "type":"xxxx",
    "submitExperience":true,
    "meetOrganizers":["5a67e08d00b0e8dfe4aab4fa"]
}

返回结果示例：

{
    "data": {
        "meetingId":"xxxxx"//添加成功后会议id
    },
    "error": null,
    "errorCode": 0,
    "success": true
}

修改单个会议接口

URL：https://www.yunzhijia.com/gateway/cloudwork/meeting/modify?accessToken=xxxx

http请求方法：post

http内容类型：Content-Type:application/json

输入参数：

json示例：

{
    "id":"5ac2e3971834a1bc583d9bb8",
    "openid": "5a67e08d00b0e8dfe4aab4fa",
    "title": "测试会议",
    "content":"更新会议测试",
    "meetingPlace":"云8会议室",
    "startDate":1522729800000,
    "endDate":1522737000000,
    "roomId":"xxxxx",
    "noticeTimes": [5,15,60],
    "actors": ["xxxxxx","xxxxxx"],
    "submitExperience":true,
    "meetOrganizers":["5a67e08d00b0e8dfe4aab4fa"]
}

返回结果示例：

{
    "success": true,
    "errorCode": 0,
    "error": null,
    "data":null
}

查看单个会议接口

URL：https://www.yunzhijia.com/gateway/cloudwork/meeting/detail?accessToken=xxxx

http请求方法：post

http内容类型：Content-Type:application/json

输入参数：

json示例：

{
    "id": "5b33275f14cada62e4e44840"
}

响应参数：

Participant

Organizer

取消单个会议接口

URL：https://www.yunzhijia.com/gateway/cloudwork/meeting/cancel?accessToken=xxxx

http请求方法：post

http内容类型：Content-Type:application/json

输入参数：

>PS：必须是发起人创建的会议，才可以取消

json示例：

{
    "openid": "5a67e08d00b0e8dfe4aab4fa",
    "id": "5b33275f14cada62e4e44840"
}

返回结果示例：

{
    "success": true,
    "errorCode": 0,
    "error": null,
    "data":null
}

新增重复会议接口

URL:https://www.yunzhijia.com/gateway/cloudwork/meeting/repeatMeeting?accessToken=xxxx

http请求方法：post

http内容类型：Content-Type:application/json

输入参数：

json示例：

{
    "openid": "5a67e08d00b0e8dfe4aab4fa",
    "title": "测试会议",
    "content": "批量修改重复会议接口",
    "startDate": 1530002768912,
    "endDate": 1530687800000,
    "noticeTimes": [5,15,60],
    "actors": ["xxxxxx","xxxxxx"],
    "submitExperience": true,
    "repeat": 1,
    "repeatEndDate": 1530687800000,
    "meetOrganizers":["5a67e08d00b0e8dfe4aab4fa"]
}

返回结果示例：

>meetingIds为添加成功后的会议id集合，其中第一个是父会议ID

{
    "data": {
        "meetingIds": ["5b614fe80e4f78209cb99689", "5b61504e0e4f78209cb99690", "5b61504e0e4f78209cb9968f"]
    },
    "error": null,
    "errorCode": 0,
    "success": true
}

批量修改重复会议接口

> 影响范围仅针对当前ID及以后的会议，如需取消全部请选择第一条，如需取消单条请使用取消单个会议

URL:https://www.yunzhijia.com/gateway/cloudwork/meeting/batchModify?accessToken=xxxx

http请求方法：post

http内容类型：Content-Type:application/json

输入参数：

json示例：

{
    "id": "5b33262e14cada62e4e44822",
    "openid": "5a67e08d00b0e8dfe4aab4fa",
    "title": "测试会议",
    "content": "在京举行还很好",
    "startDate": 1530002768912,
    "endDate": 1530687800000,
    "noticeTimes": [5,15,60],
    "actors": ["xxxxxx","xxxxxx"],
    "submitExperience": true,
    "repeat": "1",
    "repeatEndDate": 1533549600000,
    "meetOrganizers":["5a67e08d00b0e8dfe4aab4fa"]
}

返回结果示例：

{
    "success": true,
    "errorCode": 0,
    "error": null,
    "data":null
}

批量取消重复会议接口，

> 影响范围仅针对当前ID及以后的会议，如需取消全部请选择第一条，如需取消单条请使用取消单个会议

URL：https://www.yunzhijia.com/gateway/cloudwork/meeting/batchCancel?accessToken=xxxx

http请求方法：post

http内容类型：Content-Type:application/json

输入参数：

json示例：

{
    "id": "1234567890",
	"openid": "5a67e08d00b0e8dfe4aab4fa"
}

返回结果示例：

{
    "success": true,
    "errorCode": 0,
    "error": null,
    "data":null
}

按天查询工作圈下会议

*URL：https://www.yunzhijia.com/gateway/cloudwork/meeting/queryByDay?accessToken=xxxx

http请求方法：post

http内容类型：Content-Type:application/json

输入参数：

json示例：

{
    "day": 1533549600000 //时间戳
}

返回结果示例：

{
    "success": true,
    "errorCode": 0,
    "error": null,
    "data": [
        {
            "openid": "5a67e1e1e4b02f1de22a70a3",
            "type": "sign",
            "title": "测试会议",
            "content": "在京举行还很好",
            "meetingPlace":"云8会议室",
            "meetingStatus":1,
            "readStatus":1,
            "acceptStatus":2,
            "personName": "张三",
            "doneTime": 1535569199741,
            "id": "5b86ed2fbeb7cc35af769eb8",
            "noticeTime": 0,
            "startDate": 1535558400000,
            "endDate": 1535644799999,
            "createDate": 1535569199741,
            "roomId":"xx",// 会议室ID
            "roomOrderId":""// 会议订单ID
        }
    ]
}

按时间范围查询工作圈下会议

*URL：https://www.yunzhijia.com/gateway/cloudwork/meeting/queryByRange?accessToken=xxxx

http请求方法：post

http内容类型：Content-Type:application/json

输入参数：

json示例：

{
    "start": 1533549600000，
    "end": 1533569600000
}

返回结果示例：

{
    "success": true,
    "errorCode": 0,
    "error": null,
    "data": [
        {
            "openid": "5a67e1e1e4b02f1de22a70a3",
            "type": "sign",
            "title": "测试会议",
            "content": "在京举行还很好",
            "meetingPlace":"云8会议室",
            "meetingStatus":1,
            "readStatus":1,
            "acceptStatus":2,
            "personName": "张三",
            "doneTime": 1535569199741,
            "id": "5b86ed2fbeb7cc35af769eb8",
            "noticeTime": 0,
            "startDate": 1535558400000,
            "endDate": 1535644799999,
            "createDate": 1535569199741,
            "roomId":"xx",// 会议室ID
            "roomOrderId":""// 会议订单ID
        }
    ]
}

获取该最近时间的会议列表

URL:https://www.yunzhijia.com/gateway/cloudwork/meeting/pageRecentList?accessToken=xxxx

http请求方式：post

http内容类型：application/json

json示例：

{
    "lastTime": 1629445124000, //最后新增或更新的时间戳, 不填 则返回所有会议预定信息
    "page": 1  // 页数
    "size": 10，// 分页大小
    "roomIds": [  "60e55bce9c0b4c00016705ad","5ffed889d8345f0001d0e18f" ]  // 选填，会议室列表
}

返回结果示例:

{
    "success": true,
    "errorCode": 0,
    "error": "",
    "data": [
        {
            "id": "612f37faaf3efa0ed89fc332",        // 会议ID
            "oid": "5facdaf8e4b0957f4040e34f",       // 创建人id
			"name": "xx",                            // 预定人姓名			
            "title": "新建5",                        // 会议主题
            "content": "",                            //会议内容
            "roomId": "5ffed889d8345f0001d0e18f",     // 会议室id
            "roomName": null,                         //会议室名称
            "roomOrderId": "612f37f93d8e4300017071bc", // 会议室预定ID
            "roomDetail": "wjn会议室试试",             // 会议室地址
            "createTime": 1630484474295,               // 创建时间
			"updateTime": 1630484493333,               //更新时间
            "approve": 0,   //订单的审批状态 0是不用审批，1待审批状态，2 审批通过 3 审批不通过
            "startTime": 1630484462938,               // 会议开始时间 
            "endTime": 1630488062938,                 // 会议结束时间 
			"deleted": true,                          // 会议是否删除
			"batchId": 612f37faaf3efa0ed89fc332,     // 会议的批次id
            "parentBatchIds": [],                // 会议的父批次id集合
            "batchSize":1                            // 该批次的会议总数
        }
    ]
}

单个用户会议查询

URL:https://www.yunzhijia.com/gateway/cloudwork/meeting/queryByUser?accessToken=xxx

http请求方法：POST

http内容类型：Content-Type:application/json

输入参数：

json示例：

{
	"pageNum": 1,
	"pageSize": 20,
	"openId": "5fd738d3e4b002b997549efd",
	"status": null
}

返回结果示例：

{
	"data": [{
		"cancelTime": 0,
		"content": "test",
		"createDate": 1608280477189,
		"currentActor": {
			"doneTime": 1608284040039,
			"openId": "5fd738d3e4b002b997549efd",
			"workSource": "1",
			"workStatus": 1
		},
		"doneTime": 1608284040080,
		"endDate": 1608284029057,
		"id": "5fdc699daf0cab00011be447",
		"openId": "5fd738d3e4b002b997549efd",
		"personName": "张三",
		"record": false,
		"startDate": 1608280429057,
		"title": "test",
		"workStatus": 1
	}],
	"errorCode": 0,
	"success": true
}

会议室预定接口

第三方通过会议室预订接口获取自己工作圈的会议室的预定信息, 用于展示。

sequenceDiagram
title: 

客户->云之家: 轮询/api/roomBook/third/hasNew
云之家-->客户: 是否有会议预定信息
Note left of 客户: 有新增会议室预定信息的情况
客户->云之家: 查询/api/roomBook/third/bookInfo
云之家-->客户: 返回会议预定信息列表(分页返回)

> 本页的接口使用 resGroupSecret 级别的 AccessToken。

请在 管理中心-系统设置-系统集成-资源授权 中找到 会议助手管理 的授权码， 然后调用系统接口换取 AccessToken。

如果您还不了解如何获取AccessToken，请点击此处

判断该工作圈是否有新增会议预定信息

URL：https://www.yunzhijia.com/api/roomBook/third/hasNew?accessToken=xxxx

http请求方法：post

http内容类型：application/json

json示例：

{
    "eid":"10109",  //必填, 工作圈eid
    "lastTime":"1538064000000"  //选填, 判断该时间节点之后是否有新增预定信息
    //最后的时间(可根据/api/roombook/third/bookInfo接口获取的预定会议信息的updateTime)
}

返回结果示例:

{
    "success": true,
    "errorCode": 0,
    "error": "",
    "data": {
        "hasNew": true   // boolean 是否有新的会议预定信息
    }
}

获取该时间节点之后的预定信息

URL:https://www.yunzhijia.com/api/roomBook/third/bookInfo?accessToken=xxxx

http请求方式：post

http内容类型：application/json

json示例：

{
    "eid":"10109",  //必填, 工作圈eid
    "lastTime":"1538064000000"  //选填, 最后新增或更新的时间戳, 不填 则返回所有会议预定信息
    "pageIndex": 1  //选填, 默认1
    "pageSize":50   //选填, 默认50;  pageSize最大值为50
}

返回结果示例:

{
    "success": true,
    "errorCode": 0,
    "error": "",
    "data": {
        "add": [
            {
                "orderId":"eeafjkdslfjsldjfdsf",  //会议预定订单id
                "oid":"5f17ff17e4b04b91****5b",
                "roomId":"6100be01650c******492"  // 会议室id
                "roomName": "23F会议室",    //会议室名称
                "roomDetail": null,         //会议室地址
                "day": "2018-09-29",        //会议日期
                "userName": "何****",       //预定人姓名
                "eid": "10109",             //工作圈eid
                "startTime": 1538202600000, //会议开始时间
                "endTime": 1538209800000,   //会议结束时间
                "createTime": 1538201890395,//预定时间
                "updateTime": 1538201890395,//修改时间
                "meetingTopic": "云*****论",//会议主题
                "meetingContent": "*****"  , //会议内容
                "approve":"0"  //订单的审批状态 0是不用审批，1待审批状态，2 审批通过 3 审批不通过
            }...
        ],
        "delete": [
            {
                "orderId":"eeafjkdslfjsldjfdsf",  //会议预定订单id
                "roomName": "A304",
                "roomDetail": "A栋-3F",
                "day": "2018-09-28",
                "userName": "符**",
                "eid": "10109",
                "startTime": 1538121600000,
                "endTime": 1538125200000,
                "createTime": 1538201890395,
                "updateTime": 1538201890395,
                "meetingTopic": "商学院*******",
                "meetingContent": "商学院*******",
                "approve":"0"  //订单的审批状态 0是不用审批，1待审批状态，2 审批通过 3 审批不通过
            }...
        ]
    }
}

查询该工作圈空闲的会议室

URL:https://www.yunzhijia.com/api/roomBook/third/freeRooms?accessToken=xxxx

http请求方法：post

http内容类型：application/json

json示例：

{
   "openId":"fsdfsdfdsfsdfdsfewfaga",  //必填，预约人员信息openId，
   "startTime": 1538121600000,
   "endTime": 1538125200000,
   "pageIndex": 1,  //选填, 默认1
   "pageSize":50   //选填, 默认50
}

返回结果示例:

{
    "success": true,
    "errorCode": 0,
    "error": "",
    "data": [
        {
            "note": "小猪佩",
            "roomDetail": "啊啊啊啊啊",
            "tagId": null,
            "limitCount": 99999999,
            "approve": true,
            "roomId": "5c121cfd7453ed63750a9767",
            "roomName": "冥王星1号"
        },...
    ]
}

查询某个会议的与会人

URL:https://www.yunzhijia.com/api/roomBook/third/getActors?accessToken=xxxx

http请求方法：post

http内容类型：application/json

json示例：

{
    "orderId":"fsdfsdfdsfsdfdsfewfaga"  //必填，会议订单id，
}

返回结果示例:

{
    "success": true,
    "errorCode": 0,
    "error": "",
    "data": [
        {
            "openId": "5c32b90b84aef86b358bc9cc",
            "headerUrl": "http://192.168.22.144/space/c/photo/load?id=54f7b6b116b2e39217000002",
            "userName": "陈*波"
        },
        {
            "openId": "5b652863e4b0689c4f38b1d3",
            "headerUrl": "http://192.168.22.144/space/c/photo/load?id=5b602f57b6238e0c44043f51",
            "userName": "陈*略"
        }
    ]
}

查询某个会议的签到情况

URL：https://www.yunzhijia.com/gateway/cloudwork/meeting/getAttendDetail?accessToken=xxxx

http请求方法：post

http内容类型：Content-Type:application/json

输入参数：

json示例：

{
	"meetingId": "67bbcfd754f53f27f3261ad1"
}

返回结果示例：

json示例：

{
    "data": {
        "workNo": "--",
        "attendTime": "--",
        "attendStatus": "未签到",
        "companyName": "xxxxxxxxxx",
        "mobile": "xxxxxxxxxxx",
        "departmentLoneName": "xxx/xxx/xxxxx",
        "acceptStatus": "未响应",
        "department": "xxx",
        "userName": "xxx"
    },
    "error": 正确访问,
    "errorCode": 200,
    "success": true
}

--- 文档抓取完成 ---

参数 | 类型 | 是否必须 | 注释

openid | String | 是 | 会议发起人的oid

title | String | 是 | 会议标题

content | String | 否 | 会议内容

meetingPlace | String | 否 | 会议地址

encryption | bool | 否 | 是否加密，默认:false

startDate | Long | 是 | 会议开始时间戳

endDate | Long | 是 | 会议结束时间戳

roomId | String | 否 | 会议室ID

noticeTimes | array(number) | 否 | 提醒时间(-1:不提醒、0:开始时间提醒、15:开始时间前15分钟提醒、60:开始时间前1小时提醒)

actors | array(string) | 否 | 协作人oid的集合

meetOrganizers | array(string) | 是 | 组织人oid的集合

channe | string | 否 | 渠道，可根据业务需要来区分日程类型

shareIds | array(string) | 否 | 共享组id集合

images | array(FileInfo) | 否 | 图片列表

files | array(FileInfo) | 否 | 文件列表

type | String | 否 | 会议类型(null:普通会议、sign:线下签到类会议、voice:语音类会议)

submitExperience | boolean | 否 | 是否需要提交会议纪要(新的体会、总结)

agent | string | 否 | 会议代建人oid

参数 | 类型 | 是否必须 | 注释

id | String | 是 | 会议ID

openid | String | 是 | 会议发起人的oid，如果是代建会议可以是代建人oid

title | String | 是 | 会议标题

content | String | 否 | 会议内容（不传则置空）

meetingPlace | String | 否 | 会议地址（不传则置空）

encryption | bool | 否 | 是否加密

startDate | Long | 是 | 会议开始时间戳

endDate | Long | 是 | 会议结束时间戳

roomId | String | 否 | 会议室ID（不传则置空）

noticeTimes | array(number) | 否 | 提醒时间(-1:不提醒、0:开始时间提醒、15:开始时间前15分钟提醒、60:开始时间前1小时提醒)

actors | array(string) | 否 | 协作人oid的集合

meetOrganizers | array(string) | 是 | 组织人oid的集合

shareIds | array(string) | 否 | 共享组id集合（不传则置空）

images | array(FileInfo) | 否 | 图片列表

files | array(FileInfo) | 否 | 文件列表

submitExperience | boolean | 否 | 是否需要提交会议纪要(新的体会、总结)

参数 | 类型 | 注释

id | String | 会议ID

参数 | 类型 | 注释

id | string | 主键

eid | string | 圈id

openid | string | 创建人oid

personName | string | 创建人姓名

photoUrl | string | 创建人头像

title | string | 主题

content | string | 内容

meetingPlace | string | 会议地点

startDate | number | 开始时间 时间戳

endDate | number | 截止时间 时间戳

createDate | number | 创建时间 时间戳

status | number | 工作状态(0未完成, 1完成/取消, 2删除)

submitExperience | boolean | 是否需要提交会议纪要(新的体会、总结)

organizers | array[Organizer] | 会议组织人

participants | array[Participant] | 与会人

images | array[FileInfo] | 图片

files | array[FileInfo] | 文件

cancelTime | number | 取消时间 时间戳

cancelReason | string | 取消原因

roomId | string | 会议室ID

roomOrderId | string | 会议室预定ID

noticeTimes | array(number) | 提醒时间(-1:不提醒、0:开始时间提醒、15:开始时间前15分钟提醒、60:开始时间前1小时提醒)

repeat | int | 重复周期(0:不重复、1:每工作日、2:每日、3:每周、4:每两周、5:每月)

repeatEndDate | number | 重复截止时间 时间戳

batchId | string | 批次ID

encryption | bool | 是否加密

recordInfo | object | 会议纪要

agent | string | 代建人oid

参数 | 类型 | 注释

id | string | 主键

eid | string | 圈id

openid | string | 创建人oid

personName | string | 创建人姓名

photoUrl | string | 创建人头像

noticeTimes | array(number) | 提醒时间(-1:不提醒、0:开始时间提醒、15:开始时间前15分钟提醒、60:开始时间前1小时提醒)

readStatus | array(number) | 0未读，1已读

status | number | 提醒时间(-1:不提醒、0:开始时间提醒、15:开始时间前15分钟提醒、60:开始时间前1小时提醒)

joinStatus | number | 会议参与状态, 0:未响应  1:不参与  2:参与 3:委托参与 4:已取消

joinDate | number | 参与时间 时间戳

mandataryOid | string | 委托对象（英文逗号分隔代表多个），有值：委托人发起委托，选择他人参加会议

clientOid | string | 委托人(对应上方的委托发起方)

参数 | 类型 | 注释

id | string | 主键

eid | string | 圈id

openid | string | 创建人oid

personName | string | 创建人姓名

photoUrl | string | 创建人头像

参数 | 类型 | 注释

id | String | 会议ID

openid | String | 会议发起人的oid

参数 | 类型 | 是否必须 | 注释

openid | String | 是 | 会议发起人的oid

title | String | 是 | 会议标题

content | String | 否 | 会议内容

meetingPlace | String | 否 | 会议地址

encryption | bool | 否 | 是否加密

startDate | Long | 是 | 会议开始时间戳

endDate | Long | 是 | 会议结束时间戳

noticeTimes | array(number) | 否 | 提醒时间(-1:不提醒、0:开始时间提醒、15:开始时间前15分钟提醒、60:开始时间前1小时提醒)

actors | array(string) | 否 | 协作人oid的集合

meetOrganizers | array(string) | 是 | 组织人oid的集合

channe | string | 否 | 渠道，可根据业务需要来区分日程类型

shareIds | array(string) | 否 | 共享组id集合

images | array(FileInfo) | 否 | 图片列表

files | array(FileInfo) | 否 | 文件列表

submitExperience | boolean | 否 | 是否需要提交会议纪要(新的体会、总结)

repeat | int | 是 | 重复周期(0:不重复、1:每工作日、2:每日、3:每周、4:每两周、5:每月)

repeatEndDate | long | 是 | 重复截止时间

agent | string | 否 | 代建人oid

参数 | 类型 | 是否必须 | 注释

id | String | 是 | 会议ID

openid | String | 是 | 会议发起人的oid，如果是代建会议可以是代建人oid

title | String | 是 | 会议标题

content | String | 否 | 会议内容

meetingPlace | String | 否 | 会议地址

encryption | bool | 否 | 是否加密

startDate | Long | 是 | 会议开始时间戳

endDate | Long | 是 | 会议结束时间戳

noticeTimes | array(number) | 否 | 提醒时间(-1:不提醒、0:开始时间提醒、15:开始时间前15分钟提醒、60:开始时间前1小时提醒)

actors | array(string) | 否 | 协作人oid的集合

meetOrganizers | array(string) | 是 | 组织人oid的集合

channe | string | 否 | 渠道，可根据业务需要来区分日程类型

shareIds | array(string) | 否 | 共享组id集合

images | array(FileInfo) | 否 | 图片列表

files | array(FileInfo) | 否 | 文件列表

submitExperience | boolean | 否 | 是否需要提交会议纪要(新的体会、总结)

repeat | int | 是 | 重复周期(0:不重复、1:每工作日、2:每日、3:每周、4:每两周、5:每月)

repeatEndDate | long | 是 | 重复截止时间

参数 | 类型 | 注释

id | String | 会议ID

openid | String | 会议发起人的oid

参数 | 类型 | 注释

day | long | 待查询的日期时间戳（当天任意时间戳都可以）

参数 | 类型 | 注释

openid | String | 会议发起人的oid

type | String | 会议类型(null:普通会议、sign:线下签到类会议、voice:语音类会议)

title | String | 会议标题

content | String | 会议内容

meetingPlace | String | 会议地址

meetingStatus | int | 会议状态(0:未完成、1:完成、2:删除)

readStatus | int | 是否已读(0:未读、1:已读)

acceptStatus | int | 接受状态(0:未响应、1:不接受、2:接受）

personName | String | 创建者姓名

doneTime | long | 完成时间戳

id | String | 会议ID

noticeTime | int | 提醒时间(-1:不提醒、0:开始时间提醒、15:开始时间前15分钟提醒、60:开始时间前1小时提醒)

startDate | Long | 会议开始时间戳

endDate | Long | 会议结束时间戳

createDate | long | 会议创建时间

roomId | String | 会议室ID

roomOrderId | String | 会议室订单ID

approve | String | 0是不用审批，1待审批状态，2 审批通过 3 审批不通过

cancelDate | long | 取消时间

cancelReason | String | 取消原因

参数 | 类型 | 注释

start | long | 开始时间戳

end | long | 截止时间戳

参数 | 类型 | 注释

openid | String | 会议发起人的oid

type | String | 会议类型(null:普通会议、sign:线下签到类会议、voice:语音类会议)

title | String | 会议标题

content | String | 会议内容

meetingPlace | String | 会议地址

meetingStatus | int | 会议状态(0:未完成、1:完成、2:删除)

readStatus | int | 是否已读(0:未读、1:已读)

acceptStatus | int | 接受状态(0:未响应、1:不接受、2:接受）

personName | String | 创建者姓名

doneTime | long | 完成时间戳

id | String | 会议ID

noticeTime | int | 提醒时间(-1:不提醒、0:开始时间提醒、15:开始时间前15分钟提醒、60:开始时间前1小时提醒)

startDate | Long | 会议开始时间戳

endDate | Long | 会议结束时间戳

createDate | long | 会议创建时间

roomId | String | 会议室ID

roomOrderId | String | 会议室订单ID

approve | String | 0是不用审批，1待审批状态，2 审批通过 3 审批不通过

cancelDate | long | 取消时间

cancelReason | String | 取消原因

类型

Integer

Integer

String

Integer

参数 | 类型 | 注释

id | String | 主键ID

openId | String | 发起人OID

personName | String | 发起人姓名

title | String | 会议主题

content | String | 内容

createDate | long | 创建时间

startDate | long | 开始时间

endDate | long | 截止时间

workStatus | int | 工作状态(0未完成, 1已完成, 2已删除)

doneTime | long | 完成时间

cancelTime | long | 取消时间

record | boolean | 是否提交了会议纪要

currentActor | MeetingActorVo | 当前用户信息

agent | string

参数 | 类型 | 注释

meetingId | String | 会议Id

参数 | 类型 | 注释

companyName | String | 工作圈

departmentLoneName | String | 部门全路径

department | String | 末级部门

userName | String | 与会人

mobile | String | 手机号

workNo | String | 工号

attendTime | String | 签到时间

attendStatus | String | 签到状态 已签到；未签到

acceptStatus | String | 备注 未响应；不参与；参与；委托参与

---