---
domain: development
module: 知识中心
keywords: [IM, accessToken, person, role, secret]
---

## 知识中心

知识中心

知识中心

> 本页的接口使用 resGroupSecret 级别的 AccessToken。

请在 管理中心-系统设置-系统集成-资源授权 中找到 知识中心 的授权码， 然后调用系统接口换取 AccessToken。

如果您还不了解如何获取AccessToken，请点击此处

创建目录

请求方式：POST

Content-Type:application/x-www-form-urlencoded

URL： https://www.yunzhijia.com/gateway/api/yzj-info/directory/mng/addDir?accessToken=XXX  (accessToken请自行修改)

请求参数：

返回数据示例:

{
    "success": true,
    "error": null,
    "errorCode": 0,
    "data": "5f44c1db50579c65c21ae0dd" //创建成功后返回的目录Id
}

获取目录列表

根据当前传入的目录Id，获取下一级的所有子目录

请求方式：GET

URL:https://www.yunzhijia.com/gateway/api/yzj-info/directory/mng/getDirListByIdForGateway?accessToken=XXX  (accessToken请自行修改)

请求参数:

请求示例:

https://www.yunzhijia.com/gateway/api/yzj-info/directory/mng/getDirListByIdForGateway?id={您的参数}&accessToken=XXX

返回数据示例与字段注释:

{
    "success": true,
    "error": null,
    "errorCode": 0,
    "data": [
        {
            "id": "6302e87150579c30184777ba", // 目录Id
            "catalogName": "知识文档复制测试", // 目录名称
            "preCatalogId": "root", // 上一级目录Id
            "preCatalogName": "根目录", //上一级目录名称
            "catalogCode": "AO201801", // 目录编号
            "catalogOrder": 0, // 目录顺序
            "commentSwitch": 0, // 是否开启文档评论 0:关闭评论;1:开启评论
            "downloadZip": 1, // 是否允许下载附件0:不允许;1:允许
            "zipPrint": 0, // 附件是否允许打印 0-否，1-是
            "contentDownload": 0, // 正文是否允许下载 0-否，1-是
            "contentPrint": 0, // 正文是否允许打印 0-否，1-是
            "enableShare": 1, // 是否允许将本目录下的文档转发到群组，拥有权限的人员可在群组中阅读 0-否，1-是
            "watermarkSwitch": 0, // 是否显示水印0:不显示;1:显示
            "nextCatalogCount": 0,
            "documentCount": 0,  // 当前目录文档数量(不包含子目录中文档数量)
            "catalogCreator": "60f7b4bce4b0bd2174f82a45", // 目录创建者的PersonId
            "createDate": 1661134961780, // 创建时间（13位时间戳）
            "enableCopy": 0 // 目录下的文档是否可复制
        }
    ]
}

创建文档

请求方式:POST

Content-Type:application/json; charset=UTF-8

URL: https://www.yunzhijia.com/gateway/api/yzj-info/document/createForGateWay?accessToken=XXX  (accessToken请自行修改)

请求参数:

Attachement 附件对象：

如果文本中夹杂图片该如何传参？

1.首先需要将文件传递到云之家文件服务器，获得图片文件 Id（ 如何获取图片文件 Id？请点击这里）

2.示例，这一步基于获得图片文件 Id 后，比如文件 Id是64c775679f1d880001dc895e，那么在参数传递中：

<p><img src=\"/docrest/file/downloadfile/64c775679f1d880001dc895e\" title=\"64c775679f1d880001dc895e\" alt=\"64c775679f1d880001dc895e\"/></p>

禁止将图片文件的二进制流作为参数传入

3.不支持文本中夹杂视频（或视频二进制流）

4.文本中不支持除图片外的任何其他文件

5.*注意*：title、content、summary 三个字段做了xss防护，仅允许白名单html标签和属性传递，非白名单内html标签和属性将会被网络防火墙拦截 （html白名单标签及属性）

请求参数示例

