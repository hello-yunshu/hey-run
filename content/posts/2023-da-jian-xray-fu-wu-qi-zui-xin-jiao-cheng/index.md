+++
title = "搭建 Xray 服务器最新教程"
date = 2026-05-26T03:28:00+08:00
draft = false
description = "这篇按当前 Xray_bash_onekey 重新整理安装教程。脚本现在支持 Reality、Nginx+TLS、ws/gRPC/xHTTP ONLY、XTLS ONLY、Docker、Fail2ban、流量阻断、GeoData 更新和 AI Skill 自动部署。旧的 paniy 仓库、idleleo.com 安装链接和 2020/2021 模式说明都已经不再适合作为主教程。"
slug = "2023-da-jian-xray-fu-wu-qi-zui-xin-jiao-cheng"
featureimage = "images/xray-install-overview.png"
categories = ["网络技术"]
tags = ["Xray", "服务器搭建", "Reality", "代理"]
+++

这篇本来是草稿，仓库地址、安装命令、模式名称全停在 2021 年。现在按当前 [**Xray_bash_onekey**](https://github.com/hello-yunshu/Xray_bash_onekey) 重新整理一版。

如果你只是想快速搭一个能用的 Xray，全程回车就行，默认值够用了。别一上来就每个选项都自己改——翻车的多半不是脚本难，是手太痒。

![](/images/xray-install-overview.png)

## 准备工作

你需要：

  1. 一台境外 VPS，具备公网 IP。
  2. 服务器系统建议使用 Debian 12+ 或 Ubuntu 24.04+。
  3. 如果安装 TLS 模式，需要准备一个解析到服务器 IP 的域名。
  4. 如果安装 Reality 模式，需要准备符合 Xray 要求的 Target 域名。
  5. 服务器里要有 `curl`。

安装 `curl`：

```bash
apt install -y curl
```

CentOS Stream 用户可以用：

```bash
yum install -y curl
```

新手不建议使用太旧的系统模板，也不建议在装了一堆面板和环境的机器上硬装。纯净环境少很多麻烦。

## 安装命令

当前安装命令是：

```bash
bash <(curl -fsSL https://raw.githubusercontent.com/hello-yunshu/Xray_bash_onekey/main/install.sh)
```

安装完成后，可以直接输入：

```bash
idleleo
```

进入管理菜单。

## 安装模式怎么选

当前主要模式：

  1. Reality + Nginx：推荐模式，可按需附加 ws/gRPC/xHTTP 简单协议用于负载均衡。
  2. Nginx + TLS：支持 ws、gRPC、xHTTP，适合域名和证书都准备好的场景。
  3. ws/gRPC/xHTTP ONLY：无 TLS 的独立入站，主要用于后端服务器或负载均衡。
  4. XTLS ONLY：仅用于特定中转或自定义场景。
  5. Docker：镜像内预装 Xray、Nginx 与主脚本。

如果你不知道怎么选，优先 Reality + Nginx 或 Nginx + TLS。ONLY 模式不要直接暴露给公网当主节点用，它更像后端工具。

## ws、gRPC、xHTTP 怎么选

安装 ws/gRPC/xHTTP 相关模式时，会看到：

```text
1: ws
2: gRPC
3: xHTTP
4: ws+gRPC+xHTTP
```

简单建议：

  1. 想稳妥，先选 ws。
  2. 想走 HTTP/2 风格传输，可以试 gRPC。
  3. 想测试新传输，可以试 xHTTP，但注意 Clash 目前不支持 xHTTP。
  4. 想一个服务器多准备几条路，可以选 `ws+gRPC+xHTTP`。

路径也要注意：ws 和 xHTTP 的 path 客户端里要带 `/`，gRPC 的 serviceName 不要带 `/`。

## 常用命令

```bash
idleleo --show              # 查看安装信息
idleleo --update            # 更新脚本
idleleo --xray-update       # 更新 Xray
idleleo --nginx-update      # 更新 Nginx
idleleo --set-fail2ban      # 设置 Fail2ban
idleleo --traffic-blocker   # 设置 Xray 流量阻断
idleleo --port-traffic      # 查看端口实时流量
```

如果不知道命令，运行：

```bash
idleleo --help
```

## 安全建议

安装完不是结束，至少做几件事：

  1. SSH 不要用弱密码，能用密钥就用密钥。
  2. 建议安装 Fail2ban。
  3. Reality 模式建议搭配 Nginx 前置。
  4. 有滥用风险时开启流量阻断。
  5. Cloudflare 用户请先确认脚本安装成功，再开启 CDN 代理。
  6. 定期更新脚本、Xray、Nginx、证书和 GeoData。

脚本能帮你省不少事，但它不是管家。该懂的网络常识还是要懂一点，别指望脚本替你思考。

## 延伸阅读

Reality 安装：[**搭建 Xray Reality 协议服务器**](https://hey.run/posts/da-jian-xray-reality-xie-yi-fu-wu-qi)

Reality 风险：[**Xray Reality 协议的风险**](https://hey.run/posts/reality-xie-yi-de-feng-xian)

gRPC 协议：[**Xray进阶玩法 - 使用 gRPC 协议**](https://hey.run/posts/xrayjin-jie-wan-fa---shi-yong-grpcxie-yi)

xHTTP 协议：[**Xray进阶玩法 - 使用 xHTTP 协议**](https://hey.run/posts/xray-xhttp-mode)

后端负载均衡：[**XRay进阶玩法 - 搭建后端服务器负载均衡**](https://hey.run/posts/xrayjin-jie-wan-fa---da-jian-hou-duan-fu-wu-qi-fu-zai-jun-heng)
