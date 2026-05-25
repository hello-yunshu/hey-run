+++
title = "2023 搭建 Xray 服务器最新教程"
date = 2020-12-11T21:34:00+08:00
draft = true
description = "最近V2Ray更新不断，记忆中，项目默认说明变成了繁体中文，项目名又从V2Ray变成了v2fly，又多了VLESS、XTLS、fallback等功能，可谓飞速。现在又出现了Xray的项目，笔者觉得脚本再不更新一下有点说不过去了哈哈，这不新的功能它来了。 XRay_bash_onekey GitHub"
slug = "2023-da-jian-xray-fu-wu-qi-zui-xin-jiao-cheng"
featureimage = "https://img.shields.io/github/issues/paniy/Xray_bash_onekey"
+++

最近V2Ray更新不断，记忆中，项目默认说明变成了繁体中文，项目名又从V2Ray变成了v2fly，又多了VLESS、XTLS、fallback等功能，可谓飞速。现在又出现了Xray的项目，笔者觉得脚本再不更新一下有点说不过去了哈哈，这不新的功能它来了。

## XRay_bash_onekey

GitHub地址：

[Xray_bash_onekey](<https://github.com/paniy/Xray_bash_onekey>)

{{CODEshieldsio}} 

[![GitHub issues](https://img.shields.io/github/issues/paniy/Xray_bash_onekey)](<https://github.com/paniy/Xray_bash_onekey/issues>)  [![GitHub forks](https://img.shields.io/github/forks/paniy/Xray_bash_onekey?color=%230885ce)](<https://github.com/paniy/Xray_bash_onekey/network>)  [![GitHub stars](https://img.shields.io/github/stars/paniy/Xray_bash_onekey?color=%230885ce)](<https://github.com/paniy/Xray_bash_onekey/stargazers>)  [![GitHub license](https://img.shields.io/github/license/paniy/Xray_bash_onekey)](<https://github.com/paniy/Xray_bash_onekey/blob/main/LICENSE>)

### 三种安装模式

模式一：Nginx+ws/gRPC+tls模式。利用Nginx进行分流，通讯协议为Websocket/gRPC，通讯加密协议为TLS。相对传统，**可以与CDN兼容** ，Nginx的存在方便建站的朋友。简单说是Nginx在前，Xray在后，Xray不直接开放给外部。对于主要需要Xray服务的朋友，此模式下流量需要经过Nginx转发，一定程度牺牲性能，若再套用CDN，那么性能损失更大，与之带来的是安全性的提升。在脚本版本>1.5.0.0后，已支持负载均衡搭建，详细可见模式三。

模式二：Xray+Nginx+ws/gRPC模式。利用Xray的fallback功能，使流量在Xray端分流，Xray无法处理的流量将转交给Nginx处理，通讯协议为TCP，通讯加密协议为XTLS。Xray+Nginx模式利用了新协议，**不可以与CDN兼容** ，Nginx的存在主要为了防止探测，可以建站但不推荐。简单说是Xray在前，Nginx在后，Xray直接开放给外部。对于主要需要Xray服务的朋友，此模式下流量直接交由Xray处理，因此效率很高，再加上使用了最新的XTLS协议，性能更强，[但就如Trojan一般](<https://www.idleleo.com/02/4064.html>)，此模式无法套用CDN，强行套用后将失去Xray的功能。对于需要建站的朋友，由于流量由Xray分析与转发，性能有所损失，因此不推荐Nginx建站。在脚本版本>1.5.0.0后，内置了纯ws/gRPC协议的追加，方便组建后端服务器的负载均衡。

模式三：ws/gRPC ONLY模式。此模式搭建的为纯Websocket/gRPC通讯协议。此模式仅有ws/gRPC协议，没有加密，不包含Nginx，Xray直接对外通信。**此模式推荐仅作为后端服务器组建负载均衡使用** ，若直接使用不安全且非常容易导致IP被封锁。此模式配合模式一效果甚好。具体可见配置教程：[XRay进阶玩法 – 搭建后端服务器负载均衡](<https://www.idleleo.com/04/5136.html>)。

![](/images/wp-content/uploads/2021/04/20210408210029.jpg)

### 安装方式

需要一个属于你自己的域名，并且解析到你所购买的VPS的公网IP上。（在域名服务商添加A地址即可）。之后登录至VPS，运行脚本，按照提示运行即可。
[code] 
    bash <(curl -Ss https://www.idleleo.com/install.sh)
[/code]

若提示不存在`curl`命令，请先安装`curl`。Centos用户运行：`yum install -y curl`；Debian/Ubuntu用户运行：`apt install -y curl`。

更新说明（2021年9月23日）

  * 可以直接输入命令：`idleleo` 管理脚本。
  * 访问域名 302 跳转至 [https://www.bing.com](<https://www.idleleo.com/helloworld>) （了解配置过程可自行修改）。
  * 阻止 HTTP 接访问服务器 IP 。
  * 使用来自 [@DuckSoft](<https://www.idleleo.com/go?url=https://github.com/DuckSoft>) 的分享链接[提案](<https://www.idleleo.com/go?url=https://github.com/XTLS/Xray-core/issues/91>) (beta)，支持 Qv2ray、V2rayN、V2rayNG。
  * 使用来自 [XTLS](<https://www.idleleo.com/go?url=https://github.com/XTLS/Xray-core/issues/158>) 项目的提案，遵循 [UUIDv5](<https://www.idleleo.com/go?url=https://tools.ietf.org/html/rfc4122#section-4.3>) 标准，可以将自定义字符串映射至 VLESS UUID 。
  * 添加负载均衡配置，教程：[XRay进阶玩法 – 搭建后端服务器负载均衡](<https://www.idleleo.com/04/5136.html>)。
  * 添加 gRPC 协议的支持，具体可见：[Xray进阶玩法 – 使用gRPC协议](<https://www.idleleo.com/05/5225.html>)。
  * 兼容了宝塔面板

### 注意事项

  * 如果你不了解脚本中各项设置的具体含义，除域名外，请使用脚本提供的默认值（全程回车到底）。
  * Cloudflare 用户请安装完毕后再开启CDN功能。
  * 使用本脚本需要你拥有 Linux 基础及使用经验，了解计算机网络部分知识，计算机基础操作。
  * 目前支持 Debian 9+ / Ubuntu 18.04+ / Centos7+ ，部分 Centos 模板可能存在难以处理的编译问题，建议遇到编译问题时，请更换至其他系统模板。
  * 网站交流群：<https://t.me/idleleo_chat>（群主仅提供有限的支持，如有问题可以询问群友）。
  * 每周日的凌晨3点，Nginx 会自动重启以配合证书的签发定时任务进行，在此期间，节点无法正常连接，预计持续时间为若干秒至两分钟。
  * 分享链接为实验版本，不排除未来变动的可能，请自行确认客户端是否支持。
  * 自定义字符串映射至 UUIDv5 需要客户端支持。

**一些问题的说明：**

Q：为什么安装完后访问域名会跳转至bing搜索？

A：已经在上文中说明这种情况，至于为什么这么改可以看评论[30楼](<https://www.idleleo.com/09/2148.html#anchor-comment-583>)，已经较为详细的说明了原因，总之为了提高安全性，减少审查。**有能力的小伙伴，推荐自己建站。**

Q：生成证书失败是为什么?

A：情况很简单，无法通过域名经过80端口连接服务器。为什么会导致这种情况就不好说了，可能是服务器的80端口的原因，可能是域名没有解析到服务器IP的原因，可能是搭建前就开启CDN的原因等等。

PS：如果遇到问题，先别着急，**仔细翻翻评论** ，说不定有意想不到的收获。

### 实际测试

以下为模式二的测试，服务器端为谷歌云的香港节点，客户端网速为100M：

![](/images/wp-content/uploads/2020/12/20201211210524-1024x549.jpg)

## Xray简介

Xray, Penetrates Everything. Also the best v2ray-core, with XTLS support. Fully compatible configuration.

GitHub地址：[链接](<https://github.com/XTLS/>)

根据官网介绍，Xray完美兼容V2Ray，而且Xray比V2Ray性能更好，在XTLS协议上性能是V2Ray几倍。

## XTLS协议简介

VLESS XTLS Direct Mode 引入了 ReadV 增强，减少一层内存 Copy，性能已与 VLESS 无加密裸奔持平（接近于纯流量转发），为传统 VMess WS TLS 方案的五倍、VLESS TCP TLS 的三倍（且测试机器 CPU 均有 AES 指令集，否则差距更大，如硬路由器上），强烈建议测试体验。这或许是当前性能最强的安全代理方式，但并不是上限。

具体测试方式和测试结果见 [这里](<https://github.com/badO1a5A90/v2ray-doc>)

### 它是什么

  1. 简单概括：特殊处理 TLS 流量，不重复加密，提升数倍性能、更省资源。各种移动设备可以省电，路由器的加解密性能也不再是瓶颈。[rprx/v2ray-vless/releases](<https://github.com/rprx/v2ray-vless/releases>) 有关于 [XTLS Project](<https://github.com/XTLS/Go>) 原理的一些介绍。
  2. 原理：XTLS 无缝拼接了内外两条货真价实的 TLS，此时代理本身几乎无需再对数据加解密。VLESS + XTLS 可以理解为是增强版 ECH，即多支持身份认证、代理转发、明文加密、UDP over TCP 等。
  3. XTLS 本身需要是 TLSv1.3（正常情况下的协商结果），内层 TLS 可以为 1.3 或 1.2（上网时的绝大多数流量），此时特殊功能就会生效（填写 flow 是开启/指定特殊功能，生效是另一码事）。

### 注意事项

  1. 为了防止上层应用使用 QUIC，启用 XTLS 时客户端 VLESS 会自动拦截 UDP/443 的请求。若不需拦截，请在客户端填写流控： `xtls-rprx-direct-udp443`，服务端不变。Linux系统推荐设置为：`xtls-rprx-splice-udp443`。
  2. 可设置环境变量 `V2RAY_VLESS_XTLS_SHOW = true` 以显示 XTLS 的输出，适用于服务端与客户端（仅用于确信 XTLS 生效了，千万别设成永久性的，不然会很卡）。
  3. 不能开启 Mux。XTLS 需要获得原始的数据流，所以原理上也不会支持 WebSocket、不适用于 VMess。此外，UDP over TCP 时，VLESS 不会开启 XTLS 的特殊功能。

## 相关阅读

V2Ray、Trojan等主流工具安全吗：[V2Ray、Trojan等主流工具安全吗？](<https://www.idleleo.com/10/4766.html>)

使用BBR等加速TCP：[加速网络 一键部署BBR+BBR魔改+Lotsever(锐速)](<https://www.idleleo.com/05/2125.html>)

V2Ray与Trojan对比：[V2Ray / Trojan 传输方式哪个好？(原理对比)](<https://www.idleleo.com/02/4064.html>)

Xray搭建负载均衡：[XRay进阶玩法 – 搭建后端服务器负载均衡](<https://www.idleleo.com/04/5136.html>)

gRPC协议：[Xray进阶玩法 – 使用gRPC协议](<https://www.idleleo.com/05/5225.html>)
