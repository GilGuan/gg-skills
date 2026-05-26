---
domain: development
module: 组织人员
keywords: [IM, accessToken, person, role, secret]
---

## 组织安全文档

组织安全文档

组织安全API列表

接口授权

本页接口使用 resGroupSecret 级别的 AccessToken， 与获取组织数据的接口不同，请注意区分。

请在 管理中心-系统设置-系统集成-通讯录同步 中，复制 只读秘钥 或者 可编辑秘钥， 然后调用系统接口换取 AccessToken。

> 只读秘钥：只能调用查询类的接口

> 可编辑秘钥：可以调用全部接口

如果您还不了解如何获取AccessToken，请点击此处

接口列表

新增搜索可见规则

描述: 新增搜索可见规则

URL:https://www.yunzhijia.com/gateway/gateway/openorg/api/org/sync/searchVisibleRule/batchSave?accessToken=xxxxxx

请求方法：post

内容类型：Content-Type: application/json

输入参数: (注：主视角和目标必需有其中一个参与)

json格式如下：

{
    "openId":"61e010727b1ab4000xxxx",//--操作人openId
    "rules":[{
        "eid":"xxxxxx",
        "name":"测试组织安全",
        "action":"INVISIBLE",//(INVISIBLE(不可见)/VISIBLE(可见)
        "desc":"测试组织安全",
        "openIds":"[\"60ada9a4e4b084axxxxx\",\"5dc92f64e4b0b1406xxxxxx\"]",//主视角人员openId--非必传
        "orgs": "[]",//主视角部门id--非必传
        "roles": "[]",//主视角角色id-非必传(INVISIBLE时该项不支持传参)
        "targetOpenIds“:"[]",//目标人员openIds--非必传
        "targetOrgs":"[\"a030ef0e-aed4-11eb-8a77-ecfxxxxx\",\"7552d4d1-6f59-4e34-a0d4-7b4xxxxx\"]",//目标部门ids--非必传
        "excludeOpenIds":"[\"616a8cede4b00d46xxxx\"]" //不包括人员openId--非必传(INVISIBLE时生效)
        "excludeOrgs":"[\"616a8cede4b00d4642xxxxx\"]" //不包括部门orgId--非必传(INVISIBLE时生效)
    }]
}
注：excludeRoles(不包括角色)在该接口中不论INVISIBLE或VISIBLE均不支持

返回结果如：

{
    "success": true,
    "errorCode": 0,
    "error": null,
    "data": {
        "ids": "67d92f26e4b0c0bb01xxxxxx"
    }
}

注意：ids为返回创建后的规则id

postman演示：

新增可见规则

描述: 新增可见规则

URL:https://www.yunzhijia.com/gateway/gateway/openorg/api/org/sync/visibleRule/batchSave?accessToken=xxxxxx

请求方法：post

内容类型：Content-Type: application/json

输入参数:  (注：主视角和目标必需有其中一个参与)

json格式如下：

{
    "openId":"61e010727b1ab40001xxxxxx",//--操作人openId
    "rules":[{
        "eid":"xxxxx",
        "name":"测试组织安全",
        "action":"VISIBLE",//(INVISIBLE(不可见)/VISIBLE(可见)
        "desc":"测试组织安全",
        "openIds":"[\"60ada9a4e4b084ae4xxxxx\",\"5dc92f64e4b0b1406xxxxxxx\"]",//主视角人员openId--非必传(VISIBLE时生效)
        "orgs": "[]",//主视角部门id--非必传
        "roles": "[]",//主视角角色id-非必传(INVISIBLE时该项不支持传参)
        "targetOpenIds“:"[]",//目标人员openIds--非必传
        "targetOrgs":"[\"a030ef0e-aed4-11eb-8a77-xxxxxx\",\"7552d4d1-6f59-4e34-a0d4-7b4e8ffa3714\"]",//目标部门--非必传(VISIBLE时生效)
        "targetRoles":"[\"689d0d38-dd90-441d-a4f2-xxxxxx\"]",//目标角色roleId--非必传(INVISIBLE时该项不支持传参)
        "excludeOpenIds":"[\"616a8cede4b00d46de0xxxx\"]" //不包括人员openId--非必传(INVISIBLE时生效)
        "excludeOrgs":"[\"616a8cede4b00d4642xxxxx\"]" //不包括部门orgId--非必传(INVISIBLE时生效)
        "excludeRoles":"[\"616a8cede4b00d464xxxx\"]" //不包括目标角色roleId--非必传(INVISIBLE时该项不支持传参)
    }]
}

