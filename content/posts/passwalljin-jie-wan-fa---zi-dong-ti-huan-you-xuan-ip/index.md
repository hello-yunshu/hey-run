+++
title = "PassWall进阶玩法 - 自动替换优选IP"
date = 2021-04-27T15:49:25+08:00
draft = true
description = "如果你是使用 Xray_bash_onekey 搭建 Nginx+ws/gRPC/xHTTP+TLS，并且套用了 Cloudflare，那么优选 IP 依然是一个绕不过去的小麻烦。本文按现在的脚本语境重新整理 PassWall 自动替换优选 IP 的思路。"
slug = "passwalljin-jie-wan-fa---zi-dong-ti-huan-you-xuan-ip"
featureimage = "/images/posts/passwalljin-jie-wan-fa---zi-dong-ti-huan-you-xuan-ip/cover.avif"
+++

如果你用 [Xray_bash_onekey](https://github.com/hello-yunshu/Xray_bash_onekey) 搭了 Nginx+ws/gRPC/xHTTP+TLS，还套了 Cloudflare，那你大概已经发现了：Cloudflare（以下简称 CF）的 IP 多得像天上的星星，但哪个最快？靠眼睛是看不出来的。

好在有 [CloudflareSpeedTest](https://github.com/XIU2/CloudflareSpeedTest) 这个小可爱，能帮你在当前网络里挑出最快的 CF Anycast IP。可问题是——测完你还得手动去改节点地址，不觉得烦吗？反正我觉得烦。

所以这篇教你一个更懒的办法：定时测速，自动取优选 IP，静悄悄写回 PassWall 节点配置。「你只管用，我偷偷换」那种感觉，就问你香不香～

![](/images/posts/passwalljin-jie-wan-fa---zi-dong-ti-huan-you-xuan-ip/cover.avif)

## 为什么能这么玩

先快速说清楚前提，免得有人一脸懵。你需要用 [Xray_bash_onekey](https://github.com/hello-yunshu/Xray_bash_onekey) 搭好 Nginx+ws/gRPC/xHTTP+TLS，总之就是能被 CF 代理的那种 TLS 入口。然后在 CF 页面把域名的 DNS 记录改成「已代理」——这个小云朵要亮起来喔。

接下来在 PassWall 里填配置的时候，**地址那栏填 CF 优选 IP**，其他信息按脚本装完后给的值填。但别傻了——SNI、Host 或者传输层域名，要填你自己的域名。地址可以是别人的 IP，但 TLS 握手和 Host 是你自己的事儿。

![](/images/posts/passwalljin-jie-wan-fa---zi-dong-ti-huan-you-xuan-ip/01.avif)

这样做完以后，客户端走的是 CF 边缘 IP，回源还是你自己的域名。对 Xray_bash_onekey 来说，现在 ws、gRPC、xHTTP 都能走这条路，不过 xHTTP 要看客户端支不支持，别一股脑全上然后跑来问我为什么不通嘛～

## 怎么自动换

有了上面的铺垫，思路就很清楚了：你要替换的，就那么一个地址 IP。脚本我已经写好啦，底下就能下载。不过在你直接拿去跑之前，怎么用还是得说一说——毕竟我这个脚本不是那种「回车就跑，跑完拜拜」的傻瓜式，得稍微动一下小手～

### 改一下才能用

先确认系统里有 `tar` 和 `wget`，没有的话：

```bash
opkg update
opkg install tar wget
```

然后打开脚本，有几处要自己改。别怕，我都标好了～
```bash
# 注意按你的实际服务修改
/etc/init.d/haproxy stop
/etc/init.d/passwall stop
```

这两行是干嘛的呢？测 CF IP 的时候，你得把代理服务先停下来，不然流量已经走代理了，测出来的速度就是骗人的！如果你用的不是 PassWall，就换成你自己那个服务的停止命令，以此类推。

```bash
# 注意按你的实际节点 ID 修改
uci set passwall.xxxxxxxxxx.address="${first}"
uci commit passwall
/etc/init.d/haproxy restart
/etc/init.d/passwall restart
```

重点来了！上面那一大串 `xxxxxxxxxx`，要换成你自己的节点 ID。怎么找呢？打开 `/etc/config/passwall`，找到你的节点配置，里面会有类似 `config nodes 'xxxxxx'` 这样的东西——那串随机字符串就是 ID。想更新几个节点就写几行，别贪多喔～

改完以后，先试跑一下：
```bash
chmod +x cf-openwrt-auto.sh
bash cf-openwrt-auto.sh
```

没报错？恭喜你，最难的部分已经过去了～剩下的就是让它偷偷自己跑。

### 定时跑

在 OpenWrt 后台，「系统 -> 计划任务」，填上：

```cron
0 4 * * 2,4,6 /path/cf-openwrt-auto.sh >/dev/null 2>&1
```

`/path/` 换成你实际放脚本的路径。`0 4 * * 2,4,6` 就是每周二、四、六凌晨 4 点偷偷跑一次。为什么半夜跑？因为那个时候网络安静，测出来的结果更准，而且你在睡觉，不会觉得卡。

### 效果怎么样

单台后端服务器，100M 带宽，优选 IP 带来的改善肉眼可见。但也别吹得太玄乎，它主要优化的是"你到 CF 边缘节点"这段。后面的回源线路、服务器带宽、客户端实现，该拉胯还是拉胯。优选 IP 是好东西，但它不是那种「一开就加倍」的魔法，更像是一个帮你挑好路的导航。

## 脚本下载

GitHub 项目：[paniy/use-cloudflare-ip](https://github.com/paniy/use-cloudflare-ip)

点击下载：[cf-openwrt-auto.sh](https://github.com/paniy/use-cloudflare-ip/raw/main/cf-openwrt-auto.sh)

每天自动换 IP，又因为都是优选过的，速度和安全性都能往上提一提，双赢。教程确实麻烦了点，要改的地方不少，但我还是觉得值——毕竟写都写了，对吧～ 快试试！
