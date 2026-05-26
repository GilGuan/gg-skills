---
domain: development
module: 通知待办
keywords: [IM, accessToken, appId, secret, token]
---

## 通知中心+待审批

通知中心

通知中心（待办通知）和待审批

点击此处查看视频教程

接口授权

待办相关的接口鉴权使用 app 级别的 AccessToken。

如果您还不了解如何获取 AccessToken，请点击此处查看详情。

待办创建和流转的 2 种模式（同步、异步）

针对待办的创建和流转，待办平台提供两种高可靠的方案（调用模式）供三方系统选择，一种是同步模式，一种是异步模式。模式的选择是通过待办创建和流转时设置的参数 sync 字段来控制，设置为 true  走同步模式， 设置为 false 则走异步模式。

同步模式

三方系统先发起待办请求，待办平台接收此请求后执行相应的业务逻辑，执行完成后在响应报文中返回此次请求<b>接收成功<font color='red'>并且</font>业务逻辑处理完成</b>。

异步模式

三方系统发起待办请求，平台接收此请求后，会直接返回响应报文。该响应报文的成功标识只能说明待办平台收到了请求，<b><font color='red'>不能说明单据是否创建或流转成功</font>，需调用方后续通过待办消息确认接口检查状态，若发现失败，则进行重试</b>。

注意：当采用同步模式时，若请求参数 openId 数量超过 100 建议三方系统分批进行处理，否则待办平台会强制使用异步模式处理。

1.待办创建

待办创建流程图

请按照流程逻辑进行系统设计

描述： 生成并发送待办到待办平台

URL：https://www.yunzhijia.com/gateway/newtodo/open/generatetodo.json?accessToken=xxxxxxxxx

请求方法：post请求内容类型：Content-Type: application/json

限流策略：  相同appId，接口调用限制100次每秒

请求参数

请求体示例：

{
    "content": "小明的请假单据需要您审批",
    "title": "待办测试",
    "itemtitle":"请假审批",
    "headImg": "https://www.yunzhijia.com/space/c/photo/load?id=5a2f7ad750f8dd7810e79981",
    "appId": "500408114",
    "senderId": "5de50017e4b0b2767b870423",
    "params": [{
           "openId": "5de50017e4b0b2767b870423",
           "url": "https://www.yunzhijia.com",                      //可选参数，可以覆盖上层级中的url值。    注：传空值会被忽略
           "content": "小明的请假单据需要您审批，剩余处理时间：3小时"   //可选参数，可以覆盖上层级中的content值。注：传空值会被忽略
      },
      {
           "openId": "5de50083e4b09c41c10efe91",
           "url": "https://www.yunzhijia.com"                       //可选参数，可以覆盖上层级中的url值。注：传空值会被忽略
      },
      {
       	"openId":"5de5003fe4b0b998f379a05e",
        "content": "小明的请假单据需要您审批，剩余处理时间：3小时"   //可选参数，可以覆盖上层级中的content值。注：传空值会被忽略
      },
      {
       	"openId":"5de500e4e4b0b998f379afd7"
      }
    ],
    "url": "https://baike.baidu.com/item/%E4%BA%91%E4%B9%8B%E5%AE%B6/408974",
    "sourceId": "jzyj2eeappdemo",
    "sync": true
}

成功示例

请求响应体示例1，sync 字段为 false（异步模式）时:

{
    "error": "",
    "data": {},
    "errorCode": 0,
    "success": "true"
}

请求响应示例2，sync 字段为 true（同步模式）时:

//待办创建成功
{
    "data": {},
    "success": "true",
    "errorCode": 200,
    "error": "待办创建成功"
}

//超过数目限制
{
    "data": {},
    "success": "false",
    "errorCode": 203,
    "error": "批量生成待办条数超过最大数限制"
}