{
    "attachmentList": [],
    "autoCover": "",
    "carouselFileId": "",
    "catalogInfoId": "6302e87150579c30184777ba",
    "content": "test",
    "contentAttachments": [],
    "customCreateTimeStamp": null,
    "documentId": "",
    "logoFileId": "",
    "oid": "5dde0e8ae4b0d28f3ed72799",
    "pushByPubacc": false,
    "pushBySms": false,
    "summary": "test",
    "title": "testOid3",
    "type": 0,
    "urlContent": "",
    "customPermission": true,
    "all": false,
    "roles": [],
    "jonIds":[],
    "subordinateOrgs": [],
    "visibleOids":["5dde0e8ae4b0d28f3ed72799"]
}

返回数据示例:

{
	"success": true,
	"error": null,
	"errorCode": 0,
	"data": { 
    	documentId: "5dfb2b4850579c4ddd428045"   //文档id
    }
}

修改文档

请求方式:POST

Content-Type:application/json; charset=UTF-8

URL: https://www.yunzhijia.com/gateway/api/yzj-info/document/update?accessToken=XXX  (accessToken请自行修改)

请求参数:

Attachement 附件对象：

如果文本中夹杂图片该如何传参？

1.首先需要将文件传递到云之家文件服务器，获得图片文件 Id（ 如何获取图片文件 Id？请点击这里）

2.示例，这一步基于获得图片文件 Id 后，比如文件 Id是64c775679f1d880001dc895e，那么在参数传递中：

<p><img src=\"/docrest/file/downloadfile/64c775679f1d880001dc895e\" title=\"64c775679f1d880001dc895e\" alt=\"64c775679f1d880001dc895e\"/></p>

禁止将图片文件的二进制流作为参数传入

3.不支持文本中夹杂视频（或视频二进制流）

4.文本中不支持除图片外的任何其他文件

5.*注意*：title、content、summary 三个字段做了xss防护，仅允许白名单html标签和属性传递，非白名单内html标签和属性将会被网络防火墙拦截 （html白名单标签及属性）

请求参数示例

{
	"documentId": "5dfb2b4850579c4ddd428045",
    "oid": "5fd9bc95e4b09e21011eeb1f",
    "attachmentList": [],
    "carouselFileId": "",
    "catalogInfoId": "6302e87150579c30184777ba",
    "commentSwitch": 0,
    "content": "test",
    "contentAttachments": [],
    "customCreateTimeStamp": null,
    "logoFileId": "",
    "notSubordinateOrgs": [],
    "pushByPubacc": false,
    "pushBySms": false,
    "summary": "test",
    "title": "testOid3",
    "type": 0,
    "urlContent": "",
    "customPermission": true,
    "all": false,
    "roles": [],
    "jonIds":[],
    "subordinateOrgs": [],
    "visibleOids":["5dde0e8ae4b0d28f3ed72799"]
}

返回数据示例:

{
	"success": true,
	"error": null,
	"errorCode": 0,
	"data": { 
    	documentId: "5dfb2b4850579c4ddd428045"   //文档id
    }
}

获取文档详情

请求方式:GET

URL:https://www.yunzhijia.com/gateway/api/yzj-info/document/common/detailForGateWay?accessToken=XXX  (accessToken请自行修改)

请求参数:

请求示例

https://www.yunzhijia.com/gateway/api/yzj-info/document/common/detailForGateWay?documentId={您的参数}&accessToken=XXX

返回数据示例:

{

    "success": true,
    "error": null,
    "errorCode": 0,
    "data": {
        "id": "5def40d750579c3a850b5b5e",
        "catalogInfoId": "5de10a6650579c0a6f24d7f3",  // 目录id
        "eid": "100059",
        "title": "查询测试",  // 文档标题
        "content": "<p>查询测试</p>",  // 文档正文
        "summary": "",//摘要信息
        "code": "GG001",  //文档编号
        "logoFileId": "", //封面大图文件id
        "carouselFileId": "", //轮播图文件id
        "creatorPersonId": "5bcaf92ee4b0ea1ddc47d4ba",//创建者personId
        "createDate": 1575960791940, //文档创建日期(毫秒)
        "lastUpdatePersonId": "5bcaf92ee4b0ea1ddc47d4ba",
        "updateDate": 1575960791940, //文档修改日期(毫秒)
        "status": 1, //文档状态 1：正常 -1：已被禁用 -2：已被删除
        "top": false, // 置顶信息 true:被置顶 默认,false:未被置顶
        "delete": false,// 是否删除
        "forbidden": false, // 是否被禁用
        "attachmentList": [], // 文档附件
        "oldDocument": false,//是否是旧公告的文档数据
        "creatorName": null,//创建人姓名,兼容旧公告数据
        "pictureIds": null,//兼容旧公告数据
        "readNumber": 2, //文档阅读数
        "type": 0, // 0:普通文档  1:pdf为正文的文档
        "contentAttachments": null, // pdf等其他特殊形式作为正文时的文件信息 type =1时存在该值
        "attachmentNumber": 0,//附件数量
        "lastUpdateName": null,//最后一个修改人姓名
        "alreadyReadNumber": 0,//已阅读用户数量
        "unReadNumber": 0,
        "alreadyPush": false,//是否进行公众号推送
        "pushByPubacc": false,//是否进行公众号推送
        "visibleNumber": 0,//可见人数
        "downloadZip": 0,//允许下载附件0:不允许;1:允许
        "watermarkSwitch": 1,//是否显示水印0:不允许;1:允许
        "customPermission": false,//文档是否使用自定义权限 true:使用，并且permissionId必须存在, false:不使用
        "permissions": null,//文档自定义权限信息权限
        "documentPermissionsDetail": null,//permission详细信息
        "from": 0  //文档来源 0知识中心, 1审批, 2第三方, 3-网关开放, 4-头条号,5-公文
        "creatorOid": "xxx" // 文档创建者的oid,
        "approvalId":"xxx" //审批或公文流程实例Id
    }
}

Permissions对象：

Attachement 附件对象：

获取文档列表

请求方式:GET

URL:https://www.yunzhijia.com/gateway/api/yzj-info/document/list?accessToken=XXX  (accessToken请自行修改)

请求参数:

以下参数以 GET 方式的 url参数填入

请求示例

https://www.yunzhijia.com/gateway/api/yzj-info/document/list?catalogInfoId={您的参数}&pageIndex={您的参数}&pageSize={您的参数}&accessToken=XXX

返回数据示例:

{
  "success": true,
  "error": null,
  "errorCode": 0,
  "data": {
    "total": 4,
    "documentList": [ 
    {
        "id": "5def40d750579c3a850b5b5e",
        "catalogInfoId": "5de10a6650579c0a6f24d7f3",  // 目录id
        "eid": "100059",
        "title": "查询测试",  // 文档标题
        "content": "<p>查询测试</p>",  // 文档正文
        "summary": "",
        "code": "GG001",  //文档编号
        "logoFileId": "", //封面大图文件id
        "carouselFileId": "", //轮播图文件id
        "creatorPersonId": "5bcaf92ee4b0ea1ddc47d4ba",//创建者personId
        "createDate": 1575960791940, //文档创建日期(毫秒)
        "lastUpdatePersonId": "5bcaf92ee4b0ea1ddc47d4ba",
        "updateDate": 1575960791940, //文档修改日期(毫秒)
        "status": 1,
        "top": false, // 置顶信息 true:被置顶 默认,false:未被置顶
        "delete": false,// 是否删除
        "forbidden": false, // 是否被禁用
        "attachmentList": [], // 文档附件
        "oldDocument": false,
        "creatorName": null,
        "pictureIds": null,
        "readNumber": 2,
        "type": 0, // 0:普通文档  1:pdf为正文的文档
        "contentAttachments": null, // pdf等其他特殊形式作为正文时的文件信息 type =1时存在该值
        "attachmentNumber": 0,
        "lastUpdateName": null,
        "alreadyReadNumber": 0,
        "unReadNumber": 0,
        "alreadyPush": false,
        "pushByPubacc": false,
        "visibleNumber": 0,
        "downloadZip": 0,
        "watermarkSwitch": 1,
        "customPermission": false,
        "permissions": null,
        "documentPermissionsDetail": null,
        "from": 0  //文档来源 0知识中心, 1审批, 2第三方, 3-网关开放, 4-头条号,5-公文
      }
    ]
  }
}

获取文档阅读明细

备注：每分钟每个企业限制 500 次请求，超过次限制会报错：“请求过于频繁，请稍后重试！”

请求方式:POST

Content-Type:application/x-www-form-urlencoded

URL: https://www.yunzhijia.com/gateway/api/yzj-info/document/value/readStatsForGateWay?accessToken=XXX  (accessToken请自行修改)

