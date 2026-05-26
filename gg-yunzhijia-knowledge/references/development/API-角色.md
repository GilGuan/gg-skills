---
domain: development
module: 组织人员
keywords: [IM, accessToken, appId, person, role]
---

# 角色API列表

> 来源：开放平台线上文档 (https://open.yunzhijia.com/opendocs/docs/server-api/org/role.md)

# 角色API列表



### 接口授权 

本页接口使用 `resGroupSecret` 级别的 `AccessToken`， 与获取组织数据的接口不同，请注意区分。

请在 `管理中心-系统设置-系统集成-通讯录同步` 中，复制 `只读秘钥` 或者 `可编辑秘钥`， 然后调用系统接口换取 `AccessToken`。

> 只读秘钥：只能调用查询类的接口

> 可编辑秘钥：可以调用全部接口

如果您还不了解如何获取AccessToken，请<a href="docs.html#/server-api/auth/oauth" target="_blank">点击此处</a>

**接口列表**

| 接口名称                   | URL                                                                                         | 备注 |
|:---------------------------|:--------------------------------------------------------------------------------------------|:-----|
| 添加角色标签               | [/gateway/openimport/open/roletag/addRoleTag](#添加角色标签)                                |      |
| 获取工作圈角色标签列表     | [/gateway/openimport/open/roletag/getCompanyRoleTag](#获取工作圈角色标签列表)               |      |
| 删除角色标签               | [/gateway/openimport/open/roletag/deleteRoleTag](#删除角色标签)                             |      |
| 更改角色标签名字           | [/gateway/openimport/open/roletag/updateRoleTag](#更改角色标签名字)                         |      |
| 设置人员角色标签           | [/gateway/openimport/open/roletag/setPersonRoleTag](#设置人员角色标签)                      |      |
| 删除人员角色标签           | [/gateway/openimport/open/roletag/deletePersonRoleTag](#删除人员角色标签)                   |      |
| 根据角色获取人员           | [/gateway/openimport/open/roletag/getPersonByRole](#根据角色获取人员)                       |      |
| 根据用户id批量设置人员角色 | [/gateway/openimport/open/roletag/batchSetPersonRoleTag](#根据用户id批量设置人员角色)       |      |
| 根据角色id批量设置人员角色 | [/gateway/openimport/open/roletag/batchSetPersonRoleTag_other](#根据角色id批量设置人员角色)  ||
| 根据角色Id分页获取人员 | [/gateway/openimport/open/roletag/getPersonsByRoleAndPage](#根据角色Id分页获取人员) |      ||
| 根据用户id批量获取人员角色 | [/gateway/openimport/open/roletag/batchGetPersonRoleTags](#根据用户id批量获取人员角色) |      ||


**输入参数说明如下：**

| 字段名 | 数据类型 | 是否必填 | 说明                                  |
| ------ | -------- | -------- | ------------------------------------- |
| nonce  | String   | 否       | 校验重复请求,格式为16位以内随机字符串 |
| eid    | String   | 是       | 注册企业团队id                        |
| data   | String   | 是       | 业务数据,json字符串格式               |


## 添加角色标签

**URL:** `https://www.yunzhijia.com/gateway/openimport/open/roletag/addRoleTag?accessToken=xxxxxx`

**请求方法：** `post`

**内容类型：** `Content-Type: application/x-www-form-urlencoded`

**输入参数:** 

`nonce`: String // 非必填，用于校验重复请求的随机字符串

`eid`: Number // 必填，企业id

`data`: String // 必填，业务数据json字符串


> 请注意，`data` 不应是js对象而应是一个JSON格式的字符串， 即用JSON.stringify()处理以下结构对象获得的字符串：


```json
{
    "eid": "2704254", //可选，如果没有，则以外面的eid参数为准
    "roleName": "接口测试角色2"
}
```

**请求示例：**
```url
https://www.yunzhijia.com/gateway/openimport/open/roletag/addRoleTag?accessToken=xxxxxx
```

```form
nonce:abcxyXXXXzefg

eid:17951708

data:{
    "eid": "17951708", 
    "roleName": "音乐协会会长"
}
```

**返回结果示例:** 
```json
{
    "success": true,
    "error": "",
    "errorCode": 100,
    "data": {
        "id": "23994eb3-79b6-43a7-b6f1-0e1428fcf50d"  //角色id,请保存
    }
}
```

## 获取工作圈角色标签列表

**URL:** `https://www.yunzhijia.com/gateway/openimport/open/roletag/getCompanyRoleTag?accessToken=xxxxxx`

**请求方法：** `post`

**内容类型：** `Content-Type: application/x-www-form-urlencoded`

**输入参数:** 

`nonce`: String // 非必填，用于校验重复请求的随机字符串

`eid`: Number // 必填，企业id

`data`: String // 必填，业务数据json字符串


> 请注意，`data` 不应是js对象而应是一个JSON格式的字符串， 即用JSON.stringify()处理以下结构对象获得的字符串：


```json
{
    "eid": "17951708" //必选，企业id
}
```

**请求示例：**
```url
https://www.yunzhijia.com/gateway/openimport/open/roletag/getCompanyRoleTag?accessToken=xxxxxx
```

```form
nonce:abcxyXXXXzefg

eid:17951708

data:{
    "eid": "17951708", 
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
            "eid": "17951708",  //如果是企业自定义标签，就会有值,工作圈id
            "rolename": "党委宣传委员",  //角色名称
            "createPersonId": "",  //创建人id
            "type": 40,  //标签类型，10系统标签，20 自建应用标签，30 第三方应用标签,40 企业自定义标签
            "customField": "",
            "parentId": "85484a25-14fe-11ea-a634-ecf4bbea149a",
            "personCount": "1",
            "createTime": "Dec 18, 2019 10:14:43 AM",
            "appId": "SYS",  //如果是第三方应用创建，appid就会有值
            "isCommon": 0,  //是否系统常用标签
            "isgroup": 0,
            "id": "cd237014-0ef2-4909-9d37-f28617343ae8",  //角色id
            "lastUpdateTime": "Dec 18, 2019 10:14:43 AM"
        },
        {
            "eid": "17951708",
            "rolename": "音乐协会会长",
            "createPersonId": "",
            "type": 40,
            "customField": "",
            "parentId": "85484a25-14fe-11ea-a634-ecf4bbea149a",
            "personCount": "0",
            "createTime": "Jan 3, 2020 9:29:57 AM",
            "appId": "SYS",
            "isCommon": 0,
            "isgroup": 0,
            "id": "23994eb3-79b6-43a7-b6f1-0e1428fcf50d",
            "lastUpdateTime": "Jan 3, 2020 9:29:57 AM"
        },
        ...
    ]
}
```

## 删除角色标签

**URL:** `https://www.yunzhijia.com/gateway/openimport/open/roletag/deleteRoleTag?accessToken=xxxxxx`

**请求方法：** `post`

**内容类型：** `Content-Type: application/x-www-form-urlencoded`

**输入参数:** 

`nonce`: String // 非必填，用于校验重复请求的随机字符串

`eid`: Number // 必填，企业id

`data`: String // 必填，业务数据json字符串


> 请注意，`data` 不应是js对象而应是一个JSON格式的字符串， 即用JSON.stringify()处理以下结构对象获得的字符串：


```json
{
    "eid": "2704254", //可选，如果没有，则以外面的eid参数为准
    "roleId":"a20b2811-fda4-11e6-8f64-82e47cc7294a"   //角色id
}
```

**请求示例：**
```url
https://www.yunzhijia.com/gateway/openimport/open/roletag/deleteRoleTag?accessToken=xxxxxx
```

```form
nonce:abcxyXXXXzefg

eid:17951708

data:{
    "eid": "2704254", 
    "roleId": "dcafc731-f3bc-47d0-b41e-86612b973bb2"
}
```

**输出参数示例:** 
```json
{
    "success": true,
    "error": "",
    "errorCode": 100,
    "data": ""
}
```

## 更改角色标签名字

**URL:** `https://www.yunzhijia.com/gateway/openimport/open/roletag/updateRoleTag?accessToken=xxxxxx`

**请求方法：** `post`

**内容类型：** `Content-Type: application/x-www-form-urlencoded`

**输入参数:** 

`nonce`: String // 非必填，用于校验重复请求的随机字符串

`eid`: Number // 必填，企业id

`data`: String // 必填，业务数据json字符串


> 请注意，`data` 不应是js对象而应是一个JSON格式的字符串， 即用JSON.stringify()处理以下结构对象获得的字符串：


```json
{
    "eid": "2704254", //可选，如果没有，则以外面的eid参数为准
    "roleId": "acca7a9d-f4bd-11e6-8f64-82e47cc7294a",  //角色id
    "roleName": "测试角色3"  //角色名称
}
```

**请求示例：**
```url
https://www.yunzhijia.com/gateway/openimport/open/roletag/updateRoleTag?accessToken=xxxxxx
```

```form
nonce:abcxyXXXXzefg

eid:17951708

data:{
    "eid": "17951708", 
    "roleId": "7cfa8a0c-e420-4116-a132-03b00b317264", 
    "roleName": "吉他协会会长"
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


## 设置人员角色标签

**URL:** `https://www.yunzhijia.com/gateway/openimport/open/roletag/setPersonRoleTag?accessToken=xxxxxx`

**请求方法：** `post`

**内容类型：** `Content-Type: application/x-www-form-urlencoded`

**输入参数:** 

`nonce`: String // 非必填，用于校验重复请求的随机字符串

`eid`: Number // 必填，企业id

`data`: String // 必填，业务数据json字符串


> 请注意，`data` 不应是js对象而应是一个JSON格式的字符串， 即用JSON.stringify()处理以下结构对象获得的字符串：


```json
{
    "eid": "2704254",
    "roleId": "2d69412f-8de5-11e6-961a-82e47cc7294a",  //角色id
    "openId": "580d9fa000b0911f84defd18",  //用户openid
    "orgIds": "02008582-08dc-40a0-8d5b-c693f73d2798,    03c70e4b-5e10-11e6-961a-82e47cc7294a" //设置作用范围（组织id）,多个组织之间“,”号分隔--(包含子部门)
}
```
**请求示例：**
```url
https://www.yunzhijia.com/gateway/openimport/open/roletag/setPersonRoleTag?accessToken=xxxxxx
```

```form
nonce:abcxyXXXXzefg

eid:17951708

data:{
    "eid": "17951708", 
    "roleId": "7cfa8a0c-e420-4116-a132-03b00b317264", 
    "openId": "5df86ebbe4b0b7058a9efc3d", 
    "orgIds": "4fcfba72-e730-4deb-b327-7a2d5c9443ff,66f89456-22e9-4ab8-8261-f70a8fe3a648"
}
```

**返回结果示例:** 
```josn
{
    "success": true,
    "error": "",
    "errorCode": 100,
    "data": ""
}
```

## 删除人员角色标签

**URL:** `https://www.yunzhijia.com/gateway/openimport/open/roletag/deletePersonRoleTag?accessToken=xxxxxx`

**请求方法：** `post`

**内容类型：** `Content-Type: application/x-www-form-urlencoded`

**输入参数:** 

`nonce`: String // 非必填，用于校验重复请求的随机字符串

`eid`: Number // 必填，企业id

`data`: String // 必填，业务数据json字符串


> 请注意，`data` 不应是js对象而应是一个JSON格式的字符串， 即用JSON.stringify()处理以下结构对象获得的字符串：


```json
{
    "eid": "2704254",  //工作圈eid
    "roleId": "2d69412f-8de5-11e6-961a-82e47cc7294a",  //角色id
    "openId": "580d9fa000b0911f84defd18"  //用户openid
}
```
**请求示例：**
```url
https://www.yunzhijia.com/gateway/openimport/open/roletag/deletePersonRoleTag?accessToken=xxxxxx
```

```form
nonce:abcxyXXXXzefg

eid:17951708

data:{
    "eid": "17951708", 
    "roleId": "7cfa8a0c-e420-4116-a132-03b00b317264", 
    "openId": "5df86ebbe4b0b7058a9efc3d", 
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

## 根据角色获取人员（不建议使用此接口，建议使用本页1.10接口）

**URL:** `https://www.yunzhijia.com/gateway/openimport/open/roletag/getPersonByRole?accessToken=xxxxxx`

**请求方法：** `post`

**内容类型：** `Content-Type: application/x-www-form-urlencoded`

**输入参数:** 

`nonce`: String // 非必填，用于校验重复请求的随机字符串

`eid`: Number // 必填，企业id

`data`: String // 必填，业务数据json字符串


> 请注意，`data` 不应是js对象而应是一个JSON格式的字符串， 即用JSON.stringify()处理以下结构对象获得的字符串：


```json
{
    "eid": "2704254",  //可选 
    "roleId": "2d69412f-8de5-11e6-961a-82e47cc7294a"  //角色id
}
```
**请求示例：**
```url
https://www.yunzhijia.com/gateway/openimport/open/roletag/getPersonByRole?accessToken=xxxxxx
```

```form
nonce:abcxyXXXXzefg

eid:17951708

data:{
    "eid": "17951708", 
    "roleId": "7cfa8a0c-e420-4116-a132-03b00b317264", 
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
            "orgIds": "66f89456-22e9-4ab8-8261-f70a8fe3a648,4fcfba72-e730-4deb-b327-7a2d5c9443ff",  //作用范围(包含子部门)
            "openId": "5df86ebbe4b0b7058a9efc3d"  //用户openid
        }
    ]
}
```

## 根据用户id批量设置人员角色

**URL:**`https://www.yunzhijia.com/gateway/openimport/open/roletag/batchSetPersonRoleTag?accessToken=xxxxxx`

**请求方法：** `post`

**内容类型：** `Content-Type: application/x-www-form-urlencoded`

**输入参数:** 

`nonce`: String // 非必填，用于校验重复请求的随机字符串

`eid`: Number // 必填，企业id

`data`: String // 必填，业务数据json字符串


> 请注意，`data` 不应是js对象而应是一个JSON格式的字符串， 即用JSON.stringify()处理以下结构对象获得的字符串：


```json
{
    "eid": "332165", //可选
    "operate": "insert",//operate标志是添加角色/删除 insert/delete
    "roleTags": [
        {
            "openId": "580d9fa000b0911f84defd18",
            "roleOrgs": [
                {
                    "roleId": "2d69412f-8de5-11e6-961a-82e47cc7294a",
                    "orgids": [
                        "938fe848-c73c-4331-b883-144c8b9d3a06", //作用范围1(包含子部门)
                        "03c70e4b-5e10-11e6-961a-82e47cc7294a" //作用范围2(包含子部门)
                    ]
                },... // 批量操作，针对这个用户（openId），分配不同的角色（roleId）以及开通范围。不同的角色传成数组
            ]
        },... // 批量操作，不同的用户（openid）传成数组
    ]
}
```
**请求示例：**
```url
https://www.yunzhijia.com/gateway/openimport/open/roletag/batchSetPersonRoleTag?accessToken=xxxxxx
```

```form
nonce:abcxyXXXXzefg

eid:17951708

data:{
    "eid": "17951708", 
    "operate": "insert", 
    "roleTags": [
        {
            "openId": "5df87378e4b013c7ff844226", 
            "roleOrgs": [
                {
                    "roleId": "7cfa8a0c-e420-4116-a132-03b00b317264", 
                    "orgids": [
                        "c37d2483-18c5-4e8b-b89f-1bc7eb862ced", 
                        "66f89456-22e9-4ab8-8261-f70a8fe3a648"
                    ]
                }
            ]
        }
    ]
}
```

**返回结果示例:** 
```text
{
    "success": true,
    "error": "",
    "errorCode": 100,
    "data": ""
}
```

## 根据角色id批量设置人员角色

**URL:**`https://www.yunzhijia.com/gateway/openimport/open/roletag/batchSetPersonRoleTag_other?accessToken=xxxxxx`

**请求方法：** `post`

**内容类型：** `Content-Type: application/x-www-form-urlencoded`

**输入参数:** 

`nonce`: String // 非必填，用于校验重复请求的随机字符串

`eid`: Number // 必填，企业id

`data`: String // 必填，业务数据json字符串


> 请注意，`data` 不应是js对象而应是一个JSON格式的字符串， 即用JSON.stringify()处理以下结构对象获得的字符串：


```json
{
    "eid": "332165", //可选
    "operate": "insert",
    "roleTags": [
        {
            "roleId": "2d69412f-8de5-11e6-961a-82e47cc7294a",
            "personOrgs": [
                {
                    "openId": "580d9fa000b0911f84defd18",
                    "orgids": [
                        "938fe848-c73c-4331-b883-144c8b9d3a06", //作用范围1(包含子部门)
                        "03c70e4b-5e10-11e6-961a-82e47cc7294a" //作用范围2(包含子部门)
                    ]
                },... //批量操作，针对这个角色（roleId），分配不同的用户（openId），不同的用户传成数组
            ]
        },... //批量操作，不同的角色（roleId）传成数组
    ]
}
```
**请求示例：**
```url
https://www.yunzhijia.com/gateway/openimport/open/roletag/batchSetPersonRoleTag_other?accessToken=xxxxxx
```

```form
nonce:abcxyXXXXzefg

eid:17951708

data:{
    "eid": "17951708", 
    "operate": "insert", 
    "roleTags": [
        {
            "roleId": "85484a25-14fe-11ea-a634-ecf4bbea149a", 
            "personOrgs": [
                {
                    "openId": "5e0d9cd2e4b02b68c7c5b6ac", 
                    "orgids": [
                        "11e11baa-d74a-44df-b511-2b0b58d2a19e", 
                        "c37d2483-18c5-4e8b-b89f-1bc7eb862ced"
                    ]
                }
            ]
        }
    ]
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

## 根据角色Id分页获取人员

**URL:**`https://www.yunzhijia.com/gateway/openimport/open/roletag/getPersonsByRoleAndPage?accessToken=xxxxxx`

**请求方法：** `post`

**内容类型：** `Content-Type: application/x-www-form-urlencoded`

**输入参数:** 

`nonce`: String // 非必填，用于校验重复请求的随机字符串

`eid`: Number // 必填，企业id

`data`: String // 必填，业务数据json字符串


> 请注意，`data` 不应是js对象而应是一个JSON格式的字符串， 即用JSON.stringify()处理以下结构对象获得的字符串：


```json
{
    "eid": "2704254", //可选
    "roleId": "2d69412f-8de5-11e6-961a-82e47cc7294a",
	"begin"：0, //可选，默认为0 （第几页，如：第一页传0，第二页传1）
	"count"：100 // 可选，默认为100
}
```
**请求示例：**
```url
https://www.yunzhijia.com/gateway/openimport/open/roletag/getPersonsByRoleAndPage?accessToken=xxxxxx
```

```form
nonce:abcxyXXXXzefg

eid:17951708

data:{
    "eid": "17951708", 
    "roleId": "23994eb3-79b6-43a7-b6f1-0e1428fcf50d", 
    "begin": 0, 
    "count": 100
}
```

**返回结果示例:**

```json
{
    "success": true,
    "error": "",
    "errorCode": 100,
    "data": [  //人员列表信息
        {
            "orgIds": "66f89456-22e9-4ab8-8261-f70a8fe3a648,  //作用范围    4fcfba72-e730-4deb-b327-7a2d5c9443ff",
            "openId": "5df86ebbe4b0b7058a9efc3d"  //用户openid
        },
        {
            "orgIds": "66f89456-22e9-4ab8-8261-f70a8fe3a648,c37d2483-18c5-4e8b-b89f-1bc7eb862ced",
            "openId": "5df87378e4b013c7ff844226"
        }
    ]
}
```

## 根据用户id批量获取人员角色

**URL:**`https://www.yunzhijia.com/gateway/openimport/open/roletag/batchGetPersonRoleTags?accessToken=xxxxxx`

**请求方法：** `post`

**内容类型：** `Content-Type: application/x-www-form-urlencoded`

**输入参数:** 

`nonce`: String // 非必填，用于校验重复请求的随机字符串

`eid`: Number // 必填，企业id

`data`: String // 必填，业务数据json字符串


> 请注意，`data` 不应是js对象而应是一个JSON格式的字符串， 即用JSON.stringify()处理以下结构对象获得的字符串：


```json
{
    "eid": "4141719", //可选，如果没有，则以外面的eid参数为准
    "openIds": ["62621f42e4b04f05f13bc53d"]
}
```
**请求示例：**
```url
https://www.yunzhijia.com/gateway/openimport/open/roletag/batchGetPersonRoleTags?accessToken=xxxxxx
```

```form
nonce:abcxyXXXXzefg

eid:17951708

data:{
    "eid": "4141719",
    "openIds": ["5f10250be4b076350f1ec32c"]
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
            "openId": "62621f42e4b04f05f13bc53d",
            "roles": [
                {
                    "roleId": "2a418ab5-4013-407e-a9cb-37128ded88d2",
                    "roleName": "总监"
                }
            ]
        }
    ]
}
```
## FAQ

暂无