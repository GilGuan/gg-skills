---
domain: development
module: IM消息
keywords: [IM, accessToken, appId, token, 审批]
---

## 消息发送

公共号消息发送

公共号消息发送

点击此处查看视频教程

鉴权说明

请注意：公共号接口的授权并非使用 AccessToken 而是 pubtoken，了解详情请点击此处。

请求规范

网络传输协议：HTTPS

请求地址：

https://www.yunzhijia.com/pubacc/pubsendV2

请求方法，报文格式

METHOD:POST

Content-Type: application/json

请求参数

请求body参数使用符合JSON规格的数据交换格式，默认的字符编码格式为UTF-8格式。

消息内容由消息的发送发、接收方、消息类型、身份认证签名等不可见信息以及发布内容等可见信息组成。

{
  "from":"发送方信息，格式为JSON对象",
  "to":"接收方信息，格式为包含一至多个接收方信息JSON对象的JSON数组",
  "type":"消息类型，格式为整型",(取值 2：单文本,5：文本链接,6：图文链接)
  "msg":"发布到讯通的消息内容，格式为JSON对象"
}

1.from的定义

{
  "no":"发送方企业的企业注册号(eid)，格式为字符串",
  "pub":"发送使用的公共号ID，格式为字符串",
  "time":"参与pubtoken计算时所用的字符串格式时间戳",
  "nonce":"随机数，格式为字符串或数字",
  "pubtoken":"公共号加密串，格式为字符串。"
}

如果您是isv伙伴可以在创建轻应用界面查看pubid，pubsercet;

如果您是企业内部轻应用可以登录云之家公共服务平台查看,详细请参考此页FAQ;

公共号密钥验证规则pubtoken=sha(no,pub,pubsercet,nonce,time),示例代码参见此页公共号密钥验证规则

2.to的定义

[
  {
    "no":"接收方企业的企业注册号(eID)，格式为字符串",
    "user":"接收方的用户ID，格式为包含OPENID的JSON数组"
  },
  {
    ……
  },
  ……
]

其中，”to”:[] 表示所有订阅的企业和用户。(企业自建公共号此参数不起作用);

其中，”to”:[{“no”:“10001”,”code”:“all”},{“no”:“10002”,”code”:“all”}….] 表示企业10001,10002所有订阅的用户。”code”:“all”一定不要漏,否则报错;

其中，”to”:[{“no”:“10001”,”user”:[“1”,”2”]},{“no”:“10002”,”user”:[“3”,”4”]}] 表示企业10001的openid=1,2用户;企业10002的openid=3,4用户。

3.type的定义

2:纯文本信息

5:文本链接信息

6:图文混排信息

25:卡片类型消息

4.msg的定义

根据不同的type定义，msg会有不同的格式定义。

4.1.type为2时，msg的定义:

{
  "text":"文本消息内容，格式为字符串"
}

4.2.type为5时，msg的定义:

{
  "text":"必填,文本消息内容，String",
  "url":"文本链接地址，格式为经过URLENCODE编码的字符串",
  "appid": "如果想让链接地址携带用户身份（ticket），请传入轻应用ID（appid）",
  "todo":"int，必填,暂时只能为0，表示推送原公共号消息",
  "sourceid":"备用字段，暂时无用"
}

“url”:“文本链接地址，格式为参数值经过URLENCODE编码的字符串” 注意:只是参数值编码,不要编码全部路径或者路径包含非法字符,否则无法打开url

doku.php?id=使用说明&abc=123  编码后为
doku.php?id=%E4%BD%BF%E7%94%A8%E8%AF%B4%E6%98%8E&abc=123

4.3.type为6时，msg的定义:

{
  "model":"排版展现模板，格式为整型",
  "todo":"int，必填,暂时只能为0，表示推送原公共号消息",
  "sourceid":"备用字段，暂时无用",
  "list":"发布信息列表，格式为包含发布信息JSON对象的JSON数组"
}

4.3.1.model的定义:

1：单条文本编排模板

2：单条图文混排模板

3：多条图文混排模板

4.3.2.list的定义:

根据不同的model定义，list会有不同的格式定义。

4.3.2.1.model为1时，list的定义:

[
  {
    "date":"发布日期，格式为包含了'年月日时分秒'字符串",
    "title":"消息标题，格式为字符串",
    "text":"消息摘要，格式为字符串",
    "url":"原文链接，格式为经过URLENCODE编码的字符串",
    "appid": "如果想让链接地址携带用户身份（ticket），请传入轻应用ID（appid）"
  }
]