请求参数：

返回数据示例:

{
    "success": true,
    "error": null,
    "errorCode": 0,
    "data": [
        {
            "eid": "128096",
            "documentId": "64084f857cd2d70001c5d948",
            "oid": "61b15897e4b0dde4094376bc"
        }
    ]
}

返回参数说明：

errorCode错误码参考：

设置目录权限

请求方式:POST

Content-Type:application/json; charset=UTF-8

URL: https://www.yunzhijia.com/gateway/api/yzj-info/directory/mng/setPermission?accessToken=XXX  (accessToken请自行修改)

权限：此处的权限指的是有权限查看“正式发布”的文档

请求参数:

请求参数示例

{
    "oid": "57ac3c0a00b0feb131e86e7c",
    "catalogId": "6576d685513f2b0001520984",
    "all": false,
    "privilegedUserOids": [
        "57ac3c0a00b0feb131e86e7c"
    ],
    "subordinateOrg": [
        "fbb70f91-c397-4205-b541-1fcbc182a874"
    ],
    "notSubordinateOrg": [
        "a2b31826-7abd-488f-8ce4-ad8017d54457"
    ],
    "roles": [
        "0e185746-b821-40b3-ab71-f90d4d94bbfa"
    ]
}

附录：html标签白名单及属性白名单

--- 文档抓取完成 ---

类型 | 是否必填 | 说明

String | 是 | 上级目录id，若传root表示创建一级目录

String | 是 | 目录名称

String | 是 | 目录编码

String | 是 | 目录顺序

类型 | 是否必填 | 说明

String | 否 | 目录id

类型 | 是否必填 | 含义

String | 是

String | 否 | 文档创建人的Oid

Integer | 是 | 文档类型

String | 否 | 文档正文内容

String | 否 | 超链接

List`<Attachement>` | 否 | PDF文件

String | 否 | 封面大图文件Id

String | 否

String | 是

String | 否 | 文档摘要，用于三端搜索

List<`Attachement>` | 否 | 附件列表

Integer | 否 | 是否允许阅读者对这篇文章进行评论

boolean | 是 | 是否通过云之家的公共号推送消息

boolean | 是

long | 否

boolean | 是

boolean | 否 | 可见范围 true:全员，false:非全员

List`<`String`>` | 否 | 部门Id数组，指定文档可见范围为当前传入部门并且包含下级部门。

List`<`String`>` | 否 | 部门Id数组，指定文档可见范围为当前传入部门。

List`<`String`>` | 否 | 角色Id数组，指定文档可见范围为当前传入角色列表。

List`<`String`>` | 否 | 指定可见范围为个人用户，列表，个人用户的Oid，集合长度不能超过1000。指定文档可见范围为当前传入角色列表。

Integer | 否 | 正文是否允许下载 0-否，1-是

Integer | 否 | 附件允许下载0:不允许;1:允许

类型 | 是否必填 | 说明

String | 是

String | 是

String | 否

Long | 否

类型 | 是否必填 | 含义

String | 是

String | 否 | 修改文档创建人的Oid

String | 是

Integer | 是 | 文档类型

String | 否 | 文档正文内容

String | 否 | 超链接

List`<Attachement`> | 否 | PDF文件

String | 否 | 封面大图文件Id

String | 否

String | 否 | 目录Id

String | 否 | 文档摘要，用于三端搜索

List`<`Attachement`>` | 否

Integer | 否 | 是否允许阅读者对这篇文章进行评论

boolean | 是 | 是否通过云之家的公共号推送消息

boolean | 是

long | 否

boolean | 是

boolean | 否 | 可见范围 true:全员，false:非全员

List`<`String`>` | 否 | 部门Id数组，指定文档可见范围为当前传入部门并且包含下级部门。

List`<`String`>` | 否 | 部门Id数组，指定文档可见范围为当前传入部门。

List`<`String`>` | 否 | 角色Id数组，指定文档可见范围为当前传入角色列表。

List`<`String`>` | 否 | 指定可见范围为个人用户，列表，个人用户的Oid，集合长度不能超过1000。指定文档可见范围为当前传入角色列表。

类型 | 是否必填 | 说明

String | 是

String | 是

String | 否

Long | 否

类型 | 是否必填 | 说明

String | 是 | 文档id

