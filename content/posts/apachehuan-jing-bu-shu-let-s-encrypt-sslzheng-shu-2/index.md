+++
title = "Apache环境部署Let’s Encrypt SSL证书 2"
date = 2019-03-10T22:16:04+08:00
draft = false
description = "在站长（笔者）建站之初，Let’s Encrypt证书的使用率并不高。当时笔者在寻找合适的SSL证书时，发现了这个免费的证书。可惜由于Let’s Encrypt证书的部署环境并不能很好的兼容Apache，再加上笔者当时对SSL证书理解不够透彻。因而没有选择使用Let’s Encrypt证书。 具体可"
slug = "apachehuan-jing-bu-shu-let-s-encrypt-sslzheng-shu-2"
featureimage = "/images/posts/apachehuan-jing-bu-shu-let-s-encrypt-sslzheng-shu-2/cover.avif"
categories = ["网络技术"]
tags = ["Apache", "SSL", "Let's Encrypt", "证书"]
+++
> 旧文归档：本文记录的是当时用 win-acme 申请 Let's Encrypt 证书的流程。win-acme 版本、菜单、验证方式和证书导出选项可能已经变化，实际部署请以 win-acme 当前文档为准。

在站长（笔者）建站之初，Let’s Encrypt证书的使用率并不高。当时笔者在寻找合适的SSL证书时，发现了这个免费的证书。可惜由于Let’s Encrypt证书的部署环境并不能很好的兼容Apache，再加上笔者当时对SSL证书理解不够透彻。因而没有选择使用Let’s Encrypt证书。

具体可见：<https://www.idleleo.com/11/413.html>

后来笔者使用了大部分云服务商会提供的免费证书作SSL。方便快捷，但经过笔者对SSL理解越发透彻，逐步发现了免费证书的弊端。

其中，最大的弊端在于免费证书几乎都为RSA证书，此类证书虽兼容性好，但密钥长度长，导致网站加载时间变长。还有一种最新形式的证书ECC，采用椭圆加密算法，这类证书兼容性尚可，但密钥长度较之RSA要短的多的多。

本着不将就的态度，站长也就是笔者开始着手部署ECC证书，其环境依然是Apache。于是这篇文章便诞生了。

## win-acme 简介

适用于Windows的简单ACME客户端 - 用于Let’s Encrypt。（以前称为letsencrypt-win-simple（LEWS）） 

GitHub地址：**[win-acme](https://github.com/PKISharp/win-acme)**

其拥有以下优势：

  * 一个简单的CLI界面，用于请求，安装和更新IIS的证书
  * 其他应用程序的高级CLI选项
  * 运行计划任务以自动续订证书和更新应用程序
  * 支持通配符证书，OCSP Must Staple和ECDSHA密钥
  * 通过SFTP / FTPS，WebDav，acme-dns，Azure等进行高级验证
  * 支持从命令行完全无人值守的操作
  * 通过操纵.json文件支持其他形式的自动化
  * 使用.NET构建自己的插件，使程序完全按照您的意愿执行

## win-acme 使用（Apache）

此教程主要针对大部分国内服务器，如果你使用的是Azure或者dreamhost主机，可是直接使用相应的一键解析功能，在此不再赘述。

从GitHub上下载当时的最新版（笔者以win-acme.v2.0.3.210为例）。注：当前版本请以项目发布页为准，升级前请多阅读社区信息。

运行wacs.exe

![](/images/posts/apachehuan-jing-bu-shu-let-s-encrypt-sslzheng-shu-2/cover.avif)

输入`M`，进入申请SSL证书过程。

![](/images/posts/apachehuan-jing-bu-shu-let-s-encrypt-sslzheng-shu-2/01.avif)

再按照提示，输入`1`开始手动创建SSL证书。之后会弹出申请SSL证书的域名列表或单个域名。注意，域名可以为`*.idleleo.com`类型的泛域名，注意泛域名证书只能通过DNS验证，不支持HTTP验证方式。虽然域名可以输入很多，但不建议输入过多。根据证书规范，最多可输入100个域名。每个域名通过半角`,`分隔。笔者在此输入`*.idleleo.com,idleleo.com`。

![](/images/posts/apachehuan-jing-bu-shu-let-s-encrypt-sslzheng-shu-2/02.avif)

确认回车后，出现DNS解析设置。是的没错，此证书是基于DNS解析的。为拓展应用场景，笔者这里选择手动设置DNS解析。及输入`2`。

之后需要选择笔者之前所说的ECC或者RSA证书。可以按照实际需求选择。笔者在这里选择ECC。

来到第三步，选择证书格式。这里是Apache环境的教程，因此选择证书`.pem`文件，也就是输入`3`。再输入储存文件的地址即可，在这里，笔者导出至`D:`目录下。

![](/images/posts/apachehuan-jing-bu-shu-let-s-encrypt-sslzheng-shu-2/03.avif)

![](/images/posts/apachehuan-jing-bu-shu-let-s-encrypt-sslzheng-shu-2/04.avif)

新版中需要输入`3`后再输入`1`跳过不需要的步骤。来到域名的解析环节。

![](/images/posts/apachehuan-jing-bu-shu-let-s-encrypt-sslzheng-shu-2/05.avif)

进入域名解析商的操作界面。根据下图，依次对应为：主机记录、记录类型、记录值。输入后确定解析即可。  

![](/images/posts/apachehuan-jing-bu-shu-let-s-encrypt-sslzheng-shu-2/06.avif)

![](/images/posts/apachehuan-jing-bu-shu-let-s-encrypt-sslzheng-shu-2/07.avif)

![](/images/posts/apachehuan-jing-bu-shu-let-s-encrypt-sslzheng-shu-2/08.avif)

在新版中，程序会要求验证后再把解析记录删除。完成后，经过再次验证，便会得到两个`.pem`文件，一个文件名中带有...chain..字样，此为证书链文件。另一个文件带有...key..字样，此为密钥文件。将带有key的文件重命名为`.key`文件。将其放入Apache文件下。记录其文件路径。

在Apache的SSL配置中，修改：
[code] 
    SSLCertificateFile "C:********.pem"  //pem文件路径
    SSLCertificateKeyFile "C:********.key"  //key文件路径
[/code]

大功告成！

注意：若需要启用双证书，个别网上教程有误。本文不再维护当前最新步骤，实际操作请查看 win-acme 和 Web 服务器的当前文档。

## win-acme 下载

GitHub地址：**[win-acme](https://github.com/PKISharp/win-acme)**

最新版本：<https://github.com/PKISharp/win-acme/releases>
