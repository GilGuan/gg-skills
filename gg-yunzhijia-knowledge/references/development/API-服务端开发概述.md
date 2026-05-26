---
domain: development
module: 开发入门
keywords: [accessToken, appId, secret, token, 审批]
---

## 服务端开发概述

服务端开发概述

服务端开发概述

云之家开放平台的服务端开发围绕以下几个主要场景：

轻应用、门户卡片后端解析用户身份，即：解析ticket

调用平台级应用的开放接口，例如：时间助手、签到、审批等

调用融合通讯的开放接口，例如：消息、待办、公众号、群组机器人等

> 以上这些接口，都需要传入一个AccessToken作为参数。

AccessToken

AccessToken是调用平台接口的授权码，它是动态生成的，分成三个级别：app、team、resGroupSecret。

点击此处了解获取AccessToken的详细方法。

请注意：JS生成ticket的方法中用到的签名接口会用到一个access_token参数，与此处讨论的AccessToken容易混淆，一定要注意区分。

解析用户身份（单点登录）

来自客户端的请求一般都会带上ticket参数，该参数由客户端根据用户身份和当前轻应用的appId生成，只有该轻应用的所有者或者平台网关才能解析。

解析用户身份，请使用scope为app的AccessToken。

点击此处了解获取解析用户身份的详细方法。

调用平台业务开放接口

不同业务的开放接口需要的授权级别不同，请参考点击此处

资源授权密钥resGroupSecret

获取res级别的AccessToken时，所需的resGroupSecret参数需要从接口获取。

点击此处了解获取resGroupSecret的详细方法。

API调用频率限制

获取到AccessToken时，您的轻应用后台就可以成功调用开放平台所提供的各种接口或访问相应企业的资源或给成员发消息。

为了防止轻应用的程序错误频繁调用导致服务器负载异常，默认情况下，每个服务端调用接口都有一定的频率限制。

以下是当前默认的频率限制：

针对app级授权资源单个接口的频率不可超过3500次/分

针对team级授权资源单个接口的频率不可超过2000次/分

针对resGroupSecret级授权资源单个接口的频率不可超过1500次/分

针对每个IP下访问频率不可超过200000次/小时

--- 文档抓取完成 ---

开放接口数量

11 | <a href="docs.html#/server-api/business/cloudflow" target="_blank">查看</a>

6 | <a href="docs.html#/server-api/business/attendance.md" target="_blank">查看</a>

13 | <a href="docs.html#/server-api/business/cloudwork.md" target="_blank">查看</a>

13 | <a href="docs.html#/server-api/business/meeting.md" target="_blank">查看</a>

12 | <a href="docs.html#/server-api/business/linkspace.md" target="_blank">查看</a>

6 | <a href="docs.html#/server-api/business/linkerp.md" target="_blank">查看</a>

---