+++
title = "Xray进阶玩法 - 使用 xHTTP 协议"
date = 2026-05-26T02:20:00+08:00
draft = false
description = "Xray_bash_onekey 现在已经支持 xHTTP 协议了。和 ws、gRPC 一样，xHTTP 可以在 TLS 模式、Reality 附加协议以及 ONLY 后端模式中使用，也可以和 ws、gRPC 一起启用。它不是万能钥匙，但在客户端支持到位的情况下，确实又多了一条可以尝试的路。"
slug = "xray-xhttp-mode"
featureimage = "/images/posts/xray-xhttp-mode/cover.avif"
categories = ["网络技术"]
tags = ["Xray", "xHTTP", "代理", "VLESS"]
+++

Xray_bash_onekey 最近加入了 xHTTP 协议。是的，继 ws、gRPC 之后，又多了一个可以选的传输方式。协议越来越多，选择困难症也越来越严重——恭喜大家，快乐又增加了。😏

不过话先说清楚，xHTTP 不是来掀桌子的，不是要把 ws 和 gRPC 踹出门外。它更像是给不同的网络环境多留一条路：能用就试试，合适就留着，不合适就退回去。代理这事儿吧，有时候道理没用，最终还是你那条线路说了算。

## xHTTP 是什么

不扯名词了。xHTTP 就是 Xray 里一个新的 HTTP 系传输方式，和 ws、gRPC 一样，属于 VLESS 外面再包的一层。用途就是适配不同网络、不同前置、不同客户端。

在脚本里，xHTTP 已经被妥妥收进了原来的 ws/gRPC 选择流程。装 TLS 可以选、装 Reality 附加协议可以选、甚至单独装个 xHTTP ONLY 当后端也可以。

![](/images/posts/xray-xhttp-mode/01.avif)

更懒的话，直接选 `ws+gRPC+xHTTP` 同时启用。脚本会分别生成对应端口、路径、分享链接和二维码。好处是一个服务器上多放几条路，客户端支持哪个用哪个；坏处嘛——配置看起来会很热闹，别把自己看晕就行。

## 如何安装

用脚本 [**Xray_bash_onekey**](https://github.com/hello-yunshu/Xray_bash_onekey) 正常装就行。

主菜单里 xHTTP 已经是正经选项了，不是什么藏在角落里的实验品：

![](/images/posts/xray-xhttp-mode/02.avif)

全新安装，选传输协议时能看到：

```text
1: ws
2: gRPC
3: xHTTP
4: ws+gRPC+xHTTP
```

实际界面大概长这样：

![](/images/posts/xray-xhttp-mode/03.avif)

试试水就选 `3`，想多留几条路就选 `4`。脚本会接着问你 xHTTP 的端口和伪装路径——不知道怎么填就回车，默认值通常比你的临场发挥靠谱。

装完后脚本输出 xHTTP 的 VLESS 分享链接和二维码。**注意：xHTTP 的 path 在客户端要带 `/`**，脚本输出也会提醒。别学 gRPC 那个 serviceName——两个不是一种东西，搞混了就连不上，连不上就会来找我。

## 客户端支持

这里必须泼一盆冷水：**不是所有客户端都认 xHTTP。**

脚本已经做了提示——Clash 目前不支持，所以 Clash 配置里会跳过 xHTTP。ws/gRPC 有 Clash 配置，xHTTP 没有，不是脚本偷懒，是客户端那边还没接上。

如果你用的客户端支持 xHTTP，直接导入分享链接；如果导进去发现识别不了，先别怀疑人生，看看客户端版本和内核是不是真支持。

## 什么时候适合用

如果你现在 ws 舒服、gRPC 延迟也不错，那 xHTTP 未必能带来什么天翻地覆的变化。它更适合：

  1. 同一台服务器想多准备一种传输方式，方便切换。
  2. ws 或 gRPC 在某些网络下表现拉胯，想换条路试试。
  3. 做后端负载均衡时，希望后端协议选择更灵活。
  4. 单纯手痒——看到新协议不试一下浑身难受。

最后一个理由也是理由，折腾本来就是这种工具的核心乐趣，不丢人。

## 一点提醒

xHTTP 已经被脚本接入到安装、配置修改、用户管理、分享链接、状态输出里了。但「服务端显示安装成功」不等于「客户端能用」。一定要真的连一下，看看能不能稳定访问。

另外，如果你选了 `ws+gRPC+xHTTP` 同时启用，建议把每个协议的端口、路径、客户端支持情况记清楚。配置多不是问题——问题是三天后忘了自己当初填了什么，然后对着服务器进入沉默冥想状态。

总之，xHTTP 让 Xray_bash_onekey 的玩法又丰富了一点。它不是「必须换」的协议，是「值得试」的协议。至于在你这好不好用——挂上去跑两天，答案就有了。
