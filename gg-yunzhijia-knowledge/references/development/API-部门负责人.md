---
domain: development
module: 组织人员
keywords: [IM, accessToken, secret, token, 同步]
---

## 部门负责人

部门负责人API列表

部门负责人API列表

接口授权

本页接口使用 resGroupSecret 级别的 AccessToken， 与获取组织数据的接口不同，请注意区分。

请在 管理中心-系统设置-系统集成-通讯录同步 中，复制 只读秘钥 或者 可编辑秘钥， 然后调用系统接口换取 AccessToken。

> 只读秘钥：只能调用查询类的接口

> 可编辑秘钥：可以调用全部接口

如果您还不了解如何获取AccessToken，请点击此处

接口列表

输入参数说明如下：

批量设置部门负责人

描述: 设置部门负责人,人员和部门必须已经存在才能设置成功。

URL:https://www.yunzhijia.com/gateway/openimport/open/company/setOrgAdmins?accessToken=xxxxxx

请求方法：post

内容类型：Content-Type: application/x-www-form-urlencoded

输入参数:

nonce: String // 非必填，用于校验重复请求的随机字符串

eid: Number // 必填，企业id

data: String // 必填，业务数据json字符串

> 请注意，data 不应是js对象而应是一个JSON格式的字符串， 即用JSON.stringify()处理以下结构对象获得的字符串：

[ //单次同步，最多只允许1000条数据
  {
    "department": String, //部门长名称，格式："一级部门\\二级部门\\三级部门"，如 ： "研发中心\\移动平台产品部\\开发部"
    "openId": String, //人员ID
    "weights":int, //可选，部门负责人排序权重，权重越小，排序越前.若不填则以人员权重排序
    "commitId": String //唯一标识一条设置数据，建议使用自增序列（返回时，可用来判断一条记录是否成功）
  },
  ...
]

请求示例：

https://www.yunzhijia.com/gateway/openimport/open/company/setOrgAdmins?accessToken=xxxxxx

nonce:abcxyXXXXzefg

eid:17951708

data:[
    {
        "department": "A产品事业部", 
        "openId": "5df86ebbe4b0b7058a9efc3d", 
        "weights": 8, 
        "commitId": "123456"
    }
]

返回结果示例: 参见输出结果，如果批量设置全部成功，则data里返回[]，如果有未设置成功的，则data中会有未设置成功的具体信息，示例如下：

{
    "success": true,
    "error": "",
    "errorCode": 100,
    "data": [  //只有在有失败数据时返回，若成功，返回空
        {
            "commitId": "123456",  //提交ID
            "errorMsg": "department不存在"  //此处标识失败原因（假设请求的department不存在）
        }
    ]
}

根据组织id批量设置部门负责人

描述: 设置部门负责人,人员和部门必须已经存在才能设置成功。

URL:https://www.yunzhijia.com/gateway/openimport/open/company/setOrgAdminsById?accessToken=xxxxxx

请求方法：post

内容类型：Content-Type: application/x-www-form-urlencoded

输入参数:

nonce: String // 非必填，用于校验重复请求的随机字符串

eid: Number // 必填，企业id

data: String // 必填，业务数据json字符串

> 请注意，data 不应是js对象而应是一个JSON格式的字符串， 即用JSON.stringify()处理以下结构对象获得的字符串：

[ //单次同步，最多只允许1000条数据
  {
     "orgId": String, //部门id
     "openId": String, //人员ID
     "weights":int, //可选，排序权重，权重越小，排序越前.
     "commitId": String //唯一标识一条设置数据，建议使用自增序列（返回时，可用来判断一条记录是否成功）
  },
  ...
]

请求示例：

https://www.yunzhijia.com/gateway/openimport/open/company/setOrgAdminsById?accessToken=xxxxxx

nonce:abcxyXXXXzefg

eid:17951708

data:[
    {
        "orgId": "d66340ca-56ac-443d-b3a3-d9607e81cbba", 
        "openId": "5df8720de4b0ee4e15c1d0a5", 
        "weights": 0, 
        "commitId": "124"
    }, 
    {
        "orgId": "11e11baa-d74a-44df-b511-2b0b58d2a19e", 
        "openId": "5df89ed9e4b0b7058aa9c3f7", 
        "weights": 1, 
        "commitId": "142"
    }
]

返回结果示例: 参见输出结果，如果批量设置全部成功，则data里返回[]，如果有未设置成功的，则data中会有未设置成功的具体信息，示例如下：

