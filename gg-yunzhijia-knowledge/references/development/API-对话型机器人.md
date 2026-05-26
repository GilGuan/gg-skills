---
domain: development
module: 机器人
keywords: [IM, secret, 推送, 流程, 消息]
---

## 对话型机器人

对话机器人

在调用对话机器人之前，请您先阅读以下文档：

对话机器人是什么

对话流程明细

当用户@机器人时，云之家会根据开发者的 HTTPS 服务地址，把消息内容发送出去

大致流程如下：

云之家发起post请求时，报文协议如下

HTTP HEADER

{
  "Content-Type": "application/json; charset=utf-8",
  "sign":"xxxxxxxxxx",
  "sessionId":"XXXXXX"
}

HTTP BODY

{
    "type":2,
    "robotId":"xxxx",
    "robotName":"提醒机器人",
    "operatorOpenid":"xxxx",
    "operatorName":"小明同学",
    "time":1599727083000,
    "msgId":"xxx",
    "content":"多喝热水,身体健康"
}

请求header参数说明：

sign

sign 为每次请求的签名信息，开发者需进行验证，以判定是否是来自云之家的合法请求，避免其他仿冒者。

开发者需自行计算签名值，若请求头中的 sign 与开发者自行计算的不一致，则认为是非法的请求。

sign 计算方法：

将参数中的摘要信息 和 机器人的 appSecret 当做签名字符串，使用HmacSHA1算法计算签名，然后进行Base64 encode，得到最终的签名值

具体计算代码示例( Java )：

package util;
 
import org.apache.commons.codec.binary.Base64;
import org.apache.commons.lang3.StringUtils;
 
import javax.crypto.Mac;
import javax.crypto.spec.SecretKeySpec;
import java.security.InvalidKeyException;
import java.security.NoSuchAlgorithmException;
import java.util.Date;
 
public class Test {
 
    private static final String HMAC_SHA1_ALGORITHM = "HmacSHA1";
 
    public static void main(String[] args) throws NoSuchAlgorithmException, InvalidKeyException {
        String secret = "test-secret";
        String summaryInfo = getSummaryInfo();
        SecretKeySpec signKey = new SecretKeySpec(secret.getBytes(), HMAC_SHA1_ALGORITHM);
        Mac mac = Mac.getInstance(HMAC_SHA1_ALGORITHM);
        mac.init(signKey);
        byte[] signData = mac.doFinal(summaryInfo.getBytes());
        byte[] result = Base64.encodeBase64(signData);
        System.out.println(new String(result));
    }
 
    private static String getSummaryInfo() {
        String robotId = "this is robotId";
        String robotName = "this is robotName";
        String operatorOpenid = "this is operatorOpenid";
        String operatorName = "this is operatorName";
        String time = "" + new Date().getTime();
        String msgId = "this is msgId";
        String content = "this is content";
        return StringUtils.join(new String[]{robotId, robotName, operatorOpenid, operatorName, time, msgId, content}, ",");
    }
}

SessionID

考虑到每次和机器人对话时可能存在上下文语境，同时也避免多个用户同时与机器人对话时产生混淆，因此云之家提供了一个会话ID，用于开发者处理该场景。

当开发者在多个请求中收到了相同的sessionID，可以认为是同一个用户在同一个群组与同一个机器人发起的多次对话。

该会话ID只会保存 30分钟

请求body参数说明

HTTP 响应格式

开发者可根据自己实际业务，确定返回的结果。目前仅支持返回文本消息

{
    "success":true,
    "data":{
        "type":2,
        "content":"好风凭借力，送我上青云"
    }
}

接入机器人时常见问题及注意事项

机器人创建时的常见错误提示

机器人测试

在输入 消息接受地址后，云之家为确保地址输入正确，会主动发起一次测试请求，详细报文信息如下：

HTTP HEADER

{
  "Content-Type": "application/json; charset=utf-8",
  "sign":"jy/WTAtltv5UVQVDOb0f4H4JPqw=",
  "sessionId":"XXXXXX"
}

发起测试请求时 sign 计算时使用的 secret为

> test-secret

摘要信息 为

sign计算逻辑见这里

sessionID 为随机生成的一个字符串

HTTP BODY

