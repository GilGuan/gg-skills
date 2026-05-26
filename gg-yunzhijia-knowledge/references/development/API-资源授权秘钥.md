---
domain: development
module: 密钥管理
keywords: [IM, accessToken, secret, token, 同步]
---

## 资源授权秘钥

根据管理员账号信息获取资源授权密钥

根据管理员账号信息获取资源授权密钥

<span style="background-color: rgb(255,255,0)">声明： 此接口仅限后端调用。若前端调用，极易导致管理员账号密码泄露，造成的严重后果云之家概不负责。</span>

描述： 在调用获取accessToken接口，且授权级别为resGroupSecret时,其中输入参数secret可以通过此接口取到对应接口资源的密钥。资源密钥也可以手动去云之家管理中心去获取，参考本页FAQ如何获取资源授权秘钥。

注：若某团队管理员在“云之家首页--云之家web端管理中心--系统设置--系统集成”中的资源密钥从来没有勾选生成过，则此接口会自动生成密钥并返回。如果管理员把资源密钥勾选生成后又取消了勾选，则接口不会自动生成密钥且不返回。

网络传输协议：HTTPS

请求地址：https://www.yunzhijia.com/opencloud/rest/getSecretByUser

请求方法：POST

内容类型：Content-Type: application/x-www-form-urlencoded

输入参数:

输出结果:

{
    "success": true,
    "error": null,
    "errorCode": 100,
    "data": [
        {
            "alias": "[cloudwork_newwork]",
            "name": "时间助手管理",
            "secret": "SRwkcrk9mS9xj30jHHIW9f4aShGTMp"
        },
        {
            "alias": "[groupsecret_resource_attendance]",
            "name": "签到数据",
            "secret": "iF9ev2OJc5diksR2POE3hTl3S4ChHV"
        },
        {
            "alias": "[groupsecret_resource_openimport_rw]",
            "name": "组织人员通讯录同步",
            "secret": "z796uMVtsSt4z8FIZP6oATQO9GpQyo"
        },
        {
            "alias": "[document]",
            "name": "文件服务上传下载",
            "secret": "ogZ0TnALxoafkCVCU7nK0XMf0g0grX"
        },
        {
            "alias": "[groupsecret_resource_open_linkspace]",
            "name": "生态圈同步",
            "secret": "uCuEJ90RvBZNcQIwVMo7XNfkICG05D"
        },
        {
            "alias": "[groupsecret_resource_openimport_r]",
            "name": "组织人员通讯录读取",
            "secret": "DXXeUzMNDJlt9HXT4PGst5sqPc0RMp"
        }
    ]
}

错误码对照表：

FAQ

<h1> 如何获取资源授权秘钥？</h1>

用管理员账号进入"云之家首页--云之家web端管理中心--系统设置--系统集成"，

通讯录同步密钥:

参见"通讯录同步"，根据需要（“只读密钥”、“可编辑密钥”）点击“生成秘钥”获取对应资源类型的资源秘钥，点击“复制”可复制密钥到剪切板；点击“重新生成秘钥”可以重新生成秘钥

注：点击“通讯录同步”中的“重要说明--点我下载”可获得组织人员同步旧接口的鉴权“eid.key”文件。

签到密钥:

参见"资源授权--签到数据"，点击"复制"复制密钥；

时间助手:

参见"资源授权--时间助手管理"，点击"复制"复制密钥；

生态圈:

开通生态圈的白名单之后，参见"资源授权--生态圈同步"，点击"复制"复制密钥；

图示如下：

--- 文档抓取完成 ---

类型 | 是否必填

String | 是

String | 是

String | 是

error

用户名密码不能为空 或者是  获取是否是管理员接口返回的异常

用户名密码错误

工作圈不存在

不是管理员

系统异常

---