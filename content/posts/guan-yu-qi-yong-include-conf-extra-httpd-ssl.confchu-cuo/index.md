+++
title = "关于：启用Include conf/extra/httpd-ssl.conf出错"
date = 2017-10-16T14:19:08+08:00
draft = false
description = "前几天在我把网址从http升级到https时，遇到了个棘手的问题。 首先是我的服务器，我的服务器是windows系统下的利用phpStudy搭建的。然后是ssl证书，我其实比较建议大家申请Let's Encrypt的ssl证书，大家也都知道沃通等颁发的证书多少让人不放心，而Let's Encrypt"
slug = "guan-yu-qi-yong-include-conf-extra-httpd-ssl.confchu-cuo"
featureimage = "/images/posts/guan-yu-qi-yong-include-conf-extra-httpd-ssl.confchu-cuo/cover.avif"
categories = ["教程"]
tags = ["Apache", "SSL", "phpStudy"]
+++
> 旧文归档：本文保留当时的操作思路，涉及的软件版本、系统界面、命令和下载链接可能已经变化；实际使用请以官方当前说明为准。

前几天在我把网址从http升级到https时，遇到了个棘手的问题。

首先是我的服务器，我的服务器是windows系统下的利用phpStudy搭建的。然后是ssl证书，我其实比较建议大家申请Let's Encrypt的ssl证书，大家也都知道沃通等颁发的证书多少让人不放心，而Let's Encrypt本身为了普及https加之免费，推荐。但是，虽然Let's Encrypt的证书极容易申请，可是适配出了大问题，Let's Encrypt似乎更加适合Linux系统下的服务器，虽然最后我放弃使用了，但感兴趣的小伙伴不妨一试。

这里我要说的是在阿里云上申请了ssl证书。阿里云申请证书相当简单，[具体教程](https://www.idleleo.com/2017/10/16/利用阿里云部署ssl证书/)可以查看我的博客。阿里云颁发的是赛门铁克签发的证书，颁发很简答，安装证书时，根据阿里云的要求：

> ##### ( 1 ) 在Apache的安装目录下创建cert目录，并且将下载的全部文件拷贝到cert目录中。如果申请证书时是自己创建的CSR文件，请将对应的私钥文件放到cert目录下并且命名为******.key；
> 
> ##### ( 2 ) 打开 apache 安装目录下 conf 目录中的 httpd.conf 文件，找到以下内容并去掉“#”：
[code] 
    #LoadModule ssl_module modules/mod_ssl.so (如果找不到请确认是否编译过 openssl 插件) #Include conf/extra/httpd-ssl.conf
[/code]

问题就在于这个Include conf/extra/httpd-ssl.conf，在Let's Encrypt的证书颁发之后，我曾尝试应用它，（Let's Encrypt证书的配置问题，博客中也有）但问题就在这个Include conf/extra/httpd-ssl.conf，利用阿里云颁发的证书问题一致——Apache服务无法启动。

那我们来看看httpd-ssl.conf是何方神圣。

以下是httpd-ssl.conf默认激活的代码：
[code] 
    Listen 443 
    SSLPassPhraseDialog builtin 
    SSLSessionCache "shmcb:/Apache24/logs/ssl_scache(512000)" 
    SSLSessionCacheTimeout 300 
    DocumentRoot "/Apache24/htdocs" 
    ServerName www.example.com:443 
    ServerAdmin admin@example.com 
    ErrorLog "/Apache24/logs/error.log" 
    TransferLog "/Apache24/logs/access.log" 
    SSLEngine on 
    SSLCipherSuite ALL:!ADH:!EXPORT56:RC4+RSA:+HIGH:+ 
    MEDIUM:+LOW:+SSLv2:+EXP:+eNULL 
    SSLCertificateFile "/Apache24/conf/server.crt" 
    SSLCertificateKeyFile "/Apache24/conf/server.key" 
     
    SSLOptions +StdEnvVars 
     
    SSLOptions +StdEnvVars BrowserMatch ".*MSIE.*"  
    nokeepalive ssl-unclean-shutdown  
    downgrade-1.0 force-response-1.0 
    CustomLog "/Apache24/logs/ssl_request.log"  
    "%t %h %{SSL_PROTOCOL}x %{SSL_CIPHER}x "%r" %b"
[/code]

其实不用我说你也可以发现了，它默认开启的代码明显是有很大的问题的，就比如Apache24目录，我的目录下根本不存在Apache24目录，还有www.example.com等等。。毫无疑问，若按阿里云建议修改httpd-ssl.conf：

![](/images/posts/guan-yu-qi-yong-include-conf-extra-httpd-ssl.confchu-cuo/cover.avif)

很容易产生误解。如果你直接复制黏贴进httpd-ssl.conf，Apache怎么可能不出问题。

故，解决方法其中之一，很简单，你把所有代码全部修改好，并将相关证书放在指定的目录下即可。

当然解决方法还有简单的，请参见：[Include conf/extra/httpd-ssl.conf出错简单解决方法](https://www.idleleo.com/10/167.html)。
