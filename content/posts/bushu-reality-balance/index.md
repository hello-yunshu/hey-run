+++
title = "如何部署 Reality 协议服务端负载均衡"
date = 2026-05-26T01:14:52+08:00
draft = false
description = "Xray_bash_onekey 支持在服务端对 Reality 协议做负载均衡。本文保留原来的轻松写法，按当前脚本菜单修正 Reality+ws/gRPC/xHTTP+Nginx、realityServers 和 Nginx 负载均衡配置流程。"
slug = "bushu-reality-balance"
featureimage = "/images/posts/bushu-reality-balance/cover.avif"
categories = ["网络技术"]
tags = ["Xray", "Reality", "负载均衡", "代理"]
+++

最近更新了一个比较厉害的功能，嘿嘿。

就是！可以在服务端对 Xray 的 Reality 协议进行负载均衡，哼哼。

服务器示意图如下：

![](/images/posts/bushu-reality-balance/cover.avif)

大概访问情况如上。客户端只连主服务器，主服务器再把流量分给后面的二级服务器。看起来像一个入口，背后其实是一群小弟在干活，听上去就很让人安心。

如果你想看普通 ws/gRPC/xHTTP 的后端负载均衡，可以看这篇：[**XRay进阶玩法 - 搭建后端服务器负载均衡**](https://hey.run/posts/xrayjin-jie-wan-fa---da-jian-hou-duan-fu-wu-qi-fu-zai-jun-heng)。

## 一级服务器（主服务器）如何搭建

首先你要运行脚本：[**Xray_bash_onekey**](https://github.com/hello-yunshu/Xray_bash_onekey)。

```bash
bash <(curl -fsSL https://raw.githubusercontent.com/hello-yunshu/Xray_bash_onekey/main/install.sh)
```

然后，在主服务器上，正常运行：

```text
3. 安装 Xray (Reality+ws/gRPC/xHTTP+Nginx)
```

运行中，当脚本问你：

  * 要不要开「**负载均衡**」--> 必须开！
  * 要不要开「**Nginx**」--> 也必须开！（因为负载均衡就靠它诶）

脚本在运行时会提问，如下图：

![](/images/posts/bushu-reality-balance/01.avif)

在按照流程搭建时，必须要记下几个重要的值：

  1. **UUID 映射字符串（UUID）**
  2. **Target 域名、serverNames（如果你自定义了）**
  3. **privateKey**
  4. **shortIds**
  5. **主服务器 Reality 端口**

上面这些值非常重要，每个都要记下来，知道不？

忘了也别慌，可以运行：

```bash
idleleo --show
```

## 二级服务器（次服务器）如何搭建

同样是运行脚本：[**Xray_bash_onekey**](https://github.com/hello-yunshu/Xray_bash_onekey)。

然后，在次服务器上，还是正常安装：

```text
3. 安装 Xray (Reality+ws/gRPC/xHTTP+Nginx)
```

在脚本运行中：

  * 自定义端口 --> 建议用高位端口，比如 2xxxx
  * 自定义 UUID / Target / privateKey / shortIds --> 必须和主服务器一模一样！

![](/images/posts/bushu-reality-balance/02.avif)

如上图，请输入之前记下的参数，保持每个都与主服务器一致。

当脚本问你：

  * 要不要开「**负载均衡**」--> 可以开，主服务器接入时会用到这套 Reality 参数
  * 要不要开「**Nginx**」--> 建议不要开

如果只用作次服务器，Nginx 不开就行。次服务器躲在后面当小透明，别让它过度暴露。

安装完后，记下次服务器的 **IP（建议内网 IP）** 和 **端口号**。

## 一级服务器如何连接二级服务器

回到主服务器，在脚本里选择：

```text
11. 变更 Nginx 负载均衡配置
```

也可以直接运行：

```bash
idleleo --add-upstream
```

然后会有如下提示：

![wechat_2025-09-02_170104_729.png](/images/posts/bushu-reality-balance/03.avif)

根据要求，创建一个新的 `realityServers` 文件。创建过程会提示你输入：

  1. **主机 host** --> 次服务器的 IP（建议内网）
  2. **端口** --> 次服务器的端口号
  3. **权重** --> 默认就行，想偏心谁就调大点

输入完后，就自动连接上啦！！

可以在次服务器运行：

```bash
idleleo --port-traffic
```

能看到对应端口有流量，就说明没问题啦。

## 客户端怎么使用（优势）

客户端**只需要使用主服务器**生成的配置即可，**次服务器的不要使用**。

其实，完全可以搭建多个服务器，在客户端实现负载均衡。但是呢，分开请求可能会受到较慢的服务器拖累。

所以！

过去想在客户端做多 IP 负载均衡，配置一大坨还容易踩雷。现在只需要连主服务器，就等于偷偷访问了后面一群小弟，又快又稳！

而且呢，还能把次级 IP 藏起来，不怕被 ban，超安心。

## 注意事项

**强烈建议**：

  * 主服务器 + 所有次服务器放在同一个区域、同一个内网，理由如下：[关于脚本的负载均衡功能 - 云云舒](https://hey.run/posts/1715234393850)

  * **主服务器**选择**延迟低 + 带宽高**的喔，毕竟客户端连接次服务器全靠它。

记得在 VPS 控制台放行次服务器的端口，但只对内网放行就行。

次服务器没有 Nginx 挡子弹，**千万别让它乱跑流量**，只当负载均衡小透明！

安装完后，脚本会有额外提示，如图：

![](/images/posts/bushu-reality-balance/04.avif)

看到 `+Balance` 就意味着这是负载均衡的服务器，这样就不会搞错啦。

一些杂项：

  * 建议都开启 Fail2ban。
  * 建议都开启 TCP 加速。
  * 如果要做流量控制，可以配合 `idleleo --traffic-blocker`。

总之，负载均衡是把请求分摊到后端，不是把所有服务器叠起来变成一台更快的机器。搞清楚这个，就不会对它产生奇奇怪怪的期待了。