{
    "success": true,
    "error": "",
    "errorCode": 100,
    "data": [  //只有在有失败数据时返回，若成功，返回空
        {
            "commitId": "124",  //提交ID
            "errorMsg": "openId不存在"  //此处标识失败原因（假设输入的openid错误）
        }
    ]
}

查询所有部门负责人

描述: 查询所有部门负责人,该接口只返回在职的部门负责人。

URL:https://www.yunzhijia.com/gateway/openimport/open/company/queryOrgAdmins?accessToken=xxxxxx

请求方法：post

内容类型：Content-Type: application/x-www-form-urlencoded

输入参数:

nonce: String // 非必填，用于校验重复请求的随机字符串

eid: Number // 必填，企业id

data: String // 必填，业务数据json字符串

> 请注意，data 不应是js对象而应是一个JSON格式的字符串， 即用JSON.stringify()处理以下结构对象获得的字符串：

{ //分页查询部门负责人，每页限制最多返回1000条记录；count>1000时，截断为1000。
  "begin": int, // 可选，分页起始条数，比如：0
  "count": int // 可选，单次查询条数，比如： 1000
}

请求示例：

https://www.yunzhijia.com/gateway/openimport/open/company/queryOrgAdmins?accessToken=xxxxxx

nonce:abcxyXXXXzefg

eid:17951708

data:{
    "begin": 0, 
    "count": 100
}

返回结果示例:

{
    "success": true,
    "error": "",
    "errorCode": 100,
    "data": [
        {
            "openId": "5df89ed9e4b0b7058aa9c3f7",  //人员openId
            "departmentId": "11e11baa-d74a-44df-b511-2b0b58d2a19e",  //部门Id
            "department": "运营管理部"  //所负责的部门长名称
        },
        {
            "openId": "5df8720de4b0ee4e15c1d0a5",
            "departmentId": "d66340ca-56ac-443d-b3a3-d9607e81cbba",
            "department": "研发中心\\宇宙级平台产品部\\创意部"
        },
        {
            "openId": "5df86ebbe4b0b7058a9efc3d",
            "departmentId": "4fcfba72-e730-4deb-b327-7a2d5c9443ff",
            "department": "A产品事业部"
        },
        {
            "openId": "5df87378e4b013c7ff844226",
            "departmentId": "c37d2483-18c5-4e8b-b89f-1bc7eb862ced",
            "department": "B产品事业部"
        }
    ]
}

批量删除部门负责人

描述: 批量删除部门负责人

注意: deleteAll参数会导致所有部门负责人被删除，请谨慎使用。data部分，特殊含义错误码说明：900014： "负责人不存在"

URL:https://www.yunzhijia.com/gateway/openimport/open/company/deleteOrgAdmins?accessToken=xxxxxx

请求方法：post

内容类型：Content-Type: application/x-www-form-urlencoded

输入参数:

nonce: String // 非必填，用于校验重复请求的随机字符串

eid: Number // 必填，企业id

data: String // 必填，业务数据json字符串

> 请注意，data 不应是js对象而应是一个JSON格式的字符串， 即用JSON.stringify()处理以下结构对象获得的字符串：

{
  "deleteAll": Boolean, //是否删除所有,默认值为false。该值传true时，表示删除所有部门负责人（此时list可以不传）；该值为false时，表示删除指定部门负责人，list字段必传。
  "list": [ //指定人员删除时，最多允许一次删除1000条记录
    {
      "department":String, //部门长名称，格式："一级部门\\二级部门\\三级部门"，如 ： "研发中心\\移动平台产品部\\开发部"
      "openId":String, //人员ID
      "commitId":String //唯一标识一条数据，建议使用自增序列（返回时，可用来判断一条记录是否成功）
    },
    ...
  ]
}

请求示例：

https://www.yunzhijia.com/gateway/openimport/open/company/deleteOrgAdmins?accessToken=xxxxxx

nonce:abcxyXXXXzefg

eid:17951708

data:{
    "deleteAll": false, 
    "list": [
        {
            "department": "B产品事业部", 
            "openId": "5df86ebbe4b0b7058a9efc3d", 
            "commitId": "123456"
        }, 
        {
            "department": "研发中心\\移动平台产品部\\开发部", 
            "openId": "5df86ebbe4b0b7058a9efc3d", 
            "commitId": "123457"
        }
    ]
}

