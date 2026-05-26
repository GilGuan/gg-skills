---
domain: development
module: 组织人员
keywords: [IM, accessToken, person, secret, token]
---

## 兼职

人员兼职API列表

人员兼职API列表

接口授权

本页接口使用 resGroupSecret 级别的 AccessToken， 与获取组织数据的接口不同，请注意区分。

请在 管理中心-系统设置-系统集成-通讯录同步 中，复制 只读秘钥 或者 可编辑秘钥， 然后调用系统接口换取 AccessToken。

> 只读秘钥：只能调用查询类的接口

> 可编辑秘钥：可以调用全部接口

如果您还不了解如何获取AccessToken，请点击此处

接口列表

输入参数说明如下：

根据部门id批量添加兼职

描述: 批量添加兼职，设置一个人员为其它部门的兼职人员。

注意:

云之家支持多职位：人员在主职部门的职位，通过更新人员信息接口（updateInfo）去传和更新jobTitle字段（如在主职部门有多个职位，用英文,隔开）；兼职部门的职位，通过设置兼职接口（addPartTimeJobs或addPartTimeJobsFull）去传和更新jobTitle字段（如有多个，用英文,隔开）

URL:https://www.yunzhijia.com/gateway/openimport/open/company/addPartTimeJobs?accessToken=xxxxxx

请求方法：post

内容类型：Content-Type: application/x-www-form-urlencoded

输入参数:

nonce: String // 非必填，用于校验重复请求的随机字符串

eid: Number // 必填，企业id

data: String // 必填，业务数据json字符串

> 请注意，data 不应是js对象而应是一个JSON格式的字符串， 即用JSON.stringify()处理以下结构对象获得的字符串：

[
  {
   "commitId": String, //提交ID
   "openId": String, // 人员ID
   "orgId": String, // 部门ID
   "weights": Integer, //用于兼职排序时的权重
   "orgUserType":Integer,//是否设为兼职部门负责人  1：设为兼职部门负责人,0:普通人(取消负责人)
   "jobTitle": String //兼职部门里的职位,该人如果在该部门里有多个兼职职位，请使用英文逗号隔开,例："兼职职位a,兼职职位b,兼职职位3"
  }
]

请求示例：

https://www.yunzhijia.com/gateway/openimport/open/company/addPartTimeJobs?accessToken=xxxxxx

nonce:abcxyXXXXzefg

eid:17951708

data:[
    {
        "commitId": "1", 
        "openId": "5df86ebbe4b0b7058a9efc3d", 
        "orgId": "11e11baa-d74a-44df-b511-2b0b58d2a19e", 
        "orgUserType": 0,
        "weights": 1000, //用于兼职排序时的权重
        "jobTitle": "运营部资深顾问"
    }, 
    {
        "commitId": "2", 
        "openId": "5df87378e4b013c7ff844226", 
        "orgId": "d03840e2-f345-4fb2-b74a-55fce2113e6f", 
        "orgUserType":1,
        "weights": 1000, //用于兼职排序时的权重
        "jobTitle": "首席用户体验官"
    }
]

返回结果示例:

{
    "success": true,
    "error": "",
    "errorCode": 100,
    "data": []
}

根据部门id批量更新覆盖兼职职位

描述: 批量设置兼职（最多50个），设置一个人员为其它部门的兼职人员。

注意:

云之家支持多职位：人员在主职部门的职位，通过更新人员信息接口（updateInfo）去传和更新jobTitle字段（如在主职部门有多个职位，用英文,隔开）；兼职部门的职位，通过设置兼职接口（addPartTimeJobs或addPartTimeJobsFull）去传和更新jobTitle字段（如有多个，用英文,隔开）

URL:https://www.yunzhijia.com/gateway/openimport/open/company/setPartTimeJobs?accessToken=xxxxxx

请求方法：post

内容类型：Content-Type: application/x-www-form-urlencoded

输入参数:

nonce: String // 非必填，用于校验重复请求的随机字符串

eid: Number // 必填，企业id

data: String // 必填，业务数据json字符串

> 请注意，data 不应是js对象而应是一个JSON格式的字符串， 即用JSON.stringify()处理以下结构对象获得的字符串：

[
  {
   "commitId": String, //提交ID
   "openId": String, // 人员ID
   "orgId": String, // 部门ID
   "weights": Integer, //用于兼职排序时的权重
   "orgUserType":Integer,//是否设为兼职部门负责人  1：设为兼职部门负责人,0:普通人(取消负责人)
   "jobTitle": String //兼职部门里的职位,该人如果在该部门里有多个兼职职位，请使用英文逗号隔开,例："兼职职位a,兼职职位b,兼职职位3"
   （新增或覆盖部门下原有兼职职位） 如需删除该openId对应的兼职部门则 jobTitle传"!DELETE",表示删除该openId在这个部门下的所有兼职职位(即：删除该兼职部门)，标识特殊是防止误删除。
  }
]

