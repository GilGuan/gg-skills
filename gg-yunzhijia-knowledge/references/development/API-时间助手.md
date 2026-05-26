---
domain: development
module: 时间助手
keywords: [IM, accessToken, appId, callback, person]
---

## 时间助手

时间助手

时间助手相关接口

点击此处查看视频教程

AccessToken

> 本页的接口使用 resGroupSecret 级别的 AccessToken。

请在 管理中心-系统设置-系统集成-资源授权 中找到 时间助手管理 的授权码， 然后调用系统接口换取 AccessToken。

如果您还不了解如何获取AccessToken，请点击此处

日程相关接口

1、新增单个日程接口

URL:https://www.yunzhijia.com/gateway/cloudwork/newwork/create?accessToken=xxx

http请求方法：post

http内容类型：Content-Type:application/json

输入参数：

json示例：

{
    "openid": "5a67e08d00b0e8dfe4aab4fa",
	"content": "新增单个日程接口",
	"startDate": 1530002768912,
    "endDate": 1530687800000,
    "noticeTimes": [5,15,60],
	"actors": ["xxxxxx"],
	"submitExperience": true
    "files": [
              {
                  "fileName": "test.docx",
                  "FileExt": "docx",
                  "fileSize": 56836,
                  "id": "5fdaeda40b7b6400018014a3",
                  "fileType": "docx"
              }
          ],
    "images": [
              {
                  "fileName": "timg.jpg",
                  "FileExt": "jpg",
                  "fileSize": 56826,
                  "id": "5fdaeda40b7b6400010014a3",
                  "fileType": "jpg"
              }
          ],
}

返回结果示例：

{
    "data": {
        "workId": "5b33291f14cada713f839b49"
    },
    "error": null,
    "errorCode": 0,
    "success": true
}

2、查看单个日程接口

URL:

https://www.yunzhijia.com/gateway/cloudwork/newwork/detail?accessToken=xxxx

http的请求方法：post

http的内容类型：Content-Type:application/json

输入参数：

响应结果：

响应结果示例：

{
    "data": {
        "images": [],
        "endDate": 1608186753502,
        "batchId": "5fdaed780b7b640001801442",
        "content": "纪要日程",
        "repeat": 0,
        "record": {
            "photoUrl": "https://dev.kdweibo.cn/space/c/photo/load?id=1",
            "nickName": "xx",
            "commentType": "task",
            "files": [
                {
                    "fileName": "timg (1).jpg",
                    "FileExt": "jpg",
                    "apiUrl": null,
                    "fileSize": 56836,
                    "bizId": null,
                    "fileUrl": null,
                    "id": "5fdaeda40b7b6400018014a3",
                    "type": null,
                    "fileType": "jpg",
                    "fileId": "5fdaeda1ed95b70001b6946a"
                }
            ],
            "content": "发发发",
            "createDate": 1608183204349 
        },
        "files": [],
        "id": "5fdaed780b7b640001801442",
        "hasRecord": true,
        "noticeTimes": [5,15,60],
        "startDate": 1608183153502,
        "repeatEndDate": 1610899199999,
        "createDate": 1608183160582,
        "participants": [
            {
                "readStatus": 1,
                "workStatus": 1,
                "eid": "50014069",
                "photoUrl": "https://dev.kdweibo.cn/space/c/photo/load?id=1",
                "topDate": 0,
                "name": "xx",
                "workSource": "1",
                "personnelSource": 1,
                "acceptStatus": 2,
                "doneTime": 1608183204307,
                "oid": "5facdaf8e4b0957f4040e34f",
               
            }
       ] 
    },
    "agent":"",
    "error": null,
    "errorCode": 0,
    "success": true
}

3、修改单个日程接口

URL:

https://www.yunzhijia.com/gateway/cloudwork/newwork/modify?accessToken=xxxx

http的请求方法：post

http的内容类型：Content-Type:application/json

输入参数：

json示例：

{
    "id": "5b33262e14cada62e4e44822",
	"openid": "5a67e08d00b0e8dfe4aab4fa",
    "content": "修改单个日程接口",
    "startDate": 1530002768912,
	"endDate": 1530687800000,
	"noticeTimes": [5,15,60],
	"actors": ["xxxxxx","xxxxxx"],
	"submitExperience": true
    "files": [
              {
                  "fileName": "test.docx",
                  "FileExt": "docx",
                  "fileSize": 56836,
                  "id": "5fdaeda40b7b6400018014a3",
                  "fileType": "docx"
              }
          ],
    "images": [
              {
                  "fileName": "timg.jpg",
                  "FileExt": "jpg",
                  "fileSize": 56826,
                  "id": "5fdaeda40b7b6400010014a3",
                  "fileType": "jpg"
              }
          ],
}

返回结果示例：

{
    "success": true,
    "errorCode": 0,
    "error": null,
    "data":null
}

4、批量删除日程接口

URL：https://www.yunzhijia.com/gateway/cloudwork/newwork/delete?accessToken=xxxx

http请求方法：post

http内容类型：Content-Type:application/json

输入参数：

>PS：必须是发起人创建的日程，才可以删除

json示例：

{
    "ids": ["5b33275f14cada62e4e44840"],
	"openid": "5a67e08d00b0e8dfe4aab4fa"
}

返回结果示例：

{
    "success": true,
    "errorCode": 0,
    "error": null,
    "data":null
}

5、日程设置为完成

URL：https://www.yunzhijia.com/gateway/cloudwork/newwork/finish?accessToken=xxxx

http请求方法：post

http内容类型：Content-Type:application/json

输入参数：

json示例：

{
	"id": "5b33275f14cada62e4e44840",
    "openid": "5a67e08d00b0e8dfe4aab4fa"
}

返回结果示例：

{
    "success": true,
    "errorCode": 0,
    "error": null,
    "data":null
}

6、日程设置为未完成

