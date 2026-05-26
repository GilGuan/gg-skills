---
domain: product
module: 其他
keywords: [流程, 配置, 集成]
---

## 其他/Microsoft Entra

Microsoft Entra

产品介绍

在云之家网页端登陆页使用 Microsoft Entra 单点登录。

【适用客户类型：云之家混合云、公有云（旗舰版）】

配置流程

一、注册应用程序

登陆 Microsoft Entra ID 后台管理控制台：https://entra.microsoft.com

左侧菜单选择：应用程序 > 应用注册，按需填写名称和受支持的账户类型，重定向 URI 选择 Web，https://${domin}/space/c/opencloudhub/microsoft/auth/loginyzj

如果是公有云，则填写 https://www.yunzhijia.com/space/c/opencloudhub/microsoft/auth/loginyzj

二、获取参数

注册应用成功后，在应用注册页面找到刚才注册的应用，点击进入。

找到应用程序（客户端）ID、目录（租户）ID、客户端凭据、重定向URI

获取客户端凭据：

这里的值即是客户端凭据

三、配置参数

进入云之家网页端 > 管理中心 > 第三方集成平台 > Microsoft Entra

按需选择用户身份匹配方式，再将第二步获取的参数填入相应字段，点击保存。

四、重新构建

联系专属客户成功经理或客服4008308110，重新构建网页端。

重新构建后即可在云之家网页端看到 Microsoft 的入口。

---