“url”:“文本链接地址，格式为参数值经过URLENCODE编码的字符串” 注意:只是参数值编码,不要编码全部路径或者路径包含非法字符,否则无法打开url

doku.php?id=使用说明&abc=123  编码后为
doku.php?id=%E4%BD%BF%E7%94%A8%E8%AF%B4%E6%98%8E&abc=123

4.3.2.2.model为2时，list的定义:

[
  {
    "date":"发布日期，格式为包含了'年月日时分秒'字符串",
    "title":"消息标题，格式为字符串",
    "text":"消息摘要，格式为字符串",
    "url":"原文链接，格式为经过URLENCODE编码的字符串",
    "appid": "如果想让链接地址携带用户身份（ticket），请传入轻应用ID（appid）",
    "name":"图片的文件名，格式为字符串"(传图片时，必须传文件名)，
    "pic":"图片的二进制字节流，格式为经过BASE64编码的字符串"
  }
]

4.3.2.3.model为3时，list的定义:

[
  {
    "date":"发布日期，格式为包含了'年月日时分秒'字符串",
    "title":"消息标题，格式为字符串",
    "text":"消息摘要，格式为字符串",
    "url":"原文链接，格式为经过URLENCODE编码的字符串",
    "appid": "如果想让链接地址携带用户身份（ticket），请传入轻应用ID（appid）",
    "name":"图片的文件名，格式为字符串"(传图片时，必须传文件名）,
    "pic":"图片的二进制字节流，格式为经过BASE64编码的字符串"
  },
  {
    ……
  },
  ……
]

pic的定义:

讯通公共号消息大尺寸缩略图的宽度和高度规格为542px\*260px，小尺寸缩略图的宽度和高度规格为142px\*112px，如发送图片的比例不相符，将会在显示前被裁减。model为3时，第一条消息显示为大尺寸缩略图，其他的为小尺寸缩略图。

4.4.type为25时，msg的定义:

发送卡片类型消息，请参考点击此处

JSON请求格式示例1

文本链接信息内容JSON示例：

{
    "from": {
        "no": "10603457",
        "pub": "XT-d4dfc04c-9416-4b8c-86ca-dc57dc949006",
        "pubtoken": "bc3bbfab24dd995f955244fb81d671bd9f621da0",
        "nonce": "add9b617-a95f-417d-882c-722e077348c7",
        "time": "1530758888"
    },
    "to": [
        {
            "no": "10603457",
            "user": [
                "5a41b292e4b058cf3d0cf314",
                "5a39c75ae4b0a5d9edbf1d67"
            ]
        }
    ],
    "type": 5,
    "msg": {
        "appid": "10745",
        "text": "公共号消息发送测试\n打开轻应用云龙项目",
        "todo": 0,
        "url": "https://www.cloudlong.cn/yzj/index.html"
    }
}

图文混排信息内容JSON示例2：

{
    "from": {
        "no": "10250",
        "pub": "XT-95 ... 37a",
        "time": "2013-10-18 20:11"
    },
    "to": [
        {
            "no": "10250",
            "user": [
                "+8R ... wg=",
                "RMC ... wg=",
                "El4 ... wg=",
                "/Ut ... wg=",
                "cgu ... wg=",
                "Jb0 ... wg="
            ]
        }
    ],
    "type": 6,
    "msg": {
        "model": 2,
        "list": [
            {
                "date": "2013-10-18",
                "title": "金蝶K/3WISE APS成功通过BETA测试",
                "text": "2013年9月29日，在隔朗五金的大力配合下，顺利完成金蝶K/3WISE V13.1 APS 的BETA测试",
                "url": "https://easportal.kingdee.com/xt/news/XTNewsContent.jsp?contentId=+8RN5f ... YSwwg=",
                "name": "E6O2IqkURTaIoz1n ... 018201154584.jpg",
                "pic": "/9j/4AAQSkZJRgABA ... AkZ6VVlUc0UVijV7H//Z"
            }
        ]
    }
}

输出结果：

{
    "pubId": "XT-d4dfc04c-9416-4b8c-86ca-dc57dc949006",
    "sourceMsgId": "XT-5b3dc0f3e4b0ad2483c0701a"
}

返回报文说明

使用 /pubacc/pubsendV2 请求时的返回结果

成功：

当消息发送请求被成功执行时，HTTP状态码返回200, 响应体 code字段等于0, 且success字段等于true。

响应体：

{
    "code": 0,
    "data": {
        "pubId": "XT-xxxx-xxxx",
        "sourceMsgId": "XT-xxxx"
    },
    "message": "发送成功",
    "success": true
}

请求失败：

当消息发送请求执行失败时，HTTP状态码返回以下错误：

• 400:客户端参数错误，仔细确认Content-Type类型和参数
• 500:服务器内部错误

业务失败：

当消息发送请求执行失败时，HTTP状态码返回200, 响应体 code字段不等于0, 且success字段等于false。

响应体：

{
    "code": xxx,
    "message": "xxx",
    "success": false
}

code字段说明：

• 400: 检查Content-Type是否为application/json 或确认body是否为空字符串
• 500: 常规错误，根据message字段来排查相关错误。
• 5000: 检查json各个参数，object/array类型要注意区分
• 5001:公共号不存在或未审核
• 5002:数据长度超限错误，如：传入数据长度超过了1.5M
• 5003:发送的公司或用户错误，如:发送到其他企业,无发送用户或错误的openid
• 5004:公共号密钥验证失败，from.pubtoken=sha(from.no,from.pub,公共号.pubkey,from.nonce,from.time)
• 5005:发往公共号消息过多,请等x分钟
• 5102: 频率太快，请稍后再试
• 6001: 公共号平台内部错误

频率限制

公共号服务端会限制公共号发送的频率，同一from内容不能在十分钟内重复发送，否则返回5005错误。

如果有密集的业务消息发送，必须保证from内容不同，例如不同的time,nonce。

安全性和数据量过大问题

考虑到信息【安全性】及【数据量过大】问题，通过接口上传的数据不会展示至管理后台，

安全性

假如后台展示通过接口上传的数据，管理员可越权查看无权限的公共号消息；

> 例如：企业自建的【审批】公共号，通过该公共号发送审批单据给领导，管理员可在公共号后台查看领导审批单据，存在信息安全隐患；

数据量过大

目前公共号在企业应用中不仅限于推文的应用场景，还可以推送其它第三方自建应用的各种消息，业务消息量过大会影响系统稳定性，造成服务抖动

> 例如：企业自建应用【审批】通过公共号推送消息，【审批】应用日常推送消息数量较多，对于公共号管理列表性能压力过大且数据无意义

> 建议方案：管理员若想了解调用接口是否成功，可将自己添加到推送范围里，管理员将会在前端页面收到推送的消息，即可判断调用接口是否成功

FAQ

如何进入公共号管理？

公共号管理员进入公共号路径：网页端云之家-导航栏—公共服务平台

系统管理员进入公共号管理路径：网页端云之家--管理中心--公共号

---

如何获得公共号ID和公共号密钥？

企业管理员和公共号管理员进入 网页端云之家--业务中心--公共号，选择对应公共号并进入，选择“开发者”，如下图所示，通过输入正确的验证码，获取对应的公共号ID和公共号密钥：

公共号服务平台

代码示例

PHP代码示例：

<?php
   function http_post_data($url, $data_string) {

        $ch = curl_init();
        curl_setopt($ch, CURLOPT_POST, 1);
        curl_setopt($ch, CURLOPT_URL, $url);
        curl_setopt($ch, CURLOPT_POSTFIELDS, $data_string);
        curl_setopt($ch, CURLOPT_HTTPHEADER, array(
            'Content-Type: application/json; charset=utf-8',
            'Content-Length: ' . strlen($data_string))
        );
        ob_start();
        curl_exec($ch);
        $return_content = ob_get_contents();
        ob_end_clean();

        $return_code = curl_getinfo($ch, CURLINFO_HTTP_CODE);
        return array($return_code, $return_content);
    }

    $pubkey = "12345678123456781234567812345678";

    //公共号密钥验证规则pubtoken=sha(no,pub,公共号.密钥pubkey,nonce,time)
    $a = array("19901","XT-87e1732f-xxxx",$pubkey,"123456","1395460000");
    sort($a,SORT_STRING);
    $b = implode("",$a);
    echo $b."\r\n";
    $pubtoken = sha1($b);
    echo $pubtoken."\r\n";

    $data_string = '{ "from": { "no":"19901", "pub":"XT-87e1732f-xxxx", "time":"1395460000", "nonce":"123456", "pubtoken":"'.$pubtoken.'" }, '.
           '"to": [ { "no":"19901", "user": ["cde2b88a-xxxx"], "code":"0" } ], "type":2, "msg": {"text":"金蝶测试"}}';
    $url = "https://www.yunzhijia.com/pubacc/pubsend";
    list($return_code, $return_content) = http_post_data($url, $data_string);
    echo "返回值:".$return_code."\r\n";
    echo "返回内容:".$return_content."\r\n\r\n";
?>

--- 文档抓取完成 ---

---