URL：https://www.yunzhijia.com/gateway/cloudwork/newwork/unfinish?accessToken=xxxx

http请求方法：post

http内容类型：Content-Type:application/json

输入参数：

json示例：

{
	"id": "5b33275f14cada62e4e44840",
    "openid": "5a67e08d00b0e8dfe4aab4fa"
}

返回结果示例：

{
    "success": true,
    "errorCode": 0,
    "error": null,
    "data":null
}

7、查询工作圈下日程

> 批量查询accessToken对应工作圈下面的日程

> 开发指引：

> 第一页默认的lastId为空，size为每页多少条数据

> 第二页的lastId为上一页最后一条日程的ID，以此类推

URL:

https://www.yunzhijia.com/gateway/cloudwork/newwork/teamWorks?accessToken=xxxx

http请求方法：post

http内容类型：Content-Type:application/json

输入参数：

json示例:

{
    "lastId": "5a67e08d00b0e8dfe4aab4fa",
    "size": 50
}

返回结果示例：

{
    "success": true,
    "errorCode": 0,
    "error": null,
    "data": [
        {
			"id": "5b86ed2fbeb7cc35af769eb8",
			"openid": "5a67e1e1e4b02f1de22a70a3",
			"personName": "张三",
			"type": "generalWork",
			"channel": "workReport",
			"content": "别忘了今天要提交【日报】咯",
			"startDate": 1535558400000,
			"endDate": 1535644799999,
			"createDate": 1535569199741,
			"doneTime": 1535569199741,
			"noticeTime": 0,
            "workStatus": 0,
            "readStatus": 0,
            "acceptStatus": 0,
            "record": false
        }
    ]
}

8、按天查询工作圈下日程

> 按天查询accessToken对应工作圈下面当天的日程

> 开发指引：

> day为需查询的当天任意时间点的时间戳即可

URL:

https://www.yunzhijia.com/gateway/cloudwork/newwork/queryByDay?accessToken=xxxx

http请求方法：post

http内容类型：Content-Type:application/json

输入参数：

json示例：

{
    "day": 1533549600000
}

返回结果示例：

{
    "success": true,
    "errorCode": 0,
    "error": null,
    "data": [
        {
            "workStatus": 0,
            "readStatus": 0,
            "endDate": 1535644799999,
            "openid": "5a67e1e1e4b02f1de22a70a3",
            "channel": "workReport",
            "acceptStatus": 0,
            "type": "generalWork",
            "title": null,
            "content": "别忘了今天要提交【日报】咯",
            "url": null,
            "personName": "张三",
            "record": false,
            "workType": null,
            "doneTime": 1535569199741,
            "id": "5b86ed2fbeb7cc35af769eb8",
            "noticeTime": 0,
            "startDate": 1535558400000,
            "createDate": 1535569199741
        }
    ]
}

9、新增重复日程接口

URL:https://www.yunzhijia.com/gateway/cloudwork/newwork/repeatWork?accessToken=xxxx

http请求方法：post

http内容类型：Content-Type:application/json

输入参数：

json示例：

{
    "openid": "5a67e08d00b0e8dfe4aab4fa",
    "content": "新增重复日程接口",
    "startDate": 1530002768912,
    "endDate": 1530687800000, 
    "noticeTimes": [5,15,60],
    "actors": ["xxxxxx","xxxxxx"], 
    "submitExperience": true, 
    "repeat": 1,
    "repeatEndDate": 1530687800000
}

返回结果示例：

>workIds为添加成功后的日程id集合，其中第一个是父日程ID

{
    "data": {
        "workIds": ["5b614fe80e4f78209cb99689", "5b61504e0e4f78209cb99690", "5b61504e0e4f78209cb9968f"]
    },
    "error": null,
    "errorCode": 0,
    "success": true
}

10、批量修改重复日程接口

> 影响范围仅针对当前ID及以后的日程，如需取消全部请选择第一条，如需取消单条请使用取消单个日程

URL：https://www.yunzhijia.com/gateway/cloudwork/newwork/batchModify?accessToken=xxxx

http请求方法：post

http内容类型：Content-Type:application/json

输入参数：

json示例：

{
	"id": "5b33262e14cada62e4e44822",
	"openid": "5a67e08d00b0e8dfe4aab4fa",
	"content": "批量修改重复日程接口",
	"startDate": 1530002768912,
	"endDate": 1530687800000,
	"noticeTimes": [5,15,60],
	"actors": ["xxxxxx","xxxxxx"],
	"submitExperience": true,
	"repeat": "1",
    "repeatEndDate": 1533549600000
}

返回结果示例：

{
    "success": true,
    "errorCode": 0,
    "error": null,
    "data":null
}

11、批量删除重复日程接口

> 影响范围仅针对当前ID及以后的日程，如需取消全部请选择第一条，如需取消单条请使用取消单个日程

URL：https://www.yunzhijia.com/gateway/cloudwork/newwork/batchDelete?accessToken=xxxx

http请求方法：post

http内容类型：Content-Type:application/json

输入参数：

json示例：

{
    "id": "1234567890",
	"openid": "5a67e08d00b0e8dfe4aab4fa"
}

返回结果示例：

{
    "success": true,
    "errorCode": 0,
    "error": null,
    "data":null
}

12、单个用户日程查询

URL:https://www.yunzhijia.com/gateway/cloudwork/newwork/queryByUser?accessToken=xxx

http请求方法：POST

http内容类型：Content-Type:application/json

输入参数：

json示例：

{
  "pageNum": 1,
  "pageSize": 20,
  "openId": "5fd738d3e4b002b997549efd"
}

返回结果示例：

