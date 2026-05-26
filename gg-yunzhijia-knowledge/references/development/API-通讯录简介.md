---
domain: development
module: 组织人员
keywords: [IM, accessToken, person, role, secret]
---

## 通讯录简介

组织服务概述

组织服务概述

组织服务的开放能力包括两方面：

同步组织数据

获取组织数据

Postman调用示例（必读）

举例接口：新增组织：

同步组织数据

> 主要用于处理企业内部组织架构与云之家组织架构的同步

同步组织数据接口

接口授权

本部分接口使用 resGroupSecret 级别的 AccessToken， 与获取组织数据的接口不同，请注意区分。

请在 管理中心-系统设置-系统集成-通讯录同步 中，复制 只读秘钥 或者 可编辑秘钥， 然后调用系统接口换取 AccessToken。

> 只读秘钥：只能调用查询类的接口

> 可编辑秘钥：可以调用全部接口

如果您还不了解如何获取AccessToken，请点击此处

组织同步接口

新增组织

更新组织名称

删除组织

根据orgId或department查询组织信息

查询全部组织信息

查询更新部门信息

跨层次部门挪动

根据orgId更新组织名称

根据orgId删除组织

设置隐藏部门或部门仅可见

查询设置隐藏部门或者部门仅可见部门

更新组织排序码

人员同步接口

新增人员

新增人员new

更新人员信息

更新人员组织

更新人员状态

删除人员

查询全部人员信息

查询已更新人员信息

查询指定人员信息

设置或取消管理员

根据登陆账号和密码获取其是管理员的工作圈列表

修改手机号

获取手机号变更历史记录

根据组织id批量更新人员组织

添加机密组织可见成员

删除机密组织可见成员

角色同步接口

添加角色标签

获取工作圈角色标签列表

删除角色标签

更改角色标签名字

设置人员角色标签

删除人员角色标签

根据角色获取人员（不建议使用此接口）

根据用户id批量设置人员角色

根据角色id批量设置人员角色

根据角色Id分页获取人员

部门负责人同步接口

批量设置部门负责人

根据组织id批量设置部门负责人

查询所有部门负责人

批量删除部门负责人

根据组织id批量删除部门负责人

删除组织负责人

兼职同步接口

根据部门id批量设置兼职

根据部门长名称批量设置兼职

根据部门id批量删除兼职

删除所有兼职

批量查询兼职

上下级关系同步接口

批量指定上级

批量删除上级

删除所有上级

批量查询上级

域认证

新增/更新域认证账号

删除域认证账号

查询域认证账号

事件回调

第三方系统可以通过事件回调实时获取云之家的数据变更（但不建议本身是数据源的系统监听数据变更）。

推送数据

人员、部门、职位、角色的变更。

接入方法

登录云之家web端，进入“管理中心-系统集成-通讯录同步”配置接收事件通知的服务器地址，选择监听事件，云之家验证通过后，会在下次有信息变更时进行推送。

接入方法

回调url应符合以下要求：

1. 是正确URL格式，可以包含?和参数
2. 支持GET请求，并输出 ok（两个字符）
3. 响应时间不超过2秒

事件变更后，服务端推送内容如下：

DEMO

接收通讯录回调事件应用服务开发示例

旧版同步组织人员接口

点击此处查看

获取组织数据

> 主要用于向轻应用中提供组织数据

获取组织数据接口

1. 企业所有组织人员

2. 个人信息

3. 获取当前部门基本信息或部门负责人

4. 获取当前部门的所有上级部门列表

5. 获取当前部门所有下级部门列表

6. 获取所有部门列表

7. 获取企业基本信息

8. 获取当前部门成员或部门负责人信息

9. 获取当前部门下一层级的所有部门基本信息列表

10. 获取用户的默认上级或默认汇报上级或指定上级

11. 通过工作圈eid获取管理员oid

12. 根据企业eid查询全部合作伙伴信息

13. 根据手机号码和工作圈名称查询工作圈信息

14. 添加合作伙伴

15. 删除合作伙伴联系人

16. 按角色id获取人员信息

17. 查询部门信息

18. 根据orgIds获取人员信息

接口授权

本部分接口使用 app 级别的 AccessToken，与同步组织数据接口不同，请注意区分。

如果您还不了解如何获取AccessToken，请点击此处

FAQ

*"获取人员组织数据"与下面的获取部门、人员的接口有何不同？*

开放文档中“获取人员组织数据”菜单下均为轻应用鉴权接口（即使用 app 级别的 AccessToken），只有只读权限，如果做通讯录同步，建议使用通讯录鉴权接口（即使用 resGroupSecret 级别的 AccessToken）。

* 为什么接口返回鉴权失败？*

1、accessToken的有效时间为6400秒，在该有效期内多次获取均返回同一token，建议开发者将其缓存使用;

2、授权级别不同，获取accessToken接口的输入参数也是不同的，请开发者参照API与授权级别对照表填写输入参数;

* 为什么接口返回参数错误或者参数为空？*

通讯录相关同步接口目前仅支持表单格式，即content-type: application/x-www-form-urlencoded，若为其他格式，接口将获取不到传入的参数。

--- 文档抓取完成 ---

事件类型 | 推送内容 | 备注

url检验 | createTime=xxx&eid=xxx&eventId=null&eventType=check | 第一次保存时，服务端会推送此内容

新增人员事件 | createTime=xxx&eid=xxx&eventId=openId&eventType=user_enter

修改人员事件 | createTime=xxx&eid=xxx&eventId=openId&eventType=person_update | 支持部门和职位修改的监听

删除人员事件 | createTime=xxx&eid=xxx&eventId=openId&eventType=user_leave

人员手机号修改事件 | createTime=xxx&eid=xxx&eventId=openId&eventType=user_phone_update | 用户的默认工作圈为当前圈

新增部门事件 | createTime=xxx&eid=xxx&eventId=orgId&eventType=org_add

修改部门事件 | createTime=xxx&eid=xxx&eventId=orgId&eventType=org_update | 包括修改部门名称和移动部门

删除部门事件 | createTime=xxx&eid=xxx&eventId=orgId&eventType=org_delete

部门负责人变更事件 | createTime=xxx&eid=xx&eventId=orgId&eventType=org_admin | 包括设置和取消

人员角色变更事件 | createTime=xxx&eid=xxx&eventId=openId&eventType=person_role

---