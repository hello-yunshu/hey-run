+++
title = "启用Include conf/extra/httpd-ssl.conf出错的简单解决方法"
date = 2017-10-16T14:56:17+08:00
draft = false
description = "之前一篇文章提及了关于启用Include conf/extra/httpd-ssl.conf出错的问题，相信大家有一个感性的认识，其实问题很简答，很多时候，服务器不运行了，显然是你搞砸了。 好了，闲话话少说，我们就来说一下启用Include conf/extra/httpd-ssl.conf出错的简"
slug = "qi-yong-include-conf-extra-httpd-ssl.confchu-cuo-de-jian-dan-jie-jue-fang-fa"
featureimage = "/images/posts/qi-yong-include-conf-extra-httpd-ssl.confchu-cuo-de-jian-dan-jie-jue-fang-fa/cover.avif"
categories = ["教程"]
tags = ["Apache", "SSL", "phpStudy"]
+++
> 旧文归档：本文保留当时的操作思路，涉及的软件版本、系统界面、命令和下载链接可能已经变化；实际使用请以官方当前说明为准。

之前一篇文章提及了关于启用Include conf/extra/httpd-ssl.conf出错的问题，相信大家有一个感性的认识，其实问题很简答，很多时候，服务器不运行了，显然是你搞砸了。

好了，闲话话少说，我们就来说一下启用Include conf/extra/httpd-ssl.conf出错的简单解决方法。

首先，你需要申请ssl证书，若不会申请，可以参考我的相关文章。**（以下文章主要介绍是以阿里云申请的赛门铁克ssl证书为例）**

然后，你还没开启openssl等操作，那请你移步到关于ssl部署之前工作的文章。

在做好准备工作后，打开 Apache 安装目录下 conf 目录中的 httpd.conf 文件，定位到 Include conf/vhosts.conf 这条，在这条之后添加：Include conf/vhostssl.conf 代码，其实不必是vhostssl.conf，其他亦可，但方便起见，都按照此标准，添加后的效果：

![](/images/posts/qi-yong-include-conf-extra-httpd-ssl.confchu-cuo-de-jian-dan-jie-jue-fang-fa/cover.avif)

之后，在Apache 安装目录下 conf 文件夹中创建vhostssl.conf文件。可以直接复制vhost.conf文件并另存为vhostssl.conf，删除文件中所有代码，添加如下所有内容:
[code] 
    Listen 443 
    DocumentRoot "C:****"//需要修改 
    ServerName www.idleleo.com//需要修改 
    ServerAlias idleleo.com//需要修改 
    SSLEngine on 
    SSLProtocol all -SSLv2 -SSLv3//按照提供商要求修改！ 
    SSLHonorCipherOrder on SSLCipherSuite *********//按照提供商要求修改！ 
    SSLCertificateFile "C:*******certpublic.pem"//需要修改 
    SSLCertificateKeyFile "C:*******cert******.key"//需要修改 
    SSLCertificateChainFile "C:********certchain.pem"//需要修改 
    //需要修改 
    Options +Indexes +FollowSymLinks +ExecCGI 
    AllowOverride All 
    Order allow,deny 
    Allow from all 
    Require all granted
    
[/code]

需要修改处已经标出，修改方式参照vhost.conf文件中的代码。修改完后，重启Apache即可。

大功告成！

![](/images/posts/qi-yong-include-conf-extra-httpd-ssl.confchu-cuo-de-jian-dan-jie-jue-fang-fa/01.avif)
