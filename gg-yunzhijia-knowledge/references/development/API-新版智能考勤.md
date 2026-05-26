---
domain: development
module: 智能考勤
keywords: [IM, accessToken, secret, token, 任务]
---

## 新版智能考勤

新版智能考勤

新版智能考勤开放接口

点击此处查看视频教程

AccessToken

> 本页的接口使用 resGroupSecret 级别的 AccessToken。

请在 管理中心-系统设置-系统集成-资源授权 中找到 签到数据 的授权码， 然后调用系统接口换取 AccessToken。

如果您还不了解如何获取AccessToken，请点击此处

第三方考勤流水上传

批量上传考勤流水

接口地址:https://www.yunzhijia.com/gateway/smartatt-core/v2/clockIn/mutiUpload?accessToken=xxxxxxxxxxx

请求方式:POST

请求数据类型:application/json

响应数据类型:*/*

接口描述:

请求示例:

[
    {
        "actionType": "IN",
        "clockInTime": 0,
        "openId": "6438a2c5e4b06191bc71818b",
        "positionDetail": "某省某市某区测试地址",
        "positionName": "测试地址",
        "rawOffset": 28800000,
        "remark": "",
        "simpleDetail": "",
        "tradeNo": "td1001"
    },
    {
        "actionType": "OUT",
        "clockInTime": 0,
        "openId": "6438a2c5e4b06191bc71818b",
        "positionDetail": "某省某市某区测试地址",
        "positionName": "测试地址",
        "rawOffset": 28800000,
        "remark": "出差",
        "simpleDetail": "",
        "tradeNo": "td1002"
    }
]

请求参数:

响应参数:

响应示例:

{
    "data": {
        "existTradeNos": [],
        "failure": {
            "count": 0,
            "details": [
                {
                    "errorCode": "",
                    "index": 0
                }
            ]
        },
        "success": {
            "count": 0
        }
    },
    "errorCode": 0,
    "errorMsg": "",
    "success": true,
    "total": 0
}

获取云之家签到流水

根据签到流水更新时间查询签到流水

接口地址:https://www.yunzhijia.com/gateway/smartatt-core/v2/clockIn/listByUpdateTime?accessToken=xxxxxxxxxxx

请求方式:POST

请求数据类型:application/json

响应数据类型:*/*

接口描述: 此接口主要用于数据同步，比如当7月1日打了一笔未审核的外勤卡，7月1日去获取此笔流水的时候是未审核状态，然后7月2日签到管理员审核通过后，以7月2日的时间去查流水，依旧能获取到这笔流水，此时此笔流水的状态变更为审核通过状态。常用的场景：每天定时任务同步签到流水使云之家的流水和第三方服务保持最终状态等一致。

请求示例:

{
	"endDate": "2024-06-30",
	"openIds": ["5ae96c09e4b00f50b40f7d5c"],
	"startDate": "2024-06-01"
}

请求参数:

响应参数:

响应示例:

{
	"data": [
		{
			"actionType": "",
			"appVersion": "",
			"auditStatus": 0,
			"auditTime": 0,
			"auditorName": "",
			"auditorOid": "",
			"basiclat": 0,
			"basiclng": 0,
			"bizId": "",
			"bssid": "",
			"clockInTime": 0,
			"clockStatusStr": "",
			"department": "",
			"deviceId": "",
			"deviceName": "",
			"eid": "",
			"faceRecognition": true,
			"id": "",
			"manufacturer": "",
			"model": "",
			"network": "",
			"openId": "",
			"os": "",
			"osVersion": "",
			"photoIds": [],
			"positionDetail": "",
			"positionName": "",
			"remarks": "",
			"root": true,
			"screen": "",
			"simpleDetail": "",
			"source": "",
			"sourceStr": "",
			"spn": "",
			"ssid": "",
			"status": 0,
			"statusStr": "",
			"updateTime": "",
			"userName": "",
			"workNum": ""
		}
	],
	"errorCode": 0,
	"errorMsg": "",
	"success": true,
}

