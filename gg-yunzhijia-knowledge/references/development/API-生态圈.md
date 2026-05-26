---
domain: development
module: 生态圈
keywords: [IM, accessToken, appId, person, role]
---

## 生态圈

生态圈

生态圈

> 本页的接口使用 resGroupSecret 级别的 AccessToken。

请在 管理中心-系统设置-系统集成-资源授权 中找到 生态圈同步 的授权码， 然后调用系统接口换取 AccessToken。

如果您还不了解如何获取AccessToken，请点击此处

API列表

查询伙伴对应的主企业业务对接人列表

URL:/gateway/open/linkspace/spacePartnerCharge/partnerChargeList?accessToken=xxxxxx

输入参数:

{
   "spaceId":"5ab4b4212671ec49cc083914",  //空间id
   "partnerEid":"90001055"               //伙伴企业eid
}

输出结果:

{
    "data":[
        {
            "chargeUser":{                             //接口人信息
                "department":"云之家深圳rbu",
                "eid":"050040",
                "oid":"5a7a9ba5e4b08d3f6fc24b1b",
                "openId":"56eb60cf00b095754463e68d",
                "orgId":"35ab5e86-185d-4175-b93f-7794dfeb91ef",
                "phone":"18503039848",
                "photoUrl":"http://192.168.22.144/space/c/photo/load?id=57c4ecd800b0c12116476609",
                "userName":"临江鲜哈哈哈哈"
            },
            "longOrgId":"5a7a999184ae55b129144192!65031252-0bd0-11e8-9592-82e47cc7294a!35ab5e86-185d-4175-b93f-7794dfeb91ef",
            "orgId":"35ab5e86-185d-4175-b93f-7794dfeb91ef",
            "partnerEid":"2704102",                      //伙伴企业eid
            "spaceId":"5ab4b4212671ec49cc083914"         //空间id
        }
    ],
    "error":null,
    "errorCode":0,
    "success":true
}

查询该用户在生态圈的身份

URL:/gateway/open/linkspace/spaceUser/getUserIdentity?accessToken=xxxxxx

输入参数:

{
    "spaceId":"5ab4b4212671ec49cc083914",  //生态圈空间Id
    "eid":"50040",                         //用户所在企业的eid
    "phone":"13620980800"                  //用户手机号
}

输出结果:

{
    "data":{
        "partnerAdmin":false,  //是否为伙伴负责人
        "spaceAdmin":false,    //是否为主企业空间管理员
        "partnerCharge":false, //是否为业务对接人
        "mainUserFlag":false,  //是否为主企业普通成员
        "partnerContact":false //是否为伙伴企业接口人
    },
    "error":null,
    "errorCode":0,
    "success":true
}

获取伙伴企业的负责人列表

URL:/gateway/open/linkspace/spaceUser/partnerAdminList?accessToken=xxxxxx

输入参数:

{
   "spaceId":"5ab4b4212671ec49cc083914",   //空间id
   "partnerEid":"90001055"                //伙伴企业eid
}

输出结果:

{
 "data":[
        {
            "partnerEid":"2704102", //伙伴企业eid
            "partnerEname":"广州卓实有限公司",  //伙伴企业圈名
            "spaceId":"5ab4b4212671ec49cc083914", //空间id
            "user":{
                "department":"广州卓实有限公司", //部门名称
                "eid":"2704102",                 //人员所在圈的eid
                "oid":"59bb400a60b2cdf319b8f425",
                "openId":"59ba276460b2cdf319b48955",
                "orgId":"f55e4a5c-1678-11e6-8fae-82e47cc7294a",
                "phone":"13688340011",
                "photoUrl":"http://192.168.22.144/space/c/photo/load?id=59c8ab21f4f64f7d1b979da7",
                "userName":"张广翔"
            },
            "userLongOrgId":"f55e4a5c-1678-11e6-8fae-82e47cc7294a",
            "userType":"PARTER"                  //人员类型，是否为主企业或者伙伴企业
        },
        {
            "partnerEid":"2704102",
            "partnerEname":"广州卓实有限公司",
            "spaceId":"5ab4b4212671ec49cc083914",
            "user":{
                "department":"销售部",
                "eid":"2704102",
                "oid":"57318e6f00b091097b66ea1a",
                "openId":"5680a36b00b04e146ff9b6d3",
                "orgId":"39c55f0a-167a-11e6-8fae-82e47cc7294a",
                "phone":"18622331902",
                "photoUrl":"http://192.168.22.144/space/c/photo/load?id=58f9c86ff4f64f44ae1c43bb",
                "userName":"史家科"
            },
            "userLongOrgId":"f55e4a5c-1678-11e6-8fae-82e47cc7294a!39c55f0a-167a-11e6-8fae-82e47cc7294a",
            "userType":"PARTER"
        }
    ],
    "error":null,
    "errorCode":0,
   "success":true
}

