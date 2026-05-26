---
domain: product
module: 融合通讯
keywords: [IM, appId, callback, secret, token]
---

## 融合通讯(IM)/飞书

飞书

产品介绍

实现⻜书集成云之家 OA 产品能⼒，云之家的 OA 产品可以直接在⻜书客户端上使⽤，目前适配情况如下：

支持【智能审批】、【智能门户】、【知识中心】、【时间助手】集成到飞书（涉及通知类的业务功能暂不支持）

前提条件❗️

配置指南💡

账号准备

云之家管理员账号、⻜书管理员账号（可以创建和配置应⽤的权限）

一、⻜书配置

创建企业⾃建应⽤

进⼊⻜书开发者后台

1.添加应⽤能⼒

>网页应用

配置应⽤ URL

配置云之家 OA 模块的 URL 地址： https://www.yunzhijia.com/infra/login/feishu.html?app_id=cli_a6cb6f1xxxx&eid=187123&appId=101091520&urlParam=https://www.yunzhijia.com/portal/pc.html

URL 说明

跳转登录 URL：https://www.yunzhijia.com/infra/login/feishu.html

当前⻜书应⽤的 app_id: app_id=cli_a6cb6f1xxxx

云之家⼯作圈 EID: eid=187123

云之家应⽤ APPID:  appId=101091520

云之家应⽤地址：urlParam=https://www.yunzhijia.com/portal/pc.html

a.智能⻔户示例

⼿机端：https://{客户域名}/infra/login/feishu.html?app_id={飞书应用id}&eid={云之家圈eid}&appId=101091520&urlParam=https://{客户域名}/portal/mobile.html

电脑端：https://{客户域名}/infra/login/feishu.html?app_id={飞书应用id}&eid={云之家圈eid}&appId=101091520&urlParam=https://{客户域名}/portal/pc.html

b.智能审批示例

移动端：https://{客户域名}/infra/login/feishu.html?app_id={飞书应用id}&eid={云之家圈eid}&appId=10104&urlParam=https://{客户域名}/cloudflow-mobile/united-flow-center/approve

桌面端：https://{客户域名}/infra/login/feishu.html?app_id={飞书应用id}&eid={云之家圈eid}&appId=10104&urlParam=https://{客户域名}/cloudflow-mobile/united-flow-center/approve

c.知识中心示例

移动端：https://{客户域名}/infra/login/wecom.html?app_id={飞书应用id}&eid={云之家圈eid}&appId=10879&urlParam=https://{客户域名}/yzj-portal

桌面端：https://{客户域名}/infra/login/wecom.html?app_id={飞书应用id}&eid={云之家圈eid}&appId=10879&urlParam=https://{客户域名}/yzj-info

d.时间助手示例

移动端：https://{客户域名}/infra/login/wecom.html?app_id={飞书应用id}&eid={云之家圈eid}&appId=10619&urlParam=https://{客户域名}/workassistant/work

桌面端：https://{客户域名}/infra/login/wecom.html?app_id={飞书应用id}&eid={云之家圈eid}&appId=10619&urlParam=https://{客户域名}/workassistant/work

e.文事会-示例

移动端，pc端一样：https://{客户域名}/infra/login/wecom.html?app_id={飞书应用id}&eid={云之家圈eid}&appId=101091023&urlParam=https://{客户域名}/official

f.公文管理-示例

移动端，pc端一样：https://{客户域名}/infra/login/wecom.html?app_id={飞书应用id}&eid={云之家圈eid}&appId=101091020&urlParam=https://{客户域名}/official/doc

g.会议管理-示例

移动端，pc端一样：https://{客户域名}/infra/login/wecom.html?app_id={飞书应用id}&eid={云之家圈eid}&appId=101091021&urlParam=https://{客户域名}/official/meeting

>机器人

添加机器人能力即可，其他信息无需配置，在"事件与回调"里面进行配置

2.权限管理

1> 通讯录

2> 身份验证

3> 消息群组

4> 审批

注意：批量开通（批量开通只是单页，有分页的 每页都要多点批量开通）

​

