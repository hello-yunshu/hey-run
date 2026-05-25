+++
title = "永久免费的V2Ray? 利用Arukas简单搭建"
date = 2019-09-17T15:23:39+08:00
draft = true
description = "刚刚传来噩耗，Arukas将于2020年1月31日停止运行，2019年9月30日起停止注册！若想要免费搭建V2Ray可以见：免费畅用V2Ray一年？谷歌云$300试用金 若有后续反转笔者会第一时间更新文章，敬请大家关注无主界。 免费畅用V2Ray一年？谷歌云$300试用金"
slug = "yong-jiu-mian-fei-de-v2ray-li-yong-arukasjian-dan-da-jian"
featureimage = "https://cdn.idleleo.com/wp-content/uploads/2019/09/201909171439.jpg"
+++

**刚刚传来噩耗，Arukas将于2020年1月31日停止运行，2019年9月30日起停止注册！若想要免费搭建V2Ray可以见：**[**免费畅用V2Ray一年？谷歌云$300试用金**](<https://www.idleleo.com/09/3127.html>)

**若有后续反转笔者会第一时间更新文章，敬请大家关注无主界** 。

[**免费畅用V2Ray一年？谷歌云$300试用金**](<https://www.idleleo.com/09/3127.html>)

Arukas是一家日本的Docker提供商（现在已经凉凉）Arukas为所有注册者免费提供了0.1vCPU/128M内存/0.1TB流量的Docker，虽然配置简陋，但是对于搭建某些服务来说已经绰绰有余。于是乎这篇文便介绍了如何简单轻松的免费搭建V2Ray，免费翻墙使用VPN。

## 如何搭建

在以下官网完成注册：

[https://app.arukas.io](<https://app.arukas.io >)

注册时要求验证信用卡和手机号码，信用卡可以使用支付宝代替，注册不需要等待可以直接注册成功。注意，注册网址可能已经被屏蔽，需要自备梯子进行访问。

在Create App界面中创建新的Docker，注意需要填写的部分。

![](/images/wp-content/uploads/2019/09/201909171439.jpg)

其中Image栏填写`shynome/sakura-v2ray:0.0.3`这是来自[sakura-v2ray](<https://gitlab.com/shynome/sakura-v2ray>)的镜像。若不填写将直接无法运行。

在Servise Plan中选择Free，若选择其他需要额外的费用。

在Endpoint中填写英文或数字，这是一个二级域名，也是之后配置V2Ray中的服务器的地址，这非常重要，需要谨慎填写，不可有重复名称。若有重复名称下方会显示图中的This domain can not be used.

在Port中输入80，并且注意右侧选择tcp，若不填写会持续出现503错误。（感谢ceshi提醒）

其他部分均不用填写，若没有特殊要求可以直接点击下方Create APP运行了。

## 高级功能

sakura-v2ray的镜像提供了更改环境变量来一定程度的自定义V2Ray的功能。其中可以修改的环境变量有：

VMESS_ID = `8982bac0-e1fc-4c09-bea3-3a0e402fabd3`（默认值）

PROXY_PATH = `/ray`（默认值）

VMESS_ID为vmess id，PROXY_PATH为ws proxy path。建议安全起见进行更改两者值，但前提在于你需要了解相关配置。

![](/images/wp-content/uploads/2019/09/201909171438.jpg)

在配置下方的ENV中，选择Use ENV，并在下方输入你需要的环境变量即可。

## 如何使用

由于此V2Ray是利用镜像直接配置搭建的，因此相关设置不能进行太多的更改，下方已经给出了配置好的URL了。打开V2Ray客户端，选择从URL中导入V2Ray，复制下方地址即可导入配置。

这里有各平台的V2Ray客户端：[V2Ray 客户端下载](<https://www.idleleo.com/01/988.html>)
[code] 
    vmess://ew0KICAidiI6ICIyIiwNCiAgInBzIjogImFydWthcy5pbyB3cyIsDQogICJhZGQiOiAic3VpeWkuYXJ1a2FzY2xvdWQuaW8iLA0KICAicG9ydCI6ICI0NDMiLA0KICAiaWQiOiAiODk4MmJhYzAtZTFmYy00YzA5LWJlYTMtM2EwZTQwMmZhYmQzIiwNCiAgImFpZCI6ICI2NCIsDQogICJuZXQiOiAid3MiLA0KICAidHlwZSI6ICJub25lIiwNCiAgImhvc3QiOiAiIiwNCiAgInBhdGgiOiAiL3JheSIsDQogICJ0bHMiOiAidGxzIg0KfQ==
[/code]

**注意** 在导入后需要更改服务器地址，服务器地址便是刚刚笔者强调的Endpoint域名。更改完成后即可开心的免费翻墙啦！

## 注意事项

  1. 必须修改Endpoint，并且保证配置正确。
  2. 判断Docker是否创建成功，访问Endpoint看下，如果是`404`则创建成功了，`503`则是还在创建中。
  3. 若使用了环境变量，在配置中也需要更改相关的配置参数。
  4. 可以考虑使用CF等高级手法，但此免费Docker没有固定IP，若要实现“特殊”操作还是花钱去租VPS吧。
  5. [V2Ray / SSR 传输协议哪个好? (各种协议对比)](<https://www.idleleo.com/05/2071.html>)
  6. [V2RayGCon 简单使用教程](<https://www.idleleo.com/08/2912.html>)
  7. [iOS 各大 VPN(代理) 软件免费下载 – TestFlight](<https://www.idleleo.com/07/2614.html>)

## 等等？能套用CF？

经过笔者的研究，笔者发现若想要强行使用CF也不是没有办法。

上图中，在配置过程中有一个Custom Domain项，这可以理解为配置一个CNAME的自定义域名。类似无主界使用的CDN：i.idleleo.com。官网也说明了这个自定义域名的作用。

![](/images/wp-content/uploads/2019/09/201909171440.jpg)

So，如果你有自己的域名，并且你知道如何配置Cloudflare的中转，你可以套用CF了。注意， 在解析时需要把A解析改成CNAME解析，解析后的域名一定要开启SSL，否则会出现连接错误。 这里有简单的套用Cloudflare教程：[2020 搭建 V2Ray 服务器最新教程](<https://www.idleleo.com/10/2148.html>)。

这里笔者还是要多嘴一句，这个手段确实是能对源IP进行一定的伪装的（Cloudflare流弊！）实现原理很简单，这相当于给域名换了个马甲。但是需要注意的是，由于进行了多次跳转，可能会拖累运行和连接速度。
