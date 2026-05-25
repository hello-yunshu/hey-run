+++
title = "利用 Reality 协议“漏洞”加速服务器"
date = 2026-05-26T01:14:52+08:00
draft = false
description = "说是“漏洞”有点过了，其实是协议的特性，只是这个特性会带来使用的风险。具体风险可见这篇文章：Xray Reality 协议的风险。还是先回顾下这个特性吧，毕竟你不是每次默写都全对是吧 Reality 协议风险回顾 如果Target域名是套用CDN的域名，会让你的服务器变成这个CDN的边缘IP。其他人"
slug = "use-reality"
featureimage = "/images/image-oirm.png"
categories = ["网络技术"]
tags = ["Xray", "Reality", "代理", "CDN"]
+++



说是“漏洞”有点过了，其实是协议的特性，只是这个特性会带来使用的风险。具体风险可见这篇文章：[**Xray Reality 协议的风险**](https://hey.run/archives/reality-xie-yi-de-feng-xian)。还是先回顾下这个特性吧，毕竟你不是每次默写都全对是吧

## Reality 协议风险回顾

如果Target域名是套用CDN的域名，会让你的服务器变成这个CDN的边缘IP。其他人可以用你的服务器访问CDN，充当了CDN加速的功能。

为了解决这个问题，在这篇文章：[**Xray Reality 协议的风险**](https://hey.run/archives/reality-xie-yi-de-feng-xian)**** 中，用Nginx来识别不同域名的sni进行分流。也就是只有设置好匹配的域名才能通过Nginx并访问Xray。

那么，问个问题测试下你的智商：如果我设置a域名可以通过Nginx，但Xray的Target却是套用Cloudflare的b域名，会发生什么呢？

倒计时3...2...1...

## 利用“漏洞”加速服务器

答案是：会把a域名原封不动发给Cloudflare节点。如果你的a域名也套了Cloudflare，那么此时，你的Reality服务器完美充当了一次加速节点！

所以，就有了如下图的例子：

![](/images/image-oirm.png)

在这个例子中，运行在美国的Xray ws协议服务器（也就是脚本的ws/gRPC安装模式）套用了Cloudflare加速。你访问在香港的Reality服务器，利用Reality的特性，香港服务器跳转到了Cloudflare的节点，并利用Cloudflare连接美国的ws协议服务器，从而完成加速！

是不是很好玩~~这可绝不仅能加速你的服务器，任何CDN，任何域名都可以，只要你想法💡多（反正我现在就只想到这个...）

## 如何设置

首先你要安装利用脚本 [**_Xray_bash_onekey_**](https://github.com/hello-yunshu/Xray_bash_onekey) 安装好了Reality，之后在安装时需要同时安装Nginx（具体可见：[**Xray Reality 协议的风险**](https://hey.run/archives/reality-xie-yi-de-feng-xian)）。然后选择脚本选项：10. 变更 Nginx serverNames 配置，如下👇

![](/images/image-tzer.png)

选择后，根据提示，选择：2 创建一个新的 serverNames 文件

![](/images/image-cxju.png)

输入你需要加速的域名就可以啦~是不是很简单😊

## 如何使用

最近Cloudflare不允许使用优选IP了，这不正好这利用Reality的特性加速下ws/gRPC服务器

只需要在地址栏里填写Reality服务器IP，在Host栏里添加你在上面设置的要加速的域名👇就可以啦~

![](/images/image-bmvn.png)

是不是没听懂，没关系，这有点理解难度。但解释起来好麻烦的，所以。。。我懒得解释啦！！！

但这不影响你喊🐂🍺，对吧，✌️

"]},"target":{"position":0,"lines":["

说是“漏洞”有点过了，其实是协议的特性，只是这个特性会带来使用的风险。具体风险可见这篇文章：[**Xray Reality 协议的风险**](https://hey.run/archives/reality-xie-yi-de-feng-xian)。还是先回顾下这个特性吧，毕竟你不是每次默写都全对是吧

## Reality 协议风险回顾

如果Target域名是套用CDN的域名，会让你的服务器变成这个CDN的边缘IP。其他人可以用你的服务器访问CDN，充当了CDN加速的功能

为了解决这个问题，在这篇文章：[**Xray Reality 协议的风险**](https://hey.run/archives/reality-xie-yi-de-feng-xian)**** 中，用Nginx来识别不同域名的sni进行分流。也就是只有设置好匹配的域名才能通过Nginx并访问Xray

那么，问个问题测试下你的智商：如果我设置a域名可以通过Nginx，但Xray的Target却是套用Cloudflare的b域名，会发生什么呢？

倒计时3...2...1...

## 利用“漏洞”加速服务器

答案是：会把a域名原封不动发给Cloudflare节点。如果你的a域名也套了Cloudflare，那么此时，你的Reality服务器完美充当了一次加速节点！

所以，就有了如下图的例子：

![](/images/1000001405.png)

在这个例子中，运行在美国的Xray ws协议服务器（也就是脚本的ws/gRPC安装模式）套用了Cloudflare加速。你访问在香港的Reality服务器，利用Reality的特性，香港服务器跳转到了Cloudflare的节点，并利用Cloudflare连接美国的ws协议服务器，从而完成加速！

是不是很好玩~~这可绝不仅能加速你的服务器，任何CDN，任何域名都可以，只要你想法💡多（反正我现在就只想到这个...）

## 如何设置

利用脚本 [**Xray_bash_onekey**](https://github.com/hello-yunshu/Xray_bash_onekey) 安装Reality，在安装时需要同时安装Nginx（具体可见：[**Xray Reality 协议的风险**](https://hey.run/archives/reality-xie-yi-de-feng-xian)）。然后选择脚本选项：10. 变更 Nginx serverNames 配置，如下👇

![](/images/image-tzer.png)

选择后，根据提示，选择：2 创建一个新的 serverNames 文件

![](/images/image-cxju.png)

输入你需要加速的域名就可以啦~是不是很简单😊

## 如何使用

最近Cloudflare不允许使用优选IP了，这不正好这利用Reality的特性加速下ws/gRPC服务器

只需要在地址栏里填写Reality服务器IP，在Host栏里添加你在上面设置的要加速的域名👇就可以啦~

![](/images/image-bmvn.png)

是不是没听懂，没关系，这有点理解难度。但解释起来好麻烦的，所以。。。我懒得解释啦！！！

但这不影响你喊🐂🍺，对吧，✌️


