---
domain: development
module: 组织人员
keywords: [IM, accessToken, dept, secret, token]
---

# 部门组织API列表

> 来源：开放平台线上文档 (https://open.yunzhijia.com/opendocs/docs/server-api/org/dept.md)

# 部门组织API列表

**接口调用说明**

##  Postman调用示例（必读）

**举例接口：新增组织：**
![](/opendocs/file/image/f195448ed41ecb10a37b1a72efddb253)
**输入参数说明如下：**

| 字段名 | 数据类型 | 是否必填 | 说明                                  |
| ------ | -------- | -------- | ------------------------------------- |
| nonce  | String   | 否       | 校验重复请求,格式为16位以内随机字符串 |
| eid    | String   | 是       | 注册企业团队id                        |
| data   | String   | 是       | 业务数据,json字符串格式               |

**特别注意事项：**
> 请求中的ContentType 使用的是  `x-www-form-urlencoded` 。请注意区分 `获取组织同步接口`  的 `ContentType`

### 接口授权

本页接口使用 `resGroupSecret` 级别的 `AccessToken`， 与获取组织数据的接口不同，请注意区分。

请在 `管理中心-系统设置-系统集成-通讯录同步` 中，复制 `只读秘钥` 或者 `可编辑秘钥`， 然后调用系统接口换取 `AccessToken`。

> 只读秘钥：只能调用查询类的接口

> 可编辑秘钥：可以调用全部接口

如果您还不了解如何获取AccessToken，请<a href="docs.html#/server-api/auth/oauth" target="_blank">点击此处</a>

**接口列表**

| 接口名称                           | URL                                                                                    | 备注 |
|------------------------------------|----------------------------------------------------------------------------------------|------|
| 查询设置隐藏部门或者部门仅可见部门 | [/gateway/openimport/open/company/queryOrgSecret](#查询设置隐藏部门或者部门仅可见部门) |      |
| 设置隐藏部门或部门仅可见           | [/gateway/openimport/open/company/setOrgSecret](#设置隐藏部门或部门仅可见)             |      |
| 新增组织                           | [/gateway/openimport/open/dept/add](#新增组织)                                         |      |
| 新增组织(V2)                           | [/gateway/openimport/open/v2/dept/add](#新增组织--该接口返回部门信息)                                         |      |
| 根据orgId删除组织                  | [/gateway/openimport/open/dept/deleteById](#根据orgid删除组织)                         |      |
| 删除组织                           | [/gateway/openimport/open/dept/delete](#删除组织)                                      |      |
| 查询更新部门信息                   | [/gateway/openimport/open/dept/getAtTime](#查询更新部门信息)                           |      |
| 根据orgId或department查询组织信息  | [/gateway/openimport/open/dept/get](#根据orgid或department查询组织信息)                |      |
| 查询全部组织信息                   | [/gateway/openimport/open/dept/getall](#查询全部组织信息)                              |      |
| 跨层次部门挪动                     | [/gateway/openimport/open/dept/moveOrg](#跨层次部门挪动)                               |      |
| 根据orgId更新组织名称              | [/gateway/openimport/open/dept/updateById](#根据orgid更新组织名称)                     |      |
| 更新组织排序码                     | [/gateway/openimport/open/dept/updateWeightsById](#更新组织排序码)                     |      ||
| 更新组织名称                       | [/gateway/openimport/open/dept/update](#更新组织名称)                                  |      |
|添加机密组织可见部门                       | [/gateway/openimport/open/dept/addOrgSecretDeptWhitelist](#添加机密组织可见部门)                                  |      |
|删除机密组织可见部门                       | [/gateway/openimport/open/dept/deleteOrgSecretDeptWhitelist](#删除机密组织可见部门)                                  | 
|部门多语言-查询所支持语言                       | [/gateway/openimport/open/orgLang/findOrgLangModels](#部门多语言-查询所支持语言)                                  |   
|部门多语言-获取某个部门多语言信息                       | [/gateway/openimport/open/orgLang/findOrgLangByOrgId](#部门多语言-获取某个部门多语言信息)                                  | 
|部门多语言-保存多语言部门信息                       | [/gateway/openimport/open/orgLang/saveOrgLang](#部门多语言-保存多语言部门信息)                                  |  ||

组织长名称：根据组织层级包含本组织及所有上级组织的完整名称，它具有以下特点:

1. 组织长名称在工作圈中具有唯一性
1. 组织长名称中的各级组织以”\\\”为分隔符
1. 组织长名称前不能包含工作圈名称

例如: “研发中心\\\移动平台产品部\\\开发部”


**输入参数说明如下：**

| 字段名 | 数据类型 | 是否必填 | 说明                                  |
| ------ | -------- | -------- | ------------------------------------- |
| nonce  | String   | 否       | 校验重复请求,格式为16位以内随机字符串 |
| eid    | String   | 是       | 注册企业团队id                        |
| data   | String   | 是       | 业务数据,json字符串格式               |


## 新增组织

**描述:** 新增组织，每次新增记录不超过1000条，按照departments先后顺序进行排序。

**URL:** `https://www.yunzhijia.com/gateway/openimport/open/dept/add?accessToken=xxxxxx`

**请求方法：** `post`

**内容类型：** `Content-Type: application/x-www-form-urlencoded`

**输入参数:** 

`nonce`: String // 非必填，用于校验重复请求的随机字符串

`eid`: Number // 必填，企业id

`data`: String // 必填，业务数据json字符串


> 请注意，`data` 不应是js对象而应是一个JSON格式的字符串， 即用JSON.stringify()处理以下结构对象获得的字符串：


```json
{
    "eid":String, //不必须，如果没有，则以外面的eid参数为准
    "departments": [String,…], //必填，组织长名称数组，单个组织长名称格式："一级部门\\二级部门\\三级部门"，如 ： "研发中心\\移动平台产品部\\开发部"
    "weights": ["2","4","3"] //保证weights与departments长度一致，如果不传根部门，只传了子部门，根部门的排序码会依据子部门的排序码来生成 ，子部门排序码越小，生成的根部门排序码就也越小。
}
```
**请求示例：**
```url
https://www.yunzhijia.com/gateway/openimport/open/dept/add?accessToken=xxxxxx
```

```form
nonce:abcxyXXXXzefg

eid:17951708

data:{
    "departments": [
        "客户成功部\\头部客服\\技术支持", 
        "客户成功部\\头部客服\\业务运维"
    ], 
    "weights": [
        "2", 
        "7"
    ]
}
```

**返回结果示例:** 参见<a href="docs.html#/server-api/org/syncRule.md" target="_blank">输出结果</a>，如果组织全部新增成功，则data里返回[]，如果未全部新增成功的，则data中会有新增失败的具体信息，其中data字段格式如下：

```json
[
    {
    "msgId":String, //组织长名称
    "msgCode":int, //消息码
    "msg":String //消息
    },…
]
```
## 新增组织(V2) 

**描述:** 新增组织，每次新增记录不超过1000条，按照departments先后顺序进行排序。

**URL:** `https://www.yunzhijia.com/gateway/openimport/open/v2/dept/add?accessToken=xxxxxx`
传参同新增组织一样
**返回结果示例:** 参见<a href="docs.html#/server-api/org/syncRule.md" target="_blank">输出结果</a>，如果组织全部新增成功，data中返回成功后的部门信息，如果未全部新增成功的，则data中会有新增失败的具体信息，其中data字段格式如下：

```json
{
    "data": {
        "successList": [
            {
                "department": "test\\test201",
                "orgId": "ab080ff6-c8dd-4c6c-9011-29845083aca0"
            }
        ],
        "errorList": []
    },
    "success": true,
    "errorCode": 100
}
```

## 更新组织名称

**描述：** 更新组织名称，每次更新记录不超过1000条

**注意:**

- 当前接口仅仅支持同级组织名称的变化，不包括组织层级变化（原组织和新组织必须在同级目录下）。如果需要将某一部门（包括所有下级部门）整体挪动到另外一个部门，请使用接口：[跨层次部门挪动](#跨层次部门挪动)

**URL:** `https://www.yunzhijia.com/gateway/openimport/open/dept/update?accessToken=xxxxxx`

**请求方法：** `post`

**内容类型：** `Content-Type: application/x-www-form-urlencoded`

**输入参数:** 

`nonce`: String // 非必填，用于校验重复请求的随机字符串

`eid`: Number // 必填，企业id

`data`: String // 必填，业务数据json字符串


> 请注意，`data` 不应是js对象而应是一个JSON格式的字符串， 即用JSON.stringify()处理以下结构对象获得的字符串：


```json
{
    "eid":String, //不必须，如果没有，则以外面的eid参数为准
    "departments": [{
        "department":String, //必填,原组织长名称
        "todepartment":String //必填,新组织长名称,路径中不存在的组织将会自动创建
    },...]
}
```
**请求示例：**
```url
https://www.yunzhijia.com/gateway/openimport/open/dept/update?accessToken=xxxxxx
```

```form
nonce:abcxyXXXXzefg

eid:17951708

data:{
    "departments": [
        {
            "department": "客户成功部\\头部客服\\技术支持", 
            "todepartment": "客户成功部\\头部客服\\技术支持更新"
        }, 
        {
            "department": "客户成功部\\头部客服\\业务运维", 
            "todepartment": "客户成功部\\头部客服\\业务运维更新"
        }
    ]
}
```

**返回结果示例:** 参见<a href="docs.html#/server-api/org/syncRule.md" target="_blank">输出结果</a>， 如果组织全部更新成功，则data里返回[]，如果有未更新成功的，则data中会有更新失败的具体信息。其中data字段格式如下：

```json
[{
    "msgId":String, //原组织长名称
    "msgCode":int, //消息码
    "msg":String //消息
},…]
```

## 删除组织

**描述:** 根据组织长名称删除组织，如该组织及其子组织下存在“正常”的人员，则删除组织后人员将被统一移动到未分配人类别，请谨慎操作；若不存在“正常”的人员，则该组织及其子组织会被删除，同时把组织下“禁用”或“注销”的人员改为待分配状态

**URL:** `https://www.yunzhijia.com/gateway/openimport/open/dept/delete?accessToken=xxxxxx`

**请求方法：** `post`

**内容类型：** `Content-Type: application/x-www-form-urlencoded`

**输入参数:** 

`nonce`: String // 非必填，用于校验重复请求的随机字符串

`eid`: Number // 必填，企业id

`data`: String // 必填，业务数据json字符串


> 请注意，`data` 不应是js对象而应是一个JSON格式的字符串， 即用JSON.stringify()处理以下结构对象获得的字符串：


```json
{
    "eid":String, //不必须，如果没有，则以外面的eid参数为准
    "departments": [String,…] //必填,要删除的组织长名称数组
}
```
**请求示例：**
```url
https://www.yunzhijia.com/gateway/openimport/open/dept/delete?accessToken=xxxxxx
```

```form
nonce:abcxyXXXXzefg

eid:17951708

data:{
    "departments": [
        "客户成功部\\头部客服\\技术支持更新"
    ]
}
```

**返回结果示例:** 参见<a href="docs.html#/server-api/org/syncRule.md" target="_blank">输出结果</a>， 如果全部删除组织成功，则data里返回[]，如果未全部删除成功的，则data中会有未删除成功的具体信息，其中data字段格式如下：

```json
[{
    "msgId":String, //组织长名称
    "msgCode":int, //消息码
    "msg":String //消息
},…]
```

## 根据orgId或department查询组织信息

**描述:** 根据组织ID或组织长名称查询组织详细信息

**URL:** `https://www.yunzhijia.com/gateway/openimport/open/dept/get?accessToken=XXXXXXXX`

**请求方法：** `post`

**内容类型：** `Content-Type: application/x-www-form-urlencoded`

**输入参数:** 

`nonce`: String // 非必填，用于校验重复请求的随机字符串

`eid`: Number // 必填，企业id

`data`: String // 必填，业务数据json字符串


> 请注意，`data` 不应是js对象而应是一个JSON格式的字符串， 即用JSON.stringify()处理以下结构对象获得的字符串：


根据部门orgId查询时：

```json
{
    "array": [  //必填，orgId数组
        String,
        String
    ],
    "eid": String,  //不必须，如果没有，则以外面的eid参数为准
    "type": 0   //必填，查询类型，0：根据orgId查询
}

```

根据department查询时：

```json
{
    "array": [  //必填，department数组，如："开发部-22"，"bb\\开发部-22\\123123aaaa"，需注意的是，若想查根组织信息请入参 "\\"
        String,
        String
    ],
    "eid": string,  //不必须，如果没有，则以外面的eid参数为准
    "type": 1   //必填，查询类型，1：根据department查询
}

```

**请求示例：**

根据部门orgId查询时：
```url
https://www.yunzhijia.com/gateway/openimport/open/dept/get?accessToken=XXXXXXXX
```

```form
nonce:abcxyXXXXzefg

eid:17951708

data:
{
    "array": [
        "ff67b038-0639-4703-a385-3dd971804e79"
    ], 
    "type": 0
}
```

根据department查询时：

```text
https://www.yunzhijia.com/gateway/openimport/open/dept/get?accessToken=NHcGMhTF0LRVzVivAkCHn0xg0j938U0f
```

```url
nonce:abcxyXXXXzefg

eid:17951708

data:{
    "array": [
        "客户成功部\\头部客服\\业务运维更新",
        "\\"    //代表查根组织信息
    ], 
    "type": 1
}
```

**返回结果示例:**
```json
{
    "success": true,
    "error": "",
    "errorCode": 100,
    "data": [
        {
            "name": "业务运维更新",  //组织名称
            "id": "ff67b038-0639-4703-a385-3dd971804e79",  //组织id
            "weights": 7,  //排序码
            "department": "客户成功部\\头部客服\\业务运维更新",  //组织长名称
            "parentId": "2b117f95-d349-422f-9f2a-dead7e6c0375"  //上一级部门id（组织父id）
            "businessUnit":1 //是否是业务单元，1：业务单元，0：非业务单元
        }
    ]
}

```

## 查询全部组织信息

**描述:** 查询全部组织信息

**URL:** `https://www.yunzhijia.com/gateway/openimport/open/dept/getall?accessToken=xxxxxx`

**请求方法：** `post`

**内容类型：** `Content-Type: application/x-www-form-urlencoded`

**输入参数:** 

`nonce`: String // 非必填，用于校验重复请求的随机字符串

`eid`: Number // 必填，企业id

`data`: String // 必填，业务数据json字符串


> 请注意，`data` 不应是js对象而应是一个JSON格式的字符串， 即用JSON.stringify()处理以下结构对象获得的字符串：


```json
{
    "eid":String //可不填，注册号,由于外面已有eid参数，此时data字段也可不填
}
```

**请求示例：**
```url
https://www.yunzhijia.com/gateway/openimport/open/dept/getall?accessToken=xxxxxx
```

```form
nonce:abcxyXXXXzefg

eid:17951708
```

**返回结果示例:** 
```json
{
    "success": true,
    "error": "",
    "errorCode": 100,
    "data": [  //组织列表
        {
            "name": "开发部",  //组织名称
            "id": "58547b46-76d6-4d7d-ade0-be91d396cfe4",  //组织的id
            "weights": 101000,  //排序码
            "department": "研发中心\\移动平台产品部\\开发部",  //组织长名称
            "parentId": "58b62641-84bf-406b-a94b-d3bfffae22aa"  //组织父Id
            "businessUnit":1 //是否是业务单元，1：业务单元，0：非业务单元
        },
        {
            "name": "业务运维",
            "id": "ff67b038-0639-4703-a385-3dd971804e79",
            "weights": 7,
            "department": "研发中心\\移动平台产品部\\业务运维",
            "parentId": "58b62641-84bf-406b-a94b-d3bfffae22aa"
            "businessUnit":1
        },
        {
            "name": "运营管理部",
            "id": "11e11baa-d74a-44df-b511-2b0b58d2a19e",
            "weights": 5,
            "department": "运营管理部",
            "parentId": "5de50017e4b0b2767b87041b"
            "businessUnit":1
        },
        {
            "name": "人力资源部",
            "id": "42061c1f-496d-45c2-b5c2-387a3a534261",
            "weights": 0,
            "department": "人力资源部",
            "parentId": "5de50017e4b0b2767b87041b"
            "businessUnit":1
        }
        ...
    ]
}
```

## 查询更新部门信息

**描述:** 查询某个时点后有更新的部门信息

**URL:** `https://www.yunzhijia.com/gateway/openimport/open/dept/getAtTime?accessToken=xxxxxx`

**请求方法：** `post`

**内容类型：** `Content-Type: application/x-www-form-urlencoded`

**输入参数:** 

`nonce`: String // 非必填，用于校验重复请求的随机字符串

`eid`: Number // 必填，企业id

`data`: String // 必填，业务数据json字符串


> 请注意，`data` 不应是js对象而应是一个JSON格式的字符串， 即用JSON.stringify()处理以下结构对象获得的字符串：


```json
{
    "eid":String, //不必须，如果没有，则以外面的eid参数为准
    "time":String //必填,查询时点，格式：“2014-08-02 01:40:38”
}
```
**请求示例：**
```url
https://www.yunzhijia.com/gateway/openimport/open/dept/getAtTime?accessToken=xxxxxx
```

```form
nonce:abcxyXXXXzefg

eid:17951708

data:{
    "time": "2019-12-31 16:30:28"
}
```

**返回结果示例:** 
```json
{
    "success": true,
    "error": "",
    "errorCode": 100,
    "data": [
        {
            "id": "ff67b038-0639-4703-a385-3dd971804e79", //组织的id
            "parentId": "2b117f95-d349-422f-9f2a-dead7e6c0375", //组织父Id
            "name": "业务运维更新", //组织名称
            "weights": 7,  //排序码
            "department": "客户成功部\\头部客服\\业务运维更新",  //组织长名称
            "changeType": "2"  //1：新增 2：更新 3：删除
            "businessUnit":1 //是否是业务单元，1：业务单元，0：非业务单元
        },
        {
            "id": "b5c29e83-999c-40f7-800b-490f3e13d7bf",
            "parentId": "2b117f95-d349-422f-9f2a-dead7e6c0375",
            "name": "技术支持更新",
            "weights": 2,
            "department": "客户成功部\\头部客服\\技术支持更新",
            "changeType": "3"  //1：新增 2：更新 3：删除
             "businessUnit":1
        }
    ]
}
```

## 跨层次部门挪动

**描述:** 将某一个部门及其所有下级部门和这些部门所属的人员，整体挪动到另外一个部门，保持子部门、人员相对于这个部门的路径不变。

![跨层次部门挪动](/opendocs/file/image/20a7324fd6668b5ec54affd860e5f380)

**URL:** `https://www.yunzhijia.com/gateway/openimport/open/dept/moveOrg?accessToken=xxxxxx`

**请求方法：** `post`

**内容类型：** `Content-Type: application/x-www-form-urlencoded`

**输入参数:** 

`nonce`: String // 非必填，用于校验重复请求的随机字符串

`eid`: Number // 必填，企业id

`data`: String // 必填，业务数据json字符串


> 请注意，`data` 不应是js对象而应是一个JSON格式的字符串， 即用JSON.stringify()处理以下结构对象获得的字符串：

```json
{
    "orgId": "", //待挪动部门ID
    "moveToOrgId": "" //挪动到的部门ID
}
```
**请求示例：**
```url
https://www.yunzhijia.com/gateway/openimport/open/dept/moveOrg?accessToken=xxxxxx
```

```form
nonce:abcxyXXXXzefg

eid:17951708

data:{
    "orgId": "ff67b038-0639-4703-a385-3dd971804e79", 
    "moveToOrgId": "58b62641-84bf-406b-a94b-d3bfffae22aa"
}
```

**返回结果示例:** 参见<a href="docs.html#/server-api/org/syncRule.md" target="_blank">输出结果</a>，调用方需要自己保证，目标部门中不存在同名称的部门（已经存在时，挪动也会成功，但是，会导致其它业务失败）。其中data字段格式如下：

```json
{
    "data": ""
}
```

## 根据orgId更新组织名称

**描述:** 更新组织名称，每次更新记录不超过1000条

**注意:** 当前接口仅仅支持同级组织名称的变化，不包括组织层级变化（原组织和新组织必须在同级目录下）。如果需要将某一部门（包括所有下级部门）整体挪动到另外一个部门，[跨层次部门挪动](#跨层次部门挪动)

**URL:** `https://www.yunzhijia.com/gateway/openimport/open/dept/updateById?accessToken=xxxxxx`

**请求方法：** `post`

**内容类型：** `Content-Type: application/x-www-form-urlencoded`

**输入参数:** 

`nonce`: String // 非必填，用于校验重复请求的随机字符串

`eid`: Number // 必填，企业id

`data`: String // 必填，业务数据json字符串


> 请注意，`data` 不应是js对象而应是一个JSON格式的字符串， 即用JSON.stringify()处理以下结构对象获得的字符串：


```json
{
    "eid":String, //不必须，如果没有，则以外面的eid参数为准
    "departments": [
        {
        "orgId":String, //必填,原组织id
        "todepartment":String //必填,新组织名称,不是长名称
        },...
    ]
}
```
**请求示例：**
```url
https://www.yunzhijia.com/gateway/openimport/open/dept/updateById?accessToken=xxxxxx
```

```form
nonce:abcxyXXXXzefg

eid:17951708

data:{
    "departments": [
        {
            "orgId": "ff67b038-0639-4703-a385-3dd971804e79", 
            "todepartment": "业务运维"
        }
    ]
}
```

**返回结果示例:** 参见<a href="docs.html#/server-api/org/syncRule.md" target="_blank">输出结果</a>，如果更新组织全部成功，则data里返回[]，如果有未更新成功的，则data中会有未更新成功的具体信息，其中data字段格式如下：

```json
[
    {
    "msgId":String, //原组织id
    "msgCode":int, //消息码
    "msg":String //消息
    },…
]
```

## 根据orgId删除组织

**描述:** 根据组织id删除组织，如该组织及其子组织下存在“正常”的人员，则删除组织后人员将被统一移动到未分配人类别，请谨慎操作；若不存在“正常”的人员，则该组织及其子组织会被删除，同时把组织下“禁用”或“注销”的人员改为待分配状态

**URL:** `https://www.yunzhijia.com/gateway/openimport/open/dept/deleteById?accessToken=xxxxxx`

**请求方法：** `post`

**内容类型：** `Content-Type: application/x-www-form-urlencoded`

**输入参数:** 

`nonce`: String // 非必填，用于校验重复请求的随机字符串

`eid`: Number // 必填，企业id

`data`: String // 必填，业务数据json字符串


> 请注意，`data` 不应是js对象而应是一个JSON格式的字符串， 即用JSON.stringify()处理以下结构对象获得的字符串：


```json
{
    "eid":String, //不必须，如果没有，则以外面的eid参数为准
    "departments": [String,…
    ] //必填,要删除的组织id数组
}
```
**请求示例：**
```url
https://www.yunzhijia.com/gateway/openimport/open/dept/deleteById?accessToken=xxxxxx
```

```form
nonce:abcxyXXXXzefg

eid:17951708

data:{
    "departments": [
        "c983b8ea-899a-4970-b6ff-ccf84f07d261", 
        "2d0034dd-6048-4a81-99ef-5d383d055d8d"
    ]
}
```

**返回结果示例:** 参见<a href="docs.html#/server-api/org/syncRule.md" target="_blank">输出结果</a>，如果删除组织全部成功，则data里返回[]，如果有未删除成功的，则data中会有删除失败的具体信息，，其中data字段格式如下：

```json
[{
    "msgId":String, //组织id
    "msgCode":int, //消息码
    "msg":String //消息
},…]
```

## 设置隐藏部门或部门仅可见

**描述:** 批量设置隐藏部门或者部门仅可见部门，隐藏部门即其他部门人员将无法从通讯录中看到该部门的人员信息；部门仅可见即限制该部门人员不可查看其他部门人员，该部门人员从通讯录仅可看到该部门的人员信息。

**URL:** `https://www.yunzhijia.com/gateway/openimport/open/company/setOrgSecret?accessToken=xxxxxx`

**请求方法：** `post`

**内容类型：** `Content-Type: application/x-www-form-urlencoded`

**输入参数:** 

`nonce`: String // 非必填，用于校验重复请求的随机字符串

`eid`: Number // 必填，企业id

`data`: String // 必填，业务数据json字符串


> 请注意，`data` 不应是js对象而应是一个JSON格式的字符串， 即用JSON.stringify()处理以下结构对象获得的字符串：


```json
[
    {
    "commitId": String, //唯一标识一次提交，可自行选取，保证不重复即可
    "orgId": String, //部门ID
    "type": String, //类型，HIDE:隐藏部门；VISI:部门仅可见。
    "status": boolean //状态，true:开启；false：关闭
    }
]
```
**请求示例：**
```url
https://www.yunzhijia.com/gateway/openimport/open/company/setOrgSecret?accessToken=xxxxxx
```

```form
nonce:abcxyXXXXzefg

eid:17951708

data:[
    {
        "commitId": "111345", 
        "orgId": "4fcfba72-e730-4deb-b327-7a2d5c9443ff", 
        "type": "VISI", 
        "status": true
    }
]
```

**返回结果示例:** 参见<a href="docs.html#/server-api/org/syncRule.md" target="_blank">输出结果</a>，如果全部设置成功，则data里返回[]，如果有未设置成功的，则data中会有设置失败的具体信息，，其中data字段格式如下：

```json
[
    { //只有在有失败数据时返回
      "commitId": String, //提交ID
      "errorMsg": String //此处标识失败原因
    }
]
```

## 查询设置隐藏部门或者部门仅可见部门

**描述:** 查询隐藏部门或者部门仅可见的部门信息

**URL:** `https://www.yunzhijia.com/gateway/openimport/open/company/queryOrgSecret?accessToken=xxxxxx`

**请求方法：** `post`

**内容类型：** `Content-Type: application/x-www-form-urlencoded`

**输入参数:** 

`nonce`: String // 非必填，用于校验重复请求的随机字符串

`eid`: Number // 必填，企业id

`data`: String // 必填，业务数据json字符串


> 请注意，`data` 不应是js对象而应是一个JSON格式的字符串， 即用JSON.stringify()处理以下结构对象获得的字符串：


```json
{
    "type": String, //查询类型，HIDE:隐藏部门;VISI:部门仅可见
    "begin": int, // 起始
    "count": int // 条数
}
```

**请求示例：**
```url
https://www.yunzhijia.com/gateway/openimport/open/company/queryOrgSecret?accessToken=xxxxxx
```

```form
nonce:abcxyXXXXzefg

eid:17951708

data:{
    "type": "VISI", 
    "begin": 1, 
    "count": 20
}
```

**返回结果示例:**

```json
{
    "success": true,
    "error": "",
    "errorCode": 100,
    "data": [
        {
            "id": "department", 
            "department": "A产品事业部",  //组织名称
            "orgId": "4fcfba72-e730-4deb-b327-7a2d5c9443ff"  //组织Id
        },
        {
            "id": "department",
            "department": "研发中心\\宇宙级平台产品部\\创意部",
            "orgId": "d66340ca-56ac-443d-b3a3-d9607e81cbba"  
        }
        ...
    ]
}
```

## 更新组织排序码

**描述:** 更新组织排序，如果更新失败，会返回失败的orgid，更新成功data为空；

**URL:** `https://www.yunzhijia.com/gateway/openimport/open/dept/updateWeightsById?accessToken=xxxxxx`

**请求方法：** `post`

**内容类型：** `Content-Type: application/x-www-form-urlencoded`

**输入参数:** 

`nonce`: String // 非必填，用于校验重复请求的随机字符串

`eid`: Number // 必填，企业id

`data`: String // 必填，业务数据json字符串


> 请注意，`data` 不应是js对象而应是一个JSON格式的字符串， 即用JSON.stringify()处理以下结构对象获得的字符串：


```json
{
    "departments": [
        {
            "orgId": string, //部门ID
            "weights": string //排序码
        },
        ...
}
```

**请求示例：**
```url
https://www.yunzhijia.com/gateway/openimport/open/dept/updateWeightsById?accessToken=xxxxxx
```

```form
nonce:abcxyXXXXzefg

eid:17951708

data:{
    "departments": [
        {
            "orgId": "42061c1f-496d-45c2-b5c2-387a3a534261", 
            "weights": "0"
        }, 
        {
            "orgId": "4fcfba72-e730-4deb-b327-7a2d5c9443ff", 
            "weights": "1"
        }
    ]
}
```

**返回结果示例:** 参见<a href="docs.html#/server-api/org/syncRule.md" target="_blank">输出结果</a>，如果全部更新成功，则data里返回[]，如果有更新失败的，则data中会有更新失败的具体信息，其中data字段格式如下：
```json
[
    {
        "msgId": "20fcf4bc-3fdf-4d07-887f-923e3cda2c2", //消息ID
        "msgCode": "221",
        "msg": "部门ID不存在"
    }
]
```
## 添加机密组织可见部门

**描述:** 根据部门Id添加机密组织可见部门，所设置部门需已设置机密组织，否则添加失败；

**注:** 对于一个机密组织最多支持添加200个部门白名单；

**URL:** `https://www.yunzhijia.com/gateway/openimport/open/dept/addOrgSecretDeptWhitelist?accessToken=xxxxxx`

**请求方法：** `post`

**内容类型：** `Content-Type: application/x-www-form-urlencoded`

**输入参数:** 

`nonce`: String // 非必填，用于校验重复请求的随机字符串

`eid`: Number // 必填，企业id

`data`: String // 必填，业务数据json字符串


> 请注意，`data` 不应是js对象而应是一个JSON格式的字符串， 即用JSON.stringify()处理以下结构对象获得的字符串：


```json
{
    "eid":String, //企业eid
    "orgId":String, //机密组织部门id
    "secretType":int, //必须，机密组织部门对应类型，1表示隐藏部门，2表示限制该部门人员不可查看其他部门
    "whiteOrgIds":[String,...]  //必填,部门白名单的orgId数组（一次最多支持200个orgId）,用“,”号隔开
}
```

**请求示例：**
```url
https://www.yunzhijia.com/gateway/openimport/open/dept/addOrgSecretDeptWhitelist?accessToken=xxxxxx
```

```form
nonce:abcxyXXXXzefg

eid:17951708

data:{
    "eid":"50006752",
    "orgId":"daeb55ac-4ec1-4c03-bc93-9fbd9a5ae2fa",
    "secretType":1,
    "whiteOrgIds":["625b1201-8480-41e0-949c-4e300238caca","79a9f86c-9db2-4ab2-95c1-ea3359e72434"]
}
```

**返回结果示例:** 
```json
{
    "success": true,
    "error": "",
    "errorCode": 100,
    "data": ""
}
```
## 删除机密组织可见部门

**描述:** 根据部门Id删除机密组织可见部门，所设置部门需已设置机密组织，否则删除失败；

**注:** 对于一个机密组织最多支持传入200个部门白名单；

**URL:** `https://www.yunzhijia.com/gateway/openimport/open/dept/deleteOrgSecretDeptWhitelist?accessToken=xxxxxx`

**请求方法：** `post`

**内容类型：** `Content-Type: application/x-www-form-urlencoded`

**输入参数:** 

`nonce`: String // 非必填，用于校验重复请求的随机字符串

`eid`: Number // 必填，企业id

`data`: String // 必填，业务数据json字符串


> 请注意，`data` 不应是js对象而应是一个JSON格式的字符串， 即用JSON.stringify()处理以下结构对象获得的字符串：


```json
{
    "eid":String, //企业eid
    "orgId":String, //机密组织部门id
    "secretType":int, //必须，机密组织部门对应类型，1表示隐藏部门，2表示限制该部门人员不可查看其他部门
    "whiteOrgIds":[String,...]  //必填,部门白名单的orgId数组（一次最多支持200个orgId）,用“,”号隔开
}
```

**请求示例：**
```url
https://www.yunzhijia.com/gateway/openimport/open/dept/addOrgSecretDeptWhitelist?accessToken=xxxxxx
```

```form
nonce:abcxyXXXXzefg

eid:17951708

data:{
    "eid":"50006752",
    "orgId":"daeb55ac-4ec1-4c03-bc93-9fbd9a5ae2fa",
    "secretType":1,
    "whiteOrgIds":["625b1201-8480-41e0-949c-4e300238caca","79a9f86c-9db2-4ab2-95c1-ea3359e72434"]
}
```

**返回结果示例:** 
```json
{
    "success": true,
    "error": "",
    "errorCode": 100,
    "data": ""
}
```

## 部门多语言-查询所支持语言

**描述:** 根据接口获取平台当下支持哪些我多语言；

**URL:** `https://www.yunzhijia.com/gateway/gateway/openimport/open/orgLang/findOrgLangModels?accessToken=xxxxxx`

**请求方法：** `post`

**内容类型：** `Content-Type: application/x-www-form-urlencoded`

**输入参数:**  无需参数

**请求示例：**
```url
https://www.yunzhijia.com/gateway/openimport/open/orgLang/findOrgLangModels?accessToken=xxxxxx
```
**返回结果示例:** 
```json
{
    "data": [
        {
            "name": "简体中文",
            "id": "68d3c54f02aaa50d9ccbf912",
            "type": "zh-CN",
            "langSort": 1
        },
        {
            "name": "繁體中文",
            "id": "68d3c54f02aaa50d9ccbf913",
            "type": "zh-HK",
            "langSort": 2
        },
        {
            "name": "English",
            "id": "68d3c54f02aaa50d9ccbf914",
            "type": "en-US",
            "langSort": 3
        }
    ],
    "success": true,
    "errorCode": 200,
    "error": "success"
}
```

## 部门多语言-获取某个部门多语言信息

**描述:** 根据部门Id获取某个部门的多语言信息

**URL:** `https://www.yunzhijia.com/gateway/openimport/open/orgLang/findOrgLangByOrgId?accessToken=xxxxxx`

**请求方法：** `post`

**内容类型：** `Content-Type: application/x-www-form-urlencoded`

**输入参数:** 

`nonce`: String // 非必填，用于校验重复请求的随机字符串

`eid`: Number // 必填，企业id

`orgId`: String // 必填,部门id

**请求示例：**
```url
https://www.yunzhijia.com/gateway/openimport/open/orgLang/findOrgLangByOrgId?accessToken=xxxxxx
```

```form
nonce:abcxyXXXXzefg

eid:xxxxxx

orgId:xxxxx
```

**返回结果示例:** 
```json
{
    "data": {
        "orgId": "75339488-209f-48bb-beaf-0ca730dbcd6b",
        "langInfos": [
            {
                "langKey": "简体中文",
                "langValue": null,
                "langId": "68d3c54f02aaa50d9ccbf912"
            },
            {
                "langKey": "繁體中文",
                "langValue": null,
                "langId": "68d3c54f02aaa50d9ccbf913"
            },
            {
                "langKey": "English",
                "langValue": null,
                "langId": "68d3c54f02aaa50d9ccbf914"
            }
        ]
    },
    "success": true,
    "errorCode": 200,
    "error": "success"
}
```

## 部门多语言-保存多语言部门信息

**描述:** 保存多语言部门信息

**URL:** `https://www.yunzhijia.com/gateway/openimport/open/orgLang/saveOrgLang?accessToken=xxxxxx`

**请求方法：** `post`

**内容类型：** `Content-Type: application/x-www-form-urlencoded`

**输入参数:** 

`nonce`: String // 非必填，用于校验重复请求的随机字符串

`eid`: Number // 必填，企业id

`data`: String // 必填，业务数据json字符串


> 请注意，`data` 不应是js对象而应是一个JSON格式的字符串， 即用JSON.stringify()处理以下结构对象获得的字符串：


```json
{"orgId":"75339488-209f-48bb-beaf-0ca730dbcd6b","langInfo":[{"langId":"68d3c54f02aaa50d9ccbf913","langName":"研发中心繁体"},{"langId":"68d3c54f02aaa50d9ccbf914","langName":"developer"}]}
```

**请求示例：**
```url
https://www.yunzhijia.com/gateway/openimport/open/orgLang/saveOrgLang?accessToken=xxxxxx
```

```form
nonce:abcxyXXXXzefg

eid:xxxxx

data:{"orgId":"75339488-209f-48bb-beaf-0ca730dbcd6b","langInfo":[{"langId":"68d3c54f02aaa50d9ccbf913","langName":"研发中心繁体"},{"langId":"68d3c54f02aaa50d9ccbf914","langName":"developer"}]}
```

**返回结果示例:** 
```json
{
    "data": null,
    "success": true,
    "errorCode": 200,
    "error": "success"
}
```
# FAQ

## API测试工具Postman调用示例

查询全部组织信息:

![查询全部组织信息](/opendocs/file/image/a2a2bc2b21aadd1de071b60a4473085b)

新增组织：

![新增组织](/opendocs/file/image/a840e679f4ff3c36bb28ccc7fefdc5fd)