//有部分用户信息错误，该部分用户的待办生成流程失败，其余正常用户的待办流程会继续执行。
{
    "data": [
        "5b3726f884ae5c69eec1231"  //用户信息错误的用户列表
    ],
    "success": "false",
    "errorCode": 501,
    "error": "有部分用户信息错误，该部分用户的待办生成流程失败。其余正常用户的待办流程会继续执行"
}

//  params 参数中的 openId 全部错误:
{
    "data": [
        "5b3726f884ae5c69eec1231"  //用户信息错误的用户列表
    ],
    "success": "false",
    "errorCode": 505,
    "error": "参数错误，'params' 字段传值错误"
}

//参数异常
{
    "data": "param error:'sourceId' is null.",
    "success": "false",
    "errorCode": 0,
    "error": ""
}

//平台获取成员信息失败
{
    "data": {},
    "success": "false",
    "errorCode": 404,
    "error": "获取用户信息失败"
}

//请求过于频繁
{
    "data": {},
    "success": false,
    "errorCode": 202,
    "error": "数据正在由其他进程处理,请稍候再试"
}

2.待办流转

变更待办的状态（已读、已处理、删除）

待办流转流程图

请按照流程逻辑进行系统设计

URL：https://www.yunzhijia.com/gateway/newtodo/open/action.json?accessToken=xxxxxxxxx

请求方法：post

内容类型：Content-Type: application/json

限流策略：  相同sourcetype，接口调用限制100次每秒

输入参数:

待办变已读-请求示例（已读后仍是待办）

>  read--阅读状态变为 1

{
    "sourceitemid": "jzyj2eeappdemo",
    "sourcetype": "500408114",
    "actiontype": {
        "read": 1
    },
    "openids": ["5a41b292e4b058cf3d0cf313","5a39c75ae4b0a5d9edbf1d62"],
    "sync": true
}

待办变已处理-请求示例

> deal -- 处理状态变为 1

{
    "sourceitemid": "jzyj2eeappdemo",
    "sourcetype": "500408114",
    "actiontype": {
        "read": 1,
        "deal": 1
    },
    "openids": ["5a41b292e4b058cf3d0cf313","5a39c75ae4b0a5d9edbf1d62"],
    "sync": true
}

待办删除-请求示例

> delete -- 删除状态变为 1

{
    "sourceitemid": "jzyj2eeappdemo",
    "sourcetype": "500408114",
    "actiontype": {
        "delete": 1
    },
    "openids": ["5a41b292e4b058cf3d0cf313","5a39c75ae4b0a5d9edbf1d62"],
    "sync": true
}

返回结果示例1，sync字段为false（异步）时:

{
    "error": "",
    "data": {},
    "errorCode": 0,
    "success": "true"
}

返回结果示例2，sync字段为true（同步）时:

//待办转已读成功:
{
    "data": {},
    "success": "true",
    "errorCode": 200,
    "error": "待办更新阅读状态成功"
}

//待办转已办成功:
{
    "data": {},
    "success": "true",
    "errorCode": 200,
    "error": "待办转已办成功"
}

// 待办删除成功:
{
    "data": {},
    "success": "true",
    "errorCode": 200,
    "error": "待办删除成功"
}

// 处理失败，actiontype为空:
{
    "data": "param error:actiontype is null.",
    "success": "false",
    "errorCode": 1,
    "error": ""
}

// 处理失败，sourceitemid为空:
{
    "data": "param error:sourceitemid is null.",
    "success": "false",
    "errorCode": 1,
    "error": ""
}

// 处理失败，sourcetype为空:
{
    "data": "param error:sourcetype is null.",
    "success": "false",
    "errorCode": 1,
    "error": ""
}

// 处理失败，openid存在但是无值:
{
    "data": "param error:openids is null.",
    "success": "false",
    "errorCode": 1,
    "error": ""
}


// 有部分用户里没有对应待办，常为信息错误，该部分用户的待办处理流程失败。其余正常用户的待办流程会继续执行(data中为用户openId):
{
    "data": [
        "60e65677e4b015960471f596"
    ],
    "success": "false",
    "errorCode": 502,
    "error": "有成员待办更新状态失败"
}}

