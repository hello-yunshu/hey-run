+++
title = "Apache环境部署Let's Encrypt ssl证书"
date = 2017-11-23T22:32:27+08:00
draft = false
description = "在关于：启用Include conf/extra/httpd-ssl.conf出错的文章中，我提到了关于Let's Encrypt证书的部署问题。Let's Encrypt是不错的证书，把它用于http升级为https是不错的选择。 经过我的研究发现，Let's Encrypt的证书更加适合Linu"
slug = "apachehuan-jing-bu-shu-let-s-encrypt-sslzheng-shu"
featureimage = "/images/posts/apachehuan-jing-bu-shu-let-s-encrypt-sslzheng-shu/cover.avif"
categories = ["网络技术"]
tags = ["Apache", "SSL", "Let's Encrypt", "Windows"]
+++
> 旧文归档：本文写于早期 Windows/Apache 环境下折腾 Let's Encrypt 的阶段。现在 ACME 客户端、DNS 验证和证书生态已经成熟很多，下面的吐槽和步骤更适合作为旧记录，不宜当成当前部署建议。

在关于：启用Include conf/extra/httpd-ssl.conf出错的文章中，我提到了关于Let's Encrypt证书的部署问题。Let's Encrypt是不错的证书，把它用于http升级为https是不错的选择。

经过我的研究发现，Let's Encrypt的证书更加适合Linux而不是Windows。不过毕竟Windows可视化且方便，而这次就是在Windows下的apache部署Let's Encrypt的问题。

实话说，当时我折腾 Let's Encrypt 很不顺手，主要卡在 ACME 客户端、80 端口验证和国内 DNS 自动验证支持上。这个判断带有很强的时间背景：现在 Let's Encrypt 和各类 ACME 客户端已经成熟很多，Windows 用户也不必因为本文的旧经验直接放弃它。

如果你坚持要用，那么，首先，很明显你需要一个Let's Encrypt的证书，关于证书的如何得到，可以看我的另一篇文章：~~如何获得Let's Encrypt的证书~~ 。

然后，找到证书的地址，几下地址。

之后，如同我：关于：启用Include conf/extra/httpd-ssl.conf出错的简单解决方法 这篇文章一般，做好前期的准备工作，及创造一个vhostssl.conf文件，并且将其连接到httpd.conf 文件中。

![](/images/posts/apachehuan-jing-bu-shu-let-s-encrypt-sslzheng-shu/cover.avif)

其他操作完全类似此篇文章，只是vhostssl.conf中的代码改成如下：
[code] 
    ServerAdmin **@idleleo.com
    ServerName www.idleleo.com
    RewriteEngine On 
    # Redirect to the HTTPS site
    RewriteCond %{HTTPS} off
    RewriteRule ^/?(.*)$ https://www.idleleo.com/$1 [NE,L,R=301]
    ServerAdmin **@idleleo.com
    ServerName www.idleleo.com
    RewriteEngine On 
    # Redirect to the correct domain name
    RewriteCond %{HTTP_HOST} !^www.idleleo.com$ [NC]
    RewriteRule ^/?(.*)$ https://www.idleleo.com/$1 [NE,L,R=301]
    Listen 443 
    DocumentRoot "C:***********"
    ServerName www.idleleo.com
    ServerAlias idleleo.com
    SSLCipherSuite ECDHE-ECDSA-AES256-GCM-SHA384:ECDHE-RSA-AES256-GCM-SHA384:ECDHE-ECDSA-AES128-GCM-SHA256:ECDHE-RSA-AES128-GCM-SHA256:ECDHE-ECDSA-CHACHA20-POLY1305:ECDHE-RSA-CHACHA20-POLY1305:ECDHE-ECDSA-AES256-CCM8:ECDHE-ECDSA-AES256-CCM:ECDHE-ECDSA-ARIA256-GCM-SHA384:ECDHE-ECDSA-AES128-CCM8:ECDHE-ECDSA-AES128-CCM:ECDHE-ECDSA-ARIA128-GCM-SHA256:ECDHE-ECDSA-AES256-SHA384
    SSLCipherSuite TLSv1.3 TLS_AES_128_GCM_SHA256:TLS_CHACHA20_POLY1305_SHA256:TLS_AES_256_GCM_SHA384:TLS_AES_128_CCM_8_SHA256:TLS_AES_128_CCM_SHA256
    SSLProxyCipherSuite ECDHE-ECDSA-AES256-GCM-SHA384:ECDHE-RSA-AES256-GCM-SHA384:ECDHE-ECDSA-AES128-GCM-SHA256:ECDHE-RSA-AES128-GCM-SHA256:ECDHE-ECDSA-CHACHA20-POLY1305:ECDHE-RSA-CHACHA20-POLY1305:ECDHE-ECDSA-AES256-CCM8:ECDHE-ECDSA-AES256-CCM:ECDHE-ECDSA-ARIA256-GCM-SHA384:ECDHE-ECDSA-AES128-CCM8:ECDHE-ECDSA-AES128-CCM:ECDHE-ECDSA-ARIA128-GCM-SHA256:ECDHE-ECDSA-AES256-SHA384
    SSLProxyCipherSuite TLSv1.3 TLS_AES_128_GCM_SHA256:TLS_CHACHA20_POLY1305_SHA256:TLS_AES_256_GCM_SHA384:TLS_AES_128_CCM_8_SHA256:TLS_AES_128_CCM_SHA256
    SSLHonorCipherOrder on
    SSLProtocol -All +TLSv1.2 +TLSv1.3
    SSLCertificateFile "C:********.pem"
    SSLCertificateKeyFile "C:********.pemy"
    SSLCertificateChainFile "C:********.pem"
[/code]

上述代码很明显，[www.idleleo.com](http://www.idleleo.com)需要修改，以及证书的地址需要修改。上述代码考虑到安全问题只允许使用TLS1.2与TLS1.3。以上方法肯定是行得通的，如果有问题，请仔细检查各个环节。

实际上，上述代码不仅仅是适用于Let's Encrypt证书，现在你能得到的各个证书应该均支持，欢迎尝试。
