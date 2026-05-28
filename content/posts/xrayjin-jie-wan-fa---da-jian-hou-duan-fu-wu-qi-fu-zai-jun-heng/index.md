+++
title = "XRay进阶玩法 - 搭建后端服务器负载均衡"
date = 2026-05-26T03:18:00+08:00
draft = false
description = "Xray_bash_onekey 的后端负载均衡已经不再只围绕 ws/gRPC，现在 ws、gRPC、xHTTP 都可以进入 Nginx upstream 管理。本文按当前脚本重新整理主服务器、后端服务器、协议选择、权重和注意事项。"
slug = "xrayjin-jie-wan-fa---da-jian-hou-duan-fu-wu-qi-fu-zai-jun-heng"
featureimage = "/images/posts/xrayjin-jie-wan-fa---da-jian-hou-duan-fu-wu-qi-fu-zai-jun-heng/cover.avif"
categories = ["网络技术"]
tags = ["Xray", "负载均衡", "Nginx", "代理"]
+++

后端负载均衡这个功能在脚本里活了很久了，但 [**Xray_bash_onekey**](https://github.com/hello-yunshu/Xray_bash_onekey) 已经不是当年那个只会说「ws ONLY」的小可爱了。ws、gRPC、xHTTP —— 三种协议现在都能进 Nginx upstream 管理，旧教程里那套说法早就该扔进垃圾桶啦。

先泼一盆水让你冷静一下：**负载均衡不是叠加带宽，也不是一个下载任务变多线下载。** 它更像一个聪明的前台小姐姐，有客人来了就看看后面哪台机器比较闲，把你领过去。多人同时用的时候效果明显，一个人用？那就省省吧～一台就够了。

## 现在支持哪些协议

当前脚本的 Nginx upstream 管理四分类：

  1. ws → `.wsServers`
  2. gRPC → `.grpcServers`
  3. xHTTP → `.xhttpServers`
  4. Reality 负载均衡 → `.realityServers`

![](/images/posts/xrayjin-jie-wan-fa---da-jian-hou-duan-fu-wu-qi-fu-zai-jun-heng/01.avif)

这篇说的是普通后端的玩法——ws/gRPC/xHTTP 被 Nginx 转发到后端服务器那种。Reality 负载均衡是另一个话题，想看那边去：[**如何部署 Reality协议 服务端负载均衡**](https://hey.run/posts/bushu-reality-balance)。

## 准备工作

最少两台 VPS，再多也不嫌多嘛（只要钱包不哭）：

  1. 主 VPS：负责接客、TLS/Nginx、upstream 转发。这是门面，别拿 1 核小鸡糊弄。
  2. 后端 VPS：只跑 ws/gRPC/xHTTP ONLY 或者 Reality 附加的简单协议，低调地在后面扛活。

**强烈建议同一区域、同一内网。** 跨地区的后端看起来很帅是吧？实际你会发现：客户端连过来，每个后端响应时间都不一样，快的等慢的，体验反而不如一台高性能单机。

如果云厂商给了内网，用内网 IP 通信。后端端口不要暴露给全世界——那是给自己找麻烦喔。

## 主服务器怎么搭

在主服务器上运行脚本：

```bash
bash <(curl -fsSL https://raw.githubusercontent.com/hello-yunshu/Xray_bash_onekey/main/install.sh)
```

TLS 前置的话选：

```text
安装 Xray (Nginx+ws/gRPC/xHTTP+TLS)
```

传输协议选 ws、gRPC、xHTTP 或者 `ws+gRPC+xHTTP` 全都要。装完记得记下这些——**别跳过，后面后端要一模一样**：

  1. UUID 或 UUID 映射字符串
  2. ws path / gRPC serviceName / xHTTP path
  3. 对应协议的端口
  4. 域名和证书状态

主服务器一个 path，后端另一个 path，然后怪 Nginx 不干活——这种事我见太多了，别当主角嘛。

## 后端服务器怎么搭

后端选这个：

```text
安装 Xray (ws/gRPC/xHTTP ONLY)
```

这个模式给你的是纯协议入站，没有 TLS，就是给主服务器当后端小兵用的。安装时协议要和主服务器一致：UUID 一样、path/serviceName 一样。端口建议用高位的，比如 `10000+`，然后防火墙只放行主服务器的内网 IP。

如果你用 gRPC，后端 serviceName 和主服务器一致；xHTTP 的话 path 带 `/`；ws 也一样。

## 添加到主服务器

回到主服务器：

```bash
idleleo --add-upstream
```

脚本会问你要管哪个协议的负载均衡——ws、gRPC 还是 xHTTP。

![](/images/shared/xray-backend-load-balancing-inline.avif)

创建后端文件时填：

  1. host：后端 IP，优先内网。
  2. port：后端协议端口。
  3. weight：权重，越大被翻牌概率越高。

主服务器自己默认权重 `50`。后端机器性能好的调大点，线路一般的调小点。1 核小鸡权重拉满，然后问「为什么忽快忽慢」——你说呢？

## 什么时候适合用

适合的场景：

  1. 多用户同时在用，一台机器的带宽或 CPU 扛不住。
  2. 同一区域有好几台闲置 VPS。
  3. 想隐藏后端 IP，只暴露主服务器给客户端。

不太适合：

  1. 就你一个人用。
  2. 后端分布在不同国家地区，延迟参差不齐。
  3. 你指望单连接带宽直接翻倍——别想啦，不是合体。

**负载均衡是分摊请求，不是叠加强化。** 这句话值得你再读一遍。理解错了后面一定会踩坑，而且踩了还来找我哭。

## 最后絮叨

后端服务器一定配合防火墙，只让主服务器访问后端端口。主服务器可以装 Fail2ban、开流量阻断、设 GeoData 自动更新。

现在脚本入口很统一，`idleleo` 一个命令进去啥都有。功能多了以后最重要的不是每个都开，是**知道自己开了什么**。乱开一堆然后忘了，三个月后排查问题，那场面，光是想想就刺激呢～