返回结果如：

{
    "success": true,
    "errorCode": 0,
    "error": null,
    "data": {
        "ids": "67d92f26e4b0c0bb01axxxxxx"
    }
}

注：ids为返回创建后的规则id

postman演示：

删除搜索可见规则

描述: 删除搜索可见规则

URL:https://www.yunzhijia.com/gateway/gateway/openorg/api/org/sync/searchVisibleRule/batchDelete?accessToken=xxxxxx

请求方法：post

内容类型：Content-Type: application/json

输入参数:

json格式如下：

{
    "openId":"5cda2b10e4b081d2f8xxxxxx",//--操作人openId
    "ids":"67d92f26e4b0c0bb01axxxxx,67d9083ae4b0c0bb01axxxxx"//--规则id,可根据查询接口取到
}

返回结果如：

{
    "success": true,
    "errorCode": 0,
    "error": null,
    "data": {
        "ids": [
            "67d9083ae4b0c0bb01axxxx",
            "67d92f26e4b0c0bb01axxxx
        ]
    }
}

postman演示：

删除可见规则

描述: 删除可见规则

URL:https://www.yunzhijia.com/gateway/gateway/openorg/api/org/sync/visibleRule/batchDelete?accessToken=xxxxxx

请求方法：post

内容类型：Content-Type: application/json

输入参数:

json格式如下：

{
    "openId":"5cda2b10e4b081d2f8xxxxxx",//--操作人openId
    "ids":"67d92f26e4b0c0bb01axxxxx,67d9083ae4b0c0bb01axxxxx"//--规则id,可根据查询接口取到
}

返回结果如：

{
    "success": true,
    "errorCode": 0,
    "error": null,
    "data": {
        "ids": [
            "67d9083ae4b0c0bb01axxxx",
            "67d92f26e4b0c0bb01axxxx
        ]
    }
}

postman演示：

查询搜索可见规则

描述: 查询搜索可见规则

URL:https://www.yunzhijia.com/gateway/gateway/openorg/api/org/sync/searchVisibleRule/list?accessToken=xxxxxx

请求方法：post

内容类型：Content-Type: application/json

输入参数:

json格式如下：

{
    "eid":"xxxxxx",
    "page":0,
    "pageSize":20
}

返回结果如：

{
    "success": true,
    "errorCode": 0,
    "error": null,
    "data": {
        "total": 1,
        "rules": [
            {
                "id": "67d9631be4b05c833xxx",
                "name": "测试组织安全",
                "action": "INVISIBLE",
                "desc": "测试组织安全",
                "valid": "true",
                "persons": [
                    {
                        "id": "63edeed9e4b03f47cxxx",
                        "name": "1未清二",
                        "photoUrl": "https://kdtest.kdweibo.cn/space/c/photo/load?id=63edeed9cc3xxxx5",
                        "oid": "63edeed9ddbade0xxx"
                    },
                    {
                        "id": "5cbff38ce4b0d31bxxx",
                        "name": "hk12",
                        "photoUrl": "https://kdtest.kdweibo.cn/space/c/photo/load?id=5cbff38d59fbxxx0",
                        "oid": "5cbff38ce4b0d31b146fxxx"
                    }
                ],
                "orgs": [],
                "roles": [],
                "excludePersons": [
                    {
                        "id": "63edeed9e4b03fxxx",
                        "name": "1未清二",
                        "photoUrl": "https://kdtest.kdweibo.cn/space/c/photo/load?id=63edeed9cc39xx5",
                        "oid": "63edeed9ddbade0001047640"
                    }
                ],
                "excludeOrgs": [
                    {
                        "id": "9270906c-878a-4e34-9633-xxxxx",
                        "name": "登录测试-改名了1",
                        "longName": "7001常用测试圈/登录测试-改名了1"
                    }
                ],
                "excludeRoles": [],
                "targetPersons": [],
                "targetOrgs": [
                    {
                        "id": "9270906c-878a-4e34-9633-xx",
                        "name": "登录测试-改名了1",
                        "longName": "7001常用测试圈/登录测试-改名了1"
                    },
                    {
                        "id": "a0f8e23f-22b2-4b55-b187-xxx",
                        "name": "常用部门-改名了1111",
                        "longName": "7001常用测试圈/常用部门-改名了1111"
                    }
                ],
                "targetRoles": [],
                "syncStatus": "SUCCESS",
                "createBy": "hk12",
                "lastUpdatePerson": "hk12",
                "createTime": 1742299931718,
                "updateTime": 1742299931718
            }
        ]
    }
}

postman演示：

