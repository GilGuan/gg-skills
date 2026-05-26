---
domain: development
module: 智能考勤
keywords: [IM, accessToken, dept, secret, token]
---

## 旧版智能签到

智能考勤

旧版智能考勤开放接口

点击此处查看视频教程

AccessToken

> 本页的接口使用 resGroupSecret 级别的 AccessToken。

请在 管理中心-系统设置-系统集成-资源授权 中找到 签到数据 的授权码， 然后调用系统接口换取 AccessToken。

如果您还不了解如何获取AccessToken，请点击此处

获取签到记录

获取代签到数据

URL：https://www.yunzhijia.com/gateway/attendance-data/v1/clockIn/listReplaceClockIn?accessToken=PNxBCtNztJWszKVFZvhSedu0uJZLBq5s

HTTP请求方法: POST

HTTP内容类型：Content-Type: application/x-www-form-urlencoded

输入参数:

请求示例：

https://www.yunzhijia.com/gateway/attendance-data/v1/clockIn/listReplaceClockIn?accessToken=PNxBCtNztJWszKVFZvhSedu0uJZLBq5s

workDateFrom:2019-12-01
workDateTo:2019-12-25
eid:17951708

返回结果:

{
    "data": [
        {
            "deptName": "研发部",//部门信息  
            "number": 1,//序号
            "masterUserName": "张三",//设备拥有人姓名（张三）
            "openId": "xxxxx",//打卡用户openId
            "remark": "xxxxxxx",//备注 例如：张三疑似为李四代签到了
            "clockInAddress": "xxxxxxx",
            "userName": "李四",//用户名（李四）
            "day": 1571925335478, //签到日期
            "deviceId": "xxxxxx",//设备编号
            "clockInTime": 1571925335478 //签到时间为毫秒数
        }
    ],
    "success": true, // true/false
    "code": //响应码
}

根据更新时间获取获移动签到明细

根据<b style="color:red">更新时间（非打卡时间）</b>获取移动签到明细新接口,该接口从公布日起(2017-02-24)开始提供查询移动签到数据服务。该接口的使用场景主要用于同步当天新增的签到流水数据，比如有些审批补卡或者人工补卡，可能补卡的签到时间并不是当天，当数据是当天产生的，需要同步到第三方系统。

URL:https://www.yunzhijia.com/gateway/attendance-data/v1/clockIn/list?accessToken=PNxBCtNztJWszKVFZvhSedu0uJZLBq5s

HTTP请求方法: POST

HTTP内容类型：Content-Type: application/x-www-form-urlencoded

输入参数:

请求示例：

https://www.yunzhijia.com/gateway/attendance-data/v1/clockIn/list?accessToken=PNxBCtNztJWszKVFZvhSedu0uJZLBq5s

workDateFrom:2019-12-01
workDateTo:2019-12-26
eid:17951708

返回结果:

{
    "data": [
        {
            "position": String, //签到地点
            "bssid": String, //无线接入点的MAC地址
            "ssid": String,//无线网络名称
            "day": String, //签到日期 （格式：yyyy-MM-dd）
            "time": long, //签到时间 （毫秒数）
            "openId": String, //签到人员编号
            "positionResult": String, //签到位置结果（Normal:范围内；Outside:范围外）
            "clockInType":"manual",//manual为正常打卡，photo为无网络拍照打卡上传的数据
            "clockInSource":1,//1:移动端打卡,3:智能打卡,5:考勤机,6:HR补卡,7:审批补卡
            "clockId": String, //流水主键id
            "lng": Double, // GPS位置
            "lat": Double, // GPS位置
            "approveResult": { //签到审核结果
                "approveId": String, //关联的审批ID
                "approveUserOpenId": String, //签到审核用户ID
                "approveTime": long, //审批时间
                "approveStatus": String, //审批状态 （未处理:UNHANDLED、已知悉:KNOWEN、已处理:HANDLED）
                "approveType": String //签到审批类型 （外勤反馈:OUTWORK、异常反馈:EXCEPTION、迟到:LATE、早退:EARLYLEAVE、缺勤:ABSENCE）
            }
     "department": String, //部门名称
            "userName": String, //用户名
            "photoId": String, //签到拍照文件ID
            "remark": String, //签到备注
        }
    ],
    "total": long, //签到流水数据总数
    "success": boolean, //成功标识 true/false
    "errorMsg": String, //异常信息
    "errorCode": String //异常代码
}