请求示例：

https://www.yunzhijia.com/gateway/openimport/open/company/setPartTimeJobs?accessToken=xxxxxx

nonce:abcxyXXXXzefg

eid:17951708

data:[
    {
        "commitId": "1", 
        "openId": "5df86ebbe4b0b7058a9efc3d", 
        "orgId": "11e11baa-d74a-44df-b511-2b0b58d2a19e", 
        "orgUserType":0,
        "weights": 1000, //用于兼职排序时的权重
        "jobTitle": "运营部资深顾问"
    }, 
    {
        "commitId": "2", 
        "openId": "5df87378e4b013c7ff844226", 
        "orgId": "d03840e2-f345-4fb2-b74a-55fce2113e6f", 
        "orgUserType":1,
        "weights": 1000, //用于兼职排序时的权重
        "jobTitle": "首席用户体验官"
    }
]

返回结果示例:

{
    "success": true,
    "error": "",
    "errorCode": 100,
    "data": []
}

根据部门长名称批量设置兼职

描述: 批量设置兼职，设置一个人员为其它部门的兼职人员，同时可以指定兼职的权重，不传默认是取主职的权重，是否兼职部门负责人。

注意:

云之家支持多职位：人员在主职部门的职位，通过更新人员信息接口（updateInfo）去传和更新jobTitle字段（如在主职部门有多个职位，用英文,隔开）；兼职部门的职位，通过设置兼职接口（addPartTimeJobs或addPartTimeJobsFull）去传和更新jobTitle字段（如有多个，用英文,隔开）

URL:https://www.yunzhijia.com/gateway/openimport/open/company/addPartTimeJobsFull?accessToken=xxxxxx

请求方法：post

内容类型：Content-Type: application/x-www-form-urlencoded

输入参数:

nonce: String // 非必填，用于校验重复请求的随机字符串

eid: Number // 必填，企业id

data: String // 必填，业务数据json字符串

> 请注意，data 不应是js对象而应是一个JSON格式的字符串， 即用JSON.stringify()处理以下结构对象获得的字符串：

[
  {
    "commitId": "123123", //提交ID
    "jobTitle": "w1000", //兼职部门里的职位,该人如果在该部门里有多个兼职职位，请使用英文逗号隔开,例："兼职职位a,兼职职位b,兼职职位3"
    "openId": "580d9fa000b0911f84defd61",
    "department": "骨2科", //兼职部门长名称
    "weights": 1000, //用于兼职排序时的权重
    "orgUserType": 1 //是否设为兼职部门负责人 0:普通人(取消负责人)
  }
]

请求示例：

https://www.yunzhijia.com/gateway/openimport/open/company/addPartTimeJobsFull?accessToken=xxxxxx

nonce:abcxyXXXXzefg

eid:17951708

data:[
    {
        "commitId": "1", 
        "openId": "5df89ed9e4b0b7058aa9c3f7", 
        "department": "总经办", 
        "weights": 1000, //用于兼职排序时的权重
        "jobTitle": "总经办高级顾问", 
        "orgUserType": 1
    }, 
    {
        "commitId": "2", 
        "openId": "5de500e4e4b0b998f379afd7", 
        "department": "A产品事业部", 
        "weights": 1000, //用于兼职排序时的权重
        "jobTitle": "产品经理", 
        "orgUserType": 0
    }
]

返回结果示例:

{
    "success": true,
    "error": "",
    "errorCode": 100,
    "data": []
}

根据部门id批量删除兼职

描述: 根据部门id批量删除兼职

URL:https://www.yunzhijia.com/gateway/openimport/open/company/deletePartTimeJobs?accessToken=xxxxxx

请求方法：post

内容类型：Content-Type: application/x-www-form-urlencoded

输入参数:

nonce: String // 非必填，用于校验重复请求的随机字符串

eid: Number // 必填，企业id

data: String // 必填，业务数据json字符串

> 请注意，data 不应是js对象而应是一个JSON格式的字符串， 即用JSON.stringify()处理以下结构对象获得的字符串：

[
  {
   "commitId": String, //提交ID
   "openId": String, // 人员ID
   "orgId": String // 部门ID
  }
]

请求示例：

https://www.yunzhijia.com/gateway/openimport/open/company/deletePartTimeJobs?accessToken=xxxxxx

nonce:abcxyXXXXzefg

eid:17951708