返回结果示例: 参见输出结果，如果批量删除全部成功，则data里返回[]，如果有未删除成功的，则data中会有未删除成功的具体信息，示例如下：

{
    "success": true,
    "error": "",
    "errorCode": 100,
    "data": [
        {
            "errorCode": 900014,  //错误码，注意：该字段可能不返回
            "commitId": "123457",  //提交ID
            "error": "负责人不存在"  //具体错误消息
        }
    ]
}

根据组织id批量删除部门负责人

描述: 批量删除部门负责人

URL:https://www.yunzhijia.com/gateway/openimport/open/company/deleteOrgAdminsById?accessToken=xxxxxx

请求方法：post

内容类型：Content-Type: application/x-www-form-urlencoded

输入参数:

nonce: String // 非必填，用于校验重复请求的随机字符串

eid: Number // 必填，企业id

data: String // 必填，业务数据json字符串

> 请注意，data 不应是js对象而应是一个JSON格式的字符串， 即用JSON.stringify()处理以下结构对象获得的字符串：

{
  "list": [ //指定人员删除时，最多允许一次删除1000条记录
    {
      "orgId":String, //部门id
      "openId":String, //人员ID
      "commitId":String //唯一标识一条数据，建议使用自增序列（返回时，可用来判断一条记录是否成功）
    },
    ...
  ]
}

请求示例：

https://www.yunzhijia.com/gateway/openimport/open/company/deleteOrgAdminsById?accessToken=xxxxxx

nonce:abcxyXXXXzefg

eid:17951708

data:{
    "list": [
        {
            "orgId": "58547b46-76d6-4d7d-ade0-be91d396cfe4", 
            "openId": "5df86ebbe4b0b7058a9efc3d", 
            "commitId": "123456"
        }, 
        {
            "orgId": "d66340ca-56ac-443d-b3a3-d9607e81cbba", 
            "openId": "5df8720de4b0ee4e15c1d0a5", 
            "commitId": "123457"
        }
    ]
}

返回结果示例:

{
    "success": true,
    "error": "",
    "errorCode": 100,
    "data": ""
}

删除组织负责人

描述: 删除组织负责人

URL:https://www.yunzhijia.com/gateway/openimport/open/relationship/deleteOrgAdmins?accessToken=xxxxxx

请求方法：post

内容类型：Content-Type: application/x-www-form-urlencoded

输入参数:

nonce: String // 非必填，用于校验重复请求的随机字符串

eid: Number // 必填，企业id

data: String // 必填，业务数据json字符串

> 请注意，data 不应是js对象而应是一个JSON格式的字符串， 即用JSON.stringify()处理以下结构对象获得的字符串：

{
  "deleteAll": Boolean, //是否删除所有,默认值为false。该值传true时，表示删除所有部门负责人（此时list可以不传）；该值为false时，表示删除指定部门负责人，list字段必传。
  "list": [{ //指定人员删除时，最多允许一次删除1000条记录
      "orgId":String, //部门Id
      "openId":String, //人员ID
  },
  ...
  ]
}

请求示例：

https://www.yunzhijia.com/gateway/openimport/open/relationship/deleteOrgAdmins?accessToken=xxxxxx

nonce:abcxyXXXXzefg

eid:17951708

data:{
  "deleteAll": false, 
  "list": [
    {
        "orgId": "58547b46-76d6-4d7d-ade0-be91d396cfe4", 
        "openId": "5de50083e4b09c41c10efe91"
    }
]
}

返回结果示例：

{
    "success": true,
    "msgCode": null,
    "msg": null,
    "data": null
}

FAQ

暂无

--- 文档抓取完成 ---

接口名称 | URL | 备注

批量设置部门负责人 | /gateway/openimport/open/company/setOrgAdmins

查询所有部门负责人 | /gateway/openimport/open/company/queryOrgAdmins

批量删除部门负责人 | /gateway/openimport/open/company/deleteOrgAdmins

根据组织id批量设置部门负责人 | /gateway/openimport/open/company/setOrgAdminsById

根据组织id批量删除部门负责人 | /gateway/openimport/open/company/deleteOrgAdminsById

删除上级组织负责人 | /gateway/openimport/open/relationship/deleteOrgAdmins

字段名 | 数据类型 | 是否必填 | 说明

nonce | String | 否 | 校验重复请求,格式为16位以内随机字符串

eid | String | 是 | 注册企业团队id

data | String | 是 | 业务数据,json字符串格式

---