{
    "type":2,
    "robotId":"test-robotId",
    "robotName":"test-robotName",
    "operatorOpenid":"test-userId",
    "operatorName":"test-userName",
    "time":1599727083000,
    "msgId":"test-msgId",
    "content":"你好，你能做什么呢?"
}

测试请求发起后，响应时间需要在 3秒 以内

请求超时时间

对贵公司的消息接受地址发起的每次请求，需要在 3秒 以内收到响应，若在用户艾特机器人的时候无法及时得到响应，则会返回给用户一个默认的提示，提示信息为：

> 哎呀,出现了点小问题,要不等会再试试？

>请求超时时间解决思路

1.如果无法在3秒内响应请求，则可以先返回一个空的content结果，示例如下，表示不响应。

2.待请求处理完成后，再用这个对话机器人的webhook，主动推送一次响应结果 webhook使用请参见这里

{
	"success":true,
	"data":
    	{
        	"type":2,
        	"content":""
        }
}

--- 文档抓取完成 ---

参数 | 说明

sign | 签名值

sessionId | 会话 ID

参数 | 类型 | 说明 | 是否必填

type | int | 消息类型，只支持文本，即type=2 | 是

robotId | String | 加密的机器人id | 是

robotName | String | 机器人名称 | 是

operatorOpenid | String | 加密的发送者id | 是

operatorName | String | 发送者名称 | 是

msgId | String | 加密的消息id | 是

content | String | 消息内容 | 是

time | long | 当前毫秒 | 是

参数 | 类型 | 说明 | 是否必填

success | boolean | 请求是否成功,true-成功,false-失败 | 是

type | int | 消息类型，目前仅支持返回文本消息，类型为2 | 是

content | String | 返回的消息内容 | 是

错误描述 | 导致的原因

请求响应状态码错误，code=xxx | 发起对消息接受地址的请求失败,code为对应的http响应码

请求响应时间超过3秒 | 发起对消息接受地址的请求超时，超过了  3秒

请求响应结果格式不符合文档要求 | 发起对消息接受地址的请求成功，但是返回的数据格式错误，正确内容在这里

测试参数名称 | 测试参数值

robotId | test-robotId

robotName | test-robotName

operatorOpenid | test-userId

operatorName | test-userName

time | 当前时间戳，如1599727083000

msgId | test-msgId

content | 你好，你能做什么呢?

---

---

## 附录：通知型机器人教程

# 创建一个通知机器人