说明：为什么需要设置权限，因为⻜书对于每个功能都有权限控制，如果不设置⽆法获取⽤户⼿机号码导致⽤户⽆法登录，⽬前云之家的单点登录是通过⼿机号码来匹配的，后续再完善其他匹配⽅式

3.事件与回调

3.1.事件配置

a.回调方式

选择：将事件发送至 开发者服务器

b.回调请求地址

https://www.yunzhijia.com/gateway/openimport/thirdCallback/feishu/addressBookMsg?eid=23813855

eid=云之家圈子EID

c.添加事件

'通讯录' 类型的事件都勾上，表示监听人员的变动情况，同步更新云之家侧的用户信息，以维持两边数据一直

3.2.回调配置

a.订阅方式

选择：将回调发送至 开发者服务器

b.回调请求地址

https://www.yunzhijia.com/gateway/newtodo/feishu/cardMsgCallback?eid=2381321

eid=云之家圈子EID

c.添加回调

3.3.加密策略

4.安全设置

设置了安全相关的的参数之后才能正常的使⽤⻜书的应⽤

a.重定向 URL

即上⾯应⽤ URL 配置的登录跳转地址: https://www.yunzhijia.com/infra/login/feishu.html

b.IP ⽩名单

需要配置云之家服务器⼊⼝出⼝ IP 地址。以及办公⽹出⼝ IP 地址

49.232.55.238

49.232.161.33

120.92.12.124

c.H5 可信域名

云之家的域名地址: https://www.yunzhijia.com

5.版本管理与发布

需要发布应⽤才能在⽤户侧正常使⽤

注意应⽤可⻅范围配置

二、云之家配置

云之家系统管理员进入[管理中心 > 第三方集成平台 > 飞书]

1.基础参数配置

1.1.同步企业组织架构（25-2-18更新：非必选操作）

开启后将会把飞书中维护的企业组织架构和人员同步至云之家

25-2-18更新：非必选操作。

如果不想同步组织架构，这里可以不做同步。但是人员信息必须得在云之家侧存在（可以通过导入，手工录入都可以），如果人员在云之家侧不存在 单点登录是会失败的。

飞书部署方式

根据飞书的部署方式选择公有云或系有云，私有云需输入域名

用户身份匹配方式

飞书和云之家的用户映射，可以选择手机号、邮箱、或工号(云之家)

1.2.通讯录参数

飞书企业编号：

获取路径：飞书管理后台 > 企业设置 > 企业信息 > 企业编号

获取前面步骤中创建的飞书企业自建应用的相应信息：

飞书应用App ID：

飞书开发者后台 > 应用 > 凭证与基础信息 > App ID

飞书应用App Secret：

飞书开发者后台 > 应用 > 凭证与基础信息 > App Secret

Encrypt Key：

飞书开发者后台 > 应用 > 事件与回调 > 加密策略 > Encrypt Key

Verification Token：

飞书开发者后台 > 应用 > 事件与回调 > 加密策略 > Verification Token

飞书可信域名：

飞书开发者后台 > 应用 > 安全设置 > H5 可信域名

2.应用级参数

前面步骤中创建的飞书企业自建应用的相应信息：

飞书应用App ID：

飞书开发者后台 > 应用 > 凭证与基础信息 > 应用凭证

飞书应用App Secret：

飞书开发者后台 > 应用 > 凭证与基础信息 > 应用凭证

推送方式：

云之家子应用：

选择集成到飞书的云之家应用

三、FAQ

Q：为什么我开启了 同步组织架构，但是飞书的用户没有同步过来？

检查飞书中的权限，一般都是权限没开启导致云之家同步用户时拉取不到数据。

​

Q：组织架构同步，会把原来云之家的组织架构删除吗？

1、组织结构：不会全部删除，会做比对更新，对比条件：[组织层级+部门名称]，如果都一样，则不更新。如果不一样，则新增组织部门；云之家侧多出来的组织结构 不会删除；

2、用户：不会全部删除，会做对比更新，对比条件：[依据配置的'用户身份匹配方式'来查询用户]，若查询到，则对比更新，如果查不到，则新增用户；云之家侧多出来的用户不会删除。

​

---