---
domain: development
module: 密钥管理
keywords: [IM, secret, token]
---

## 密钥验证规则

公共号密钥验证规则

公共号密钥验证规则

前面经常见到公共号密钥验证规则，使用到了一个sha1哈希算法：

pubtoken=sha(no,pub,公共号.密钥pubkey,nonce,time)

*参数介绍*

sha的java代码示例

import org.apache.commons.codec.digest.DigestUtils;
import org.apache.commons.lang3.StringUtils;
public class PubaccUtil {

  public static JSONObject genernateFrom(String no, String pubId, String pubsercet, String nonce, String time) {
    JSONObject jsonFrom = new JSONObject();
    jsonFrom.put("no", no);
    jsonFrom.put("pub", pubId);
    jsonFrom.put("nonce", nonce);
    jsonFrom.put("time", time);
    String pubtoken = sha(no, pubId, pubsercet, nonce, time);
    jsonFrom.put("pubtoken", pubtoken);
    return jsonFrom;
  }

  private static String sha(String... data) {
    Arrays.sort(data);
    String join = StringUtils.join(data);
    String pubtoken = DigestUtils.sha1Hex(join);
    return pubtoken;
  }
}

sha的.net代码示例

using System.Web.Security;
using System;

  public static string sha(string[] data){
            Array.Sort(data, StringComparer.Ordinal);
            string sortdata = String.Join("", data);
            return BitConverter.ToString(SHA1.Create().ComputeHash(Encoding.UTF8.GetBytes(sortdata)))
    .Replace("-", null).ToLower();
}

sha的node.js代码示例

var CryptoJS = require("crypto-js");

var pubtokenBody = {
    "no": eid,
    "pub": pubId,
    "pubsercet": pubsercet,
    "nonce": nonce,
    "time": timestamp
};
var list = [];
for (var k in pubtokenBody) {
    list.push(pubtokenBody[k]);
}
list.sort();
var pubtoken = CryptoJS.SHA1(list.join("")).toString();
console.log("pubtoken:" + "\n" + pubtoken);

sha的js代码示例

function sha(arr){

    arr.sort();
    var as=arr.join('');
     as=hex_sha1(as);
     return as;

}

var hexcase = 0;  /* hex output format. 0 - lowercase; 1 - uppercase        */
var b64pad  = ""; /* base-64 pad character. "=" for strict RFC compliance   */
function hex_sha1(s)    { return rstr2hex(rstr_sha1(str2rstr_utf8(s))); }

function rstr_sha1(s)
{
  return binb2rstr(binb_sha1(rstr2binb(s), s.length * 8));
}


function rstr2hex(input)
{
  try { hexcase } catch(e) { hexcase=0; }
  var hex_tab = hexcase ? "0123456789ABCDEF" : "0123456789abcdef";
  var output = "";
  var x;
  for(var i = 0; i < input.length; i++)
  {
    x = input.charCodeAt(i);
    output += hex_tab.charAt((x >>> 4) & 0x0F)
           +  hex_tab.charAt( x        & 0x0F);
  }
  return output;
}

function str2rstr_utf8(input)
{
  var output = "";
  var i = -1;
  var x, y;

  while(++i < input.length)
  {
    /* Decode utf-16 surrogate pairs */
    x = input.charCodeAt(i);
    y = i + 1 < input.length ? input.charCodeAt(i + 1) : 0;
    if(0xD800 <= x && x <= 0xDBFF && 0xDC00 <= y && y <= 0xDFFF)
    {
      x = 0x10000 + ((x & 0x03FF) << 10) + (y & 0x03FF);
      i++;
    }

    /* Encode output as utf-8 */
    if(x <= 0x7F)
      output += String.fromCharCode(x);
    else if(x <= 0x7FF)
      output += String.fromCharCode(0xC0 | ((x >>> 6 ) & 0x1F),
                                    0x80 | ( x         & 0x3F));
    else if(x <= 0xFFFF)
      output += String.fromCharCode(0xE0 | ((x >>> 12) & 0x0F),
                                    0x80 | ((x >>> 6 ) & 0x3F),
                                    0x80 | ( x         & 0x3F));
    else if(x <= 0x1FFFFF)
      output += String.fromCharCode(0xF0 | ((x >>> 18) & 0x07),
                                    0x80 | ((x >>> 12) & 0x3F),
                                    0x80 | ((x >>> 6 ) & 0x3F),
                                    0x80 | ( x         & 0x3F));
  }
  return output;
}


function rstr2binb(input)
{
  var output = Array(input.length >> 2);
  for(var i = 0; i < output.length; i++)
    output[i] = 0;
  for(var i = 0; i < input.length * 8; i += 8)
    output[i>>5] |= (input.charCodeAt(i / 8) & 0xFF) << (24 - i % 32);
  return output;
}


function binb2rstr(input)
{
  var output = "";
  for(var i = 0; i < input.length * 32; i += 8)
    output += String.fromCharCode((input[i>>5] >>> (24 - i % 32)) & 0xFF);
  return output;
}


function binb_sha1(x, len)
{
  /* append padding */
  x[len >> 5] |= 0x80 << (24 - len % 32);
  x[((len + 64 >> 9) << 4) + 15] = len;

  var w = Array(80);
  var a =  1732584193;
  var b = -271733879;
  var c = -1732584194;
  var d =  271733878;
  var e = -1009589776;

  for(var i = 0; i < x.length; i += 16)
  {
    var olda = a;
    var oldb = b;
    var oldc = c;
    var oldd = d;
    var olde = e;

    for(var j = 0; j < 80; j++)
    {
      if(j < 16) w[j] = x[i + j];
      else w[j] = bit_rol(w[j-3] ^ w[j-8] ^ w[j-14] ^ w[j-16], 1);
      var t = safe_add(safe_add(bit_rol(a, 5), sha1_ft(j, b, c, d)),
                       safe_add(safe_add(e, w[j]), sha1_kt(j)));
      e = d;
      d = c;
      c = bit_rol(b, 30);
      b = a;
      a = t;
    }

    a = safe_add(a, olda);
    b = safe_add(b, oldb);
    c = safe_add(c, oldc);
    d = safe_add(d, oldd);
    e = safe_add(e, olde);
  }
  return Array(a, b, c, d, e);

}

function sha1_ft(t, b, c, d)
{
  if(t < 20) return (b & c) | ((~b) & d);
  if(t < 40) return b ^ c ^ d;
  if(t < 60) return (b & c) | (b & d) | (c & d);
  return b ^ c ^ d;
}

function sha1_kt(t)
{
  return (t < 20) ?  1518500249 : (t < 40) ?  1859775393 :
         (t < 60) ? -1894007588 : -899497514;
}

function safe_add(x, y)
{
  var lsw = (x & 0xFFFF) + (y & 0xFFFF);
  var msw = (x >> 16) + (y >> 16) + (lsw >> 16);
  return (msw << 16) | (lsw & 0xFFFF);
}

function bit_rol(num, cnt)
{
  return (num << cnt) | (num >>> (32 - cnt));
}

--- 文档抓取完成 ---

字段 | 说明

no | 团队号eid

pub | 公共号ID (<a href="docs.html#/server-api/im/pubSend?id=FAQ" target="_blank">如何获得公共号ID和公共号密钥</a>)

pubkey | 公共号密钥pubsecret

nonce | 随机唯一值

time | 10位unix时间戳

---