{
  "data": [
    {
      "channel": "work",
      "content": "test",
      "createDate": 1608109597703,
      "currentActor": {
        "doneTime": 0,
        "noticeTime": 0,
        "pushState": 0,
        "record": false,
        "repeat": 0,
        "submitExperience": false,
        "workPriority": 0,
        "workStatus": 0
      },
      "endDate": 1608113154183,
      "id": "5fd9ce1d41f445000106637c",
      "openId": "5fd738d3e4b002b997549efd",
      "personName": "刘琳",
      "record": false,
      "repeat": 0,
      "repeatEndDate": 1610812799999,
      "startDate": 1608109554183,
      "workStatus": 0
    }
  ],
  "errorCode": 0,
  "success": true
}

任务相关接口

1、查询任务详情接口

URL：https://www.yunzhijia.com/gateway/cloudwork/worktask/find?accessToken=xxx

http请求方法：post

http内容类型：Content-Type:application/json

输入参数：

json示例：

{
	"openId":"5bc58d65e4b0aed875a362cb",
	"id":"5cc55b6fb6238e6f079ddc1f"
}

返回结果示例：

>PS：关于actors

>actors是相关人的集合，通过source字段进行区分身份，source=1(创建人)，source=2(执行人)，source=3(抄送人)。

{
    "data": {
    	"actors": [{
    		"department": "XX科技公司",
    		"eid": "6821512",
    		"openId": "5bc58d65e4b0aed875a362cb",
    		"personName": "张三",
    		"photoUrl": "http://192.168.22.144/space/c/photo/load?id=123456",
    		"progress": 0,
    		"readStatus": 1,
    		"source": 2,
    		"status": 0,
    		"userId": "5bc58d65e4b0aed875a362c4"
    	}],
    	"content": "JUNIT ThirdApi测试",
    	"createDate": 1556417201162,
    	"endDate": 1556294399000,
    	"files": [],
    	"id": "5cc50ab112043d558e1bfd0d",
    	"images": [],
    	"important": 0,
    	"noticeTime": 5,
    	"openId": "5bc58d65e4b0aed875a362cb",
    	"personName": "张三",
    	"status": 0,
    	"timingNoticeTime": 0
    },
    "error": null,
    "errorCode": 0,
    "success": true
}

2、分页查询任务列表接口

URL：https://www.yunzhijia.com/gateway/cloudwork/worktask/page?accessToken=xxx

http请求方法：post

http内容类型：Content-Type:application/json

输入参数：

json示例：

{
    "channel":"FEED",
    "createChannel":"SUGGEST",
	"openId":"5bc58d65e4b0aed875a362cb",
	"pageNum":"1",
	"pageSize":"10"
}

返回结果示例：

>PS：关于actors

>actors是相关人的集合，通过source字段进行区分身份，source=1(创建人)，source=2(执行人)，source=3(抄送人)。

{
	"data": {
    	"data": [{
    		"actors": [{
    			"department": "XX科技公司",
    			"eid": "6821512",
    			"openId": "5bc58d65e4b0aed875a362cb",
    			"personName": "张三",
    			"photoUrl": "http://192.168.22.144/space/c/photo/load?id=123456",
    			"progress": 0,
    			"readStatus": 1,
    			"source": 2,
    			"status": 0,
    			"userId": "5bc58d65e4b0aed875a362c4"
    		}],
    		"content": "JUNIT ThirdApi测试",
    		"createDate": 1556417201162,
    		"endDate": 1556294399000,
    		"files": [],
    		"id": "5cc50ab112043d558e1bfd0d",
    		"images": [],
    		"important": 0,
    		"noticeTime": 5,
    		"openId": "5bc58d65e4b0aed875a362cb",
    		"personName": "张三",
    		"status": 0,
    		"timingNoticeTime": 0
    	}],
    	"pageNum": 1,
    	"pageSize": 10,
    	"totalCount": 1
    },
    "error": null,
    "errorCode": 0,
    "success": true
}

3、新增任务接口

URL：https://www.yunzhijia.com/gateway/cloudwork/worktask/create?accessToken=xxx

http请求方法：post

http内容类型：Content-Type:application/json

输入参数：

PS：关于channel和createChannel

>例如同事圈团队，想创建一个建议的任务，那么channel就是同事圈(FEED)，createChannel就是建议(SUGGEST)；如果同事圈团队想创建其他类型的任务，那么channel还是同事圈(FEED)，createChannel改为其他(XX)

>extApps为外部应用集合，可跳转到第三方轻应用，其中，icon为应用icon，url为跳转地址，desc为对跳转的描述，appId和appName为待跳转应用的appId和appName

json示例：

{
	"openId":"5bc58d65e4b0aed875a362cb",
	"content":"JUNIT测试",
    "startDate":"1556294400000",
	"endDate":"1556294399000",
    "noticeTime":"5",
    "timingNoticeTime":"0",
    "important":0,
	"files": [{
		"fileId": "5cc55b6fb6238e6f079ddc1f",
		"fileName": "qrcode.png",
		"fileSize": 19292,
		"fileExt": "png",
		"fileType": "png"
	}],
	"images": [{
		"fileExt": "png",
		"fileId": "5cc55b64b6238e6f079ddc16",
		"fileName": "qrcode.png",
		"fileSize": 19292,
		"fileType": "image/png"
	}],
    "executors":[
		"5bc58d65e4b0aed875a362cb","5a67f00ee4b06d73f355b6e9"
	],
    "ccs":[
		"5bc58d65e4b0aed875a362cb"
	],
    "channel":"FEED",
    "createChannel":"SUGGEST",
    "extApps": [
        {
            "icon": "http://xxx.com/xxx.png",
            "url": "http://xxx.com/xxx/xxx",
            "desc": "跳转到审批应用",
            "appId": "123456",
            "appName": "审批"
        }
    ]
}

返回结果示例：

{
    "data": {
        "workTaskId": "5b33291f14cada713f839b49"
    },
    "error": null,
    "errorCode": 0,
    "success": true
}

4、 修改任务

URL：POST /gateway/cloudwork/worktask/modify?accessToken=xx

