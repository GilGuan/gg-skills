---
domain: product
module: 融合通讯
keywords: [IM, appId, callback, secret, token]
---

## 融合通讯(IM)/企业微信

企业微信

产品介绍

💡 支持在企业微信客户端使用云之家的平台轻应用，目前适配情况如下：

前提准备

1.账号准备

​

2.域名准备

【云之家私有云客户无需这一步，直接用客户私有云域名即可】

1、备案域名、备案域名的SSL证书需客户自行准备

配置流程

一、企微侧配置

1）查看企业信息（corpId，secret）

1.找到企微的企业ID，即corpId。

【复制出来，等会要填写到云之家-通讯录参数】

获取路径：企业微信管理后台 > 我的企业 > 企业ID

2.找到企微的secret (通讯录同步)

获取路径：企业微信管理后台 > 安全与管理 > 管理工具 > 通讯录管理 > 通讯录同步

开启接口同步，权限 > 编辑 > 开启手动编辑

获取企微secret，Secret > 查看

【复制出来，等会要填写到云之家-通讯录参数】

2）企业可信IP (通讯录同步)

企业可信IP，IP列表请联系客户经理。（2.域名准备-->审批流程完成后，会把IP备注到流程中的）

【云之家私有云客户，这个可信IP就是客户环境云之家的出口IP】

3）接收事件服务器 (通讯录同步)

URL：替换下客户域名、corpId这两个参数

https://{客户域名}/space/c/opencloudhub/wecom/UserOrgCallback/{客户corpId}

4）企微-创建自建应用

1.应用首页

a.智能审批-示例

移动端，pc端一样：

https://{客户备案域名}/infra/login/wecom.html?agentid={企微自建应用ID}&corpid={企微企业ID}&appId=10104&urlParam=https://{客户备案域名}/cloudflow-mobile/united-flow-center/approve

b.知识中心-示例

移动端：

https://{客户备案域名}/infra/login/wecom.html?agentid={企微自建应用ID}&corpid={企微企业ID}&appId=10879&urlParam=https://{客户备案域名}/yzj-portal

pc端：

https://{客户备案域名}/infra/login/wecom.html?agentid={企微自建应用ID}&corpid={企微企业ID}&appId=10879&urlParam=https://{客户备案域名}/yzj-info

c.智能门户-示例

备注：【智能门户】暂只支持智能审批、知识中心、时间助手的卡片与企微集成。

移动端:

https://{客户备案域名}/infra/login/wecom.html?agentid={企微自建应用ID}&corpid={企微企业ID}&appId=101091520&urlParam=https://{客户备案域名}/portal/mobile.html

pc端:

https://{客户备案域名}/infra/login/wecom.html?agentid={企微自建应用ID}&corpid={企微企业ID}&appId=101091520&urlParam=https://{客户备案域名}/portal/pc.html

d.时间助手-示例

移动端，pc端一样：

https://{客户备案域名}/infra/login/wecom.html?agentid={企微自建应用ID}&corpid={企微企业ID}&appId=10619&urlParam=https://{客户备案域你要名}/workassistant/work

e.文事会-示例

移动端，pc端一样：

https://{客户备案域名}/infra/login/wecom.html?agentid={企微自建应用ID}&corpid={企微企业ID}&appId=101091023&urlParam=https://{客户备案域名}/official​

f.公文管理-示例

pc端一样

https://{客户备案域名}/infra/login/wecom.html?agentid={企微自建应用ID}&corpid={企微企业ID}&appId=101091020&urlParam=https://{客户备案域名}/official/doc/home/manage/official-main?__wsh_menuID=101091020%7CGW_GWSY

移动端

https://{客户备案域名}/infra/login/wecom.html?agentid={企微自建应用ID}&corpid={企微企业ID}&appId=101091020&urlParam=https://{客户备案域名}/official/doc/mobile/official-home​

g.会议管理-示例

移动端，pc端一样：

https://{客户备案域名}/infra/login/wecom.html?agentid={企微自建应用ID}&corpid={企微企业ID}&appId=101091022&urlParam=https://{客户备案域名}/official/meeting

2.网页授权及JS-SDK

这里都填客户备案域名即可

3.企业微信授权登录

iOS：“设置Bundle ID”，获取schema，填入Bundle ID（com.kdweibo.client）

Android：填入应用签名（EE4464E857ADE497F9687FA7ED806951）、应用包名（com.kdweibo.client）

【云之家私有云客户：应用签名：应用包名是私有云客户端包名】

4.企业可信IP（自建应用）

企业可信IP，IP列表请联系客户经理。（2.域名准备-->审批流程完成后，会把IP备注到流程中的）

【云之家私有云客户，这个可信IP就是客户环境云之家的出口IP】

5. 接收消息 > 启用/设置API接收（自建应用）-这步可以稍后再做，需要先在云之家侧管理中心配置完后再来配置

获取路径：企业微信管理后台 > 应用管理  > 应用 > 自建 > 应用详情 > 接收消息 > 启用/设置API接收

注意：这里是应用详情的。和前面通讯录那里的回调是不同的

URL：https://${客户备案域名}/gateway/newtodo/wework/callback?corpId=${企微corpID}&agentId=${应用agentID}

例如：https://www.yunzhijia.com/gateway/newtodo/wework/callback?corpId=wwa816f09936xxxxxb&agentId=10000xx

