+++
title = "搭建 Xray Reality 协议服务器"
date = 2026-05-26T01:14:52+08:00
draft = false
description = "Xray_bash_onekey 从 2.0 开始正式支持 Reality，现在脚本的 Reality 模式也已经变成 Reality+ws/gRPC/xHTTP+Nginx。本文保留原来的教程语气，按当前脚本重新修正菜单和链接。"
slug = "da-jian-xray-reality-xie-yi-fu-wu-qi"
featureimage = "/images/posts/da-jian-xray-reality-xie-yi-fu-wu-qi/cover.avif"
categories = ["网络技术"]
tags = ["Xray", "Reality", "服务器搭建", "代理"]
+++

最近脚本 [**Xray_bash_onekey**](https://github.com/hello-yunshu/Xray_bash_onekey) 更新后，Reality 已经不是当年那个「咦这是什么好新鲜」的小玩具了。现在 Reality、ws、gRPC、xHTTP、Nginx 全塞在同一个安装流程里，选项多得眼花缭乱。这篇帮你理一理，别到时候参数填错了还以为是玄学——玄学不背这锅喔～

## Reality 介绍

Xray Reality 协议，说白了就是让代理流量看起来像正常访问别人的网站。关键信息整理一下：

  1. **安全性**：消除 TLS 指纹特征，证书链攻击无效，比常规 TLS 更像样。

  2. **省事**：可以指向别人的网站，不用自己买域名配 TLS。对中间人来说，全程都是真实 TLS。

  3. **代理专用**：目标网站最低得是国外的、支持 TLSv1.3 和 H2，域名不要搞跳转那种。

  4. **小心机**：禁止回国流量，转发 TCP/80 和 UDP/443。Reality 对外就是端口转发，目标 IP 冷门点更佳。

  5. **CDN 不能乱套**：Target 域名乱选会出事，下面会细说。

  6. **性能**：配上 XTLS Vision 流控，表现不错。

## 如何搭建

运行脚本：

```bash
bash <(curl -fsSL https://raw.githubusercontent.com/hello-yunshu/Xray_bash_onekey/main/install.sh)
```

选择第三个：

```text
3. 安装 Xray (Reality+ws/gRPC/xHTTP+Nginx)
```

![](/images/posts/da-jian-xray-reality-xie-yi-fu-wu-qi/cover.avif)

接下来一步一步走就行，该填的填，不想改的直接回车。真的很简单～

装完之后如果忘了自己填了啥：

```bash
idleleo --show
```

不要问我为什么要记参数。你当然可以不记，但以后排查问题的时候，你会对着屏幕沉默，而屏幕也会沉默地看着你。那种沉默，比尴尬还尴尬。

## 重要参数

### Target 域名

Target 域名就是 Reality 用来伪装的目标——流量看起来像在访问这个域名。通常是国外的、支持 TLSv1.3/H2 的大站，比如 Apple、Microsoft、Google 那些。

推荐几个，拿去用：

  1. **Apple 系**

     * `swdist.apple.com`
     * `swcdn.apple.com`
     * `updates.cdn-apple.com`
     * `mensura.cdn-apple.com`
     * `osxapps.itunes.apple.com`
     * `aod.itunes.apple.com`

  2. **Microsoft 系**

     * `www.microsoft.com`
     * `cdn-dynmedia-1.microsoft.com`
     * `update.microsoft`
     * `software.download.prss.microsoft.com`

  3. **Amazon 系**

     * `s0.awsstatic.com`
     * `d1.awsstatic.com`
     * `images-na.ssl-images-amazon.com`
     * `m.media-amazon.com`
     * `player.live-video.net`

  4. **Google 系**

     * `dl.google.com`

  5. **其他**

     * `gateway.icloud.com`
     * `itunes.apple.com`
     * `download-installer.cdn.mozilla.net`
     * `airbnb`（不同区域域名不同，自己搜）
     * `addons.mozilla.org`
     * `www.lovelive-anime.jp`

当然，**最好用你自己的 Target 域名**。没有的话用上面的也行。还可以用 [**RealiTLScanner**](https://github.com/XTLS/RealiTLScanner) 扫一下服务器附近 IP 段有什么好域名——这个工具是个小天使。

#### 务必注意

**Target 域名不要用套了 Cloudflare 的。** 原因看这篇：[**Xray Reality 协议的风险**](https://hey.run/posts/reality-xie-yi-de-feng-xian)。

不是吓唬你。设错了，你的服务器会被别人拿去薅流量——羊毛长在你账单上，那画风可不美。

### serverNames

serverNames 就是 TLS 握手时告诉服务器「我要连哪个域名」的参数。

大多数情况跟 Target 域名保持一致就行。乱填就等着连不上吧～

以后要改的话：

```text
12. 变更 Nginx serverNames 配置
```

或者：

```bash
idleleo --add-servernames
```

## 写在最后

Reality 很强，但不是「开了就无敌」那种强。第一次搭建议全用默认值，等确认能稳定跑了，再去折腾 Nginx 分流、负载均衡、流量阻断这些进阶操作。

先走通，再跑快。别还没学会走路就想着飞～
