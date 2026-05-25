+++
title = "搭建 Xray Reality 协议服务器"
date = 2026-05-26T01:14:52+08:00
draft = false
description = "最近脚本 Xray_bash_onekey 更新到了2.0，从这个版本开始，脚本就正式支持Reality啦！ Reality 介绍 Xray Reality协议是一种新兴的网络传输协议，它旨在提高网络传输的效率和安全性。以下是关于Reality协议的一些关键信息： 安全性提升：Reality协议通过"
slug = "da-jian-xray-reality-xie-yi-fu-wu-qi"
featureimage = "/images/image-dgib.png"
categories = ["网络技术"]
tags = ["Xray", "Reality", "服务器搭建", "代理"]
+++



最近脚本 **Xray_bash_onekey** 更新到了2.0，从这个版本开始，脚本就正式支持Reality啦！

## Reality 介绍

Xray Reality协议是一种新兴的网络传输协议，它旨在提高网络传输的效率和安全性。以下是关于Reality协议的一些关键信息：

  1. **安全性提升** ：Reality协议通过使用TLS加密来保护用户流量，并支持多种身份验证方式，以确保数据在传输过程中的安全性。如果用REALITY取代传统的TLS服务，可以消除服务端TLS指纹特征，同时保留前向保密性等功能，证书链攻击也无效，这样的安全性超越了常规的TLS。

  2. **便捷性** ：使用REALITY协议可以指向别人的网站，无需自己购买域名和配置TLS服务端，更为方便。同时，实现了向中间人呈现指定SNI的全程真实TLS。

  3. **代理用途** ：Reality协议通常用于代理目的，目标网站最低标准是支持TLSv1.3和H2的国外网站，域名非跳转使用（主域名可能被用于跳转到www）。

  4. **配置加分项** ：配置方面，禁止回国流量，并转发TCP/80和UDP/443等端口（Reality对外表现为端口转发，目标IP冷门或许更佳）。

  5. **不支持套CDN** ：Reality协议不支持套CDN。

  6. **与其他协议的集成** ：Reality协议将与其他协议，例如VLESS和Trojan集成，以提供更强大的代理功能。

  7. **新的功能和特性** ：Reality协议将扩展以支持新的功能和特性，例如负载均衡和多路径选择。

  8. **更广泛的应用** ：Reality协议将用于更广泛的应用，例如企业网络和物联网。

  9. **性能提升** ：启用Reality并且配置合适的XTLS Vision流控模式，可以达到数倍甚至十几倍的性能提升。

## 如何搭建

在脚本中，选择第三个：安装 Xray (Reality+ws/gRPC+Nginx)

![](/images/image-dgib.png)

根据说明，一步一步执行即可，输入必要的参数，其他直接回车即可，非常简单~

## 重要参数介绍

### Target域名

Target域名非常重要。Target域名是指在配置Reality协议时，用于伪装流量的目标域名。这个域名通常是国外的、支持TLSv1.3和HTTP/2的大厂域名，如Apple、Microsoft、Google等，它们被用来隐藏代理流量的真实目的地，使得流量看起来像是正常访问这些网站的数据。

所以，你需要先准备一个Target域名，下面是推荐的几个Target域名：

  1. **Apple相关域名** ：

     * `swdist.apple.com`

     * `swcdn.apple.com`

     * `updates.cdn-apple.com`

     * `mensura.cdn-apple.com`

     * `osxapps.itunes.apple.com`

     * `aod.itunes.apple.com`

  2. **Microsoft相关域名** ：

     * `www.microsoft.com`

     * `cdn-dynmedia-1.microsoft.com`

     * `update.microsoft`

     * `software.download.prss.microsoft.com`

  3. **Amazon相关域名** ：

     * `s0.awsstatic.com`

     * `d1.awsstatic.com`

     * `images-na.ssl-images-amazon.com`

     * `m.media-amazon.com`

     * `player.live-video.net`

  4. **Google相关域名** ：

     * `dl.google.com`

  5. **其他推荐的域名** ：

     * `gateway.icloud.com`

     * `itunes.apple.com`

     * `download-installer.cdn.mozilla.net`

     * `airbnb`（不同区域有不同的域名，建议自行搜索）

     * `addons.mozilla.org`

     * `www.lovelive-anime.jp`