二、云之家侧配置

云之家系统管理员进入 [管理中心 > 第三方集成平台 > 企业微信]

1）初始化 - 前提：把通讯录参数填完整 (可选操作)

该初始化，仅把 企微的组织架构 同步到 云之家组织架构来，里面的员工是不同步的

疑问1：组织架构同步，会把原来云之家的组织架构删除吗？

答：不会全部删除，会做比对更新，对比条件：[组织层级+部门名称]，如果都一样，则不更新。如果不一样，则新增组织部门；云之家侧多出来的组织结构 不会删除

疑问2：这个初始化同步，是一定要做的吗？

答：可选操作。如果客户在云之家侧还没有维护组织架构信息，想以企微的组织架构为准，那么可以用此操作把企微的组织架构一键同步到云之家；如果客户在云之家侧已经有组织架构了，那么就可以不初始化来同步组织架构。

疑问3：不同步用户，那云之家侧的用户从哪里来？

答：1.可以手动导入；2.如果开启了自动新增用户，那么在企微单点登录到云之家侧时，会自动把该用户导入到云之家的组织架构中。

2）基础参数配置

a.企业微信部署方式

公有云：域名填写客户自己的备案域名（协议用http）-（必填）

私有云：域名填写客户私有化部署的企微的域名-（必填）

​

b.用户身份匹配方式(必填)

企业微信用户和云之家用户之间的对应的字段，支持手机号、邮箱、工号三种方式。（当用户信息相同时按勾选顺序匹配下一个方式）

若选择工号，则还需输入企业微信对应的工号字

3）通讯录参数

a.企微corpId（From:企微-我的企业）（必填）

获取路径：企业微信管理后台 > 我的企业 > 企业ID

详情参考 1.找到企微的企业ID（corpId）

​

b.企微secret（From：企微-通讯录同步）（可选-不需要和企微通讯录实时同步更新的话可以不填）

获取路径：企业微信管理后台 > 安全与管理 > 管理工具 > 通讯录管理 > 通讯录同步  ---> Secret > 查看

详情参考 2.找到企微的secret (通讯录同步)

​

c.回调token & 回调aes秘钥（From：企微-通讯录同步）（可选-不需要和企微通讯录实时同步更新的话可以不填）

获取路径：企业微信管理后台 > 安全与管理 > 管理工具 > 通讯录管理 > 通讯录同步 > 设置接收事件服务器

注意：这里是通讯录同步的

回调Token：企微侧通讯录同步的token

回调aes秘钥：企微侧的通讯录同步的EncodingAESKey

详情参考 3）接收事件服务器（通讯录同步）

​

d.可信域名（必填）

填客户已备案的域名（一定要https开头的）

4）应用参数配置（必填）

a.企微corpId（From:企微-我的企业）（必填）

与基础参数配置中的企微corpId一致

获取路径：企业微信管理后台 > 我的企业 > 企业ID

详情参考 1）查看企业信息（corpId，secret）

​

b.企微应用id & 企微应用的secret （From:企微-应用详情）（必填-获取个人信息时需要用到）

获取路径：企业微信管理后台 > 应用管理 > 应用 > 自建 > 应用详情

企微应用id：AgentId

企微应用secret：Secret

c.回调token & 回调aes密钥（应用参数的）（From:企微-应用详情）（推荐填写-在企微快捷审批时会调用到云之家时要用到）

获取路径：企业微信管理后台 > 应用管理  > 应用 > 自建 > 应用详情 > 接收消息 > 启用/设置API接收

注意：这里是应用详情的

URL：https://${客户备案域名}/gateway/newtodo/wework/callback?corpId=${企微corpID}&agentId=${应用agentID}

例如：https://www.yunzhijia.com/gateway/newtodo/wework/callback?corpId=wwa816f09936xxxxxb&agentId=10000xx

回调token：企微侧应用管理-API接收的Token​

回调aes秘钥：企微侧应用管理-API接收的EncodingAESKey

d. schema （From:企微-应用详情）

获取路径：企业微信管理后台 > 应用管理  > 应用 > 自建 > 应用详情 > 开发这接口 > 企业微信授权登录

e. appId（云之家的应用id）

f. 子应用appid（云之家的应用id）

适用于，第三方业务也把待办、待审批 流程推送到我们平台，同时也想在企微接收到通知，那么，就把该第三方业务的应用appId配置到这里来。然后第三方业务推送待办时，在企微侧也就能收到通知了

5）配置开关-控制推送企微通知（仅私有云需要此操作）

key：DISTRIBUTION_CENTER_SWITCH

​

三、FAQ-常见问题处理

1.单点登录时，提示：invalid credential

解：

2.单点登录时，提示：not allow to access from your ip.

解：这种一般就是没有做域名解析（域名需要解析到单独一台服务器上），即该文档 第一项：前提准备-->2.域名准备

3.企微侧配置时，提示回调地址请求不通过

解：这种一般是域名解析后，没有把域名证书发给我们。即该文档 第一项：前提准备-->2.域名准备

4.单点登录时，提示：handshake failure

解：这种一般时，云之家侧配置的通讯录基础参数：企微的域名地址用了https导致的，改成 http 即可

5.重新授权，授权清理

1.应用消息 ->	右上角 打开详情

2.工作台 -> 应用 -> 右上角 小点 -> 应用信息

---