+++
title = "PassWall进阶玩法 - 自动替换优选IP"
date = 2021-04-27T15:49:25+08:00
draft = true
description = "如果你是使用Xray_bash_onekey搭建Nginx+ws+TLS的服务器，又套用了Cloudflare。那么也许你会发现，属于Cloudflare（以下简称CF）的IP非常多，但到底那个才是连接最快的却无从得知。 好在现在有一个GitHub项目可以查找适合自己当前网络环境的优选Cloudfl"
slug = "passwalljin-jie-wan-fa---zi-dong-ti-huan-you-xuan-ip"
featureimage = "https://cdn.idleleo.com/wp-content/uploads/2021/04/20210427093333.jpg"
+++

如果你是使用[Xray_bash_onekey](<https://www.idleleo.com/go?url=https://github.com/paniy/Xray_bash_onekey>)搭建Nginx+ws+TLS的服务器，又套用了Cloudflare。那么也许你会发现，属于Cloudflare（以下简称CF）的IP非常多，但到底那个才是连接最快的却无从得知。

好在现在有一个[GitHub项目](<https://github.com/XIU2/CloudflareSpeedTest>)可以查找适合自己当前网络环境的优选Cloudflare Anycast IP，但这依然不够简单，毕竟每次优选只能选出一个，而且需要手动替换IP，还是挺麻烦的。为了一劳永逸的解决这类问题，这里教大家一个简单办法。

## 如何利用CF的IP

为了防止有小伙伴不知所云，这里简单说一下使用CF的IP问题。使用CF的IP，首先你需要使用[Xray_bash_onekey](<https://www.idleleo.com/go?url=https://github.com/paniy/Xray_bash_onekey>)搭建Nginx+ws+TLS的服务器，这是必须的步骤，而且也只能是Nginx+ws+TLS的服务器，原因在[2021 搭建 Xray 服务器最新教程](<https://www.idleleo.com/12/4876.html>)这篇文章中略有提及。然后，你需要在CF页面的DNS解析中，将你使用的域名代理状态改为已代理（如图）。

![](/images/wp-content/uploads/2021/04/20210427093333.jpg)

接下来，在诸如PassWall中添加配置时，地址这栏中填上CF的IP，其他按照Xray安装后的值填写。**注意，需要在SNI（TLS选项后的域名），以及WebSocket Host中填上你解析的域名** ，这非常关键，否则将无法使用。

![](/images/wp-content/uploads/2021/04/20210427103824.jpg)

按图填写完成后，你的Xray服务器就成功被CF代理了。直接ping域名是找不到你的服务器真实IP的。这也就能让你的服务器更加安全，也是脚本Nginx+ws+TLS这个选项的主要意义。

## 自动替换优选IP

有了上述的基础，替换优选IP的操作就很明确了。需要替换的就是那个地址的IP，脚本笔者已经写好了，文章底下大家可以直接下载。但在这之前，如何使用是非常有必要说一下的。

### 脚本如何使用

首先确保系统安装了`tar`、`wget`程序，如果未安装，先运行命令：
[code] 
    opkg update
    opkg install tar
    opkg install wget
[/code]

其次，是脚本需要修改。在脚本需要修改的地方，笔者已经进行了标记。这里简单说明一下。
[code] 
    _##注意修改_ ！
    /etc/init.d/haproxy stop
    /etc/init.d/passwall stop
[/code]

脚本中这两行目的在于关闭已有的服务，以防止测试CF的IP被代理，影响测试结果。如果你使用的不是PassWall，那么你需要做的是停止你运行的服务，以此可推，下面的代码中也有需要根据实际使用的服务修改。
[code] 
    _##注意修改_ ！
    wait
    uci commit passwall
    wait
    sed -i "s/$(uci get passwall.xxxxxxxxxx.address)/${first}/g" /etc/config/passwall
    sed -i "s/$(uci get passwall.xxxxxxxxxx.address)/${second}/g" /etc/config/passwall
    sed -i "s/$(uci get passwall.xxxxxxxxxx.address)/${third}/g" /etc/config/passwall
    wait
    uci commit passwall
    wait
    /etc/init.d/haproxy restart
    wait
    /etc/init.d/passwall restart
    wait
[/code]

上述代码除去由于使用服务不同需要修改的地方外，主要需要修改的地方在于`passwall.xxxxxxxxxx.address`这几段。这几段主要来自于PassWall的配置文件。配置文件所在的地方即`/etc/config/passwall`。如果你创建过PassWall的文件，不难发现，它的节点配置格式如下：

![](/images/wp-content/uploads/2021/04/20210427095914.jpg)

上述的`passwall.xxxxxxxxxx.address`中的一堆x，需要修改为你需要自动更新IP的那个配置，它所在的`config nodes`后面的单引号中的随机字符串。在脚本中设置了可以同时自动更新三个不同的配置，可以根据实际需要删改，也就是脚本中的三个`passwall.xxxxxxxxxx.address`。

搞定完所有要修改的地方后，建议试着运行一下。只需要把脚本复制到你想要的任何目录，再运行命令：
[code] 
    chmod +x cf-openwrt-auto.sh && bash cf-openwrt-auto.sh
[/code]

如果没有任何报错，就可进行下一步啦~

### 设置自动运行

如果你设置的都没啥问题，那么就可以直接在OpenWrt后台设置个计划任务。非常简单，找到系统 -> 计划任务，在文本框中填写：
[code] 
    0 4 * * 2,4,6 bash /path/cf-openwrt-auto.sh > /dev/null
[/code]

如下图所示，填写完后点击保存就可以自动运行啦~当然你也可以直接修改`/etc/crontabs/root`文件，在文件最后追加以上的代码即可。

![](/images/wp-content/uploads/2021/04/20210427100751.jpg)

注意`/path/cf-openwrt-auto.sh`为实际你存放脚本的路径。`0 4 * * 2,4,6`的意思是在每周二、周四、周六的凌晨4点会自动运行一次。

### 实际测试

单个后台服务器，实际宽带100M，利用优选IP后的测试：

![](/images/wp-content/uploads/2021/04/20210426200740.jpg)

实际体验非常良好，毕竟IP是经过优选的。直接芜湖起飞！

## 脚本下载

GitHub项目：[paniy/use-cloudflare-ip](<https://github.com/paniy/use-cloudflare-ip>)

点击下载：[下载](<https://github.com/paniy/use-cloudflare-ip/raw/main/cf-openwrt-auto.sh>)

此脚本可以自动替换IP，由于每天都在更换访问Xray服务器的IP，又因为IP经过优选，整体上是即能增加使用的速度又能提高安全性，实在是双赢之举。这就是为什么此教程比较复杂，需要根据实际情况修改的地方较多，但笔者依然觉得需要写出来的原因。 小伙伴们快来试试吧！
