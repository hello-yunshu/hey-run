+++
title = "替代V2Ray？- Trojan搭建教程"
date = 2020-02-01T17:40:00+08:00
draft = true
description = "写在前面 1、Trojan的设计类似于V2Ray+ws+tls，他更多的是解决了一个伪装问题，不要对高峰拥堵的线路抱有幻想，不提倡暴力发包，不要做”吵闹的邻居”，够用即可，近期考虑写一篇两者对比文章 2、BBR是很好的，配合Trojan一起使用，自行安装。至于Trojan效果如何，和你的线路品质有较"
slug = "ti-dai-v2ray---trojanda-jian-jiao-cheng"
featureimage = "/images/posts/ti-dai-v2ray---trojanda-jian-jiao-cheng/cover.png"
+++

#### 写在前面

1、Trojan的设计类似于V2Ray+ws+tls，他更多的是解决了一个伪装问题，不要对高峰拥堵的线路抱有幻想，不提倡暴力发包，不要做”吵闹的邻居”，够用即可，近期考虑写一篇两者对比文章

2、BBR是很好的，配合Trojan一起使用，自行安装。至于Trojan效果如何，和你的线路品质有较大关系，影响因素也挺多，自行体验吧

#### 关于一键脚本

1、系统支持centos7+/debian9+/ubuntu16+

2、域名解析到VPS并生效

3、脚本自动续签https证书

4、自动配置伪装网站，位于/usr/share/nginx/html/目录下，可自行替换其中内容

5、请不要在任何生产环境使用一键脚本，此条适用于本站所有脚本，专门用来科学上网的VPS可以随意使用

#### 教程步骤综述

1、申请一个域名，这里我们用免费域名演示

2、一键脚本安装服务端

3、客户端配置+chrome插件配置

#### 教程开始

1、申请免费域名，freenom.com

你应该申请了域名并绑定VPS IP，这里演示域名为：91hub.ga

2、一键脚本安装服务端

连接VPS，执行这条命令，直接回车，开始安装。
[code] 
    curl -O https://raw.githubusercontent.com/atrandys/trojan/master/trojan_mult.sh && chmod +x trojan_mult.sh && ./trojan_mult.sh
[/code]

安装过程中需要输入

1、你申请的域名：例如91hub.ga

2、密钥密码：随意设置一个5位密码，需要输入4次，此密码

3、验证密码：自行设置，客户端配置文件中的密码需要

如下图[](/images/posts/ti-dai-v2ray---trojanda-jian-jiao-cheng/cover.png)

![](/images/posts/ti-dai-v2ray---trojanda-jian-jiao-cheng/cover.png)

输入完成，等待安装完成即可，服务端就搭建完成了。

若需要启用BBR加速可见于：[加速网络 一键部署BBR+BBR魔改+Lotsever(锐速)](https://www.idleleo.com/05/2125.html)

3、客户端配置

这里我们演示Windows客户端使用，首先下载客户端。

**安装完成脚本后会显示下载地址** ，如果你忘记下载了，那么进入/usr/share/nginx/html/目录下，找到一个乱码文件夹，进入会看到客户端文件，使用sftp下载下来即可。 

直接下载客户端：[Trojan.zip](https://github.com/atrandys/trojan/releases/download/1.0.0/trojan.zip)

下载后，解压得到trojan文件夹，打开文件夹，编辑config.json，修改其中的域名和验证密码（安装服务端时设置的验证密码）。[](/images/posts/ti-dai-v2ray---trojanda-jian-jiao-cheng/01.png)

![](/images/posts/ti-dai-v2ray---trojanda-jian-jiao-cheng/01.png)

用ftp连接VPS，下载/usr/src/trojan/private.crt，存放到trojan客户端的文件夹。[](/images/posts/ti-dai-v2ray---trojanda-jian-jiao-cheng/02.avif)

![](/images/posts/ti-dai-v2ray---trojanda-jian-jiao-cheng/02.avif)

然后，运行start.bat，开启Trojan服务，Trojan会监听本地1080端口。然后下载switchomega。

下载插件：[switchyomega](https://github.com/atrandys/trojan/releases/download/1.0.0/SwitchyOmega_Chromium.crx)

安装插件，打开chrome，打开扩展程序，将下载的插件拖动到扩展程序页面，添加到扩展。[](/images/posts/ti-dai-v2ray---trojanda-jian-jiao-cheng/03.avif)

![](/images/posts/ti-dai-v2ray---trojanda-jian-jiao-cheng/03.avif)

完成添加，会跳转到switchyomega页面，点跳过教程，然后点击proxy，如图填写，最后点击应用选项。[](/images/posts/ti-dai-v2ray---trojanda-jian-jiao-cheng/08.avif)

![](/images/posts/ti-dai-v2ray---trojanda-jian-jiao-cheng/04.avif)

然后进入auto switch，删除最上方两条规则，然后点击添加规则列表。[](/images/posts/ti-dai-v2ray---trojanda-jian-jiao-cheng/09.avif)

![](/images/posts/ti-dai-v2ray---trojanda-jian-jiao-cheng/05.avif)

然后，在规则列表规则中，情景模式改为proxy，规则列表网站复制下面的网址，然后点击立即更新情景模式，保存即可。

https://raw.githubusercontent.com/atrandys/proV/master/gfwlist.txt[](/images/posts/ti-dai-v2ray---trojanda-jian-jiao-cheng/06.avif)

![](/images/posts/ti-dai-v2ray---trojanda-jian-jiao-cheng/06.avif)

点击chrome右上角switchyomega图标，选择auto switch模式即可。[](/images/posts/ti-dai-v2ray---trojanda-jian-jiao-cheng/07.avif)

![](/images/posts/ti-dai-v2ray---trojanda-jian-jiao-cheng/07.avif)

之后你便可以自由上网，教程到此结束。

#### 电脑上其他软件如何使用Trojan

1、如果软件支持配置socks5，直接指向127.0.0.1:1080即可。

2、如果软件不支持配置socks5，可选择sstap/sockscap64/supercap等软件，曲线实现代理。

#### 常见问题总结

1、Trojan客户端打开无法运行，提示缺少找不到vcruntime140.dll或找不到msvcp140.dll

原因缺少运行库，[点击下载链接](https://www.idleleo.com/05/2175.html)中的两个软件，一个是32位一个是64位，请全部安装即可。

2、如果遇到vcruntime140_1的错误，下载下面的文件放到C:windowssystem32目录下即可

[点击下载140_1.dll](https://github.com/atrandys/trojan/raw/master/vcruntime140_1.dll)

3、Trojan服务端怎么修改密码

Trojan服务端配置文件路径如下，如需修改内容，修改以下文件即可。
[code] 
    /usr/src/trojan/server.conf
[/code]

修改完成后，重启trojan服务端即可，同时客户端的密码也要同步修改哦。
[code] 
    systemctl restart trojan
[/code]

4、关于申请证书没有成果的处理

出现这个问题最可能的原因之一是你的同一个域名多次申请证书，导致let's encrypt官方的限制，同一域名每周最多5次申请。

如果你的同一个域名申请了很多此证书，这个处理方法可能有用：更换二级域名，例如原来使用的域名是www.abc.com或abc.com或xyz.abc.com，那么现在你添加一个二级域名解析例如xxx.abc.com，安装时使用这个域名即可。

#### 相关阅读推荐

Trojan与V2Ray对比：[V2Ray / Trojan 传输方式哪个好？(原理对比)](https://www.idleleo.com/02/4064.html)

如何部署V2ray：[2020 搭建 V2Ray 最新教程](https://www.idleleo.com/10/2148.html)