// 有openId错误，查询不到对应用户:
{
    "data": {},
    "success": "false",
    "errorCode": 404,
    "error": "获取用户信息失败"
}

// 平台获取成员信息失败:
{
    "data": {},
    "success": "false",
    "errorCode": 404,
    "error": "获取用户信息失败"
}

3.待办状态查询

URL：https://www.yunzhijia.com/gateway/newtodo/open/checkcreatetodo.json?accessToken=xxxxxxxxx

请求方法：post

内容类型：Content-Type: application/json

限流策略： 相同 sourcetype+sourceitemid 每分钟限制查询 5 次

参数说明

json示例：

{
    "sourceitemid": "jzyj2eeappdemo",
    "sourcetype": "500408114",
    "openId": "5de50017e4b0b2767b870423"
}

返回结果示例:

{
    "data": {
        "sourceid": "jzyj2eeappdemo",  //对应入参的sourceitemid
        "appid": "500408114",  //对应入参的souretype
        "check": true,  //标识业务检查成功,true:成功，false:失败/被限流
        "dealCount": 0,   //标识已办单据数量。此处dealCount=0,undelCount=1,表示待办生成成功
        "undelCount": 1,  //标识待办单据数量
        "errormsg" : "Request too frequent, try later." // 标识请求被限流(只有限流时才返回此字段)
    },
    "success": "true", //请求接收成功
    "errorCode": 0,
    "error": ""
}

参数说明

dealCount与undelCount说明

dealCount=0，undelCount=0：表示待办单据不存在(即没有待办，也没有已办)

dealCount=0，undelCount=1：表示单据存在，目前为待处理的状态

dealCount=1，undelCount=0：表示单据存在，目前为已办状态

4.待办批量快捷审批

准入标准： 用户需要及时查看并处理的，并且处理能推动业务的应用消息，如流程审批、请假审批，需要推送单据到【待审批】，仅需用户知悉，如抄送、会议通知等，不需要进行审批操作的单据，建议推送至【待办通知】或通过订阅号推送

接入方法：

【手动归类】开发者可登陆应用中心管理平台，将待办关联的应用勾选为【审批类】（勾选此类可将应用消息推送至【待审批】）。勾选【审批类】后会生成一个signKey值（该signKey值用于接口对接时的安全校验）

前提： 应用设置为【审批类】

待办流转流程图

请按照流程逻辑进行系统设计

