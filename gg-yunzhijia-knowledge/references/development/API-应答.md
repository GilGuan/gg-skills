---
domain: development
module: 机器人
keywords: [IM, accessToken, token, 消息, 配置]
---

## 应答

公共号消息应答

公共号消息应答

点击此处查看视频教程

请注意：公共号接口的授权并非使用 AccessToken 而是 pubtoken，了解详情请点击此处。

网络传输协议规范

网络传输协议：

HTTPS

HTTP请求地址：

公共号菜单配置的URL.

如果匹配菜单规则,则向该URL POST消息.

注意:10秒超时,则中断失败.

HTTP请求方法：

POST

HTTP内容类型：

Content-Type: application/json

消息内容定义规范

内容格式：

默认的字符编码格式为UTF-8格式

内容组成：

{
    "ServiceType": "xt讯通、wx微信、lw来往…",
    "PubAccId": "讯通公众号id",
    "FromUserName": "如果是微信类型则为微信用户的openid，如果为讯通类型则为讯通用户ID",
    "ToUserName": "如果是微信类型，则为微信公众号ID",
    "MsgType": "消息类型",
    "MsgId": "消息ID",
    "Eid": "企业号",
    "CreateTime": "时间",
    "PubToken": "讯通公众号密钥加密",
    "Payload": {
        "Content": "",
        "PicUrl": "",
        "MediaId": "",
        "Format": "",
        "Title": "",
        "Description": "",
        "Url": "",
        "Location_X": "",
        "Location_Y": "",
        "Scale": "",
        "Label": "",
        "ThumbMediaId": ""
    }
}

消息类型MsgType定义:

public static String TEXT = "text";
public static String IMAGE = "image";
public static String VOICE = "voice";
public static String LINK = "link";
public static String VIDEO = "video";
public static String LOCATION = "location";
public static String CLICK = "click";//菜单点击事件
public static String VIEW = "view"; //菜单连接事件
public static String SUBSCRIBE = "subscribe"; //订阅事件
public static String XT="xt";
public static String WX="wx";

讯通公众号密钥加密PubToken:

用于企业对公共号消息来源的验证，如果业务不需要这么安全，可以忽略验证。 PubToken=sha(PubAccId,FromUserName,CreateTime,MsgId,公众号密钥pubkey),sha哈希算法

import org.apache.commons.codec.digest.DigestUtils;
import org.apache.commons.lang.StringUtils;
import java.util.Arrays;

    public static String sha(String... data){
        Arrays.sort(data);//按字母顺序排序数组
        return DigestUtils.shaHex(StringUtils.join(data));//把数组连接成字符串（无分隔符），并sha1哈希
    }

完整范例

{
    "ServiceType": "xt",
    "PubAccId": "XT-a833d285-xxx",
    "FromUserName": "c51b52e8-xxx",
    "ToUserName": "XT-a833d285-xxx",
    "MsgType": "text",
    "MsgId": "XT-baa6c6fd-xxx",
    "CreateTime": "1396593594951",
    "PubToken": "82490e344986c798e7d600ce8417cbb80a6axxx",
    "Payload": {
        "Content": "TEST"
    }
}

FAQ

暂无

--- 文档抓取完成 ---

---