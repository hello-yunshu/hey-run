+++
title = "浏览器开发工具中加入聊天室 - Console.chat"
date = 2019-06-16T15:41:45+08:00
draft = true
description = "在网上找到一些介绍一些特殊、趣味性十足（mei shen me luan yong）的小工具吧！如果你是网站开发者，一定知道浏览器都会内建“开发人员工具”，也就是闲着没事按一下F12跳出来的东西，例如最常用的是检查打开网页时载入那些图片、CSS或JS，这也可用于了解网站是否有被拖慢速度的问题，还能点"
slug = "liu-lan-qi-kai-fa-gong-ju-zhong-jia-ru-liao-tian-shi-console-chat"
featureimage = "/images/posts/liu-lan-qi-kai-fa-gong-ju-zhong-jia-ru-liao-tian-shi-console-chat/cover.avif"
+++

![](/images/posts/liu-lan-qi-kai-fa-gong-ju-zhong-jia-ru-liao-tian-shi-console-chat/cover.avif)

在网上找到一些介绍一些特殊、趣味性十足（mei shen me luan yong）的小工具吧！如果你是网站开发者，一定知道浏览器都会内建“开发人员工具”，也就是闲着没事按一下F12跳出来的东西，例如最常用的是检查打开网页时载入那些图片、CSS或JS，这也可用于了解网站是否有被拖慢速度的问题，还能点选网页中的元件，快速查看相关代码、CSS 等资讯，非常好用！当然开发人员工具功能不少，这只是其中几项，那还有没有其他的应用方式呢？

本文要介绍的“Console.chat”非常有意思，利用一段 JavaScript 程式码将聊天室放进开发人员工具里，就能直接在浏览器的控制台（Console）在全世界进行文字对话，听起来好像没什么用，实际上也真的没什么用，利用指令功能文字聊天似乎已经是上个时代的事了。

在网站里插入一段 Console.chat 的 JavaScript 就能完成，功能不多，只有设定昵称、传送讯息和讯息变色三种功能，之后回来可以看到其他人留下的对话纪录，能正常显示中文，如果想研究一下 Console.chat 是如何做到也能从 GitHub 页面找到完整的原始码。

网站名称：Console.chat

网站链结：<https://console.chat/>

## 使用教学

### STEP 1

开启 Console.chat 网站会有简单介绍，下方有一段 JavaScript 程式码可以让你将控制台聊天室功能放入任何网页，不过在此之前，可直接从 Console.chat 网站进行测试。

![](/images/posts/liu-lan-qi-kai-fa-gong-ju-zhong-jia-ru-liao-tian-shi-console-chat/01.avif)

### STEP 2

打开浏览器的“开发人员工具”点选“Console”会随即看到介绍，要启动聊天室功能必须先输入一段指令：`cc()` ，再输入一次 `cc()` 就能停止载入聊天室讯息。

![](/images/posts/liu-lan-qi-kai-fa-gong-ju-zhong-jia-ru-liao-tian-shi-console-chat/02.avif)

### STEP 3

开启 Console 聊天室，可能一开始不知道要如何使用，输入 `help()` 指令会有简单教学。

`username(“your username”)` 设定你的昵称。

`send(“your message”)` 传送你输入的讯息。

`send(“your message”,”254cf5")` 输入色码可改变讯息颜色。

![](/images/posts/liu-lan-qi-kai-fa-gong-ju-zhong-jia-ru-liao-tian-shi-console-chat/03.avif)

### STEP 4

实际测试一下 Console.chat 确实可以设定昵称。

![](/images/posts/liu-lan-qi-kai-fa-gong-ju-zhong-jia-ru-liao-tian-shi-console-chat/04.avif)

设定后就能传送讯息，如果讯息中带有链结，会在传送出去后自动转为超链接。

Console.chat 本身有防止讯息洗版的设计，无法连续传送相同讯息，会跳出错误提示。

![](/images/posts/liu-lan-qi-kai-fa-gong-ju-zhong-jia-ru-liao-tian-shi-console-chat/05.avif)

若要关闭聊天室，只要把网页关闭，或是输入 `cc()` 即可结束对话，浏览器就不会继续载入更多讯息，目前没有更多的功能，如果对原始码有兴趣可以前往Console.chat 的 GitHub 页面，能找到更多开发相关资讯。

## 值得一试的三个理由

以 JavaScript 程式码在开发人员工具加入聊天功能。

纯文字聊天模式，可设定昵称、讯息颜色。

可查看过往的聊天纪录。