类型 | 含义

String | 文档Id

Integer | 文档类型

String | 目录id

String | 文档所属目录Id

String

String | 文档标题

String | 文档正文

List`<`Attachement`>` | 文档正文附件列表

String | 超链接

String | 文档摘要

String | 文档编号

String | 封面大图文件Id

String | 轮播图文件id

String | 文档创建人的PersonId

String | 文档创建人的部门Id

String | 文档创建人的部门名称

Long | 文档创建日期(毫秒，13位时间戳)

Long | 文档修改日期(毫秒，13位时间戳)

Integer | 文档状态 | 1:正常,  -1:已被禁用， -2:已被删除

Boolean | 文档是否被置顶 true:被置顶 默认,false:未被置顶

Boolean | 是否删除

Boolean | 是否被禁用

List`<`Attachement`>` | 文档附件列表

String | 文档创建者姓名

Integer

Boolean

Boolean

Integer | 文档来源

Boolean | 文档是否使用自定义权限

Permissions | 文档自定义权限信息权限

Integer | 是否显示水印

Integer | 是否允许下载附件

Integer | 正文是否允许下载

Integer | 正文是否允许打印

Integer | 附件是否允许打印

Integer | 是否允许将本目录下的文档转发到群组，拥有权限的人员可在群组中阅读

Integer | 文档是否开启评论

Integer | 文档是否允许复制

String

类型 | 说明

Boolean

List`<`String`>`

List`<`String`>`

List`<`String`>`

List`<`String`>`

类型 | 是否必填 | 说明

String | 是

String | 是

String | 否

Long | 否

类型 | 是否必填 | 说明

String | 是 | 目录id

String | 是 | 页码,从1开始

String | 是 | 每页数量

类型 | 是否必填 | 说明

String | 是 | 文档 Id

int | 是 | 阅读状态 0未读 1已读

int | 是 | 页码，从1开始

int | 是 | 每页返回数据量,从1开始，最大100

类型 | 是否必填 | 说明

String | 是 | 圈 id

是 | String | 文档id

String | 是 | 用户id

long | `否` | 阅读时间，13位时间戳，请求`已读数据`（即readStatus=1）时才会返回

说明

网关参数错误，缺少必要参数：eid

documentId 参数错误，此文档不存在，需要检查documentId是否正确

当前文档无权限查看

参数%s错误

未读记录正在生成中，需要稍后重试

请求过于频繁，请稍后重试！

类型 | 是否必填 | 含义

String | 是 | 调用接口的用户的oid | 将会作为操作人记录到管理中心，可在管理中心-系统日志-管理员操作日志-事件类型“知识中心”查看修改权限的记录

String | 是

Boolean | 是 | true-全公司可见, false-指定人员可见

List`<`String`>` | 否 | 有权限查看此目录的用户的Oid列表

List`<`String`>` | 否 | 有权限查看此目录的用户的部门Id列表，包含下级部门

List`<`String`>` | 否 | 有权限查看此目录的用户的部门Id列表，不包含下级部门

List`<`String`>` | 否 | 有权限查看此目录的用户的角色列表

List`<`String`>` | 否 | 有权限查看此目录的用户的职位Id列表

标签白名单 | 属性白名单

h1 | style,class

h2 | style,class

h3 | style,class

h4 | style,class

h5 | style,class

h6 | style,class

hr | style,class

span | style,class

strong | style,class

b | style,class

i | style,class

br

p | style,class

pre | style,class

code | style,class

a | style,class,target,href,title,rel

img | style,class,src,alt,title,_url

div | style,class

table | style,class,width,border

tr | style,class

td | style,class,width,colspan,rowspan

th | style,class,width,colspan,rowspan

tbody | style,class

ul | style,class

li | style,class

ol | style,class

dl | style,class

dt | style,class

em | style

cite | style

section | style,class

header | style,class

footer | style,class

blockquote | style,class

audio | autoplay,controls,loop,preload,src

video | autoplay,controls,loop,preload,src,height,width

figure | style,class

figcaption | style,class

mark | style,class

u | style,class

s | style,class

source | src,type

embed | type,class,pluginspage,src,width,height,align,style,wmode,play,autoplay,loop,menu,allowscriptaccess,allowfullscreen,controls,preload

---