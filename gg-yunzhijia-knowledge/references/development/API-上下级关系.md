---
domain: development
module: 组织人员
keywords: [IM, accessToken, secret, token, 同步]
---

## 上下级关系

上下级关系API列表

上下级关系API列表

接口授权

本页接口使用 resGroupSecret 级别的 AccessToken， 与获取组织数据的接口不同，请注意区分。

请在 管理中心-系统设置-系统集成-通讯录同步 中，复制 只读秘钥 或者 可编辑秘钥， 然后调用系统接口换取 AccessToken。

> 只读秘钥：只能调用查询类的接口

> 可编辑秘钥：可以调用全部接口

如果您还不了解如何获取AccessToken，请点击此处

接口列表

输入参数说明如下：

批量指定上级

描述: 批量指定上级

URL:https://www.yunzhijia.com/gateway/openimport/open/company/addRelations?accessToken=xxxxxx

请求方法：post

内容类型：Content-Type: application/x-www-form-urlencoded

输入参数:

nonce: String // 非必填，用于校验重复请求的随机字符串

eid: Number // 必填，企业id

data: String // 必填，业务数据json字符串

> 请注意，data 不应是js对象而应是一个JSON格式的字符串， 即用JSON.stringify()处理以下结构对象获得的字符串：

[
  {
    "commitId": String, //唯一标识一次提交
    "openId": String, // 人员ID
    "leaderOpenId": String, // 上级ID
    "relationType": String // 指定上级:”LEADER”,汇报上级：”REPORT”（部门负责人默认为汇报上级）
  }
]

请求示例：

https://www.yunzhijia.com/gateway/openimport/open/company/addRelations?accessToken=xxxxxx

nonce:abcxyXXXXzefg

eid:17951708

data:[
    {
        "commitId": "124", 
        "relationType": "LEADER", 
        "openId": "5de50017e4b0b2767b870423", 
        "leaderOpenId": "5de5003fe4b0b998f379a05e"
    }, 
    {
        "commitId": "12564", 
        "relationType": "LEADER", 
        "openId": "5df870e6e4b0b7058a9f8aef", 
        "leaderOpenId": "5df89ed9e4b0b7058aa9c3f7"
    }, 
]

返回结果示例: 如果批量指定成功，则data里返回[]，如果有未指定成功的，则data中会有指定失败的具体信息，示例如下：

{
    "success": true,
    "error": "",
    "errorCode": 100,
    "data": [  //只有在有失败数据时返回
        {
            "commitId": "124",  //提交ID 
            "errorMsg": "openId不存在"  //此处标识失败原因(随机输一个openid时)
        }
    ]
}

批量删除上级

描述: 批量删除上级关系

URL:https://www.yunzhijia.com/gateway/openimport/open/company/deleteRelations?accessToken=xxxxxx

请求方法：post

内容类型：Content-Type: application/x-www-form-urlencoded

输入参数:

nonce: String // 非必填，用于校验重复请求的随机字符串

eid: Number // 必填，企业id

data: String // 必填，业务数据json字符串

> 请注意，data 不应是js对象而应是一个JSON格式的字符串， 即用JSON.stringify()处理以下结构对象获得的字符串：

[
  {
    "openId": String, // 人员ID
    "leaderOpenId": String, // 上级ID
    "relationType": String // 指定上级:”LEADER”,汇报：”REPORT”
    "commitId": String, //唯一标识一次提交
  }
]

请求示例：

https://www.yunzhijia.com/gateway/openimport/open/company/deleteRelations?accessToken=xxxxxx

nonce:abcxyXXXXzefg

eid:17951708

data:[
    {
        "commitId": "124", 
        "relationType": "LEADER", 
        "openId": "5de50017e4b0b2767b870423", 
        "leaderOpenId": "5de5003fe4b0b998f379a05e"
    }, 
    {
		"commitId": "125",
        "relationType": "LEADER", 
        "openId": "5df89ed9e4b0b7058aa9c3f7", 
        "leaderOpenId": "5de5003fe4b0b998f379a05e"
    }
]