> 来源：开放平台线上文档 (https://open.yunzhijia.com/opendocs/docs/tutorial/index/robot.md)

##  通知型机器人
### 通知型机器人简介

群组机器人是聊天群组中虚拟成员，群组的管理员可以自由创建聊天机器人并设置其名称。

该机器人可以发送 `文本`、`应用` 等类型的消息，均通过调用 http 接口来触发。

基于此种能力，您可以将企业所需要的自定义消息，如系统运维监控通知、日常运营数据等行为通知推送到指定群组。

没耐心看文档？ 跳过文档，[立即体验](/tutorial/index/robot?id=通知型机器人控制台)

![](/opendocs/file/image/0b08d44f40a377961ab48abd6f7255c0)

### 创建通知型机器人

1. 点击群组右上角的 `群设置` 图标（以桌面端为例，移动端也是类似的）

![](/opendocs/file/image/fc3d0059d2c18ec4cf62e5e981761295)

2. 找到 `群组机器人` 选项，点击其右侧的按钮

![](/opendocs/file/image/fea87af984b4710d0111b9c17428355f)

3. 点击 `创建` 按钮

![](/opendocs/file/image/e71271ff9809b6c726ebb80ccd73d4ee)

4. 输入机器人名称

![](/opendocs/file/image/3ce882ac6a652c2efc08bb1b3716b680)

<a id="如何获得webhook"></a>

5. 创建完成，复制Webhook地址

![](/opendocs/file/image/419c7ea378dd321fc56055be73809b37)

Webhook是一个url字符串，它包含接口地址和授权码，通过向该url进行post数据即可控制机器人发送消息。

#### 通知型机器人接口

**接口地址：**

通过向 Webhook 地址 `post` 消息内容，即可让机器人发言。

**消息格式：**

消息内容应为 json 格式，例如：

```json
{
  "content": "大家好，我是天气预报机器人，我将每天为大家推送天气信息。@ALL"
}
```


**接口调用频率控制：**

每个机器人每分钟最多只能发送60条消息

**报文长度限制：**

'content' 字段长度限制：字符数最大3000。



**可选的消息类型：**

*  <a href="docs.html#/server-api/im/index?id=_1发送文本类消息" target="_blank">发送文本类消息</a>
*  <a href="docs.html#/server-api/im/index?id=_2发送应用类消息" target="_blank">发送应用类消息</a>
*  <a href="docs.html#/server-api/im/index?id=_3发送消息卡片类型消息" target="_blank">发送消息卡片类型消息</a>


**可选的通知参数**

*  <a href="docs.html#/server-api/im/index?id=-可选的通知参数效果" target="_blank">通知全员息</a>
*  <a href="docs.html#/server-api/im/index?id=-可选的通知参数效果" target="_blank">通知部分人员</a>


### >>通知型机器人调试控制台

在下面的表单里填入在[上一步](#如何获得webhook)获得的`Webhook`和你要发送的消息内容，就可以控制你的机器人发送消息了。

还可以点击 `查看代码` 按钮查看请求的详情哦。

<iframe src="./demo/robot.html" style="height:450px; border:none;"></iframe>


## 对话机器人

### 对话机器人是什么

云之家为企业提供一种以机器人身份实现群内用户与业务系统对话的能力。可实现将用户群组内发送的指令传递到业务系统，满足咨询问题、查询数据等多种人机对话场景

#### 对话机器人能做什么

**场景举例1：咨询服务**


![](/opendocs/file/image/026a5647d0f43a0dd7bca7548f0a5ea6)

**场景举例二：日程创建**


![](/opendocs/file/image/1f52c764beadf5a1ee402e21ac71469c)


### 如何接入

#### 创建对话机器人

##### 1. 创建入口

###### 手机端创建入口

手机端打开任一群组-->点击右上角的人员图标-->下拉找到群组机器人-->创建自定义机器人--><font color = red>创建对话型机器人</font>

###### 桌面端创建入口

桌面端打开一个群组-->点击右上角的人员图标-->下拉找到群组机器人-->创建自定义机器人--><font color = red>创建对话型机器人</font>

> 创建前需将手机端或桌面端更新至最新版本

##### 2. 基本信息填写

包括机器人名称、机器人Logo、机器人描述

| 填写内容   | 说明                                                         |
| :--------- | ------------------------------------------------------------ |
| 机器人名称 | 请使用意图正确、文明的词汇，避免歧义、错别字及不合规词汇     |
| 机器人头像 | 建议大小为220像素*220像素，请使用清晰的图片，图片核心内容居中。<br>尽量避免尺寸过小、过大或者内容不合规图片 |
| 机器人描述 | 请使用意图正确、文明的词汇，避免歧义、错别字及不合规词汇     |

##### 3. 配置开发信息

点击消息接受地址，填写一个公网可访问的本企业 HTTPS 服务地址，用于接收 POST 过来的消息，之后将对应的响应信息封装为结果展示给用户。

> 在机器人创建过程中，为保证该服务地址真实可用，会进行一次简单的测试，具体测试的参数见[这里](https://open.yunzhijia.com/opendocs/docs.html#/api/im/chatbot?id=%e6%9c%ba%e5%99%a8%e4%ba%ba%e6%b5%8b%e8%af%95)

#### 机器人创建结果

机器人创建成功后会返回<font color=red>该机器人的密钥，即下图中的加密sign. 请妥善保管</font>

![](/opendocs/file/image/89c125ab153d33848cab3e2036017eae)

### 创建后怎么使用

#### 对话机器人唤起方式

##### 手机端

输入@ 或者 点击左下角的艾特图标，然后选择想对话的机器人，后面附带信息即可

##### 桌面端

输入@后点击想对话的机器人，后面附带信息即可

#### 唤起流程明细

当用户@机器人时，云之家会根据发者的 HTTPS 服务地址，把消息内容发送出去

大致流程如下：

![](/opendocs/file/image/7b825c39e9f7a1fa18a69be8f98bdd36)

立刻开始体验？ <a href="docs.html#/server-api/im/chatbot" target="_blank">点击这里</a>


[下一个：开发一个小程序](/tutorial/index/mapp)