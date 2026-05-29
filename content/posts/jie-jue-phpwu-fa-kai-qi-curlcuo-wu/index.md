+++
title = "解决PHP无法开启cURL错误"
date = 2019-10-22T21:12:15+08:00
draft = false
description = "最近笔者收到一条朋友发来的错误消息。原来，这位朋友发现PHP的cURL功能没有开启。在这之前，笔者并未有注意过cURL异常。笔者让这位朋友使用phpinfo()函数查看后，发现只有cURL Sterling Hughes这一条相关的配置。 <"
slug = "jie-jue-phpwu-fa-kai-qi-curlcuo-wu"
featureimage = "/images/posts/jie-jue-phpwu-fa-kai-qi-curlcuo-wu/cover.avif"
categories = ["教程"]
tags = ["PHP", "cURL", "故障排查"]
+++
> 旧文归档：本文记录的是旧 Windows/PHP 环境下 cURL 扩展无法开启的处理。PHP 7.4 以后 OpenSSL 相关 DLL 命名和加载方式已有变化，排查时请先看当前 PHP 版本的 `phpinfo()`、错误日志和扩展目录。

最近笔者收到一条朋友发来的错误消息。原来，这位朋友发现PHP的cURL功能没有开启。在这之前，笔者并未有注意过cURL异常。笔者让这位朋友使用`phpinfo()`函数查看后，发现只有`cURL Sterling Hughes`这一条相关的配置。

![](/images/posts/jie-jue-phpwu-fa-kai-qi-curlcuo-wu/cover.avif)

经过研究发现，此错误出现以及解决有一定的条件。出错的PHP环境为：Windows、Apache。函数cURL是一个非常简单的打开外部链接的函数，对于很多开发者来说，此函数十分重要。朋友也很着急，那么如何解决呢？

首先，需要确定PHP有无正确编译cURL，若在`phpinfo()`函数运行的结果中出现了上述的`cURL Sterling Hughes`字段，则说明已经完成了编译。

其次，查看`php.ini`文件中是否成功配置了`extension=curl`以及`extension_dir=`选项，前者确保开启了cURL功能，后者确定了cURL动态文件所在的具体位置。

![](/images/posts/jie-jue-phpwu-fa-kai-qi-curlcuo-wu/01.avif)

在确认上述没问题的情况下。笔者提出的解决办法（也是笔者自己发现的**最简单的办法** ）在Apache配置文件`httpd.conf`中加入以下代码：

`LoadFile "C:/xxxphp-pathxxx/libssh2.dll"`

其中`xxxphp-pathxxx`为PHP程序文件的根目录。

也可以试试网友提出的其他几种办法：

  1. 直接替换他人编译好后的php_curl.dll文件。
  2. 将主要的php文件夹添加到Windows中的`Path/Env`变量中（使libeay32.dll和ssleay32.dll文件可访问；也可以将两个文件复制到`Windows/System32`文件夹内，但此办法较为麻烦不能一劳永逸）。
  3. 在Windows中将`Apache/bin`文件夹添加到`Path/Env`变量中。
  4. 将文件libssh2.dll从PHP文件夹复制到Apache的bin文件夹（Apache似乎需要此文件才能使PHP的curl在Windows中工作）。

![](/images/posts/jie-jue-phpwu-fa-kai-qi-curlcuo-wu/02.avif)

在当时环境中，重启 Apache 后问题已经解决。今天遇到类似问题时，请结合当前 PHP 版本继续核对依赖库名称和加载路径。

更多新奇网络功能、资源，可以持续关注 [无主界](https://www.idleleo.com) 喔~
