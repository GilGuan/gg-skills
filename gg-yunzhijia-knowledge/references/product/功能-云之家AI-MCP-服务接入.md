---
domain: product
module: 云之家AI
keywords: [配置]
---

## 云之家AI/MCP 服务接入

MCP 服务接入

💡 在小K中通过 AgentHub 配置接入第三方开放的或企业自定义 MCP 服务。

了解什么是 MCP

MCP 是一套模型与外部系统交互的标准协议，也是目前业界普遍遵循的一套开发和对接模型工具的协议。MCP 接口就好像是大模型领域的 USB 接口协议，通过标准化协议，企业可以快速接入自己的系统到智能助手中。

​

MCP 架构中有几个核心概念：Host、Client、Server，具体的概念解释可以查看官方文档。在云之家内，小K即为 MCP Host，您需要封装好自己的 MCP Server，通过在 AgentHub 中创建与您的 MCP Server 1:1 的 Client，从而完成两个系统之间的对接。

💡一些Tips：

如何实现一个 MCP 服务，可参考以下文档：

您也可以参考已有的社区高质量 MCP Servers 的实现：

哪里可以找到更多 MCP 服务：

在小K中接入自定义 MCP 服务

使用示例（以接入高德 MCP 为例）

参考高德地图的 MCP server 文档，完成认证拿到 API Key 和对应的 MCP Server 地址：

在 AgentHub 中新增自定义 MCP 服务

将 MCP server 的JSON 复制粘贴到配置输入框。

⚠️ 注意：

💡 可增加相关的描述，并支持设置使用范围（无此 MCP 服务权限的用户，小K将不会调用该工具）

保存后，可在界面上进行查看此 MCP 服务包含的工具、编辑 MCP 服务配置、启用/禁用/删除 MCP 服务。

在小K调用 MCP 服务

以如上高德地图 MCP server 接入为例：

高德地图提供了 LBS 相关的开放工具能力，通过 AgentHub 注册进来后，小K会根据用户输入的指令由 LLM 进行意图识别并路由调用适合的工具执行，最终整合所有信息后回答用户的问题。

MCP 服务注意事项

调用 MCP 服务的出口 IP 地址

💡小K将会从下列 IP 地址（互联网出口地址）发起对自定义 MCP 服务的访问。若需进行访问 IP 控制，需为以下 IP 地址单独开通白名单：

MCP 传输类型支持说明

💡 AgentHub 仅支持传输类型为远程API的接入（SSE和Streamable HTTP），不支持 Stdio（NPX和UVX）的接入

---