查询生态圈内的主企业和伙伴企业间的授权状态

URL:/gateway/open/linkspace/spacePartner/getPartnerIdentity?accessToken=xxxxxx

输入参数:

{
    "spaceId":"5ab4b4212671ec49cc083914",   //空间id
    "eid":"050040",                        //主企业eid
    "partnerEid":"90001055"               //伙伴企业eid
}

输出结果:

{
    "data":{
        "status":1     //1：正常，2：解除
    },
    "error":null,
    "errorCode":0,
    "success":true
}

查询主企业所负责的合作伙伴列表

URL:/gateway/open/linkspace/spacePartner/search?accessToken=xxxxxx

输入参数:

{
    "spaceId" : "5ab4b4212671ec49cc083914", // 空间ID，对应空间列表接口的ID值
    "key":"测试",                           // 搜索关键字，只支持伙伴名称查找
    "page": 1,
    "size": 10
}

输出结果:

{
    "data": {
    "milliseconds": 54,
    "pageNumber": 1,
    "totalPages": 1,
    "count": 5,
    "pageSize": 10,
    "list": [
            {
            "spaceId": "5ab4b4212671ec49cc083914",// 空间ID
            "eid": "050040",// 主企业EID
            "userCount": 1,// 伙伴企业的可见人数
            "partnerName": "515测试自建应用测试",// 伙伴企业公司名称
            "partnerEid": "6815821",// 伙伴企业EID
            "id": "5abc5267b65a1832e7c3cd7e",// 伙伴企业ID,用于查询具体的伙伴企业信息
            "partnerEname": "515测试自建应用"// 伙伴企业工作圈名称
            }
        ]
    },
    "error": null,
    "errorCode": 0,
    "success": true
}

批量新增伙伴企业

URL:/gateway/open/linkspace/spacePartner/batchSaveSpacePartner?accessToken=xxxxxx

输入参数:

{
    "spaceId":"5ab4b4212671ec49cc083914",
    "data":[
        {
            "partnerEid":"2704102",
            "partnerEname":"广州卓实有限公司",
            "partnerUsers":[
                {
                    "userName":"张广翔111",
                    "phone":"13682341022"
                }
            ],
            "chargeUsers":[
                {
                    "userName":"wwww",
                    "phone":"15625123759"
                }
            ],
            "address":"地址111",
            "roleGroup":[

            ]
        },
        {
            "partnerEid":"2704103",
            "partnerEname":"广州卓越有限公司",
            "partnerUsers":[
                {
                    "userName":"张广翔123",
                    "phone":"13682341022"
                }
            ],
            "chargeUsers":[
                {
                    "userName":"wwww",
                    "phone":"15625123759"
                }
            ],
            "address":"地址111",
            "roleGroup":[

            ]
        }
    ]
}

输出结果:(返回出错的伙伴列表):

{
    "data":[
        "xxxx",
        "xxxx"
    ],
    "error": null,
    "errorCode": 0,
    "success": true
}

启用伙伴企业合作

URL:/gateway/open/linkspace/spacePartner/resumeSpacePartner?accessToken=xxxxxx

输入参数:

{
    "spaceId":"5ab4b4212671ec49cc083914",//主企业生态圈id
    "phone":"1365682214",//操作者手机号
    "eid":"5623",//操作者所在云之家团队eid
    "partnerEids":[
            "123",//伙伴的eid
            "124",
            "125"
     ]
}

输出结果:

{
    "data":[
        "123",//操作成功的伙伴的eid
        "123",
        "123"
    ],
    "error": null,
    "errorCode": 0,
    "success": true
}

解除伙伴企业合作

URL:/gateway/open/linkspace/spacePartner/cancelSpacePartner

输入参数:

{
    "spaceId":"5ab4b4212671ec49cc083914",//主企业生态圈id
    "phone":"1365682214",//操作者手机号
    "eid":"5623",//操作者所在云之家团队eid
    "partnerEids":[
            "123",//伙伴的eid
            "123",
            "123"
    ]
}

输出结果:

{
    "data":[
        "123",//操作成功的伙伴的eid
        "123",
        "123"
    ],
    "error": null,
    "errorCode": 0,
    "success": true
}

删除伙伴企业

URL:/gateway/open/linkspace/spacePartner/delSpacePartner?accessToken=xxxxxx

输入参数:

{
    "eid":"050040",                   //主企业eid
    "phone":"18503039848",           //空间管理员的手机号
    "ids":[
        "123",                      //伙伴的id，可以从伙伴列表接口获取
        "123",
        "123"
    ]
}

输出结果:

{
    "data":[
        "123",              //伙伴的id
        "123",
        "123"
    ],
    "error": null,
    "errorCode": 0,
    "success": true
}

生态圈发送待办消息

URL:/gateway/open/linkspace/spaceApp/sendToDoMessage?accessToken=XXXXXXXXX

输入参数:

{
	"sourceId": "112233449",//生成的待办所关联的第三方服务业务记录的ID，待办的批次号
	"senderId": "43434343434",//发送人oid
	"appId": "11111",//自建应用id
	"headImg": "https://www.yunzhijia.com/space/c/photo/load?id=5a2f7ad750f8dd7810e79981",//待办在客户端显示的图URL
	"itemtitle": "itemtitle",//待办项标题内容显示,选填，如不填，则默认为title值
	"title": "title",//来自字段的内容显示
	"params": [{
		"openId": "7878787",//待办接收人oid
		"status": {
			"READ": 0,//目标读状态，0表示未读，1表示已读，默认为0
			"DO": 0//目标处理状态，0表示未办，1表示已办，默认为0
		}
	},
	{
		"openId": "78787871",
		"status": {
			"READ": 0,
			"DO": 0
		}
	}],
	"content": "待办内容",
	"url": "http://www.baidu.com";//待办在客户端显示的图URL
}

输出结果:

{
    "data": true,
    "error": null, 
    "errorCode": 0, 
    "success": true
}

通过ticket获取生态圈成员身份信息

URL:/gateway/open/linkspace/linkSpace/getUserInfoByTicket?accessToken=54bq6YKnPuWlkaT0JmHUbQreQgN29PQ5

输入参数:

{
    "userTicket":"ddfdfvbvb vw2121242"          //生态圈成员的ticket
}

输出结果:

{
    "data": {
        "eid": "50017884",
        "gender": "1",
        "openId": "5acf48a084ae4c7aea91da1d",
        "jobTitle": "",
        "oid": "5b8cdc3e84ae6a7deda48180",
        "userName": "张金云yy",
        "userId": "5acf48a084ae4c7aea91da1d",
        "orgId": "",
        "photoUrl": "http://192.168.22.144/space/c/photo/load?id=5aefaf82b6238e31a8f48101",
        "phone": "18520894078",
        "name": "张金云yy2",
        "personId": "5b8cdc3e84ae6a7deda4817f",
        "department": "",
        "email": "",
        "status": 1
    },
    "error": null,
    "errorCode": 0,
    "success": true
}

新增业务范围

URL:/gateway/open/linkspace/spaceRoleGroup/addRoleGroupAndParent?accessToken=54bq6YKnPuWlkaT0JmHUbQreQgN29PQ5

输入参数:

{
    "spaceId":"5ab4b4212671ec49cc083914",   //生态圈空间Id
    "eid":"050040",                         //用户所在企业的eid
    "phone":"18520894078",                  //用户手机号
    "data":[
		{
			"name": "机构类q\\广东省公司\\东莞2\\k"
		},
		{
			"name": "机构类额\\\\广东省公司\\东莞2\\k"
		},
		{
			"name": "机构类别\\广东省公司d\\东莞2\\k"
		}
    ]
}

输出结果:

{
    "data": [    //添加成功的的返回id，失败的errCode，message会提示失败原因
        {
            "name": "机构类q\\广东省公司\\东莞2\\k",
            "id": "5d1d9c7fb65a184a85c39715"
        },
        {
            "errCode": 3200010,
            "name": "机构类额\\\\广东省公司\\东莞2\\k",
            "message": "参数错误"
        },
        {
            "errCode": 3214002,
            "name": "机构类别\\广东省公司d\\东莞2\\k",
            "message": "业务范围名称已存在"
        }
    ],
    "error": null,
    "errorCode": 0,
    "success": true
}

更新业务范围

URL:/gateway/open/linkspace/spaceRoleGroup/updateRoleGroup?accessToken=54bq6YKnPuWlkaT0JmHUbQreQgN29PQ5

输入参数:

{
    "spaceId":"5ab4b4212671ec49cc083914",  //生态圈空间Id
    "eid":"050040",                         //用户所在企业的eid
    "phone":"18520894078",                  //用户手机号
    "data":[
        {
          "id": "5b44814b329ab928f8f2aacdw",//父节点id,没有可不传
          "name": "webApp2621",
        },
        {
          "id": "5b44814b329ab928f8f2aacdw2",//父节点id,没有可不传
          "name": "webApp262e1"
        }
    ]
}

