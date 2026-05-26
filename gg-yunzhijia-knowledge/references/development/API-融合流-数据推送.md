---
domain: development
module: 融合中心
keywords: [IM, dept, secret, 推送, 流程]
---

## 融合流-数据推送

融合流-数据推送

融合流-数据推送

填写服务器地址要求：需填写标准的HTTP接口，为了防止数据被篡改建议采用HTTPS协议

推送方法：post

推送参数类型：Content-Type:application/json

推送参数描述：

推送Json示例：

{
    "data": {
        "redirectUrl": "......",
        "data": {
            "formInstance": {
                ......
                "createTime": "2023-07-10 14:41:53.373",
                "creator": "6437a246e4b01c2909637004",
                "details": {},
                "eid": "6822727",
                "flowInstId": "737fafc92226478794bfaf7767889967",
                "formCodeId": "737fafc92226478794bfaf33fb951c24",
                "id": "64aba8311c25d8000170ad57",
                "noProcess": true,
                "updateTime": "2023-07-10 16:38:35.466",
                "updator": "6437a246e4b01c2909637004",
                "widgetValue": {
                    "_S_TITLE": "4/30-fff标题",
                    "_S_SERIAL": "FFF-20240430-001",
                    "_S_APPLY": [
                        "6437a246e4b01c2909637004"
                    ],
                    "_S_DEPT": [
                        "357a8434-002e-11e8-9592-82e47cc7294a"
                    ],
                    "_S_DATE": 1714464722458,
                    "Da_0": 1715133660000
                }
            }
        },
        "lightcloud_codeId": [
            "_S_TITLE",
            "_S_APPLY"
        ]
    },
    "triggerType": "lightcloud_create",
    "time": 1715167381757,
    "sign": "edf99ab3617ade3f634346b9fd75ced64501b4150821d98038e33a30a2068b13"
}

返回结果需按照如下格式：

{
  "data": "",
  "error": null,
  "errorCode": 0,
  "success": true 
}

签名sign值用于校验收到的数据是否被篡改，如果使用HTTPS协议接收可以忽略

签名生成规则，如果按照代码段生成的sign值和推送过来的sign值一致表示参数中途没有被篡改!
1、获取参数的JSONObject的所有的字段
2、排除sign字段
3、按key的自然排序
4、拼接成md5(value1)=key1&md5(value2)=key2字符串:join
5、secret内容=secret&join 字符串src
6、sha256Hex 作用src 得到签名sign

代码段：
public static String sign(JSONObject params, String secret) {
    String join = params.keySet().stream()
            .filter(key -> !"sign".equals(key))
            .sorted()
            .map(key -> md5Hex(JSONObject.toJSONString(params.get(key))) + "=" + key)
            .collect(Collectors.joining("&"));
    String src = secret + "=secret&" + join;
    String sign = sha256Hex(src);
    return sign;
}

获取secret途径：业务中心-轻云-xxx应用-基础设置-SECRET

--- 文档抓取完成 ---

参数 | 类型 | 注释

redirectUrl | String | 单据详情url

formInstance | Object | 单据实例数据

createTime | String | 单据创建时间

creator | String | 单据创建人oid

details | Object | 明细字段值对象

eid | String | 表单所属工作圈eid

flowInstId | String | 流程实例id，有流程表单该值不为空

formCodeId | String | 表单模版id

id | String | 单据实例id

noProcess | Boolean | true-无流程单据，false-无流程单据

updateTime | String | 单据最后更新时间

updator | String | 单据最后更新人oid

widgetValue | Object | 主表单字段值对象

lightcloud_codeId | JsonArray | 如果监听事件类型为-数据更新，这里会列出具体更新的字段

triggerType | String | 单据事件类型，lightcloud_create(新增)｜lightcloud_update(更新)｜lightcloud_delete(删除)｜lightcloud_approval(审核通过)｜lightcloud_reject(审核不通过)｜lightcloud_back_root(回到开始节点)

time | Long | 推送时间

sign | String | 签名串

参数 | 类型 | 注释

success | Boolean | true-运行监控-融合流-成功；false-运行监控-融合流-失败，失败描述会展示error字段返回内容

---