---
domain: development
module: 组织人员
keywords: [IM, accessToken, appId, person, role]
---

# 获取组织人员角色数据—app级授权

> 来源：开放平台线上文档 (https://open.yunzhijia.com/opendocs/docs/server-api/org/index.md)

# 获取组织人员角色数据—app级授权

### 接口授权

本部分接口使用 `app` 级别的 `AccessToken`，与同步组织数据接口不同，请注意区分。

如果您还不了解如何获取AccessToken，请<a href="docs.html#/server-api/auth/oauth" target="_blank">点击此处</a>

###  企业所有组织人员

**URL:**`https://www.yunzhijia.com/gateway/opendata-control/data/getallpersons?accessToken=xxxxxxxxx`

**http请求方法：** `post`

**http内容类型：** `application/x-www-form-urlencoded`

**输入参数:**

参数名 | 数据类型 | 是否必传 | 说明
-------|----------|----------|--------------------------------------------------------------------------------------------------------------------------------------------------
eid    | string   | 必传 | 需要拉取数据的企业
time   | String   | 必传 | 查询时间，查询这个时刻之后所有变更的数据，第一次拉取时，传递`2008-08-02 01:40:38`。格式为24小时制，如Java中的`yyyy-MM-dd HH:mm:ss`
begin  | Integer  | 可选 | 默认0
count  | Integer  | 可选 | 默认1000，每次拉取限制1000条以内（包括1000条），如果返回条数不足count条，表示分页拉取已结束

**请求示例：**
```url
https://www.yunzhijia.com/gateway/opendata-control/data/getallpersons?accessToken=xxxxxxxxx
```

```form
eid:17951708
time:2019-12-01 01:40:29
begin:0
count:1000
```

**返回结果:**

```json
{
    "success": true,
    "error": null,
    "errorCode": 100,
    "data": {
        "persons": [
            {
                "photoUrl": "http://static.yunzhijia.com/space/c/photo/load?id=5dc22499a372591da29c50a7",
                "gender": "1",
                "openId": "5de50017e4b0b2767b870423",
                "jobTitle": "",
                "jobNo": "",
                "name": "印*",
                "globalId": "5bc159e3e4b036230d719547",
                "isAdmin": "1",
                "department": "运营管理部",
                "orgId": "11e11baa-d74a-44df-b511-2b0b58d2a19e",
                "status": "1"
            },
            {
                "photoUrl": "http://static.yunzhijia.com/space/c/photo/load?id=5d7a0e7d6d67ff3ad38c25d3",
                "gender": "1",
                "openId": "5de5003fe4b0b998f379a05e",
                "jobTitle": "",
                "jobNo": "",
                "name": "cym",
                "globalId": "5ba1fbabe4b0001ffdaa7be4",
                "isAdmin": "0",
                "department": "B产品事业部",
                "orgId": "c37d2483-18c5-4e8b-b89f-1bc7eb862ced",
                "status": "1"
            }
            ...
        ],
        "time": "2019-12-19 13:50:57" //与传入参数格式一致，表示本次拉取数据的截止时刻
    }
}

```

**说明:**

- 同一个openId多次出现的问题：这是一个增量事件接口，它拉取的不单是整个企业的人员情况，只包括time时刻点到当前时刻的变更的人员情况，因此，出现openId重复的情况，应当用后续数据更新已经存在的openId人员信息。

###  个人信息

**URL:**`https://www.yunzhijia.com/gateway/opendata-control/data/getperson?accessToken=xxxxxxxxx`

**http请求方法：** `post`

**http内容类型：** `application/x-www-form-urlencoded`

**输入参数:**

参数名 | 数据类型 | 是否必传 | 说明
-------|----------|----------|--------
openId | String   | 是       | 人员ID
eid    | String   | 是       | 企业ID

**请求示例：**
```url
https://www.yunzhijia.com/gateway/opendata-control/data/getperson?accessToken=xxxxxxxxx
```

```form
openId:5de50017e4b0b2767b870423
eid:17951708
```

**返回结果:**

```json
{
    success: Boolean,
    error: String,
    errorCode: Integer,
    data: [
        {
            "photoUrl": "http://static.yunzhijia.com/space/c/photo/load?id=5dc22499a372591da29c50a7",
            "gender": "1",
            "openId": "5de50017e4b0b2767b870423",
            "jobTitle": "",
            "jobNo": "",
            "name": "印*",
            "globalId": "5bc159e3e4b036230d719547",
            "isAdmin": "1",
            "department": "运营管理部",
            "orgId": "11e11baa-d74a-44df-b511-2b0b58d2a19e",
            "status": "1"
        }
    ]
}

```

###  获取当前部门基本信息或部门负责人

**URL:**`https://www.yunzhijia.com/gateway/opendata-control/data/getorg?accessToken=xxxxxxxxx`

**http请求方法：** `post`

**http内容类型：** `application/x-www-form-urlencoded`

**输入参数:**

参数名 | 数据类型 | 是否必传 | 说明
-------|----------|----------|--------
orgId  | String   | 是       | 部门ID
eid    | String   | 是       | 企业ID

**请求示例：**
```url
https://www.yunzhijia.com/gateway/opendata-control/data/getorg?accessToken=xxxxxxxxx
```

```form
orgId:4fcfba72-e730-4deb-b327-7a2d5c9443ff
eid:17951708
```

**返回结果:**

```json
{
    "success": true,
    "error": null,
    "errorCode": 100,
    "data": {
        "inChargers": [ //负责人信息
            {
                "photoUrl": "http://static.yunzhijia.com/space/c/photo/load?id=5df86ebb6d67ff1f2a97e92b",
                "gender": "2",
                "openId": "5df86ebbe4b0b7058a9efc3d",
                "jobTitle": "开发工程师",
                "jobNo": "111131111",
                "name": "吴**",
                "globalId": "5df86ebbe4b0b7058a9efc35",
                "isAdmin": "0",
                "department": "A产品事业部",
                "orgId": "4fcfba72-e730-4deb-b327-7a2d5c9443ff",
                "status": "1"
            }
        ],
        "name": "A产品事业部",
        "orgId": "4fcfba72-e730-4deb-b327-7a2d5c9443ff",
        "parentId": "5de50017e4b0b2767b87041b",
        "status": "1"
    }
}

```

###  获取当前部门的所有上级部门列表

**URL:**`https://www.yunzhijia.com/gateway/opendata-control/data/getancestororgs?accessToken=xxxxxxxxx`

**http请求方法：** `post`

**http内容类型：** `application/x-www-form-urlencoded`

**输入参数:**

参数名 | 数据类型 | 是否必传 | 说明
-------|----------|----------|--------
orgId  | String   | 是       | 部门ID
eid    | String   | 是       | 企业ID

**请求示例：**
```url
https://www.yunzhijia.com/gateway/opendata-control/data/getancestororgs?accessToken=xxxxxxxxx
```

```form
orgId:4fcfba72-e730-4deb-b327-7a2d5c9443ff
eid:17951708
```

**返回结果:**

```JSON
{
    "success": true,
    "error": null,
    "errorCode": 100,
    "data": [
        { //当前部门信息
            "inChargers": [  //负责人信息
                {
                    "photoUrl": "http://static.yunzhijia.com/space/c/photo/load?id=5df86ebb6d67ff1f2a97e92b",
                    "gender": "2",
                    "openId": "5df86ebbe4b0b7058a9efc3d",
                    "jobTitle": "开发工程师",
                    "jobNo": "111131111",
                    "name": "吴**",
                    "globalId": "5df86ebbe4b0b7058a9efc35",
                    "isAdmin": "0",
                    "department": "A产品事业部",
                    "orgId": "4fcfba72-e730-4deb-b327-7a2d5c9443ff",
                    "status": "1"
                }
            ],
            "name": "A产品事业部",
            "orgId": "4fcfba72-e730-4deb-b327-7a2d5c9443ff",
            "parentId": "5de50017e4b0b2767b87041b"
        },
        { //上一级部门信息
            "inChargers": [],  //负责人为null,即未设置部门负责人
            "name": "印*测试团队2",
            "orgId": "5de50017e4b0b2767b87041b",
            "parentId": ""
        }
        ...  //上多级部门信息
    ]
}
```

###  获取当前部门所有下级部门列表

**URL:**`https://www.yunzhijia.com/gateway/opendata-control/data/getsuborgs?accessToken=xxxxxxxxx`

**http请求方法：** `post`

**http内容类型：** `application/x-www-form-urlencoded`

**输入参数:**

参数名 | 数据类型 | 是否必传 | 说明
-------|----------|----------|--------
orgId  | String   | 是       | 部门ID
eid    | String   | 是       | 企业ID

**请求示例：**
```url
https://www.yunzhijia.com/gateway/opendata-control/data/getsuborgs?accessToken=xxxxxxxxx
```

```form
orgId:5de50017e4b0b2767b87041b
eid:17951708
```

**返回结果:**

```JSON
{
    "success": true,
    "error": null,
    "errorCode": 100,
    "data": [
        {
            "inChargers": [  //负责人信息
                {
                    "photoUrl": "http://static.yunzhijia.com/space/c/photo/load?id=5df86ebb6d67ff1f2a97e92b",
                    "gender": "2",
                    "openId": "5df86ebbe4b0b7058a9efc3d",
                    "jobTitle": "开发工程师",
                    "jobNo": "111131111",
                    "name": "吴**",
                    "globalId": "5df86ebbe4b0b7058a9efc35",
                    "isAdmin": "0",
                    "department": "A产品事业部",
                    "orgId": "4fcfba72-e730-4deb-b327-7a2d5c9443ff",
                    "status": "1"
                }
            ],
            "name": "A产品事业部",
            "orgId": "4fcfba72-e730-4deb-b327-7a2d5c9443ff",
            "parentId": "5de50017e4b0b2767b87041b"
        },
        {
            "inChargers": [  //负责人信息
                {
                    "photoUrl": "http://static.yunzhijia.com/space/c/photo/load?id=5da98ac3b54c8d6b11b19964",
                    "gender": "1",
                    "openId": "5df89ed9e4b0b7058aa9c3f7",
                    "jobTitle": "",
                    "jobNo": "0001111",
                    "name": "宇*",
                    "globalId": "58805746e4b054803acf8596",
                    "isAdmin": "0",
                    "department": "运营管理部",
                    "orgId": "11e11baa-d74a-44df-b511-2b0b58d2a19e",
                    "status": "1"
                }
            ],
            "name": "运营管理部",
            "orgId": "11e11baa-d74a-44df-b511-2b0b58d2a19e",
            "parentId": "5de50017e4b0b2767b87041b"
        },
        ...    
    ]
}
```

###  获取所有部门列表

**URL:**`https://www.yunzhijia.com/gateway/opendata-control/data/getallorgs?accessToken=xxxxxxxxx`

**http请求方法：** `post`

**http内容类型：** `application/x-www-form-urlencoded`

**输入参数:**

参数名 | 数据类型 | 是否必传 | 说明
-------|----------|----------|---------------------------------
eid    | String   | 是       | 企业ID
begin  | Integer  | 否       | 分页起始位置，从0开始
count  | Integer  | 否       | 分页记录条数，这个值不要大于1000

**请求示例：**
```url
https://www.yunzhijia.com/gateway/opendata-control/data/getallorgs?accessToken=xxxxxxxxx
```

```form
eid:17951708
```

**返回结果:**

```json
{
    "success": true,
    "error": null,
    "errorCode": 100,
    "data": [
        {
            "inChargers": [],
            "name": "客户服务部",
            "orgId": "6984e032-a17b-400c-8b34-529e0b9105ba",
            "parentId": "5de50017e4b0b2767b87041b"
        },
        {
            "inChargers": [],
            "name": "信息部",
            "orgId": "d037f98f-6d21-4df0-9998-88c86db89a06",
            "parentId": "5de50017e4b0b2767b87041b"
        },
        {
            "inChargers": [],
            "name": "用户体验部",
            "orgId": "d03840e2-f345-4fb2-b74a-55fce2113e6f",
            "parentId": "5de50017e4b0b2767b87041b"
        },
        {
            "inChargers": [],
            "name": "创意部",
            "orgId": "266b196f-c0b6-4301-85a8-d916e806c9f2",
            "parentId": "859d0357-b94f-4a6c-b9dc-6ec4a83e91b4"
        },
        ...
    ]
}
```

###  获取企业基本信息

**URL:**`https://www.yunzhijia.com/gateway/opendata-control/data/getcompany?accessToken=xxxxxxxxx`

**http请求方法：** `post`

**http内容类型：** `application/x-www-form-urlencoded`

**输入参数:**

参数名 | 数据类型 | 是否必传 | 说明
-------|----------|----------|---------------------------------
eid    | String   | 是       | 企业ID

**请求示例：**
```url
https://www.yunzhijia.com/gateway/opendata-control/data/getcompany?accessToken=xxxxxxxxx
```

```form
eid:17951708
```

**返回结果:**

```JSON
{
    "success": true,
    "error": null,
    "errorCode": 100,
    "data": {
        "eid": "17951708",
        "userCount": "11",
        "name": "印*测试团队2"
    }
}
```

###  获取当前部门成员或部门负责人信息

**URL:**`https://www.yunzhijia.com/gateway/opendata-control/data/getorgpersons?accessToken=xxxxxxxxx`

**http请求方法：** `post`

**http内容类型：** `application/x-www-form-urlencoded`

**输入参数:**

参数名 | 数据类型 | 是否必传 | 说明
-------|----------|----------|---------------------------------
eid    | String   | 是       | 企业ID
orgId  | String   | 是       | 部门ID
begin  | Integer  | 否       | 默认0
count  | Integer  | 否       | 默认1000，每次拉取限制1000条以内（包括1000条）

**请求示例：**
```url
https://www.yunzhijia.com/gateway/opendata-control/data/getorgpersons?accessToken=xxxxxxxxx
```

```form
orgId:4fcfba72-e730-4deb-b327-7a2d5c9443ff
eid:17951708
```

**返回结果:**

```JSON
{
    "success": true,
    "error": null,
    "errorCode": 100,
    "data": {
        "inChargers": [ //部门负责人
            {
                "photoUrl": "http://static.yunzhijia.com/space/c/photo/load?id=5da98ac3b54c8d6b11b19964",
                "gender": "1",
                "openId": "5df89ed9e4b0b7058aa9c3f7",
                "jobTitle": "",
                "jobNo": "",
                "name": "宇*",
                "globalId": "58805746e4b054803acf8596",
                "isAdmin": "0",
                "department": "运营管理部",
                "orgId": "11e11baa-d74a-44df-b511-2b0b58d2a19e",
                "status": "1"
            }
        ],
        "members": [  //成员
            {
                "photoUrl": "http://static.yunzhijia.com/space/c/photo/load?id=5da98ac3b54c8d6b11b19964",
                "gender": "1",
                "openId": "5df89ed9e4b0b7058aa9c3f7",
                "jobTitle": "",
                "jobNo": "",
                "name": "宇*",
                "globalId": "58805746e4b054803acf8596",
                "isAdmin": "0",
                "department": "运营管理部",
                "orgId": "11e11baa-d74a-44df-b511-2b0b58d2a19e",
                "status": "1"
            },
            {
                "photoUrl": "http://static.yunzhijia.com/space/c/photo/load?id=5dc22499a372591da29c50a7",
                "gender": "1",
                "openId": "5de50017e4b0b2767b870423",
                "jobTitle": "",
                "jobNo": "",
                "name": "印*",
                "globalId": "5bc159e3e4b036230d719547",
                "isAdmin": "1",
                "department": "运营管理部",
                "orgId": "11e11baa-d74a-44df-b511-2b0b58d2a19e",
                "status": "1"
            }
        ]
    }
}

```

**说明:**

1. inChargers只有在begin为0时返回，分页参数控制members的返回条数
2. 部门负责人允许其它部门的人担任

###  获取当前部门下一层级的所有部门基本信息列表

**URL:**`https://www.yunzhijia.com/gateway/opendata-control/data/getsublevelorgs?accessToken=xxxxxxxxx`

**http请求方法：** `post`

**http内容类型：** `application/x-www-form-urlencoded`

**输入参数:**

参数名 | 数据类型 | 是否必传 | 说明
-------|----------|----------|---------------------------------
eid    | String   | 是       | 企业ID
orgId  | String   | 是       | 部门ID

**请求示例：**
```url
https://www.yunzhijia.com/gateway/opendata-control/data/getsublevelorgs?accessToken=xxxxxxxxx
```

```form
orgId:467f8bba-a855-4fef-9e83-0867d8e03d77
eid:17951708
```

**返回结果:**

```JSON
{
    "success": true,
    "error": null,
    "errorCode": 100,
    "data": [
        {
            "inChargers": [],
            "name": "移动平台产品部",
            "orgId": "58b62641-84bf-406b-a94b-d3bfffae22aa",
            "parentId": "467f8bba-a855-4fef-9e83-0867d8e03d77"
        },
        {
            "inChargers": [],
            "name": "宇宙级平台产品部",
            "orgId": "d382c2e6-4777-4f8b-8198-a925ee0190e0",
            "parentId": "467f8bba-a855-4fef-9e83-0867d8e03d77"
        }
    ]
}
```

###  获取用户的默认上级或默认汇报上级或指定上级

**URL:**`https://www.yunzhijia.com/gateway/opendata-control/data/getparentperson?accessToken=xxxxxxxxx`

**http请求方法：** `post`

**http内容类型：** `application/x-www-form-urlencoded`

**输入参数:**

参数名 | 数据类型 | 是否必传 | 说明
-------|----------|----------|--------
eid    | String   | 是       | 企业ID
openId | String   | 是       | 人员ID

**请求示例：**
```url
https://www.yunzhijia.com/gateway/opendata-control/data/getparentperson?accessToken=xxxxxxxxx
```

```form
eid:17951708
openId:5df8a114e4b02b68c57147e7
```

**返回结果:**

```json
{
    "success": true,
    "error": null,
    "errorCode": 100,
    "data": {
        "defaultParentPersons": [ //默认上级
            {
                "photoUrl": "http://static.yunzhijia.com/space/c/photo/load?id=5da98ac3b54c8d6b11b19964",
                "gender": "1",
                "openId": "5df89ed9e4b0b7058aa9c3f7",
                "jobTitle": "",
                "jobNo": "0001111",
                "name": "宇*",
                "globalId": "58805746e4b054803acf8596",
                "isAdmin": "0",
                "department": "运营管理部",
                "orgId": "11e11baa-d74a-44df-b511-2b0b58d2a19e",
                "status": "1"
            }
        ],
        "defaultParentSecPersons": [ //默认汇报上级
            {
                "photoUrl": "http://static.yunzhijia.com/space/c/photo/load?id=5da98ac3b54c8d6b11b19964",
                "gender": "1",
                "openId": "5df89ed9e4b0b7058aa9c3f7",
                "jobTitle": "",
                "jobNo": "0001111",
                "name": "宇*",
                "globalId": "58805746e4b054803acf8596",
                "isAdmin": "0",
                "department": "运营管理部",
                "orgId": "11e11baa-d74a-44df-b511-2b0b58d2a19e",
                "status": "1"
            }
        ],
        "selectParentPersons": null  //指定上级
    }
}

```

###  通过工作圈eid获取管理员oid

**URL:**`https://www.yunzhijia.com/gateway/opendata-control/data/getAdminOidsByEid?accessToken=xxxxxxxxx`

**http请求方法：** `post`

**http内容类型：** `application/x-www-form-urlencoded`

**输入参数:**

参数名 | 数据类型 | 是否必传 | 说明
-------|----------|----------|--------
eid    | String   | 是       | 企业ID

**请求示例：**
```url
https://www.yunzhijia.com/gateway/opendata-control/data/getAdminOidsByEid?accessToken=xxxxxxxxx
```

```form
eid:17951708
```

**返回结果:**

```JSON
{
    "success": true,
    "error": null,
    "errorCode": 100,
    "data": {
        "oids": "5de50083e4b09c41c10efe91,5de50017e4b0b2767b870423,5df885fbe4b0c908e1a58ffe"  //多个管理员，其oid用“，”号隔开
    }
}

```

###  根据企业eid查询全部合作伙伴信息

**URL:**`https://www.yunzhijia.com/gateway/opendata-control/partner/getPartners?accessToken=xxxxxxxxx`

**http请求方法：** `post`

**http内容类型：** `application/x-www-form-urlencoded`

**输入参数:**

参数名 | 数据类型 | 是否必传 | 说明
-------|----------|----------|--------------------------------------------------------------------------------------------------
eid    | string   | 是       | 企业ID
time   | String   | 否       | 时间戳（精确到毫秒）;传空或者不传表示全部查询
begin  | Integer  | 否       | 默认0
count  | Integer  | 否       | 默认1000，查询使用分页机制，每次查询总数不能超过1000条；，如果输出条数不足count条，表示分页拉取已结束

**请求示例：**
```url
https://www.yunzhijia.com/gateway/opendata-control/partner/getPartners?accessToken=xxxxxxxxx
```

```form
eid:17951708
```
**返回结果:**

```json
{
    "success": true,
    "error": null,
    "errorCode": 100,
    data: {
        partners: [
            { //合作伙伴列表
        "partnerId": "2b76ed83-c8f2-4331-9a9e-4e0cee56be22", //合作伙伴id
        "code": "18013450", //合作伙伴编号
        "name": "印****", //合作伙伴管理员名称
        "hasCertified": 0, //0,未认证；1，已认证
        "eid": "18013450", //合作伙伴对应的云之家团队eid
        "companyName": "***测试333", //合作伙伴名称
        contacts: [
                    {
                "name": "印*", //联系人名称
                "phone": "156****5320", //联系人手机号码
                "openid": "", //联系人云之家对应openid
                "contactId": "36338b20-b11a-4088-838e-6cc29b151d39", //联系人id
                    }.....
                ]
            },....
        ]
    }
}
```

###  根据手机号码和工作圈名称查询工作圈信息

**URL:**`https://www.yunzhijia.com/gateway/opendata-control/partner/searchNetwork?accessToken=xxxxxxxxx`

**http请求方法：** `post`

**http内容类型：** `application/x-www-form-urlencoded`

**输入参数:**

参数名 | 数据类型 | 是否必传 | 说明
-------|----------|----------|----------
eid    | String   | 是       | 企业ID
phone  | String   | 是       | 手机号
name   | String   | 是       | 团队名称

**请求示例：**
```url
https://www.yunzhijia.com/gateway/opendata-control/partner/searchNetwork?accessToken=xxxxxxxxx
```

```form
eid:17951708
name:印*测试团队2
phone:156****5320
```

**返回结果:**

```json
{
    "success": true,
    "error": null,
    "errorCode": 100,
    "data": {
        "newtorks": [//工作圈列表
            { 
                "eid": "17951708", //工作圈eid
                "networkId": "5de50017e4b0b2767b87041b", //工作圈networkId
                "name": "印*测试团队2" //工作圈名称
            },
            ...
        ]
    }
}

```




###  按角色id获取人员信息

**URL:**`https://www.yunzhijia.com/gateway/opendata-control/data/getpersonByRoleIds?accessToken=xxxxxxxxx`

**http请求方法：** `post`

**http内容类型：** `application/x-www-form-urlencoded`

**输入参数:**

参数名  | 数据类型 | 是否必传 | 说明
--------|----------|----------|--------------------------------
eid     | String   | 是       | 企业ID
roleIds | String   | 是       | 多个角色ID之间用下划线 _  连接
begin   | Integer  | 否       | 分页开始  默认0
count   | Integer  | 否       | 每页数量  默认1000

**请求示例：**
```url
https://www.yunzhijia.com/gateway/opendata-control/data/getpersonByRoleIds?accessToken=xxxxxxxxx
```

```form
eid:17951708
roleIds:cdb374f2-103b-4eb0-9ef0-b3dd3cf8ad18
```

**返回结果:**
```json
{
    "success": true,
    "error": null,
    "errorCode": 100,
    "data": [
        {
            "eid": "17951708",
            "roleId": "cdb374f2-103b-4eb0-9ef0-b3dd3cf8ad18",  //角色id
            "members": [  //成员
                {
                    "uid": "125154854",
                    "photoUrl": "http://static.yunzhijia.com/space/c/photo/load?id=5df8720db54c8d61c2842711",
                    "openId": "5df8720de4b0ee4e15c1d0a5",
                    "name": "尹**"
                }
            ],
            "roleName": "皇马队长"  //角色名称
        }
    ]
}

```

###  查询部门信息

**URL:**`https://www.yunzhijia.com/gateway/opendata-control/data/getorginfos?accessToken=xxxxxxxxx`

**http请求方法：** `post`

**http内容类型：** `application/x-www-form-urlencoded`

**输入参数:**

参数名   | 数据类型 | 是否必传 | 说明
---------|----------|----------|----------------------------------------------
eid      | String   | 是       | 企业ID
orgIds   | String   | 是       | 部门ID 必填  多个部门ID之间用下划线  _  连接
begin    | Integer  | 否       | 分页开始  默认0
count    | Integer  | 否       | 每页数量  默认1000
hasChild | Boolean  | 是       | 是否查询子部门信息

**请求示例：**
```url
https://www.yunzhijia.com/gateway/opendata-control/data/getorginfos?accessToken=xxxxxxxxx
```

```form
orgIds:58b62641-84bf-406b-a94b-d3bfffae22aa
eid:17951708
hasChild:true
```

**返回结果:**

```json
{
    "success": true,
    "error": null,
    "errorCode": 100,
    "data": [
        {
            "subOrgs": [  //子部门信息
                {
                    "name": "开发部",
                    "orgId": "58547b46-76d6-4d7d-ade0-be91d396cfe4",
                    "parentId": "58b62641-84bf-406b-a94b-d3bfffae22aa"
                }
            ],
            "org": {  
                "name": "移动平台产品部",
                "orgId": "58b62641-84bf-406b-a94b-d3bfffae22aa",
                "parentId": "467f8bba-a855-4fef-9e83-0867d8e03d77"
            },
            "members": [  //部门成员信息
                {
                    "uid": "125154606",
                    "photoUrl": "http://static.yunzhijia.com/space/c/photo/load?id=5df870e690144e5959d6a521",
                    "openId": "5df870e6e4b0b7058a9f8aef",
                    "name": "猪**",
                    "orgId": "58b62641-84bf-406b-a94b-d3bfffae22aa"
                }
            ]
        }
    ]
}
```

###  根据orgIds获取人员信息

**URL:**`https://www.yunzhijia.com/gateway/opendata-control/data/org/getUserInfoRelyOrgIds?accessToken=xxxxxxxxx`

**http请求方法：** `post`

**http内容类型：** `application/x-www-form-urlencoded`

**输入参数:**

参数名       | 数据类型 | 是否必传 | 说明
-------------|----------|----------|----------------------------------------------
eid          | String   | 是       | 企业ID
orgIds       | String   | 是       | 部门ID 必填  多个部门ID之间用逗号隔开
begin        | Integer  | 否       | 分页开始  默认0
count        | Integer  | 否       | 每页数量  最大限制500
isIncludeSub | Boolean  | 是       | 是否包含下级部门人员信息

**请求示例：**
```url
https://www.yunzhijia.com/gateway/opendata-control/data/org/getUserInfoRelyOrgIds?accessToken=xxxxxxxxx
```

```form
orgIds:4fcfba72-e730-4deb-b327-7a2d5c9443ff
eid:17951708
isIncludeSub:false
```

**返回结果：**
```json
{
    "success": true,
    "error": null,
    "errorCode": 100,
    "data": [
        {
            "photoUrl": "http://static.yunzhijia.com/space/c/photo/load?id=5df86ebb6d67ff1f2a97e92b",
            "gender": "2",
            "phone": "130****3055",
            "openId": "5df86ebbe4b0b7058a9efc3d",
            "jobTitle": "开发工程师",
            "jobNo": "",
            "name": "吴**",
            "isAdmin": 0,
            "department": "A产品事业部",
            "email": "1587954@163.com",
            "orgId": "4fcfba72-e730-4deb-b327-7a2d5c9443ff",
            "status": 1
        },
        {
            "photoUrl": "http://static.yunzhijia.com/space/c/photo/load?id=5df8720db54c8d61c2842711",
            "gender": "2",
            "phone": "130****5321",
            "openId": "5df8720de4b0ee4e15c1d0a5",
            "jobTitle": "开发工程师",
            "jobNo": "8546",
            "name": "尹**",
            "isAdmin": 0,
            "department": "A产品事业部",
            "email": "1581154@163.com",
            "orgId": "4fcfba72-e730-4deb-b327-7a2d5c9443ff",
            "status": 1
        }
    ]
}
```

## FAQ

### 为什么接口返回错误“企业未授权”？

请检查生成accessToken的appId（轻应用）是否和eid（团队）保持一致的。