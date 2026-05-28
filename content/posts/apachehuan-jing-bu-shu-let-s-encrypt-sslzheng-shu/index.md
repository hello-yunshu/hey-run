+++
title = "Apache环境部署Let's Encrypt ssl证书"
date = 2017-11-23T22:32:27+08:00
draft = true
description = "在关于：启用Include conf/extra/httpd-ssl.conf出错的文章中，我提到了关于Let's Encrypt证书的部署问题。Let's Encrypt是不错的证书，把它用于http升级为https是不错的选择。 经过我的研究发现，Let's Encrypt的证书更加适合Linu"
slug = "apachehuan-jing-bu-shu-let-s-encrypt-sslzheng-shu"
featureimage = "/images/posts/apachehuan-jing-bu-shu-let-s-encrypt-sslzheng-shu/cover.avif"
+++

在关于：启用Include conf/extra/httpd-ssl.conf出错的文章中，我提到了关于Let's Encrypt证书的部署问题。Let's Encrypt是不错的证书，把它用于http升级为https是不错的选择。

经过我的研究发现，Let's Encrypt的证书更加适合Linux而不是Windows。不过毕竟Windows可视化且方便，而这次就是在Windows下的apache部署Let's Encrypt的问题。

实话说，Let's Encrypt是个坑，我折腾了好多次，还是不成功，主要的原因在于签发的CA十分拉跨，很容易直接宕机没法签发，再加上如果是服务器验证又必须开放80端口不得占用，比较繁琐。而且Let's Encrypt自动的DNS验证对于国内的域名解析网站并不友好。因此，使用Windows的小伙伴可以直接无视Let's Encrypt证书。免费的证书一大把，百度一下有一堆，一年签一次，并不困难。

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
