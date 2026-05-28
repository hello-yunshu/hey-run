+++
title = "国内网络启用 IPv6 方法及注意事项"
date = 2019-07-15T22:26:49+08:00
draft = true
description = "由于我国没有IPv4根服务器，因此在IPv6大发展的今天，IPv6是我国下一代互联网技术重中之重的一部分。虽然IPv6在国内进行的如火如荼，甚至已经出现了IPv6的根服务器，但是对于我们个人而言，要使用IPv6网络依然不切实际。姑且看现在大型网络公司，除去苹果强制要求外，很少有公司主动对IPv6进行"
slug = "guo-nei-wang-luo-qi-yong-ipv6-fang-fa-ji-zhu-yi-shi-xiang"
featureimage = "/images/shared/201907151015.avif"
+++

由于我国没有IPv4根服务器，因此在IPv6大发展的今天，IPv6是我国下一代互联网技术重中之重的一部分。虽然IPv6在国内进行的如火如荼，甚至已经出现了IPv6的根服务器，但是对于我们个人而言，要使用IPv6网络依然不切实际。姑且看现在大型网络公司，除去苹果强制要求外，很少有公司主动对IPv6进行适配。一方面，IPv6的需求普遍较低，IPv4资源并没有像之前担心的一般这么快干涸；另一方面IPv6技术并不成熟，企业部署需要花费不低的成本，利益驱动的企业现阶段很难去主动适配IPv6。

![](/images/shared/201907151015.avif)

对于像笔者兼站长这样的个人开发者。IPv6技术就是另外一回事了。对于笔者而言，这更像是一种兴趣，就是会浪费时间甚至浪费钱的兴趣咯（真惨。。）。在之前的文章：[一些功能性 iOS 描述文件](https://www.idleleo.com/03/1726.html)中，笔者说明了iOS如何强制开启运营商的IPv6地址。经过笔者测试，中国三大运营商已经有足够的能力使用IPv6技术了，只是现在使用环境依旧不佳，因此经常被人淡忘。不过相信5G技术普及，物联网快速发展，情况会大有变化。

回到主题，这次笔者就说明一些国内主机诸如：阿里云、腾讯云、华为云开启IPv6的方法，当然普通电脑用户也完全可以开启IPv6，只不过需要一些其他的技术手段 才行。本文主要以Windows系统为主。

## 使用HE的tunnelbroker开启IPv6

此开启方法为IPv6中间技术之一的IPv6隧道技术。由于现今免费方法有限，笔者推荐使用此免费方法。

首先进入[tunnelbroker官网](https://www.tunnelbroker.net/)注册一个账户，登陆后，点击左侧的 Create Regular Tunnel 。

在IPv4 Endpoint (Your side)填你VPS的公网IP地址，是的，**你必须有个公网固定的IP** ，在Available Tunnel Servers选一个隧道接入服务器，选择亚洲的几个接入点都可以，这样速度会快一点，建议选择香港，点击Create Tunnel添加完成。

![](/images/posts/guo-nei-wang-luo-qi-yong-ipv6-fang-fa-ji-zhu-yi-shi-xiang/01.avif)

在Example Configurateions里选择你的操作系统，这里以Windows 10为例。选择后会出现配置方法，HE给出的命令如下，整个拷贝到服务器的终端命令行，在Windows中便是CMD(需要管理员权限)。

![](/images/posts/guo-nei-wang-luo-qi-yong-ipv6-fang-fa-ji-zhu-yi-shi-xiang/02.avif)

在图中红色圈中的地方便是你的IPv6地址。如果你有域名的话，在域名中加入AAAA值便可以访问IPv6地址了。根据笔者测试，由于隧道服务器不在国内的原因，访问延迟很大，甚至会出现中断的情况，因此并不推荐在生产环境使用。

**值得注意，在Windows 10部分版本配置中，需要手动设定IPv6的DNS地址，具体DNS地址是多少以及怎么修改可以查看我的另一篇文章。** 详见：[IPv6 国内外优秀DNS推荐](https://www.idleleo.com/07/2654.html)。

以上是对于VPS或者云服务器的用户而言的，对于一般用户而言由于没有固定的IP地址就相对困难的多了。不过如果你利用一些固定IP方法如花生壳之类，自然也是可以实现IPv6访问的。若是你使用的是DDNS，理论可是现实，但实际情况估计很难。

若要删除建立的IPv6隧道或者提示有重名可以使用以下命令：

`netsh interface ipv6 delete interface ip6tunnel`

`netsh interface ipv6 reset all`

## 使用6Plat 46模块开启IPv6

这是咱们中国自己的服务。6Plat来头很大，是[下一代互联网工程国家中心（CFIEC）](http://www.cfiec.net/)的“产物”。也就那个部署了中国第一台IPv6的协会，他们制作了一个超前体验IPv6的手段。

![](/images/posts/guo-nei-wang-luo-qi-yong-ipv6-fang-fa-ji-zhu-yi-shi-xiang/03.avif)

6Plat的46模块采用开源软件OpenVPN搭建，通过客户端与服务端建立隧道，并通过隧道为客户端分配IPv6地址，获取IPv6 DNS的方式，使客户端远程接入IPv6网络；客户端所有IPv6数据由服务端代为转发。也就是说，就是开一个VPN代理IPv6的流量。

想法很简单，对于用户而言使用起来也很方便，具体怎么操作这里便不再详细叙述，若有需求可见[文章](http://bbs2.6plat.org/d/19)。

本方法非常适合个人普通用户，至于希望固定IPv6地址的，这个显然是不行的。笔者在这里说一句，因为IPv6发展迅速，因此此服务存在随时废弃的风险，所以只要体验体验便好，运用在生产环境中还是算了吧。

## 阿里云开启IPv6的方法

除去以上那些无偿服务，那肯定还有有偿服务嘛！

对于国内几大云服务商，自然有他们IPv6的方案。比如阿里云有“IPv6 解决方案”也就是做IPv4/IPv6双栈，直接给你一个IPv6地址和专有网络。现在可以去[直接申请测试](https://www.aliyun.com/solution/ip/index)，现阶段免费，但只支持呼和浩特以及深圳两地。相信其他地区也会相继开放，不过还没有明确的时间点。

![](/images/posts/guo-nei-wang-luo-qi-yong-ipv6-fang-fa-ji-zhu-yi-shi-xiang/04.avif)

当然阿里云提供IPv6转换服务，这个价格就有点感人了，如果不是企业需求的话，相信很少有人会需要这类的服务的吧。

说了这么多，其实是笔者突发奇想：如果在纯IPv6环境下怎么访问无主界呢？才有了上述的教程。笔者现在并不推荐使用IPv6，若你可以直接得到国内的IPv6地址还好说，但像是前面提到的两种方法**实际体验不佳** ，而在正常情况下主机又会自动优先使用IPv6地址，这样反而得不偿失。诚然对于真正纯IPv6的用户来说，服务器适配IPv6是很有价值，可这样的用户又有多少呢？
