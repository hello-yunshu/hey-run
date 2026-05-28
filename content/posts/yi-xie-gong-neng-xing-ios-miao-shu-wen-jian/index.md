+++
title = "一些功能性 iOS 描述文件"
date = 2019-03-21T22:46:48+08:00
draft = true
description = "之前笔者给大家带来过最新的iOS 12的阻止更新描述文件。描述文件如果你使用iPhone时间久的话或多或少会注意到。诸如iOS的开发者预览版、网络模式切换、控制参数调整等多个特殊功能。 现在笔者给大家带来的是另外两个功能性的iOS描述文件。 开启iOS IPv6 描述文件 IPv6是英文“Inter"
slug = "yi-xie-gong-neng-xing-ios-miao-shu-wen-jian"
featureimage = "/images/posts/yi-xie-gong-neng-xing-ios-miao-shu-wen-jian/cover.avif"
+++

之前笔者给大家带来过[最新的iOS 12的阻止更新描述文件](https://www.idleleo.com/02/1260.html)。描述文件如果你使用iPhone时间久的话或多或少会注意到。诸如iOS的开发者预览版、网络模式切换、控制参数调整等多个特殊功能。

现在笔者给大家带来的是另外两个功能性的iOS描述文件。

## 开启iOS IPv6 描述文件

> IPv6是英文“Internet Protocol Version 6”（互联网协议第6版）的缩写，是互联网工程任务组（IETF）设计的用于替代IPv4的下一代IP协议，其地址数量号称可以为全世界的每一粒沙子编上一个地址。  
> 由于IPv4最大的问题在于网络地址资源有限，严重制约了互联网的应用和发展。IPv6的使用，不仅能解决网络地址资源数量的问题，而且也解决了多种接入设备连入互联网的障碍。  
> 互联网数字分配机构（IANA）在2016年已向国际互联网工程任务组（IETF）提出建议，要求新制定的国际互联网标准只支持IPv6，不再兼容IPv4。 

IPv6是未来的网络标准，但毕竟没有普及。那为什么iOS需要IPv6呢？因为大家知道中国的特殊国情。而某些高校为了保证网络安全，针对网络的封锁大家心知肚明。再者某些宽带公司因为利益的原因，并不会封配IPv4的地址给用户。这使得用户访问网络资源的能力大为减弱。

![](/images/posts/yi-xie-gong-neng-xing-ios-miao-shu-wen-jian/cover.avif)

而IPv6由于地址之多，完全没有IPv4的烦恼。因此，开启IPv6能有更好的上网体验，就现在情况来说。这几个描述文件便是强制开启运营商的IPv6地址的工具。

### 下载

中国移动：[使用Safari打开点击](https://d.idleleo.com/IPv6%20Support%20for%20CMCC.mobileconfig)

中国联通：[使用Safari打开点击](https://d.idleleo.com/IPv6%20Support%20for%20CU.mobileconfig)

中国电信：[使用Safari打开点击](https://d.idleleo.com/IPv6%20Support%20for%20CT.mobileconfig)  

## 开启 iOS TLS 1.3 描述文件

对于https协议，需要经过几次往返才能成功的连接。也就是说，在访问带有https字样的地址时（有个小锁），会因为加密的原因而减少访问速度。之前的协议主要是TLS 1.2，对于使用TLS 1.2，需要两次往返才能完成TLS handshake。使用1.3时，它只需要一次往返， 从而将加密延迟减少一半。这有助于这些加密连接感觉比以前更快一点。

![](/images/posts/yi-xie-gong-neng-xing-ios-miao-shu-wen-jian/01.avif)

所以如果网站支持TLS 1.3、浏览器也支持TLS 1.3，访问网站的速度会大大的加快。现今TLS 1.3的正式协议已经在去年正式的发布。部分网站也成功的开启了新的协议。现在无主界也在之前第一时间支持到了TLS 1.3。

![](/images/posts/yi-xie-gong-neng-xing-ios-miao-shu-wen-jian/02.avif)

对于浏览器，使用Chrome 63，可以为传出连接启用TLS 1.3。Chrome 56中添加了对TLS 1.3的支持，Chrome for Android也支持。

Firefox 52及更高版本（包括Quantum）默认启用TLS 1.3。他们保留了对TLS 1.2的不安全后备，直到他们更多地了解服务器容忍度和1.3 handshake。

而iOS使用的Safari其实也在iOS12中对TLS 1.3提供了支持。但是由于苹果公司的策略。 TLS 1.3默认并不启用，这时候就需要安装描述文件了。

### 下载

点击安装：[使用Safari打开点击](https://d.idleleo.com/enable_tls13.mobileconfig)