**最好使用自己的Target域名** ，没有的话，可以试试上面的域名。除此以外，可以利用[**RealiTLScanner**](https://github.com/XTLS/RealiTLScanner)这个项目扫描服务器附近IP段的域名

#### 务必注意

Target域名不建议使用套用CF的域名，具体原因看这一篇：

### serverNames

简单说，serverNames是告诉服务器“我们想要连接到哪个域名”的一个参数，它在TLS握手过程中用于服务器身份验证和安全连接的建立

一般与Target域名保持一致即可，胡乱设置会导致连不上的喔👀

"]},"target":{"position":0,"lines":["

最近脚本 [**Xray_bash_onekey**](https://github.com/hello-yunshu/Xray_bash_onekey) 更新到了2.0，从这个版本开始，脚本就正式支持Reality啦！

## Reality 介绍

Xray Reality协议是一种新兴的网络传输协议，它旨在提高网络传输的效率和安全性。以下是关于Reality协议的一些关键信息：

  1. **安全性提升** ：Reality协议通过使用TLS加密来保护用户流量，并支持多种身份验证方式，以确保数据在传输过程中的安全性。如果用REALITY取代传统的TLS服务，可以消除服务端TLS指纹特征，同时保留前向保密性等功能，证书链攻击也无效，这样的安全性超越了常规的TLS。

  2. **便捷性** ：使用REALITY协议可以指向别人的网站，无需自己购买域名和配置TLS服务端，更为方便。同时，实现了向中间人呈现指定SNI的全程真实TLS。

  3. **代理用途** ：Reality协议通常用于代理目的，目标网站最低标准是支持TLSv1.3和H2的国外网站，域名非跳转使用（主域名可能被用于跳转到www）。

  4. **配置加分项** ：配置方面，禁止回国流量，并转发TCP/80和UDP/443等端口（Reality对外表现为端口转发，目标IP冷门或许更佳）。

  5. **不支持套CDN** ：Reality协议不支持套CDN。

  6. **与其他协议的集成** ：Reality协议将与其他协议，例如VLESS和Trojan集成，以提供更强大的代理功能。

  7. **新的功能和特性** ：Reality协议将扩展以支持新的功能和特性，例如负载均衡和多路径选择。

  8. **更广泛的应用** ：Reality协议将用于更广泛的应用，例如企业网络和物联网。

  9. **性能提升** ：启用Reality并且配置合适的XTLS Vision流控模式，可以达到数倍甚至十几倍的性能提升。

## 如何搭建

在脚本中，选择第三个：安装 Xray (Reality+ws/gRPC+Nginx)

![](/images/image-dgib.png)

根据说明，一步一步执行即可，输入必要的参数，其他直接回车即可，非常简单~

## 重要参数介绍

### Target域名

Target域名非常重要。Target域名是指在配置Reality协议时，用于伪装流量的目标域名。这个域名通常是国外的、支持TLSv1.3和HTTP/2的域名，如Apple、Microsoft、Google等，它们被用来隐藏代理流量的真实目的地，使得流量看起来像是正常访问这些网站的数据

所以，你需要先准备一个Target域名，下面是推荐的几个Target域名：

  1. **Apple相关域名** ：

     * `swdist.apple.com`

     * `swcdn.apple.com`

     * `updates.cdn-apple.com`

     * `mensura.cdn-apple.com`

     * `osxapps.itunes.apple.com`

     * `aod.itunes.apple.com`

  2. **Microsoft相关域名** ：

     * `www.microsoft.com`

     * `cdn-dynmedia-1.microsoft.com`

     * `update.microsoft`

     * `software.download.prss.microsoft.com`

  3. **Amazon相关域名** ：

     * `s0.awsstatic.com`

     * `d1.awsstatic.com`

     * `images-na.ssl-images-amazon.com`

     * `m.media-amazon.com`

     * `player.live-video.net`

  4. **Google相关域名** ：

     * `dl.google.com`

  5. **其他推荐的域名** ：

     * `gateway.icloud.com`

     * `itunes.apple.com`

     * `download-installer.cdn.mozilla.net`

     * `airbnb`（不同区域有不同的域名，建议自行搜索）

     * `addons.mozilla.org`

     * `www.lovelive-anime.jp`

当然，**最好是使用自己的Target域名** ，没有的话，可以试试上面的域名。除此以外，可以利用[**RealiTLScanner**](https://github.com/XTLS/RealiTLScanner)这个项目扫描服务器附近IP段的域名

#### 务必注意

Target域名不建议使用套用CloudFlare的域名，具体原因看这一篇：[**Xray Reality 协议的风险**](https://hey.run/archives/reality-xie-yi-de-feng-xian)

### serverNames

简单说，serverNames是告诉服务器“我们想要连接到哪个域名”的一个参数，它在TLS握手过程中用于服务器身份验证和安全连接的建立

一般与Target域名保持一致即可，胡乱设置会导致连不上的喔👀