data:[
    {
        "commitId": "1", 
        "openId": "5df89ed9e4b0b7058aa9c3f7", 
        "orgId": "bfb2c33f-02e6-4a39-8082-1c3383fc9597"
    }, 
    {
        "commitId": "2", 
        "openId": "5de500e4e4b0b998f379afd7", 
        "orgId": "4fcfba72-e730-4deb-b327-7a2d5c9443ff"
    }
]

返回结果示例:

{
    "success": true,
    "error": "",
    "errorCode": 100,
    "data": []
}

删除所有兼职

描述: 删除所有兼职

URL:https://www.yunzhijia.com/gateway/openimport/open/relationship/deleteAllPartTimeJobs?accessToken=xxxxxx

请求方法：post

内容类型：Content-Type: application/x-www-form-urlencoded

输入参数:

nonce: String // 非必填，用于校验重复请求的随机字符串

eid: Number // 必填，企业id

data: String // 必填，业务数据json字符串

> 请注意，data 不应是js对象而应是一个JSON格式的字符串， 即用JSON.stringify()处理以下结构对象获得的字符串：

{
  "deleteAll": Boolean, //是否删除所有,默认值为false。该值传true时，表示删除所有部门兼职人员（此时list可以不传）；该值为false时，表示删除指定部门兼职人员，list字段必传。
  "list": [ //指定人员删除时，最多允许一次删除1000条记录
      {
      "openId": String, // 人员ID
      "orgId": String // 部门ID
      }
  ]
}

请求示例：

https://www.yunzhijia.com/gateway/openimport/open/relationship/deleteAllPartTimeJobs?accessToken=xxxxxx

nonce:abcxyXXXXzefg

eid:17951708

data:{
    "deleteAll": false, 
    "list": [
        {
            "openId": "5df86ebbe4b0b7058a9efc3d", 
            "orgId": "11e11baa-d74a-44df-b511-2b0b58d2a19e"
        }, 
        {
            "openId": "5df87378e4b013c7ff844226", 
            "orgId": "d03840e2-f345-4fb2-b74a-55fce2113e6f"
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

批量查询兼职

描述: 批量查询兼职

注意:

该接口只会返回所有人在兼职部门里的职位，主职部门里的职位不会返回，可以使用人员部分里的接口，例如：/gateway/openimport/open/person/getall进行查询。

URL:https://www.yunzhijia.com/gateway/openimport/open/company/queryPartTimeJobs?accessToken=xxxxxx

请求方法：post

内容类型：Content-Type: application/x-www-form-urlencoded

输入参数:

nonce: String // 非必填，用于校验重复请求的随机字符串

eid: Number // 必填，企业id

data: String // 必填，业务数据json字符串

> 请注意，data 不应是js对象而应是一个JSON格式的字符串， 即用JSON.stringify()处理以下结构对象获得的字符串：

{
  "begin": int, // 起始，可选
  "count": int // 条数，可选
}

请求示例：

https://www.yunzhijia.com/gateway/openimport/open/company/queryPartTimeJobs?accessToken=xxxxxx

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
            "openId": "5df87378e4b013c7ff844226",  人员ID
            "jobTitle": "首席用户体验官",  //兼职部门里的职位,该人如果在该部门里有多个兼职职位，会返回英文逗号隔开的形式,例："兼职职位a,兼职职位b,兼职职位3"
            "weights": 2147483647,
            "orgId": "d03840e2-f345-4fb2-b74a-55fce2113e6f"  部门ID
        },
        {
            "openId": "5df86ebbe4b0b7058a9efc3d",
            "jobTitle": "运营部资深顾问",//兼职部门里的职位,该人如果在该部门里有多个兼职职位，会返回英文逗号隔开的形式,例："兼职职位a,兼职职位b,兼职职位3"
            "weights": 2147483647,
            "orgId": "11e11baa-d74a-44df-b511-2b0b58d2a19e"
        }
    ]
}

FAQ

暂无

--- 文档抓取完成 ---

接口名称 | URL | 备注

根据部门id批量添加兼职 | /gateway/openimport/open/company/addPartTimeJobs

根据部门id批量更新覆盖兼职职位 | /gateway/openimport/open/company/setPartTimeJobs

根据部门长名称批量设置兼职 | /gateway/openimport/open/company/addPartTimeJobsFull

根据部门id批量删除兼职 | /gateway/openimport/open/company/deletePartTimeJobs

删除所有兼职 | /gateway/openimport/open/relationship/deleteAllPartTimeJobs

批量查询兼职 | /gateway/openimport/open/company/queryPartTimeJobs

字段名 | 数据类型 | 是否必填 | 说明

nonce | String | 否 | 校验重复请求,格式为16位以内随机字符串

eid | String | 是 | 注册企业团队id

data | String | 是 | 业务数据,json字符串格式

---