Content-Type: application/json

输入参数：

返回结果示例：

{
    "success": true,
    "errorCode": 0,
    "error": null,
    "data":null
}

5、 完成任务

URL：POST /gateway/cloudwork/worktask/finish?accessToken=xx

Content-Type: application/json

输入参数：

返回结果示例：

{
    "success": true,
    "errorCode": 0,
    "error": null,
    "data":null
}

6、 激活任务

URL：POST /gateway/cloudwork/worktask/activate?accessToken=xx

Content-Type: application/json

输入参数：

返回结果示例：

{
    "success": true,
    "errorCode": 0,
    "error": null,
    "data":null
}

7、 删除任务

URL：POST /gateway/cloudwork/worktask/delete?accessToken=xx

Content-Type: application/json

输入参数：

返回结果示例：

{
    "success": true,
    "errorCode": 0,
    "error": null,
    "data":null
}

8、关闭任务

URL：POST /gateway/cloudwork/worktask/close?accessToken=xx

Content-Type: application/json

输入参数：

返回结果示例：

{
    "success": true,
    "errorCode": 0,
    "error": null,
    "data":null
}

9、更新进度评论

URL：POST /gateway/cloudwork/worktask/actor/comment?accessToken=xx

Content-Type: application/json

输入参数：

extJsonData示例：