根据签到时间获取移动签到明细

获取移动签到明细新接口,该接口从公布日起(2017-02-24)开始提供查询移动签到数据服务。

URL:https://www.yunzhijia.com/gateway/attendance-data/v1/clockIn/clockintime/list?accessToken=PNxBCtNztJWszKVFZvhSedu0uJZLBq5s

HTTP请求方法: POST

HTTP内容类型：Content-Type: application/x-www-form-urlencoded

输入参数:

请求示例：

https://www.yunzhijia.com/gateway/attendance-data/v1/clockIn/clockintime/list?accessToken=PNxBCtNztJWszKVFZvhSedu0uJZLBq5s

workDateFrom:1575158400000
workDateTo:1578464923975
openIds:5b582fe2e4b0326c567c1778,5b582fe2e4b0326c567c1778
lastId:5de4fbace4b02868120c590d
limit:15

返回结果:

{
    "data": [
        {
            "position": String, //签到地点
            "bssid": String, //无线接入点的MAC地址
            "ssid": String,//无线网络名称
            "day": String, //签到日期 （格式：yyyy-MM-dd）
            "time": long, //签到时间 （毫秒数）
            "openId": String, //签到人员编号
            "positionResult": String, //签到位置结果（Normal:范围内；Outside:范围外）
             "clockInType":"manual",//manual为正常打卡，photo为无网络拍照打卡上传的数据
            "clockInSource":1,//1:移动端打卡,3:智能打卡,5:考勤机,6:HR补卡,7:审批补卡
            "clockId": String, //流水主键id
            "lng": Double, // GPS位置
            "lat": Double, // GPS位置
            "approveResult": { //签到审核结果
                "approveId": String, //关联的审批ID
                "approveUserOpenId": String, //签到审核用户ID
                "approveTime": long, //审批时间
                "approveStatus": String, //审批状态 （未处理:UNHANDLED、已知悉:KNOWEN、已处理:HANDLED）
                "approveType": String //签到审批类型 （外勤反馈:OUTWORK、异常反馈:EXCEPTION、迟到:LATE、早退:EARLYLEAVE、缺勤:ABSENCE）
            }
     "department": String, //部门名称
            "userName": String, //用户名
            "photoId": String, //签到拍照文件ID
            "remark": String, //签到备注
        }
    ],
    "total": long, //签到流水数据总数
    "success": boolean, //成功标识 true/false
    "errorMsg": String, //异常信息
    "errorCode": String //异常代码
}

按具体日期查询签到明细

根据<b style="color:red">更新时间（非打卡时间）</b>获取移动签到明细新接口

URL:https://www.yunzhijia.com/gateway/attendance-data/v1/clockIn/day/list?accessToken=PNxBCtNztJWszKVFZvhSedu0uJZLBq5s

HTTP请求方法: POST

HTTP内容类型：Content-Type: application/x-www-form-urlencoded

输入参数:

请求示例：

https://www.yunzhijia.com/gateway/attendance-data/v1/clockIn/day/list?accessToken=PNxBCtNztJWszKVFZvhSedu0uJZLBq5s

eid:17951708
day:2019-12-26
start:1
limit:100
openIds:5de50017e4b0b2767b870423

返回结果:

{
    "data": [
        {
            "position": String, //签到地点
            "bssid": String, //无线接入点的MAC地址
            "ssid": String,//无线网络名称
            "day": String, //签到日期 （格式：yyyy-MM-dd）
            "time": long, //签到时间 （毫秒数）
            "openId": String, //签到人员编号
            "positionResult": String, //签到位置结果（Normal:范围内；Outside:范围外）
            "clockInType":"manual",//manual为正常打卡，photo为无网络拍照打卡上传的数据
            "clockInSource":1,//1:移动端打卡,3:智能打卡,5:考勤机,6:HR补卡,7:审批补卡
            "clockId": String, //流水主键id
            "lng": Double, // GPS位置
            "lat": Double, // GPS位置
            "approveResult": { //签到审核结果
                "approveId": String, //关联的审批ID
                "approveUserOpenId": String, //签到审核用户ID
                "approveTime": long, //审批时间
                "approveStatus": String, //审批状态 （未处理:UNHANDLED、已知悉:KNOWEN、已处理:HANDLED）
                "approveType": String //签到审批类型 （外勤反馈:OUTWORK、异常反馈:EXCEPTION、迟到:LATE、早退:EARLYLEAVE、缺勤:ABSENCE）
            }
     "department": String, //部门名称
            "userName": String, //用户名
            "photoId": String, //签到拍照文件ID
            "remark": String, //签到备注
        }
    ],
    "total": long, //签到流水数据总数
    "success": boolean, //成功标识 true/false
    "errorMsg": String, //异常信息
    "errorCode": String //异常代码
}