根据签到时间查询签到流水

接口地址:https://www.yunzhijia.com/gateway/smartatt-core/v2/clockIn/listByClockInTime?accessToken=xxxxxxxxxxx

请求方式:POST

请求数据类型:application/json

响应数据类型:*/*

接口描述:

请求示例:

{
	"endDate": "2024-06-30",
	"openIds": ["5ae96c09e4b00f50b40f7d5c"],
	"startDate": "2024-06-01"
}

请求参数:

响应参数:

响应示例:

{
	"data": [
		{
			"actionType": "",
			"appVersion": "",
			"auditStatus": 0,
			"auditTime": 0,
			"auditorName": "",
			"auditorOid": "",
			"basiclat": 0,
			"basiclng": 0,
			"bizId": "",
			"bssid": "",
			"clockInTime": 0,
			"clockStatusStr": "",
			"department": "",
			"deviceId": "",
			"deviceName": "",
			"eid": "",
			"faceRecognition": true,
			"id": "",
			"manufacturer": "",
			"model": "",
			"network": "",
			"openId": "",
			"os": "",
			"osVersion": "",
			"photoIds": [],
			"positionDetail": "",
			"positionName": "",
			"remarks": "",
			"root": true,
			"screen": "",
			"simpleDetail": "",
			"source": "",
			"sourceStr": "",
			"spn": "",
			"ssid": "",
			"status": 0,
			"statusStr": "",
			"updateTime": "",
			"userName": "",
			"workNum": ""
		}
	],
	"errorCode": 0,
	"errorMsg": "",
	"success": true,
}

--- 文档抓取完成 ---

参数名称 | 参数说明 | in | 是否必须 | 数据类型 | schema

data | data | body | true | array | OpenClockInRequest

actionType | 可用值:IN,OUT | true | string

clockInTime | true | integer(int64) | 打卡时间戳

openId | true | string | 用户openid，请通过人员接口获取

positionDetail | false | string | 打卡地点详细信息

positionName | false | string | 打卡地点

rawOffset | true | integer(int32) | 时区偏移量，默认请传东8区，即28800000

remark | false | string | 备注

simpleDetail | false | string | 打卡地点省市区地址(仅外勤使用)

tradeNo | true | string | 第三方单条流水唯一ID，如果云之家系统中已经存在该笔tradeNo的流水，该笔流水会被忽略

参数名称 | 参数说明 | 类型 | schema

data | OpenClockInUploadResultResponse | OpenClockInUploadResultResponse

existTradeNos | array | 云之家考勤流水中已经存在的tradeNo

failure | UploadFailure | UploadFailure

count | integer(int32)

details | array | UploadFailureDetail

errorCode | string

index | integer(int32) | 错误数据的位置，上传时，数组的索引位置

success | UploadSuccess | UploadSuccess

count | integer(int32)

errorCode | integer(int32) | integer(int32)

errorMsg | string

success | boolean

total | integer(int32) | integer(int32)

参数名称 | 参数说明 | in | 是否必须

endDate | 结束时间,与开始时间的时间范围最大不超过31天，格式为yyyy-MM-dd | true

openIds | 查询的用户范围，用户数量不能超过100人 | true

startDate | 开始时间,与结束时间的时间范围最大不超过31天，格式为yyyy-MM-dd | true

参数名称 | 参数说明 | 类型 | schema

actionType | 打卡类型,可用值:IN（内勤）,OUT（外勤）,NO_TYPE（无类型） | string

appVersion | 应用版本号 | string

auditStatus | 审核状态,系统设置-打卡流水默认审核状态设置 | integer(int32)

auditTime | 审核时间 | integer(int64)

auditorName | 审核人名称 | string

auditorOid | 审核人openId | string

basiclat | 纬度 | number(double)

basiclng | 经度 | number(double)

bizId | 业务id,关联业务单据id | string

bssid | bssid | string

clockInTime | 打卡时间 | integer(int64)

clockStatusStr | 打卡状态描述 | string

department | 部门名称 | string

deviceId | 设备id | string

deviceName | 设备名称 | string

eid | eid | string

faceRecognition | 人脸识别标识 | boolean

id | 打卡流水id | string

manufacturer | 制造商 | string

model | 制造商型号 | string

network | 网络 | string

openId | 用户openId | string

os | 手机操作系统 | string

osVersion | 手机操作系统版本 | string

photoIds | 照片文件id,下载照片参考,bizKey:attendance | array | string

positionDetail | 打卡地点详细信息 | string

positionName | 打卡地点 | string

remarks | 备注 | string

root | 是否root或越狱 | boolean

screen | 屏幕大小 | string

simpleDetail | 打卡地点省市区地址(仅外勤使用) | string

source | 流水来源,可用值:API（接口上传）,MOBILE（移动端打卡）NO_TYPE（无类型）,PHOTO（拍照打卡）,AUTO（辅助打卡）,CLOUDFLOW（审核单据补卡）,HR（HR补卡）,EXCEL（Excel上传） | string

sourceStr | 来源描述 | string

spn | 运营商 | string

ssid | wifi ssid | string

status | 状态,0:临时卡,1:正式卡,2:审核不通过卡 | integer(int32)

statusStr | 状态描述 | string

updateTime | 更新时间 | string(date-time)

userName | 用户名 | string

workNum | 工号 | string

参数名称 | 参数说明 | in | 是否必须

endDate | 结束时间,与开始时间的时间范围最大不超过31天，格式为yyyy-MM-dd | true

openIds | 查询的用户范围，用户数量不能超过100人 | true

startDate | 开始时间,与结束时间的时间范围最大不超过31天，格式为yyyy-MM-dd | true

参数名称 | 参数说明 | 类型 | schema

actionType | 打卡类型,可用值:IN（内勤）,OUT（外勤）,NO_TYPE（无类型） | string

appVersion | 应用版本号 | string

auditStatus | 审核状态,系统设置-打卡流水默认审核状态设置 | integer(int32)

auditTime | 审核时间 | integer(int64)

auditorName | 审核人名称 | string

auditorOid | 审核人openId | string

basiclat | 纬度 | number(double)

basiclng | 经度 | number(double)

bizId | 业务id,关联业务单据id | string

bssid | bssid | string

clockInTime | 打卡时间 | integer(int64)

clockStatusStr | 打卡状态描述 | string

department | 部门名称 | string

deviceId | 设备id | string

deviceName | 设备名称 | string

eid | eid | string

faceRecognition | 人脸识别标识 | boolean

id | 打卡流水id | string

manufacturer | 制造商 | string

model | 制造商型号 | string

network | 网络 | string

openId | 用户openId | string

os | 手机操作系统 | string

osVersion | 手机操作系统版本 | string

photoIds | 照片文件id 下载照片参考,bizKey:attendance | array | string

positionDetail | 打卡地点详细信息 | string

positionName | 打卡地点 | string

remarks | 备注 | string

root | 是否root或越狱 | boolean

screen | 屏幕大小 | string

simpleDetail | 打卡地点省市区地址(仅外勤使用) | string

source | 流水来源,可用值:API（接口上传）,MOBILE（移动端打卡）NO_TYPE（无类型）,PHOTO（拍照打卡）,AUTO（辅助打卡）,CLOUDFLOW（审核单据补卡）,HR（HR补卡）,EXCEL（Excel上传） | string

sourceStr | 来源描述 | string

spn | 运营商 | string

ssid | wifi ssid | string

status | 状态,0:临时卡,1:正式卡,2:审核不通过卡 | integer(int32)

statusStr | 状态描述 | string

updateTime | 更新时间 | string(date-time)

userName | 用户名 | string

workNum | 工号 | string

---