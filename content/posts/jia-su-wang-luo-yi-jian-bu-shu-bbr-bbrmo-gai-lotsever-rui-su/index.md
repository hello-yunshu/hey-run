+++
title = "加速网络 一键部署BBR+BBR魔改+Lotsever(锐速)"
date = 2019-05-19T00:35:03+08:00
draft = true
description = "笔者在文章V2Ray / SSR 传输协议哪个好? (各种协议对比)中简述了关于TCP阻塞的情况，这里笔者提供了BBR/BBR PLUS/Lotsever的一键部署脚本。通过脚本可以一定程度加速服务器连接速度。 <"
slug = "jia-su-wang-luo-yi-jian-bu-shu-bbr-bbrmo-gai-lotsever-rui-su"
featureimage = "https://cdn.idleleo.com/wp-content/uploads/2019/05/201905191231.jpg"
+++

笔者在文章[V2Ray / SSR 传输协议哪个好? (各种协议对比)](<https://www.idleleo.com/05/2071.html>)中简述了关于TCP阻塞的情况，这里笔者提供了BBR/BBR PLUS/Lotsever的一键部署脚本。通过脚本可以一定程度加速服务器连接速度。

![](/images/wp-content/uploads/2019/05/201905191231.jpg)

脚本中BBR魔改版不一定有好的效果，其受到服务器网络环境的影响。最新的拥塞控制方法为BBR PLUS，Lotsever(锐速)效果类似。这里主要是以Linux系统为主，在Centos7的测试中，效果显著。

## 部署脚本

### chiakge的脚本

**支持的系统：**`CentOS 6+`、`Debian 8+`、`Ubuntu 14+`。

**注意：** 过程有2步，第1步安装相应的内核，第2步开启内核对应的加速。

运行以下命令：
[code] 
    wget -N --no-check-certificate "https://raw.githubusercontent.com/chiakge/Linux-NetSpeed/master/tcp.sh" && chmod +x tcp.sh && ./tcp.sh
[/code]

运行后出现如下的界面：

![](/images/wp-content/uploads/2019/05/20190519001440.png)

根据提示安装即可，重启后可以使用`./tcp.sh`命令接着操作。

### ylx2016的脚本

支持的系统：`CentOS 6+`、`Debian 8+`、`Ubuntu 16+`等。

ylx2016的脚本来自与上述的脚本，在经过二次加工后，有些青出于蓝而胜于蓝的味道。

**注意：** 在第一次使用此脚本前需要运行`[ -f "tcp.sh" ] && rm -rf ./tcp.sh`命令。每次运行此脚本请使用`./tcp.sh`。其他均与上述脚本一致。

运行以下命令：
[code] 
    wget -N --no-check-certificate "https://github.com/ylx2016/Linux-NetSpeed/releases/download/sh/tcp.sh" && chmod +x tcp.sh && ./tcp.sh
[/code]

国内可以运行以下命令：
[code] 
    wget -N --no-check-certificate "https://github.000060000.xyz/tcpx.sh" && chmod +x tcpx.sh && ./tcpx.sh
[/code]

运行后出现如下的界面：

![](/images/wp-content/uploads/2020/02/20200210013226.jpg)

根据提示安装即可，重启后可以使用`./tcp.sh`命令接着操作。

## 注意事项

安装期间会更换系统内核。因此，若是使用类似WireGuard等网络工具，需要小心失效。

如果在删除内核环节出现如下情况：

![](/images/wp-content/uploads/2019/05/201905191221.png)

需要选择`No`，否则可能导致意外情况。
