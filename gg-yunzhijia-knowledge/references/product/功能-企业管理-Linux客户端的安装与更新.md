---
domain: product
module: 企业管理
keywords: [配置]
---

## 企业管理/Linux客户端的安装与更新

Linux客户端的安装与更新

推荐配置

基础配置

推荐配置（100用户）

超过300用户配置

内存：4G

CPU：双核

硬盘：100G

内存：8G-16G

CPU：四核

硬盘：300G左右

内存：32

CPU：八核

硬盘：500G

注：初始硬盘可以设置为100G，后续根据需要扩容

​

操作系统

Debian、RedHat、CentOS6.0/7.4/7.5等64位Linux操作系统

浏览器

Google Chrome、Firefox、Edge、IE10等HTML5浏览器

（注：设计报表时不支持IE浏览器）

获取安装程序

https://pan.yunzhijia.com/s/MTI4OTQ1NCxmYmM4#/share/456854998823735297

​

根据不同的操作系统下载对应的安装包与应用更新包

将安装包拷贝至服务器目录：

/opt/maco_client_linux_x64_xxx.tar.gz

执行以下命令:

解压缩安装包

cd /opt

tar -zxvf maco_client_linux_x64_xxx.tar.gz

更换应用包

执行命令如下：

cd /opt/maco/maco.war

rm -rf *

cp /opt/maco_client.xxx.war .

unzip maco_client.xxx.war

修改端口号（可选）

默认为9090

当安装过程中，忘记修改端口号，可通过以下方式进行修改

/opt/maco/tomcat8/conf/server.xml

启动客户端（大约等待30秒）

启动客户端

cd /opt/maco

./run.sh

访问

在浏览器中输入： http://客户端服务器IP:端口

出现如下页面

​

点击上传许可证

将申请好的许可证上传即可进入登陆界面

​

---