{\"workId\":\"5f56f6bb53b1ab0001fb3a0e\",\"progress\":60,\"content\":\"60\",\"commentType\":\"workTask\"}"

返回结果示例：

{
    "success": true,
    "errorCode": 0,
    "error": null,
    "data":null
}

10、单个用户任务查询

URL:https://www.yunzhijia.com/gateway/cloudwork/worktask/queryByUser?accessToken=xxx

http请求方法：POST

http内容类型：Content-Type:application/json

输入参数：

json示例：

{
  "pageNum": 1,
  "pageSize": 20,
  "openId": "5fd738d3e4b002b997549efd",
  "condition": 0
}

返回结果示例：

{
  "data": [
    {
      "content": "test",
      "createDate": 1608281550899,
      "currentActor": {
        "openId": "5fd738d3e4b002b997549efd",
        "progress": 0,
        "source": 4,
        "status": 0
      },
      "doneTime": 0,
      "endDate": 1608285145798,
      "executors": [
        "刘琳"
      ],
      "id": "5fdc6dceaf0cab00011be4d5",
      "openId": "5fd738d3e4b002b997549efd",
      "personName": "刘琳",
      "progress": 0,
      "scoreSwitch": false,
      "status": 0
    }
  ],
  "errorCode": 0,
  "success": true
}

备忘相关接口

1、新增备忘接口

URL:https://www.yunzhijia.com/gateway/cloudwork/notes/addNotes?accessToken=xxx

http请求方法：post

http内容类型：Content-Type:application/json

输入参数：

json示例：

{
    "files": [{
        "fileName": "测试文档.txt",
        "fileSize": 4,
        "fileType": "txt",
        "fileExt": "txt",
        "fileId": "5fdaf7bee602080001fde873"
    }],
    "images": [{
        "fileName": "测试图片.png",
        "fileSize": 537,
        "fileExt": "png",
        "fileType": "image/png",
        "fileId": "5fdaf7bb57d8300001154f66"
    }],
    "participants": [{
        "ids": [],
        "source": 1,
        "type": "OID",
        "workSource": 2
    }],
    "content": "备忘内容",
    "startDate": 1608185775587,
    "openId": "5fd738d3e4b002b997549efd"
}

返回结果示例：

{
	"success": true,
	"errorCode": 0,
	"error": "",
	"data": "5fdaf7c18929d800016eea6d" 
}

2、编辑备忘

URL:https://www.yunzhijia.com/gateway/cloudwork/notes/editNotes?accessToken=xxx

http请求方法：POST

http内容类型：Content-Type:application/json

输入参数：

json示例：

{
	"id": "5fdb12bb13e1630001d6db77",
	"content": "备忘内容",
	"images": [{
		"fileId": "5fdaf7bb57d8300001154f66",
		"fileName": "测试图片.png",
		"fileSize": 537,
		"fileType": "image/png",
		"fileUrl": "https://dev.kdweibo.cn/docrest/file/downloadfile/5fdaf7bb57d8300001154f66"
	}],
	"files": [{
	"fileId": "5fdaf7bee602080001fde873",
		"fileName": "测试文档.txt",
		"fileSize": 4,
		"fileType": "txt",
		"fileUrl": "https://dev.kdweibo.cn/docrest/file/downloadfile/5fdaf7bee602080001fde873"
	}]
}

返回结果示例：

{"errorCode":0,"success":true}

3、删除备忘

URL:https://www.yunzhijia.com/gateway/cloudwork/notes/delNotes?accessToken=xxx

http请求方法：POST

http内容类型：Content-Type:application/json

输入参数：

json示例：

{"id":"5fdb138113e1630001d6dbb5","openId":"5fd738d3e4b002b997549efd"}

返回结果示例：

{"errorCode":0,"success":true}

4、前用户备忘查询

URL:https://www.yunzhijia.com/gateway/cloudwork/notes/queryNotes?accessToken=xxx

http请求方法：POST

http内容类型：Content-Type:application/json

输入参数：

json示例：

{"openId":"5fd738d3e4b002b997549efd","pageNo":1,"limit":20}

返回结果示例：

{"data":[{"content":"备忘内容","createDate":1608192897658,"doneTime":1608189375587,"endDate":1608189375587,"id":"5fdb138113e1630001d6dbb5","openid":"5fd738d3e4b002b997549efd","personName":"刘琳","startDate":1608185775587,"topDate":0,"updateTime":1608209634000,"workSource":"1"},{"content":"备忘内容","createDate":1608192699810,"doneTime":1608189375587,"endDate":1608189375587,"id":"5fdb12bb13e1630001d6db77","openid":"5fd738d3e4b002b997549efd","personName":"刘琳","startDate":1608185775587,"topDate":1608192699810,"updateTime":0,"workSource":"1"}],"errorCode":0,"success":true}

共享日历相关接口

1、查看我共享给他人

URL：GET /gateway/cloudwork/shareCalendar/list/myShares?accessToken=xx&&openId=xx

Content-Type: application/json

输入参数：

返回结果示例：

2、查看他人共享给我

URL：GET /gateway/cloudwork/shareCalendar/list/shareToMe?accessToken=xx&&openId=xx

Content-Type: application/json

输入参数：

返回结果示例：

3、新增/修改我的共享

URL：POST /gateway/cloudwork/shareCalendar/share?accessToken=xx

Content-Type: application/json

输入参数：

json示例：

{
	"openId": "5b33262e14cada62e4e44822",
    "permissions":[1,2],
    "shareOpenIds":["5b33262e14cada62e4e44822"]
}

返回结果示例：

{
    "success": true,
    "errorCode": 0,
    "error": null,
    "data":null
}

4、批量更新我的共享

注意：该接口为全量覆盖式更新我的共享，非单个操作

URL：POST /gateway/cloudwork/shareCalendar/share/batch?accessToken=xx

Content-Type: application/json

输入参数：

<table>

<tr style="font-weight: bold;text-align: center">

<td colspan="2">参数名</td><td>类型</td><td>注释</td>

</tr>

<tr>

<td colspan="2">openId</td><td>string</td><td>共享人oid</td>

</tr>

<tr>

<td rowspan="2">items</td><td>permissions</td><td>array</td><td>权限集合：只查看[1], 允许创建日程和会议[1,2]</td>

</tr>

<tr>

<td>shareOpenId</td><td>string</td><td>被共享人oid</td>

</tr>

</table>

json示例：

{
  "openId": "5facdaf8e4b0957f4040e34f",
  "items": [
    {
      "permissions": [1,2],
      "shareOpenId": "5fb1e61fe4b0c35b1fa03d00"
    },
    {
      "permissions": [1, 2],
      "shareOpenId": "5fb1e649e4b0c35b1fa03d48"
    }
  ]
}

返回结果示例：

{
    "success": true,
    "errorCode": 0,
    "error": null,
    "data":null
}

* 附录

Participant

Record

SubTask

AssociatedTask

Actor

AddSubTask

EditSubTask

>  与AddSubTask一致 增加了id

FileInfo

*回调接口

配置回调地址后，可实现时间助手的增删改数据变化，通过回调的方式告诉第三方开发者，以便第三方开发者在其他系统实现数据的同步修改。

回调地址配置路径（管理员身份）：时间助手>更多>开放平台

callBackUrl为一个Http地址(post请求，Content-Type为application/json，不要鉴权，带有两个入参：id和method)，id就代表该条业务的id，method为执行的业务方法。

回调地址因为不鉴权，所以最好做好限流，避免恶意攻击

在回调方法里面根据需要监听的method，来查询详情接口，然后更新您本地的数据

method示例

查询回调错误日志列表

URL:https://www.yunzhijia.com/gateway/cloudwork/callback/errorLogs?accessToken=xxx

http请求方法：GET

查询参数：

返回结果：

{
  "lastCursorId": "60d5746f40354b64f8b2408d",   // 游标id，用于拉取后续数据时使用
  "data": [
    {
      "id": "60d5745b40354b64f8b24075",  // 业务id，分别是日程，会议和任务
      "method": "1001",                   // 回调方法
      "time": 1624601691929           // 时间戳
    },
    {
      "id": "60d5745b40354b64f8b24075",
      "method": "1003",
      "time": 1624601711094
    }
  ]
}

--- 文档抓取完成 ---

参数 | 类型 | 是否必须 | 注释

openid | string | 是 | 日程发起人的oid

content | string | 是 | 日程内容

startDate | number | 是 | 日程开始时间戳

endDate | number | 是 | 日程结束时间戳

noticeTimes | array(number) | 是 | 提醒时间(-1:不提醒、0:开始时间提醒、15:开始时间前15分钟提醒、60:开始时间前1小时提醒)

actors | array(string) | 是 | 协作人oid的集合

submitExperience | bool | 否 | 是否需要提交日程纪要(新的体会、总结)

repeat | number | 否 | 默认0，重复类型(0不重复, 1每工作日, 2每日, 3每周, 4每两周, 5每月)

repeatEndDate | number | 否 | 重复截止时间，毫秒时间戳，repeat不为0时必填

channel | string | 否 | 渠道，可根据业务需要来区分日程类型

images | array(FileInfo) | 否 | 图片列表

files | array(FileInfo) | 否 | 文件列表

agent | string | 否 | 代建人（代建日程时代建人oid）

参数 | 类型 | 注释

workId | String | 添加成功后日程id

参数名 | 类型 | 注释

id | string | 日程ID

字段 | 类型 | 注释

id | string | 日程ID

content | string | 日程内容

noticeTimes | array(number) | 提醒时间(-1:不提醒、0:开始时间提醒、15:开始时间前15分钟提醒、60:开始时间前1小时提醒)

startDate | number | 日程开始时间，毫秒时间戳

endDate | number | 日程截止时间，毫秒时间戳

repeat | number | 重复周期(0:不重复、1:每工作日、2:每日、3:每周、4:每两周、5:每月)

repeatEndDate | number | 重复截止时间（不要与日程结束时间戳混淆）

batchId | string | 批次ID，仅针对重复日程

createDate | number | 创建时间，毫秒时间戳

participants | array(Participant) | 协作人列表

images | array(FileInfo) | 图片列表

files | array(FileInfo) | 文件列表

hasRecord | bool | 是否有日程总结

record | Record | 日程总结

agent | string | 代建人（代建日程时代建人oid）

参数 | 类型 | 是否必须 | 注释

id | String | 是 | 日程id

openid | String | 是 | 日程发起人的oid，如果是代建日程可以是代建人oid

content | String | 是 | 日程内容

startDate | Long | 是 | 日程开始时间戳

endDate | Long | 是 | 日程结束时间戳

noticeTimes | array(number) | 否 | 提醒时间(-1:不提醒、0:开始时间提醒、15:开始时间前15分钟提醒、60:开始时间前1小时提醒)

actors | 集合 | 否 | 协作人oid的集合

submitExperience | boolean | 否 | 是否需要提交日程纪要(新的体会、总结)

images | array(FileInfo) | 否 | 图片列表

files | array(FileInfo) | 否 | 文件列表

参数 | 类型 | 注释

ids | 集合 | 日程id的集合

openid | String | 日程发起人的oid

参数 | 类型 | 注释

id | String | 日程id

openid | String | 日程发起人的oid

参数 | 类型 | 注释

id | String | 日程id

openid | String | 日程发起人的oid

参数 | 类型 | 注释

lastId | String | 最后一条日程id(默认为空,第一页是为空)

size | int | 每次查多少条(最多不能超过1000条)

参数 | 类型 | 注释

id | String | 日程id

openid | String | 日程发起人的oid

personName | String | 日程创建者的姓名

type | String | 日程类型(cooperationWork:协作日程、generalWork:普通日程)

channel | String | 日程产生渠道(默认为空，只有第三方渠道产生的才有这个标识。recordWork:记事、birthday:生日祝福、workReport:工作汇报、boss:报表秀秀)

content | String | 日程内容

startDate | Long | 日程开始时间戳

endDate | Long | 日程结束时间戳

createDate | Long | 日程创建时间

doneTime | Long | 日程完成时间

noticeTime | int | 提醒时间(-1:不提醒、0:开始时间提醒、15:开始时间前15分钟提醒、60:开始时间前1小时提醒)

workStatus | int | 日程状态(0:待办、1:已办、2:删除)

readStatus | int | 是否已读(0:未读、1:已读)

acceptStatus | int | 接受状态(0:未响应、1:不接受、2:接受)

record | boolean | 是否提交纪要

参数 | 类型 | 注释

day | Long | 需查询当天任意时间点的时间戳(只能查询当日创建的日程)

参数 | 类型 | 是否必须 | 注释

openid | String | 是 | 日程发起人的oid

content | String | 是 | 日程内容

startDate | Long | 是 | 日程开始时间戳

endDate | Long | 是 | 日程结束时间戳

noticeTimes | array(number) | 否 | 提醒时间(-1:不提醒、0:开始时间提醒、15:开始时间前15分钟提醒、60:开始时间前1小时提醒)

actors | 集合 | 否 | 协作人oid的集合

submitExperience | boolean | 否 | 是否需要提交日程纪要(新的体会、总结)

repeat | int | 是 | 重复周期(0:不重复、1:每工作日、2:每日、3:每周、4:每两周、5:每月)

repeatEndDate | long | 是 | 重复截止时间（不要与日程结束时间戳混淆）

channe | string | 否 | 渠道，可根据业务需要来区分日程类型

shareIds | array(string) | 否 | 共享组id集合

images | array(FileInfo) | 否 | 图片列表

files | array(FileInfo) | 否 | 文件列表

agent | string | 否 | 代建人（代建日程时代建人oid）

参数 | 类型 | 是否必须 | 注释

id | String | 是 | 日程id

openid | String | 是 | 日程发起人的oid，如果是代建日程可以是代建人oid

content | String | 是 | 日程内容

startDate | Long | 是 | 日程开始时间戳

endDate | Long | 是 | 日程结束时间戳

noticeTimes | array(number) | 否 | 提醒时间(-1:不提醒、0:开始时间提醒、15:开始时间前15分钟提醒、60:开始时间前1小时提醒)

actors | 集合 | 否 | 协作人oid的集合

submitExperience | boolean | 否 | 是否需要提交日程纪要(新的体会、总结)

repeat | int | 是 | 重复周期(0:不重复、1:每工作日、2:每日、3:每周、4:每两周、5:每月)

repeatEndDate | long | 是 | 重复截止时间

参数 | 类型 | 注释

id | String | 日程id

openid | String | 日程发起人的oid

参数 | 类型 | 注释

pageNum | Integer | 第几页，从1开始

pageSize | Integer | 每页多少条

openId | String | 人员oid

status | Integer | 状态(0未完成, 1已完成,null 所有)

参数 | 类型 | 注释

id | String | 主键ID

channel | String | 渠道

createChannel | String | 创建渠道, 为了区分渠道里面的更细粒度

content | String | 工作内容

openId | String | 发起人OID

personName | String | 发起人名字

startDate | long | 开始时间

endDate | long | 截止时间

workStatus | int | 工作状态(0待办, 1已办, 2删除)

repeat | int | 重复类型(0不重复, 1每工作日, 2每日, 3每周, 4每两周, 5每月)

repeatEndDate | Long | 重复日程截止时间

createDate | long | 创建时间

currentActor | NewWorkActorVo | 当前用户信息

doneTime | Long | 完成时间

record | boolean | 标记是否提交了总结

参数 | 类型 | 注释

openId | String | 任务创建者的oid

id | String | 任务id

参数 | 类型 | 注释

actors | array(Actor) | 任务相关人的集合

content | String | 任务内容

createDate | long | 任务创建时间

endDate | Long | 任务结束时间戳

files | array(FileInfo) | 附件

id | String | 主键ID

images | array(FileInfo) | 图片

important | int | 是否重要(0:不重要、1:重要)

noticeTime | int | 提醒时间(-1:不提醒、0:开始时间提醒、15:开始时间前15分钟提醒、60:开始时间前1小时提醒)

openId | String | 任务创建者的oid

personName | String | 任务创建者姓名

status | int | 任务状态(0:未完成、1:完成、2:已关闭)

timingNoticeTime | int | 任务定时提醒时间(0:不提醒、1:每天、2:每工作日、3:每周、4:每两周、5:每月)

progress | int | 任务进度%

subtasks | array(SubTask) | 子任务集合

associatedTask | AssociatedTask | 关联任务

currentActor | Actor | 当前操作人信息

参数 | 类型 | 注释

openId | String | 任务创建者的oid

pageNum | int | 第几页(从1开始)

pageSize | int | 每页多少条(最多100条)

参数 | 类型 | 注释

actors | 集合 | 任务相关人的集合

content | String | 任务内容

createDate | long | 任务创建时间

endDate | Long | 任务结束时间戳

files | 文件格式 | 附件

id | String | 主键ID

images | 文件格式 | 图片

important | int | 是否重要(0:不重要、1:重要)

noticeTime | int | 提醒时间(-1:不提醒、0:开始时间提醒、15:开始时间前15分钟提醒、60:开始时间前1小时提醒)

openId | String | 任务创建者的oid

personName | String | 任务创建者姓名

status | int | 任务状态(0:未完成、1:完成、2:已关闭)

timingNoticeTime | int | 任务定时提醒时间(0:不提醒、1:每天、2:每工作日、3:每周、4:每两周、5:每月)

参数 | 类型 | 是否必须 | 注释

openId | String | 是 | 任务创建者的oid

content | String | 否 | 任务内容

startDate | Long | 是 | 任务开始时间戳

endDate | Long | 是 | 任务结束时间戳

noticeTime | int | 否 | 提醒时间(-1:不提醒、0:开始时间提醒、15:开始时间前15分钟提醒、60:开始时间前1小时提醒)

timingNoticeTime | int | 否 | 任务定时提醒时间(0:不提醒、1:每天、2:每工作日、3:每周、4:每两周、5:每月)

important | int | 否 | 是否重要(0:不重要、1:重要)

images | 文件格式 | 否 | 图片

files | 文件格式 | 否 | 附件

executors | 集合 | 否 | 执行人oid的集合

ccs | 集合 | 否 | 抄送人oid的集合

channel | String | 否 | 来源渠道

createChannel | String | 否 | 来源渠道细分，相当于子渠道

extApps | 集合 | 否 | 外部跳转应用集合

参数 | 类型 | 注释

workTaskId | String | 添加成功后任务id

参数名 | 类型 | 是否必须 | 注释

id | string | 是 | 任务ID

openId | string | 是 | 操作人oid

content | string | 是 | 任务内容

endDate | string | 是 | 任务截止时间，毫秒时间戳

noticeTime | number | 是 | 任务提醒时间， 分钟数，-1不提醒 0截止时提醒，如5代表截止前5分钟

timingNoticeTime | number | 是 | 任务定时提醒时间(0不提醒, 1每天, 2每工作日, 3每周, 4每两周, 5每月)

important | number | 是 | 是否重要(0不重要, 1重要)

associatedTaskId | string | 否 | 关联任务, 被关联任务ID

images | array(FileInfo) | 否 | 图片列表

files | array(FileInfo) | 否 | 文件列表

addExecutors | array | 否 | 新增执行人列表， oid集

delExecutors | array | 否 | 删除的执行人列表， oid集合

addCcs | array | 否 | 新增的抄送人列表， oid集合

delCcs | array | 否 | 删除的抄送人列表，oid集合

subAddWorkTasks | array(AddSubTask) | 否 | 新增的子任务集合

subModifyWorkTasks | array(EditSubTask) | 否 | 修改的子任务集合

subDelWorkTaskIds | array | 否 | 删除的子任务Id集合

参数名 | 类型 | 注释

id | string | 任务ID

openId | string | 操作人oid

参数名 | 类型 | 注释

id | string | 任务ID

openId | string | 操作人oid

参数名 | 类型 | 注释

id | string | 任务ID

参数名 | 类型 | 注释

id | string | 任务ID

参数名 | 类型 | 注释

openId | string | 操作人oid

workId | string | 任务ID

commentType | string | 固定为"workTask"

content | string | 评论内容

progress | number | 进度整数百分比（如70, 100）代表30%，100%

extJsonData | string | 上述除openId以外的字段组成的json字符串

参数 | 类型 | 注释

pageNum | Integer | 第几页，从1开始

pageSize | Integer | 每页多少条

openId | String | 人员oid

condition | Integer | 条件(0全部,1我创建, 2我执行, 3抄送我, 4已完成, 5未完成)

参数 | 类型 | 注释

id | String | 主键ID

content | String | 任务内容

openId | String | 创建人OID

personName | String | 创建人名字

endDate | long | 截止时间

createDate | long | 创建时间

parentTaskId | String | 父任务，父任务ID

status | int | 任务状态(0未完成, 1完成, 2已关闭)

progress | Integer | 任务进度

doneTime | long | 完成时间

currentActor | WorkTaskActorVo | 当前用户

executors | Set | 执行人列表

scoreSwitch | boolean | 是否启用评分

参数 | 类型 | 注释

files | array(FileInfo) | 附件

images | array(FileInfo) | 图片

participants | array | 创建者人员信息

content | string | 内容

startDate | Long | 开始时间

openId | string | 创建人openId

参数 | 类型 | 注释

workId | String | 添加成功后日程id

参数 | 类型 | 注释

id | String | 主键ID

content | String | 内容

images | array(FileInfo) | 图片

files | array(FileInfo) | 附件

参数 | 类型 | 注释

id | String | 需要删除的id

openId | String | openId

参数 | 类型 | 注释

openId | String | 相关人openId

pageNo | int | 第几页，从1开始

limit | int | 每页多少条

参数 | 类型 | 注释

id | String | id

topDate | long | 置顶时间

endDate | long | 会议结束时间

openid | String | oid

workSource | String | 工作来源 1:自己创建，2:协作创建，3:第三方应用创建(会议通知，IM消息，审批)

updateTime | long | 更新时间

content | String | 工作内容

personName | String | 创建人姓名

doneTime | long | 已办时间

startDate | long | 工作开始时间

createDate | long | 创建时间

参数名 | 类型 | 注释

openId | string | 人员oid

字段 | 类型 | 注释

openId | string | 共享人

personName | string | 共享人姓名

photoUrl | string | 共享人头像

eid | string | 共享人eid

shareOpenId | string | 被共享人

sharePersonName | string | 被共享人姓名

sharePhotoUrl | string | 被共享人头像

shareEid | string | 被共享人eid

permissions | array(number) | 权限集合：只查看[1], 允许创建日程和会议[1,2]

updateDate | number | 更新时间戳

参数名 | 类型 | 注释

openId | string | 人员oid

字段 | 类型 | 注释

openId | string | 共享人

personName | string | 共享人姓名

photoUrl | string | 共享人头像

eid | string | 共享人eid

shareOpenId | string | 被共享人

sharePersonName | string | 被共享人姓名

sharePhotoUrl | string | 被共享人头像

shareEid | string | 被共享人eid

permissions | array(number) | 权限集合：只查看[1], 允许创建日程和会议[1,2]

updateDate | number | 更新时间戳

参数名 | 类型 | 注释

openId | string | 共享人oid

permissions | array(number) | 权限集合：只查看[1], 允许创建日程和会议[1,2]

shareOpenIds | array(string) | 被共享人oid集合, 集合内所有被共享人的权限都一致，

body | 类型 | 注释

eid | string | 工作圈ID

oid | string | 人员oid

name | string | 用户姓名

photoUrl | string | 用户头像

workStatus | number | 日程状态(0:待办、1:已办、2:删除)

readStatus | number | 是否已读(0:未读、1:已读)

acceptStatus | number | 接受状态(0:未响应、1:不接受、2:接受)

topDate | number | 置顶时间，毫秒时间戳

doneTime | number | 日程完成时间，毫秒时间戳

workSource | string | 工作来源1:自己创建;2:协作创建;3:第三方应用创建(会议通知, IM消息, 审批)

personnelSource | number | 人员来源：1、内部协作人；2、外部好友；3、手机联系人

body | 类型 | 注释

nickName | string | 评论人姓名

photoUrl | string | 评论人头像

content | string | 评论内容

createDate | number | 创建时间，毫秒时间戳

files | array(FileInfo) | 文件列表

body | 类型 | 注释

openId | string | 操作人oid

content | string | 任务内容

createDate | number | 创建时间

endDate | number | 任务截止时间

doneTime | number | 任务截止时间

noticeTime | number | 任务提醒时间， 分钟数，-1不提醒 0立即提醒，如5代表提前5分钟

timingNoticeTime | number | 任务定时提醒时间(0不提醒, 1每天, 2每工作日, 3每周, 4每两周, 5每月)

progress | number | 任务进度%

important | number | 是否重要(0不重要, 1重要)

images | array(FileInfo) | 图片列表

files | array(FileInfo) | 文件列表

actors | array(Actor) | 相关人集合

status | number | 任务状态(0:未完成、1:完成、2:已关闭)

body | 类型 | 注释

id | string | 任务ID

content | string | 任务内容

openId | string | 操作人oid

body | 类型 | 注释

openId | string | 操作人的oid

personName | string | 操作人的名称

department | string | 部门名称

photoUrl | string | 头像

progress | number | 操作人的任务进度

source | number | 任务来源：1、自己创建；2、执行人；3、抄送人

status | number | 操作人的任务状态(0:未完成、1:完成、2:已关闭)

readStatus | number | 工作消息是否已读，0为未读，1为已读

doneTime | number | 完成时间

body | 类型 | 是否必须 | 注释

openId | string | 是 | 操作人oid

content | string | 是 | 任务内容

endDate | number | 是 | 任务截止时间，毫秒时间戳

noticeTime | number | 是 | 任务提醒时间， 分钟数，-1不提醒 0立即提醒，如5代表提前5分钟

timingNoticeTime | number | 是 | 任务定时提醒时间(0不提醒, 1每天, 2每工作日, 3每周, 4每两周, 5每月)

important | number | 是 | 是否重要(0不重要, 1重要)

parentTaskId | string | 否 | 父任务, 父任务ID

images | array(FileInfo) | 否 | 图片列表

files | array(FileInfo) | 否 | 文件列表

addExecutors | array | 否 | 新增执行人列表， oid集

delExecutors | array | 否 | 删除的执行人列表， oid集合

addCcs | array | 否 | 新增的抄送人列表， oid集合

delCcs | array | 否 | 删除的抄送人列表，oid集合

body | 类型 | 是否必须 | 注释

id | string | 是 | 子任务ID

body | 类型 | 注释

fileId | string | 文件id

fileName | string | 文件名称

fileSize | number | 文件大小

FileExt | string | 文件扩展名 如：png

fileType | string | 文件类型 如：image/png

method | 描述

1001 | 创建日程

1002 | 修改日程

1003 | 删除日程

1006 | 完成日程

1007 | 重新发起日程

method | 描述

2001 | 创建任务

2002 | 修改任务

2003 | 删除任务

2004 | 完成任务

2005 | 关闭任务

2009 | 激活任务

method | 描述

3001 | 创建会议

3002 | 修改会议

3003 | 删除会议

3006 | 结束会议

3007 | 取消会议

3008 | 参加会议

3009 | 不参加会议

3010 | 委托会议

参数 | 类型 | 是否必须 | 注释

limit | Integer | 否 | 每页多少条，默认100

cursorId | String | 否 | 游标id，从游标开始拉取，默认不传则从头开始拉数据

---