1:在创建待办消息时接口参数中需要增加passUrl字段。[https://www.yunzhijia.com/gateway/newtodo/open/generatetodo.json?accessToken=xxxxxxxxx]

json示例：

{
    "content": "印*的请假单据需要您审批",
    "title": "待办测试",
    "itemtitle":"请假审批",
    "headImg": "https://www.yunzhijia.com/space/c/photo/load?id=5a2f7ad750f8dd7810e79981",
    "appId": "500408114",
    "senderId": "5de50017e4b0b2767b870423",
    "params": [{
        "openId": "5de50017e4b0b2767b870423"
    },{
        "openId": "5de50083e4b09c41c10efe91"
    }],
    "url": "https://baike.baidu.com/item/%E4%BA%91%E4%B9%8B%E5%AE%B6/408974",
    "sourceId": "jzyj2eeappdemo",
    "passUrl": "https://{domain}/xxx/batchDealTodo"     //此传参，标识支持快捷审批
}

第三方业务需要实现 passUrl: https://{domain}/xxx/batchDealTodo 对应接口，完成批量审批处理逻辑。

请求方法：POST

内容类型：Content-Type: application/json

json示例：

{
    "param":{
        "eid":"17951708",
        "sourceType":"500408114",
        "openId":"5de50017e4b0b2767b870423",
        "sourceIds":[
            "5dc0d35866b6746a7a5e5bb1",
            "5dc0d35866b6746a7a5e5bb2"
        ]
    },
    "sign":"Eg0HrAkbJve/tivfIBlpxwFlHUI=" 
}

返回结果示例：

{
    "data":{
        "successIds":[
            "5dc0d35866b6746a7a5e5bb1",
            "5dc0d35866b6746a7a5e5bb2"
        ]
    },
    "error":null,
    "errorCode":0,
    "success":true
}

#注:返回的successIds里即为业务方处理成功的单据，云之家待办系统会将这些待办进行转已办操作，无需业务方再次调用待办流转接口将待办转为已办（此为快捷同意的功能意义）。 如业务方无法同步将自系统内单据转为已办并返回给接口，需要异步处理，则请避免将单据id放在返回结果的successIds中，此时用户点击审批以后会提示审批失败(因为successIds无对应数据)，在业务方异步处理完成自己的单据后，业务方调用云之家流转接口将待办转为已办。

passUrl对应的接口的伪代码如下：

@RestController("/xxx")
public class DealTodoRest {

    @RequestMapping(value = "/batchDealTodo", produces = "application/json;charset=utf-8", method = RequestMethod.POST)
    public String batchDealTodo(@RequestBody String jsonParam){
        //sign值校验是否合法（第三方业务用请求报文生成一个sign值【genSign()】，与报文中的sign值进行对比）
        boolean succ = checkSign(jsonParam);
        if (!succ){
            return "{\"error\":\"check sign error.\",\"errorCode\":5001,\"success\":false}";
        }        

        //批量完成待办逻辑
        return dealTodos();
    }
    
    private boolean checkSign(String jsonParam){
        String origSign = getBy(jsonParam);
        String currSign = genSign(signKey, openId, sourceType, sourceIds);
        return StringUtils.equals(origSign, currSign);
    }
}

生成sign值得算法[java版]

//signKey :在设置应用为审批类时生成的signKey值
private static String genSign(String signKey, String openId, String sourceType, JSONArray sourceIds) throws Exception {
    List<String> vals = new ArrayList<>();
    vals.add(openId);
    vals.add(sourceType);
    if (CollectionUtils.isNotEmpty(sourceIds)){
        for (int i = 0; i < sourceIds.size(); i++) {
            String sourceId = sourceIds.getString(i);
            vals.add(sourceId);
        }
    }
    Collections.sort(vals, new Comparator<String>() {
        @Override
        public int compare(String o1, String o2) {
            return o1.compareTo(o2);
        }
    });
    String sortedVal = StringUtils.join(vals, "&");

    return SignUtil.genHmacSHA1(sortedVal, signKey);
}

签名工具类[java版]

import org.apache.commons.codec.binary.Base64;
import javax.crypto.Mac;
import javax.crypto.spec.SecretKeySpec;

public class SignUtil {

    private static final String HMAC_SHA1_ALGORITHM = "HmacSHA1";

    /**
     * 使用 HMAC-SHA1 签名方法对data进行签名
     * @param data 被签名的字符串
     * @param key 密钥
     * @return
    加密后的字符串
     */
    public static String genHmacSHA1(String data, String key) throws Exception{
        SecretKeySpec signKey = new SecretKeySpec(key.getBytes(), HMAC_SHA1_ALGORITHM);
        Mac mac = Mac.getInstance(HMAC_SHA1_ALGORITHM);
        mac.init(signKey);
        byte[] rawHmac = mac.doFinal(data.getBytes());
        byte[] result = Base64.encodeBase64(rawHmac);

        if (null != result) {
            return new String(result);
        } else {
            return null;
        }
    }
}

--- 文档抓取完成 ---

字段 | 类型 | 是否必填 | 说明

openId | String | 是 | 待办接收人 Id，可填多人，不要超过100个

appId | String | 是 | 生成待办所关联的应用 id，注意：<span style="background-color:rgb(255,255,0)">待办平台通过 appId 和 sourceId 组合在一起标识待办的唯一性</span>，被标识重复的请求会被<font color="red"><b>忽略</b></font>

sourceId | String | 是 | 生成的待办所关联的三方业务系统的单据ID(待办的批次号)， [ 对应待办处理中的 sourceitemid ]，<span style="background-color:rgb(255,255,0)">其值由三方系统自行设定并需保证其<b><font color="red">唯一性</b></font> </span>，被标识重复的请求会被<b><font color="red">忽略</font></b>。

sync | Boolean | 否 | 待办的生成模式，true: 同步，false: 异步，默认为 false ( <font color="red">推荐使用 sync=true 的方式 </font><span style="background-color:rgb(255,255,0)">注意：当 openId 数量超过 100 时，即使 sync 为 true 设置为走同步模式，待办平台将会强制使用异步模式 ) <font color="red">异步模式下，在调用创建接口后，请调用 '待办状态查询' 接口,查询实际处理结果</font></span>，以确保数据的最终一致性(3.待办状态查询详细描述)

todoType | int | 否 | 待办显示分类类型，可选值： 0 ：通知中心 ， 1 ：待审批(<b>流程中心(推荐直接使用流程中心的接口进行对接)</b>) （也可以在 应用中心-应用管理中，对关联 应用 的'待办类型'选项进行设置(此设置优先级低于 todoType 的传参值)【注意：在应用中心更改待办类型后，需要<b>'保存'</b>，然后<b>'提交审核'</b>；待<b>应用管理员审核通过</b>后，该配置方可生效(单向0->1)】）

tagId | String | 否 | 若<b>todoType=0 或未传 todoType 且该应用为通知类</b> 则通过此参数设置 通知中心 的二级分类。tagId 可从管理中心系统设置->待办设置->待办中心分类设置中新增及获取

url | String | 是 | 点击该待办时跳转的URL，需要全路径

content | String | 否 | 待办内容  （移动端顶部通知栏显示的内容，<span style="background-color:rgb(255,255,0)">为空时则不会有顶部通知</span>）

title | String | 是 | 待办主标题 ，一般对应轻应用名称

itemtitle | String | 否 | 待办项标题内容显示，选填，如不填，则默认取 title 的值

headImg | String | 是 | 待办在客户端显示的 icon url

senderId | String | 否 | 待办的发送人的 openId

字段 | 类型 | 是否必填 | 说明

sourcetype | String | 是 | 应用ID，即 appId

sourceitemid | String | 是 | 生成的待办所关联的三方系统的单据ID(待办的批次号), (<b>对应生成待办时的sourceId</b>)

deal | Integer | 否 | 目标处理状态，0表示未办，1表示已办，默认为0

read | Integer | 否 | 目标读状态，0表示未读，1表示已读，默认为0

delete | Integer | 否 | 目标删除状态，0表示未删除，1表示已删除

openids | String | 否 | 待办所属用户id (注意大小写)，可填多人，<font color="red">不填则更改sourceitemid对应所有人员的待办状态</font>

sync | Boolean | 否

字段 | 类型 | 是否必填 | 说明

sourcetype | String | 是 | 应用ID，即appId

sourceitemid | String | 是 | 即sourceId,生成的待办所关联的三方业务系统的单据ID(待办的批次号)

openId | String | 是 | 待办接受人ID

字段 | 类型 | 说明

appid | String | 对应请求参数中的sourcetype

sourceid | String | 对应请求参数中的sourceitemid

check | boolean | 检查结果，true：成功，false：失败

dealCount | int | 表示生成已办成功的数量

undelCount | int | 表示变待办成功的数量

---

---

## 附录：待办推送教程

# 推送一条待办消息

> 来源：开放平台线上文档 (https://open.yunzhijia.com/opendocs/docs/tutorial/index/todo.md)

## 简单介绍

应用可以把需要用户处理的业务信息通过待办的方式推送到消息列表，用户点击待办消息后可以进入对应的应用中完成处理。

云之家待办系统中，单据有 2 个状态， 待处理和已处理，每条单据只会处于 2 者中的一个。

它们的数量和入口会一直显示在 `消息` 页签的顶部，如下图：

![](https://www.yunzhijia.com/opendocs/file/image/b923e975d7894d2d6c15a28b363d22a4)

待办系统中的单据，每一条必须包含以下 3个属性，

`openId`  : 接收人

`appId `: 轻应用 id，比如智能审批，签到，用于说明单据的来源系统

`sourceId `: 源id , 可为任意值，一般为对接的业务系统中具体某一条单据的 id

待办的唯一性是通过 openId + appId + sourceId  三者联合起来作为主键来保证的

## 前期准备

获取 accessToken 用于鉴权，获取方式请<a href="docs.html#/server-api/auth/oauth" target="_blank">点击此处</a>

待办的授权级别为 <font color = "red">app</font> 级，轻应用 secret 是通过管理员账号进入 `管理中心--应用管理--应用详细` 处获取

![](/opendocs/file/image/3c6ae129dcac0f79fd507a8f8b5f2afe)

## 待办创建和流转的 2 种模式

针对待办的创建和流转，云之家平台提供两种高可靠方案供调用方选择，一种是同步模式，一种是异步模式。模式的选择是通过 创建和 流转时的参数 `sync` 来控制，true -同步，false-异步

**同步模式**

调用方先发起请求，云之家将对应的单据创建或流转后，在 http 响应里面说明此次请求是否成功

**异步模式**

调用方发起请求后，立刻会收到请求响应，该响应只能说明云之家平台是否受到了用户的请求，<font color='red'>不能说明单据是否创建/流转成功</font>，用户需后续不断调用待办消息确认接口检查状态，若发现失败，则进行重试

当用户请求量较大时，可以使用异步模式。同步模式虽然性能稍差一点，但简化了流程的逻辑。

>建议使用<font color='red'>同步</font>模式，但是当一次请求生成待办数在100条及以上时，建议使用异步

## 待办创建

创建一条待办，推送至云之家客户端指定区域

### [待办创建API](https://open.yunzhijia.com/opendocs/docs.html#/server-api/im/im-todo?id=%e5%be%85%e5%8a%9e%e5%88%9b%e5%bb%ba)

### 成功示例

![](/opendocs/file/image/265a343d309ff19e2a4f865c3c3acddb)

## 待办流转

变更待办单据的状态，变为已读，已处理 或者删除

### [待办流转API](https://open.yunzhijia.com/opendocs/docs.html#/server-api/im/im-todo?id=%e5%be%85%e5%8a%9e%e6%b5%81%e8%bd%ac)


### 注意事项

参数 `openIds` 表示变更的用户的 id， 若为空，则表示处理该 `sourceId + appId` 下的所有用户

## 待办状态查询

### 在线查询测试接口
可以点击 `查看代码` 按钮查看请求的详情哦。
<iframe src="./demo/todo.html" style="height:450px; border:none;"></iframe>

### [待办状态查询API](https://open.yunzhijia.com/opendocs/docs.html#/server-api/im/im-todo?id=%e5%be%85%e5%8a%9e%e7%8a%b6%e6%80%81%e6%9f%a5%e8%af%a2)




## 待办快捷审批

### 什么是快捷审批

对于审批的单据，用户在处理时，需要先点击单据，跳转到相应的系统中，然后进行审批处理。然而实际工作中，会存在某些不太需要“仔细”审核的单据，比如审核请假流程等。
为了提高用户工作效率，对于支持快捷审批的单据，用户在云之家内直接点击同意按钮，即可立刻将单据处理完毕。

### 如何接入快捷审批

建议接入类型： 用户需要及时查看处理的，并且处理能推动业务的应用消息，如流程审批、请假审批等。

接入方法：
1.开发者登陆应用管理后台，将自己的应用勾选为【审批类】，此时会生成一个signKey值，该signKey值用于表明请求是来自于云之家，开发者在接收审批请求时，需要验证 signKey是否合法，从而保证数据安全。
2.创建待办时加入参数 `passUrl` ，该 url 即为快捷审批专用
3.业务需要实现 passUrl: https://{domain}/xxx/batchDealTodo 对应接口，完成批量审批处理逻辑

### [API](https://open.yunzhijia.com/opendocs/docs.html#/server-api/im/im-todo?id=%e5%be%85%e5%8a%9e%e6%89%b9%e9%87%8f%e5%bf%ab%e6%8d%b7%e5%ae%a1%e6%89%b9)




## 常见问题

**1.为什么待办 创建 时请求的响应返回了  成功（success)，但是用户却没有在云之家收到待办？**

首先，请检查使用的模式是否为异步。异步模式返回的success<font color="red">只表示云之家收到了请求，不表示最终处理结果</font>，建议出现问题时，先改为同步模式

其次，云之家待办使用 `openId + appId + sourceId`  三者联合起来作为主键，当创建时发现主键重复，会自动忽略，因此，可以先用 待办查询接口，检查下该单据是否存在，若存在，则建议更换参数，避免重复。

**2.我的轻应用配置为审批类，但是我想用同一个`appId` 发送通知类的消息，该如何操作？**

创建待办时有个参数 `todoType`，用来表明单据目的地。若在创建时指定了，则会以创建的为准，若未指定，则会读取轻应用的配置信息。因此，可以在创建时指定 `todoType` 为 0

> 若想使用通知类的轻应用，发送审批类的待办，也是一样的道理

**3.用户点击“待审批”，查看了某条消息，为什么“待审批”上的未读数仍然没有清除？**

云之家待办平台可开启强提醒模式，开启后，若待办消息未处理完毕，该未读数会一直保持，用于增强提醒功能。

开启前提：在手机系统设置开启云之家消息推送；

设置路径：（移动端）头像-设置-新消息通知-顶部强提醒模式

![](/opendocs/file/image/e8965c148db02692112d87fe03466bd2)

> 强提醒功能开启后，该用户的所有团队都会设置为相同的模式

**4.待办流转的请求如果在创建之前发出了，会有什么问题？**

收到某条单据的流转请求后，云之家待办平台会查询该单据是否存在，若不存在，即为这个场景，此时，待办平台会将该单据的流转状态缓存 一个小时。

若在这一小时内，收到了创建请求，则会自动将该单据直接变为 流转请求里面的结果。

若超过了一个小时，缓存到期，则系统直接将流转请求从缓存中删除，回到初始未收到该单据的状态

**5.为什么我点开了某条审批单据，发现这条单据已经处理完了，但云之家上仍然存在？**

主要的原因是业务系统处理完单据后，例如变完成，取消，撤回等等操作时，未及时通知云之家待办平台，即未发送待办流转的请求，请联系该业务系统负责人

> 用户可以点击该单据右上角 忽略，将这条单据先去掉，避免干扰

**6.推送给了一条单据给某个用户，后面撤回了，但是最后又提交给了这个用户，该如何操作？**

该问题的本质是主键重复了。待办系统的主键是  `openId + appId + sourceId` ，调用方一般会将单据的 id 作为`sourceId`，当同一个流程 多次推送给同一个用户时，可能会出现这个问题。

> 云之家待办平台的单据，状态不可逆，只支持待处理-> 已处理，不支持 已处理->待处理

解决的方法：

1） 遇到这种情况时，变更`sourceId`

> 云之家待办平台 不会对 `sourceId` 做任何校验，因此任意字符都是可以的

2） 先删除旧 待办，检查到删除成功后，重新推新的待办 

> 删除旧待办建议使用同步模式，根据返回的响应判断是否删除成功


[下一个：创建一个聊天机器人](/tutorial/index/robot)