注意： 为了保证签到系统的稳定性，此接口需在早晚签到高峰期(8:00至10:00，17:00至18:00)以外的时间段调用，否则获取数据失败。

上传签到数据

获取某个用户打卡的地点列表信息（公司地址信息）

URL: https://www.yunzhijia.com/gateway/attendance-data/v1/attSet/getUserPositionList?accessToken=xxxxxxxxx

说明：本接口获取的positionId 只适用于当前openId 用户，其他用户不可共用。

HTTP请求方法: POST

HTTP内容类型：Content-Type: application/json

json示例：:

{
    "openId":"xxxx" //用户编号,必填
}

返回结果：:

{
         "success":boolean, //成功标识 true/false
         "resultCode":Integer, //异常代码
         "error":String,//异常信息
         "data":
         {
             "attSets":
             [
                 {
                     "position":String, //签到点名称
                     "positionId":String, //签到点编号
                     "lng":Double,//经度
                     "lat":Double //纬度
                 }
             ]
         }
    }

单条打卡记录上传

URL: https://www.yunzhijia.com/gateway/attendance-data/v1/clockIn/singleUpload?accessToken=xxxxxxxxx

HTTP请求方法: POST

HTTP内容类型：Content-Type: application/json

json示例:

{
    "openId":"xxxx", //用户编号,必填
    "clockType":1, //1内勤,必填
    "clockInTime":1532501437000, // 考勤时间,毫秒数,必填
    "positionId":"xxxxx", //考勤点编号,必填
    "remark":"xxxx" //备注,非必填
}

返回结果：:

{
        "success":true, //成功标识 true/false
        "error":"",//异常信息
        "resultCode":200, //异常代码
        "data":{
            "success":{
                "count":1 //成功数量
            }
        }
     }

多条打卡记录上传 (最多一次性200条数据)

URL: https://www.yunzhijia.com/gateway/attendance-data/v1/clockIn/mutiUpload?accessToken=xxxxxxxxx

HTTP请求方法: POST

HTTP内容类型：Content-Type: application/json

json示例：:

[
    {
        "index":1, //保证每一次调用的唯一性,必填
        "openId":"xxxxx", //用户编号,必填
        "clockType":1, //1内勤,必填
        "clockInTime":1532501437000, // 考勤时间,毫秒数,必填
        "positionId":"xxxx", //考勤点编号,必填
        "remark":"xxx" //备注,非必填
    },
    {
        "index":2, //保证每一次调用的唯一性,必填
        "openId":"xxxx", //用户编号,必填
        "clockType":1, //1内勤,必填
        "clockInTime":1532501437000, // 考勤时间,毫秒数,必填
        "positionId":"xxx", //考勤点编号,必填
        "remark":"xxx" //备注,非必填
    }
]

返回结果：:

{
    "success":true, //成功标识 true/false
    "error":"xxxx",//异常信息
    "resultCode":200,  //异常代码
    "data":{
        "success":{
            "count":1 //处理成功数量
        },
        "failure":{
            "count":1, //处理失败数量
            "details":[
                {
                    "index":1, //处理失败数据的编号
                    "errorCode":"xxxxxxxxx" //处理失败编码
                }
            ]
        }
    }
}

--- 文档抓取完成 ---

数据类型 | 是否必传

String | 是

String | 是

Integer | 否

Integer | 否

String | 是

数据类型 | 是否必传

String | 是

String | 是

Integer | 否

Integer | 否

String | 是

String | 否

数据类型 | 是否必传

Long | 是

Long | 是

Integer | 否

String | 否

String | 否

数据类型 | 是否必传

String | 是

String | 是

Integer | 否

Integer | 否

String | 否

---