查询可见规则

描述: 查询可见规则

URL:https://www.yunzhijia.com/gateway/gateway/openorg/api/org/sync/visibleRule/list?accessToken=xxxxxx

请求方法：post

内容类型：Content-Type: application/json

输入参数:

json格式如下：

{
    "eid":"xxxxx",
    "page":0,
    "pageSize":20
}

返回结果如：

{
    "success": true,
    "errorCode": 0,
    "error": null,
    "data": {
        "total": 2,
        "rules": [
            {
                "id": "67d92ab8e4b0ef7ebe2xxx0",
                "name": "测试组织安全",
                "action": "VISIBLE",
                "desc": "测试组织安全",
                "valid": "true",
                "persons": [
                    {
                        "id": "63edeed9e4b03f47cxxx",
                        "name": "1未清二",
                        "photoUrl": "https://kdtest.kdweibo.cn/space/c/photo/load?id=63edeed9cc39bxxx",
                        "oid": "63edeed9ddbade00010xx"
                    },
                    {
                        "id": "5cbff38ce4b0d31b146fxx",
                        "name": "hk12",
                        "photoUrl": "https://kdtest.kdweibo.cn/space/c/photo/load?id=5cbff38d59fbf9165xx",
                        "oid": "5cbff38ce4b0d31b14xx"
                    }
                ],
                "orgs": [],
                "roles": [],
                "excludePersons": [
                    {
                        "id": "63edeed9e4b03f47ce5xxx",
                        "name": "1未清二",
                        "photoUrl": "https://kdtest.kdweibo.cn/space/c/photo/load?id=63edeed9cc39bbxxx",
                        "oid": "63edeed9ddbade0001xx"
                    }
                ],
                "excludeOrgs": [
                    {
                        "id": "9270906c-878a-4e34-9633-xxx",
                        "name": "登录测试-改名了1",
                        "longName": "7001常用测试圈/登录测试-改名了1"
                    }
                ],
                "excludeRoles": [
                    {
                        "id": "538d396c-a0d1-4336-b7eb-xxx",
                        "name": "审批节点1",
                        "groupId": "4194f4ef-0358-11e9-91e8-xxx",
                        "groupName": "默认"
                    }
                ],
                "targetPersons": [],
                "targetOrgs": [
                    {
                        "id": "9270906c-878a-4e34-9633-xxxx",
                        "name": "登录测试-改名了1",
                        "longName": "7001常用测试圈/登录测试-改名了1"
                    },
                    {
                        "id": "a0f8e23f-22b2-4b55-b187-xxxxxf",
                        "name": "常用部门-改名了1111",
                        "longName": "7001常用测试圈/常用部门-改名了1111"
                    }
                ],
                "targetRoles": [],
                "syncStatus": null,
                "createBy": "hk12",
                "lastUpdatePerson": "hk12",
                "createTime": 1742285496269,
                "updateTime": 1742285496269
            },
            {
                "id": "673e97ede4b036cxx",
                "name": "不可见",
                "action": "INVISIBLE",
                "desc": "1",
                "valid": "true",
                "persons": [],
                "orgs": [
                    {
                        "id": "5bfcfe2be4b0ffeff9axxx",
                        "name": "7001常用测试圈",
                        "longName": "7001常用测试圈"
                    }
                ],
                "roles": [],
                "excludePersons": [],
                "excludeOrgs": [],
                "excludeRoles": [],
                "targetPersons": [],
                "targetOrgs": [
                    {
                        "id": "a0f8e23f-22b2-4b55-b187-xxx",
                        "name": "常用部门-改名了1111",
                        "longName": "7001常用测试圈/常用部门-改名了1111"
                    }
                ],
                "targetRoles": [],
                "syncStatus": null,
                "createBy": "7001",
                "lastUpdatePerson": "7001",
                "createTime": 1732155373225,
                "updateTime": 1732155548113
            }
        ]
    }
}

postman演示：

--- 文档抓取完成 ---

接口名称 | URL | 备注

新增搜索可见规则 | /gateway/openorg/api/org/sync/searchVisibleRule/batchSave

新增可见规则 | /gateway/openorg/api/org/sync/visibleRule/batchSave

删除搜索可见规则 | /gateway/openorg/api/org/sync/searchVisibleRule/batchDelete

删除可见规则 | /gateway/openorg/api/org/sync/visibleRule/batchDelete

查询搜索可见规则 | /gateway/openorg/api/org/sync/searchVisibleRule/list

查询可见规则 | /gateway/openorg/api/org/sync/visibleRule/list

---