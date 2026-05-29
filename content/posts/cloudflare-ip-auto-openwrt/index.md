+++
title = "优选 CF IP：让 OpenWrt 代理快起来"
date = 2026-05-29T10:30:00+08:00
draft = false
description = "use-cloudflare-ip 新版脚本可以在 OpenWrt 上调用 CloudflareSpeedTest 自动优选 Cloudflare IP，并写回 PassWall 或 OpenClash 配置。本文按新版配置方式整理：同目录配置、PassWall/OpenClash 双模式、多域名、IPv4/IPv6、HTTPing、GitHub 下载兜底、静默定时运行和排错方式。"
slug = "cloudflare-ip-auto-openwrt"
featureimage = "/images/posts/cloudflare-ip-auto-openwrt/cover.avif"
categories = ["网络技术"]
tags = ["Cloudflare", "OpenWrt", "PassWall", "OpenClash", "优选 IP"]
+++

套了 Cloudflare 以后，很多人都会遇到一个很微妙的问题：域名是同一个域名，节点是同一个节点，可今天丝滑得飞起，明天就开始卡成电子相册。你问它为什么，它不说；你测一下 IP，哦～原来走的边缘节点又开始表演了。

所以优选 CF IP 这件事，听起来像玄学，其实朴素得很：**在你当前这条宽带上，挑几个更顺手的 Cloudflare Anycast IP，让客户端先连它们，再靠 SNI / Host 回到你的真实域名。** 地址换成 IP，域名信息别丢。就这么点事，偏偏手动做起来又烦又容易翻车，讨厌死了。

