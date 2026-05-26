---
domain: product
module: 企业管理
keywords: [文件, 配置]
---

## 企业管理/Windows客户端的安装

Windows客户端的安装

第一步：获取授权License

用户在首次登录取数客户端之前，需要先到获取license许可文件

下单成功后，需要使用云之家管理员账号 通过 管理中心-->订单中心 获取License

​

需要在能和数据库连接的内网环境安装客户端，否则无法连接对应数据库

每个eid对应的license只需要安装在一台服务器上，如果同一个license文件上传在多台机器，取数时会发生冲突

​

​

第二步：安装Windows客户端

​

基础配置

推荐配置（100用户）

超过300用户配置

内存：2G-4G

CPU：双核

硬盘：50-100G

内存：8G-16G

CPU：四核

硬盘：300G左右

内存：32

CPU：八核

硬盘：500G

​

操作系统

Windows Server 2008 或以上版本，64位操作系统

Win7、Win8、Win8.1、Win10 等，64位操作系统

浏览器

Google Chrome、Firefox、Edge、IE10等HTML5浏览器

​

注意：设计报表时不支持IE浏览器。

​

​

【Windows系统】

获取安装包

安装包下载地址 ：https://pan.yunzhijia.com/s/MTI4OTQ1NCxmYmM4#/share/456854845345771521

安装包： maco_client_win_x64_x.x.x.zip

更新包： maco_client.x.x.x.war

​

将安装包解压缩到路径

d:\maco

请确保安装路径结构

（若不是安装在d:\maco，需修改配置文件，详见本步骤末【5. 客户端安装在其他盘】）

​

修改服务器端口（默认端口9090）

文件为...maco\tomcat8\conf\server.xml；

​

进入bin目录

注：若安装正常，但启动不起来的情况下，需要把 d:/maco/tomcat8/bin/tcnative-1.dll 文件替换即可。

tcnative-1.dll文件下载：https://pan.yunzhijia.com/s/MTI4OTQ1NCxmYmM4#/share/456854845345771521

​

5.客户端安装在其它盘

客户端在windows操作系统的安装中，默认是安装在D盘，路径为 d:\maco

如果需要将取数客户端安装在其它盘，可以做如下操作。

​

假如将客户端安装在C盘，路径为 c:\maco

修改下列配置文件：

1.编辑文件 c:\maco\bin\install.bat

将全部 d:\maco 修改为 c:\maco

将第三行的d:改为c:

2.编辑文件 c:\maco\bin\uninstall.bat

将全部 d:\maco 修改为 c:\maco

将第三行的d:改为c:

3.编辑文件 c:\maco\tomcat8\conf\server.xml

将全部 d:\maco 修改为 c:\maco

4.编辑文件 c:\maco\tomcat8\bin\catalina.bat

将全部 d:\maco 修改为 c:\maco

5.编辑文件 c:\maco\tomcat8\bin\service.bat

将全部 d:\maco 修改为 c:\maco

​

经过以上操作后，即可正常安装服务和启动服务

​

第三步：上传licence文件

用户首次登录取数客户端时，需要上传从报表秀秀授权管理人员处获得的license文件。

​

​

恭喜您！报表秀秀BI客户端安装完毕！

---