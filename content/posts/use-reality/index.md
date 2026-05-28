+++
title = "利用 Reality 协议「漏洞」加速服务器"
date = 2026-05-26T01:14:52+08:00
draft = false
description = "说是「漏洞」有点过了，其实是 Reality 协议的特性，只是这个特性会带来使用风险。本文保留原来的玩法思路，按当前 Xray_bash_onekey 修正 serverNames 菜单和链接。"
slug = "use-reality"
featureimage = "/images/posts/use-reality/cover.avif"
categories = ["网络技术"]
tags = ["Xray", "Reality", "代理", "CDN"]
+++

说是"漏洞"有点过了，其实就是协议的一个特性——只不过这个特性玩不好的话会出事。具体风险看这篇：[**Xray Reality 协议的风险**](https://hey.run/posts/reality-xie-yi-de-feng-xian)。先回顾下这个特性吧，毕竟不是每次默写都能全对，对吧～

## Reality 协议风险回顾

如果 Target 域名套了 CDN，你的服务器就变成这个 CDN 的边缘 IP。其他人可以用你的服务器访问 CDN——相当于免费给别人加速，而流量从你账单上走。这种好人，咱不当。

为了解决这个问题，[**Xray Reality 协议的风险**](https://hey.run/posts/reality-xie-yi-de-feng-xian) 里的方案是：给 Reality 前面套个 Nginx，用 SNI 分流。只有那些匹配了域名的请求才能通过 Nginx 到达 Xray，不匹配的直接挡掉。

那么，问个问题测测你的智商：如果我设置 a 域名可以通过 Nginx，但 Xray 的 Target 却是套了 Cloudflare 的 b 域名，会发生什么？

倒计时 3...2...1...

## 利用"漏洞"加速服务器

答案是：**a 域名会被原封不动发给 Cloudflare 节点！** 如果你把 a 域名也套了 Cloudflare，那你的 Reality 服务器就完美充当了一个加速节点。是不是很妙😏

于是就有了下图：

![](/images/posts/use-reality/cover.avif)

美国的 Xray ws 服务器套了 Cloudflare，你访问香港的 Reality 服务器，利用 Reality 的转发特性，香港跳转到 Cloudflare 边缘，Cloudflare 再回源到美国的 ws 服务器——一条加速链路就形成了！

是不是很好玩～这可不只能加速你自己的服务器，什么 CDN、什么域名都行，只要你脑洞够大（好吧我现在就只想到这一个……）

## 如何设置

先用 [**Xray_bash_onekey**](https://github.com/hello-yunshu/Xray_bash_onekey) 装好 Reality，注意安装时要同时装 Nginx（搭配 Nginx 是必须的，原因上面说了）。然后在脚本里：

```text
12. 变更 Nginx serverNames 配置
```

或者直接：

```bash
idleleo --add-servernames
```

就这：

![](/images/posts/use-reality/02.avif)

创建新的 serverNames 文件：

![](/images/posts/use-reality/03.avif)

输入你要加速的域名就好啦～是不是超简单。

## 怎么用

以前大家说优选 IP，但优选 IP 这东西吧，不是时时都好使。这不正好，用 Reality 的特性给自己的 ws/gRPC/xHTTP 服务器加个速。

地址栏填 Reality 服务器 IP，Host 栏填你上面设置的加速域名：

![](/images/posts/use-reality/04.avif)

是不是没听懂？没关系，这个确实有点绕。但解释起来好麻烦的……所以我懒得解释啦！！！

反正知道好用就行，对吧～

## 还是要提醒一句

玩法有趣归有趣，别忘了这本质上是在利用 Reality 的回落/转发特性。玩可以，防护一定要上：Nginx serverNames 分流、Fail2ban、流量阻断，该配的全配上。不然一边加速，一边被别人薅——从"玩法"变"赔法"，那可太惨了。