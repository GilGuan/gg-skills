---
domain: product
module: 协同OA
keywords: [IM, OAuth, accessToken, secret, token]
---

## 协同OA/外部系统公文交换

外部系统公文交换

对接流程

第三方oa系统往云之家平台发文

第三方oa系统接受云之家平台的公文

先创建外部平台，再创建外部平台下面的外部单位（实施配？这一步是为了创建内部外部单位，能选择哪个平台）

创建外部平台

url：http://{{host}}/gateway/workflow/api/v1/form/document/platform/create?accessToken=****

method:post

Content-Type: application/json

{

"name":"平台name"//国资委等平台name

}

return

{

"success":true,

"data":"1123df23213adsfa"//平台id

}

公文相关接口

查询签收单位公文列表接口

//根据签收单位查询公文单

url：http://{{host}}/gateway/workflow/api/v1/form/document/inner/receiptList?accessToken=****

method:post

Content-Type: application/json

{

"key":"",//自定义内部单位的密钥属性，必填

"status":"sent"//待签收sent、已签收received、退回returned、撤回withdrawn、取消canceled，必填

"lastDocumentId":""//必填，公文id，如果第一次传"start"，后续继续拉的时候，根据上一次最后一条公文id传参

}

//顺序默认创建升序

return

{

"success":true,

"data":{

"hasMore":true/false //是否还有

"document":[

"documentId1",//公文id

"documentId2"

]

"size":20 //默认返回20条

}

}

查询分发单位公文列表接口

//根据签收单位查询公文单

url：http://{{host}}/gateway/workflow/api/v1/form/document/inner/postList?accessToken=****

method:post

Content-Type: application/json

{

"key":"",//自定义内部单位的密钥属性，必填

"status":"sent"//待签收sent、已签收received、退回returned、撤回withdrawn、取消canceled，必填

"lastDocumentId":""//必填，公文id，如果第一次传"start"，后续继续拉的时候，根据上一次最后一条公文id传参

}

//顺序默认创建升序

return

{

"success":true,

"data":{

"hasMore":true/false //是否还有

"document":[

"documentId1",//公文id

"documentId2"

]

"size":20 //默认返回20条

}

}

创建发文接口（外部oa往云之家发文 ）

url：http://{{host}}/gateway/workflow/api/v1/form/document/inner/create?accessToken=****

method:post

Content-Type: application/json

{

"title":"",//String，标题，直接展示，必填

"number":"",//文号，格式同标题，必填

//下面的附件与正文，二者不能同时为空

//附件

"attachments":[{

"fileId":"",//上传到云之家文件的id

"fileName":"",

"fileSize":10101//Long，文件大小

}];

//正文

"content":{

"fileId":"",//上传到云之家文件的id

"fileName":"",

"fileSize":10101//Long，文件大小

};

"postUnit":"",//发文单位（单位key），必填

"receiptUnit":""//收文单位（单位key），必填

"receiptCCUnit":""//抄送单位（单位key），非必填

//紧急程度

"urgency":"紧急/特急";//String类型，接口传递什么就展示什么，选填

//密级

"security":"绝密"//同紧急程度，选填

"extOrgName":"来文单位"//展示在交换列表的来文单位名称，选填

}

}

return

{

"success":true,

"data":"adsfasdf" //公文id

}

更改公文状态

url：http://{{host}}/gateway/workflow/api/v1/form/document/inner/updateStatus?accessToken=****

method:post Content-Type: application/json

{

"id":"",//公文id（发文接口返回的id或者查询列表接口返回的id），必填

"status":""//待签收sent、已签收received、退回returned、撤回withdrawn、取消canceled，必填

}

return

{

"success":true,

"error":"",

"errorCode":0

}

查询公文详情接口

url：http://{{host}}/gateway/workflow/api/v1/form/document/inner/findById?accessToken=****

method:post

Content-Type: application/json

{

"id":"",//公文id，必填

}

return

{

"success":true.

"data":[{

"id":"",

//标题

"title":"",

//文号

"number":"",

"attachments":[{

"fileId":"",

"fileName":""

"filzeSize":100

}];

//正文

"content":{

"fileId":"",

"fileName":"",

"filzeSize":100

};

"postUnit":"",//发文单位名称

"receiptUnit":"",//收文单位名称

//紧急程度

"urgency":"紧急";//文本

//密级

"security":"绝密",//文本

"status":"sent"//待签收sent、已签收received、退回returned、撤回withdrawn、取消canceled

}]

}

文件操作接口

文件操作accessToken获取

文件操作接口使用独立的accessToken，需要区别于其他业务的accessToken

accessToken获取

URL：https://{{host}}/gateway/oauth2/token/getAccessToken

方法：POST

请求head：Content-Type：application/json

请求参数说明

参数

类型

是否必填

说明

eid

String

是

企业eid

secret

String

是

从管理中心->系统设置->系统集成->资源授权下面的文件服务上传下载那里获得

timestamp

long

是

unix时间戳，单位毫秒

scope

String

是

这里填

resGroupSecret

文件操作accessToken获取

文件操作接口使用独立的accessToken，需要区别于其他业务的accessToken

accessToken获取

URL：https://{{host}}/gateway/oauth2/token/getAccessToken

方法：POST

请求head：Content-Type：application/json

请求参数说明

参数

类型

是否必填

说明

eid

String

是

企业eid

secret

String

是

从管理中心->系统设置->系统集成->资源授权下面的文件服务上传下载那里获得

timestamp

long

是

unix时间戳，单位毫秒

scope

String

是

这里填

resGroupSecret

文件下载接口

说明：在http header中设置x-accessToken，值为第一步获取的accessToken

URL：https://{{host}}/docrest/doc/user/downloadfile?bizkey=official&fileId={fileId}

方法：GET

x-accessToken: ******

请求参数示例

参数

类型

是否必填

说明

fileId

String

是

文件id，可以通过文件上传接口获得

文件上传接口

参数

类型

是否必填

说明

file

multipart/form-data

是

文件

bizkey

String

是

这里填

document

说明：以标准multipart方式提交，并在http header中设置x-accessToken，值为第一步获取的accessToken

url：https://{{host}}/docrest/doc/file/uploadfile

method:post

Content-Type: multipart/form-data

请求head：x-accessToken: xxxxxx

return

{

"success":true.

"data":[{

"fileId": "xxxxxx", // 文件id

"fileType": "image", // 文件类型

"isEncrypted": false,

"fileName": "xpic4271.jpg", // 文件名

"length": 56416 // 文件size

}]

}

---