新版 [**use-cloudflare-ip**](https://github.com/hello-yunshu/use-cloudflare-ip) 就是把这套流程塞进 OpenWrt：自动下载 CloudflareSpeedTest、测速、挑 IP、验证连通性，然后写回 PassWall 或 OpenClash。你负责把配置填对，它负责半夜悄悄干活。很懒，但懒得有章法，我喜欢～😏

![](/images/posts/cloudflare-ip-auto-openwrt/cover.avif)

## 它到底解决什么嘛

旧玩法大家应该都见过：跑 CloudflareSpeedTest，复制第一个 IP，打开 PassWall 或 OpenClash，找到节点，把地址改掉，保存，重启。然后过几天线路一抽风，再来一遍。再来一遍！再来一遍！！人类发明自动化，就是为了不做这种重复小苦力活嘛，不然要机器干嘛，供起来拜吗？

新版脚本现在走的是配置文件方式：`cf-openwrt-auto.sh` 和 `cf-openwrt-auto.conf` 放在同一个目录，脚本运行时自动读配置。成功时默认一声不吭，适合丢进 cron 装死；真出错才把错误打到 stderr。也就是说，它平时安静得像不存在，出事才会跳出来告状——这种性格我还挺喜欢的，不像某些工具，成功也要刷你一屏幕。

![](/images/posts/cloudflare-ip-auto-openwrt/01.svg)

它就是一个正经小工具。时代在进步，咱的工具也得跟上，对吧～

## 先装依赖呀

OpenWrt 25.12 之后用 `apk`：

```sh
apk update
apk add bash curl tar jq ca-bundle ca-certificates
```

OpenWrt 24.10 及更早版本用 `opkg`：

```sh
opkg update
opkg install bash curl tar jq ca-bundle ca-certificates
```

然后把项目放到路由器上，初始化配置：

```sh
cp cf-openwrt-auto.conf.example cf-openwrt-auto.conf
chmod +x cf-openwrt-auto.sh
```

接下来编辑 `cf-openwrt-auto.conf`。先别急着扔进计划任务哦，第一次建议手动跑：

```sh
./cf-openwrt-auto.sh --verbose
```

`--verbose` 会把自升级检查、CloudflareSpeedTest 下载、测速、连通性验证、配置写入、服务重启这些步骤都打印出来。等确认没问题了，再让它定时偷偷跑。先看日志再装死，这点小谨慎很有必要哦——毕竟谁也不想半夜发现路由器把节点改成了一坨不可名状的东西。

## 配置怎么填呢

最核心的就是 `MODE`。用 PassWall 就填：

```sh
MODE="passwall"
PASSWALL_TARGET_DOMAIN="cdn.example.com"
```

用 OpenClash 就填：

```sh
MODE="openclash"
OPENCLASH_CONFIG="/etc/openclash/config/config.yaml"
OPENCLASH_TARGET_DOMAIN="cdn.example.com"
```

多个域名可以用逗号分隔，比如：

```sh
OPENCLASH_TARGET_DOMAIN="cdn1.example.com,cdn2.example.com"
```

IP 数量用 `IP_COUNT` 控制，默认 4 个。测速类型用 `IP_TYPE` 控制，支持 `ipv4`、`ipv6`、`both`。如果你想更贴近真实访问体验，可以把测速协议改成 HTTPing：

```sh
SPEEDTEST_PROTOCOL="http"
SPEEDTEST_CFCOLO="HKG,NRT,LAX"
```

`SPEEDTEST_CFCOLO` 是按 Cloudflare 数据中心筛选，适合你明确知道自己想靠近哪些节点的时候用。不知道就留空，别为了显得专业乱填，网络不会因为你填了三个缩写就突然爱上你，真的不会。

![](/images/posts/cloudflare-ip-auto-openwrt/02.svg)

## PassWall 怎么更新

PassWall 模式会读取：

```sh
uci show passwall
```

然后找 `address` 等于 `PASSWALL_TARGET_DOMAIN` 的节点，把 `address` 改成优选 IP，再 `uci commit passwall`，最后重启 PassWall。就这三板斧，朴实无华。

这里有一个重点，敲黑板：**你的 SNI、Host 或传输层域名，还是应该填自己的域名。** 优选 IP 只是连接地址，不是你的证书名字，也不是你的 CDN 回源域名。把它们混成一坨，能连上才奇怪，真的。这就好比快递地址写了隔壁小区门牌号，收件人写的却是你自己——快递小哥不懵谁懵？

另外，PassWall 模式的匹配条件很直接：它看的是节点 `address`。所以首次配置时，节点地址要先填目标域名，让脚本找得到。手动排查时如果看到：

```text
[cloudflare-ip] ERROR: no PassWall nodes matched address: cdn.example.com
```

那大概率就是节点当前地址已经不是这个域名了，或者你配置里的域名写错了。这个错误信息很朴素，朴素到有点不给面子，但它说的是实话。说实话的人不讨喜，但有用，对吧～

## OpenClash 更适合多 IP 变体呀

OpenClash 模式会修改 YAML 配置文件。首次运行时，它会找 `server` 等于目标域名的代理节点当模板，然后按 `IP_COUNT` 生成类似 `[CF-1]`、`[CF-2]` 的代理节点。后续运行会优先刷新这些标记节点，缺了还会自动补齐——像个小管家，操心但不烦人。

它会把：

```yaml
server: cdn.example.com
```

改成测速得到的 IP，但会保留：

```yaml
servername: cdn.example.com
ws-opts:
  headers:
    Host: cdn.example.com
```

xHTTP 也是一样，`xhttp-opts.headers.Host` 会继续保留域名。说人话就是：**连接可以冲着 IP 去，身份识别还得拿域名说话。** 不然 TLS 和 CDN 都会一脸「你谁啊」，然后把你晾在门外，门都不给你开，超冷淡的。

![](/images/posts/cloudflare-ip-auto-openwrt/03.svg)

如果你的 OpenClash 配置里有一堆代理节点，可以用 `OPENCLASH_TRANSPORT_FILTER` 限制只改某些传输：

```sh
OPENCLASH_TRANSPORT_FILTER="ws,xhttp"
```

支持 `ws`、`grpc`、`xhttp`、`h2`、`http`。留空就是所有支持的节点都看一遍。脚本只处理常见的 `vless`、`vmess`、`trojan`，并且会跳过明显不适合保留 SNI / Host 的节点，避免把无关代理也拿去「优选」。谢谢它，没有到处乱动，算是有点边界感——比某些什么都想管的工具懂事多了。

## GitHub 抽风怎么办呀

路由器访问 GitHub，有时候就像薯片袋里的空气，存在感很强，实际东西不多。新版脚本做了几个兜底：

```sh
DOWNLOAD_RETRIES="3"
DOWNLOAD_RETRY_DELAY="5"
GITHUB_MIRROR=""
```

下载失败会重试。如果 GitHub 实在不通，可以手动下载对应架构的 CloudflareSpeedTest 压缩包，比如：

```text
cfst_linux_amd64.tar.gz
```

把它放到工作目录里。脚本下载失败时会优先用本地包；如果已经有可执行的 `cfst`，也会继续用现有二进制。比起一报错就倒地不起，这种「能跑就先跑」的态度还是比较可爱的。我写代码最烦那种一遇到问题就摆烂的工具——喂，你倒是挣扎一下啊！

## 定时怎么设呢

推荐从每 6 小时一次开始：

```cron
0 */6 * * * /path/to/cf-openwrt-auto.sh
```

网络稳定的话每天一次也行，波动明显可以每 3 小时一次。别低于每小时一次哦，测速会吃路由器 CPU 和网络资源。你是想优化网络，不是想把路由器训练成健身器材，对吧～

如果你不想收到 cron 邮件，可以重定向：

```cron
0 */6 * * * /path/to/cf-openwrt-auto.sh >/dev/null 2>&1
```

还有一个挺贴心的小设置：

```sh
STARTUP_DELAY="random"
```

这样脚本启动后会随机等 0 到 300 秒，适合多台设备同一时间跑任务，避免大家一起冲出去测速。网络已经够忙了，别再集体排队踩油门——又不是抢演唱会门票，急什么嘛！

## 新版和老版有什么不一样

如果你是从旧版教程过来的，可能会发现几个变化：

**配置文件独立了。** 旧版是把配置写在脚本里面，改一次配置就得打开脚本对着那堆变量发呆。新版 `cf-openwrt-auto.conf` 单独出来，干干净净，改配置不用碰脚本逻辑。这才对嘛，配置和代码本来就不该挤在一起，又不是合租。

**自升级有了。** 脚本启动时会检查 GitHub 有没有新版本，有就自己更新，不用你手动下载替换。当然啦，更新前会备份，翻车了也能滚回去——这点良心还是有的。

**下载渠道多了。** GitHub 不通的时候能走本地包，本地也没有才会彻底放弃。三层兜底，比我出门带伞还周全。

**IPv6 支持。** `IP_TYPE="ipv6"` 或者 `IP_TYPE="both"`，IPv6 用户不用再手动改一堆东西了。之前没有这个的时候，IPv6 用户每次都得自己折腾半天，想想就心疼。

## 一点小提醒

优选 IP 提升的是「你到 Cloudflare 边缘节点」这一段。后面的回源、服务器带宽、客户端内核、运营商晚高峰，该拉的还是会拉。它不是魔法棒，是一个自动挑路的小工具。别指望它把 1M 小水管变成千兆光纤——做不到的啦，物理定律又不是我写的。

所以我的建议是：先用 `--verbose` 手动跑一遍，看它到底改了哪些节点；再打开客户端实际连一下；最后再丢进 cron。工具再自动，也别闭眼开车。知道了没！

如果你还在用旧教程手动复制 IP，那现在真的可以收手啦。新版脚本已经把最烦的那部分接过去了：测速、筛选、验证、写回、重启。你只要把域名和模式填对，然后让它安安静静工作。网络工具能做到「不打扰但有用」，已经很难得了，哼～

好啦，去试试吧，路由器在等你宠幸它呢～