返回结果示例: 如果批量删除成功，则data里返回[]，如果有未成功的，则data中会有删除失败的具体信息，示例如下：

{
    "success": true,
    "error": "",
    "errorCode": 100,
    "data": [  //只有在有失败数据时返回
        {  
            "errorCode": 900018,  //错误码
            "commitId": "125",  //提交ID
            "error": "对应上级不存在"  //此处标识失败原因
        } 
    ]
}

删除所有上级

描述: 删除所有上级

URL:https://www.yunzhijia.com/gateway/openimport/open/relationship/deleteAllRelation?accessToken=xxxxxx

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
      "openId": String, // 人员ID
      "leaderOpenId": String, // 上级ID
      "relationType": String // 指定上级:”LEADER”,汇报：”REPORT”           
      }
  ]
}

请求示例：

https://www.yunzhijia.com/gateway/openimport/open/relationship/deleteAllRelation?accessToken=xxxxxx

nonce:abcxyXXXXzefg

eid:17951708

data:{
    "deleteAll": false, 
    "list": [
        {
            "commitId": "124", 
            "relationType": "LEADER", 
            "openId": "5de50017e4b0b2767b870423", 
            "leaderOpenId": "5de5003fe4b0b998f379a05e"
        }, 
        {
            "commitId": "12564", 
            "relationType": "LEADER", 
            "openId": "5df870e6e4b0b7058a9f8aef", 
            "leaderOpenId": "5df89ed9e4b0b7058aa9c3f7"
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

批量查询上级

描述: 批量查询上级关系

URL:https://www.yunzhijia.com/gateway/openimport/open/company/queryRelations?accessToken=xxxxxx

请求方法：post

内容类型：Content-Type: application/x-www-form-urlencoded

输入参数:

nonce: String // 非必填，用于校验重复请求的随机字符串

eid: Number // 必填，企业id

data: String // 必填，业务数据json字符串

> 请注意，data 不应是js对象而应是一个JSON格式的字符串， 即用JSON.stringify()处理以下结构对象获得的字符串：

{
  "relationType": String, //指定上级:”LEADER”,汇报：”REPORT”
  "begin": String, // 起始，可选
  "count": String //  条数，可选
}

请求示例：

https://www.yunzhijia.com/gateway/openimport/open/company/queryRelations?accessToken=xxxxxx

nonce:abcxyXXXXzefg

eid:17951708

data:{
    "relationType": "LEADER", 
    "begin": "0", 
    "count": "100"
}

返回结果示例:

{
    "success": true,
    "error": "",
    "errorCode": 100,
    "data": [
        {
            "relationType": "LEADER",  // 指定上级:”LEADER”,汇报：”REPORT”(只能查出未选中的汇报上级，有些部门负责人不需要汇报关系)
            "openId": "5de5003fe4b0b998f379a05e",  // 人员ID
            "leaderOpenId": "5df87378e4b013c7ff844226"  // 上级ID
        },
        {
            "relationType": "LEADER",
            "openId": "5df870e6e4b0b7058a9f8aef",
            "leaderOpenId": "5df86ebbe4b0b7058a9efc3d"
        }
    ]
}

FAQ

暂无

--- 文档抓取完成 ---

接口名称 | URL | 备注

批量指定上级 | /gateway/openimport/open/company/addRelations

批量删除上级 | /gateway/openimport/open/company/deleteRelations

删除所有上级 | /gateway/openimport/open/relationship/deleteAllRelation

批量查询上级 | /gateway/openimport/open/company/queryRelations

字段名 | 数据类型 | 是否必填 | 说明

nonce | String | 否 | 校验重复请求,格式为16位以内随机字符串

eid | String | 是 | 注册企业团队id

data | String | 是 | 业务数据,json字符串格式

---