输出结果:

{
    "data": [
        {
            "errCode": 3214003,
            "name": "webApp2621",
            "weight": "6",
            "id": "5b44814b329ab928f8f2aacdw",
            "message": "选择节点不存在"
        },
        {
            "errCode": 3214003,
            "name": "webApp262e1",
            "weight": "6",
            "id": "5b44814b329ab928f8f2aacdw2",
            "message": "选择节点不存在"
        }
    ],
    "error": null,
    "errorCode": 0,
    "success": true
}

删除业务范围

URL:/gateway/open/linkspace/spaceRoleGroup/deleteRoleGroup?accessToken=54bq6YKnPuWlkaT0JmHUbQreQgN29PQ5

输入参数:

{
    "spaceId":"5ab4b4212671ec49cc083914",    //生态圈空间Id
    "eid":"050040",                          //用户所在企业的eid
    "phone":"18520894078",                   //用户手机号
    "data":["5b447ffb329ab928f8f2aac2","dd"] //业务范围id

}

输出结果:

{
    "data": [
        {
            "errCode": 3214003,
            "id": "5b447ffb329ab928f8f2aac2",
            "message": "选择节点不存在"
        },
        {
            "errCode": 3214003,
            "id": "dd",
            "message": "选择节点不存在"
        }
    ],
    "error": null,
    "errorCode": 0,
    "success": true
}

查询业务范围

URL:/gateway/open/linkspace/spaceRoleGroup/listRoleGroup?accessToken=54bq6YKnPuWlkaT0JmHUbQreQgN29PQ5

输入参数:

{
    "spaceId":"5ab4b4212671ec49cc083914",  //生态圈空间Id
    "eid":"050040",                         //用户所在企业的eid
    "phone":"18520894078"                  //用户手机号
}

输出结果:

{
    "data": [
        {
            "spaceId": "5ab4b4212671ec49cc083914",
            "children": [
                {
                    "spaceId": "5ab4b4212671ec49cc083914",
                    "children": [],
                    "name": "珠海",
                    "weight": "",
                    "pid": "5b3206b8b65a1848e97159be",
                    "permission": null,
                    "id": "5b345a85b65a1825aecc4910",
                    "longId": "5b32013db65a18086b0ef530!5b3206b8b65a1848e97159be!5b345a85b65a1825aecc4910",
                    "longName": "EAS!广州!珠海"
                },
                {
                    "spaceId": "5ab4b4212671ec49cc083914",
                    "children": [],
                    "name": "佛山",
                    "weight": "",
                    "pid": "5b3206b8b65a1848e97159be",
                    "permission": null,
                    "id": "5b345a8db65a1825aecc4911",
                    "longId": "5b32013db65a18086b0ef530!5b3206b8b65a1848e97159be!5b345a8db65a1825aecc4911",
                    "longName": "EAS!广州!佛山"
                }
            ],
            "name": "广州",
            "weight": "",
            "pid": "5b32013db65a18086b0ef530",
            "id": "5b3206b8b65a1848e97159be",
            "longId": "5b32013db65a18086b0ef530!5b3206b8b65a1848e97159be",
            "longName": "EAS!广州"
        }
    ],
    "error": null,
    "errorCode": 0,
    "success": true
}

FAQ

如何获取spaceId？

spaceId在web端的首页可以查看，为生态圈id，如下图：

[图片加载失败]

--- 文档抓取完成 ---

接口名称 | 请求方法 | URL

查询伙伴对应的主企业业务对接人列表 | get | /gateway/open/linkspace/spacePartnerCharge/partnerChargeList

查询该用户在生态圈的身份 | get | /gateway/open/linkspace/spaceUser/getUserIdentity

获取伙伴企业的负责人列表 | get | /gateway/open/linkspace/spaceUser/partnerAdminList

查询生态圈内的主企业和伙伴企业间的授权状态 | get | /gateway/open/linkspace/spacePartner/getPartnerIdentity

查询主企业所负责的合作伙伴列表 | get | /gateway/open/linkspace/spacePartner/search

批量新增伙伴企业 | post | /gateway/open/linkspace/spacePartner/batchSaveSpacePartner

启用伙伴企业合作 | post | /gateway/open/linkspace/spacePartner/resumeSpacePartner

解除伙伴企业合作 | post | /gateway/open/linkspace/spacePartner/cancelSpacePartner

删除伙伴企业 | post | /gateway/open/linkspace/spacePartner/delSpacePartner

生态圈发送待办消息 | post

---