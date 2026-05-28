+++
title = "Xray进阶玩法 - 使用 gRPC 协议"
date = 2026-05-26T03:10:00+08:00
draft = false
description = "gRPC 早就不是 Xray_bash_onekey 里的新鲜玩意了，现在它已经和 ws、xHTTP 一起进入同一套安装、分享链接、用户管理和负载均衡流程。本文按当前脚本重新说明 gRPC 的使用方式、serviceName 注意点、CDN 设置以及和 xHTTP 的取舍。"
slug = "xrayjin-jie-wan-fa---shi-yong-grpcxie-yi"
featureimage = "/images/posts/xrayjin-jie-wan-fa---shi-yong-grpcxie-yi/cover.avif"
categories = ["网络技术"]
tags = ["Xray", "gRPC", "代理", "CDN"]
+++

gRPC 刚进 Xray 那会儿确实像个「新玩具」，人人都想上去摸两把。现在回头一看，它已经是 [**Xray_bash_onekey**](https://github.com/hello-yunshu/Xray_bash_onekey) 里的老面孔了嘛——单独选也行，和 ws、xHTTP 一起开也行，低调地住在菜单第 2 号位。

所以这篇不搞 2021 年那种「快来尝鲜」的口吻了。现在该问的是：在当前脚本里，gRPC 怎么选，跟 ws/xHTTP 到底啥区别，以及——哪些地方最容易手滑填错。

![](/images/posts/xrayjin-jie-wan-fa---shi-yong-grpcxie-yi/cover.avif)

## gRPC 是什么

基于 HTTP/2，多路复用、头部压缩、双向流——这些都是 HTTP/2 系的能力。放到 Xray 里，可以先粗暴理解为「另一种走 HTTP/2 风格的传输方式」。不玄乎。

它不一定比 ws 快，也不一定比 xHTTP 好。快不快最终看你那条线路给不给面子——客户端、CDN、运营商、服务器位置，哪个不是变量呢？**别把协议当玄学神器，能稳定跑的才是好协议。**

## 怎么装

现在脚本入口统一，装就完事：

```bash
bash <(curl -fsSL https://raw.githubusercontent.com/hello-yunshu/Xray_bash_onekey/main/install.sh)
```

装 TLS、Reality 附加协议、或者 ws/gRPC/xHTTP ONLY 后端的时候，都会看到这个选择：

```text
1: ws
2: gRPC
3: xHTTP
4: ws+gRPC+xHTTP
```

单走 gRPC 就 `2`。想给客户端多备几条路就 `4`——脚本会同时生成 ws、gRPC、xHTTP 的端口、路径、分享链接和二维码，一次给你配齐。

## serviceName 别画蛇添足

gRPC 最容易翻车的地方：`serviceName`。

ws 和 xHTTP 像正常 URL 路径，要带 `/`。但 gRPC 的 `serviceName` **不要 `/`**！脚本输出是 `grpcdemo`，客户端就填 `grpcdemo`。你自作主张加个 `/grpcdemo`？恭喜，连不上。

![](/images/posts/xrayjin-jie-wan-fa---shi-yong-grpcxie-yi/01.avif)

这个小细节，错了就真的不通。每次有人说「我配置完全一样就是不通」，我心里都先默念：你是不是多打了一个 `/`？

## 负载均衡

现在 Nginx 负载均衡支持 ws、gRPC、xHTTP 三种协议。在主服务器上：

```bash
idleleo --add-upstream
```

然后选 gRPC。它对应的后端文件是 `.grpcServers`，后端服务器需要相同 UUID、相同 serviceName、开放对应的 gRPC 端口。详细看：[**XRay进阶玩法 - 搭建后端服务器负载均衡**](https://hey.run/posts/xrayjin-jie-wan-fa---da-jian-hou-duan-fu-wu-qi-fu-zai-jun-heng)。

![](/images/shared/xray-backend-load-balancing-inline.avif)

## CDN 别忘开开关

gRPC 能套 Cloudflare——但你去 CF 控制面板把 gRPC 打开了吗？没开的话，服务端怎么配都是白搭，CDN 那边一句「不认识」就给你拦了。

![](/images/posts/xrayjin-jie-wan-fa---shi-yong-grpcxie-yi/02.avif)

另外，CDN 不是万能加速器。想藏源站就开，想极限速度就直连。性能、安全、稳定，三样全都要？醒醒，不存在那种好事。

## gRPC vs xHTTP 怎么选

现在脚本有 xHTTP 了，gRPC 不是你唯一的选择。

简单粗暴的建议：

  1. 客户端支持 gRPC + 你要走 CDN → 试 gRPC。
  2. 想要最大兼容性 → ws 永远是最稳的。
  3. 想尝鲜 → xHTTP，但 Clash 目前不支持，注意避坑。
  4. 做负载均衡 → 主服务器和后端协议必须一致，别 gRPC 对 xHTTP 乱搭。

最后一句真心话：**协议好不好，跑一下就知道。** 选项全在同一个菜单里摆着呢，实测十分钟比你脑子里纠结一晚上靠谱一百倍。