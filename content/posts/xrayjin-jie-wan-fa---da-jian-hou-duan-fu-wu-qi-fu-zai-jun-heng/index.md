+++
title = "XRay进阶玩法 - 搭建后端服务器负载均衡"
date = 2021-04-07T22:56:00+08:00
draft = true
description = "很久没有更新文章了，最近很多文章受到压力而404了😭。今天给大家带来一个XRay的进阶玩法，服务器的负载均衡。 功能简介 负载均衡对于使用软路由的小伙伴应该不陌生，其中HAProxy应用甚广。对于单个VPS用户，HAProxy搭配Cloudflare的多IP同时访问，能够有效防止访问阻塞。但是，此"
slug = "xrayjin-jie-wan-fa---da-jian-hou-duan-fu-wu-qi-fu-zai-jun-heng"
featureimage = "https://cdn.idleleo.com/wp-content/uploads/2021/04/202104071017-1024x619.jpg"
+++

很久没有更新文章了，最近很多文章受到压力而404了😭。今天给大家带来一个XRay的进阶玩法，服务器的负载均衡。 

## 功能简介

负载均衡对于使用软路由的小伙伴应该不陌生，其中HAProxy应用甚广。对于单个VPS用户，HAProxy搭配Cloudflare的多IP同时访问，能够有效防止访问阻塞。但是，此办法毕竟后端仅依托于单个VPS，再怎么加速依然不能超过单个VPS的上限。

那能不能将利用Nginx搭建Xray的负载均衡，实现多个VPS同时作为负载呢？答案当然是可以的，只是有些需要注意的地方。

![](/images/wp-content/uploads/2021/04/202104071017-1024x619.jpg)

## 配置过程

笔者更新了[一键脚本](<https://www.idleleo.com/12/4876.html>)（版本>1.5.0.0）后，脚本已经自带了组建负载均衡的基础功能了。以下就结合脚本的操作来详细描述一下搭建过程。

### 准备工作

  1. 准备好多个VPS，选择一个作为主要的VPS（以下简称：主VPS），其他作为后端服务器（以下简称：后端VPS）。
  2. 安装好`curl`。Centos用户运行：`yum install -y curl`；Debian/Ubuntu用户运行：`apt install -y curl`。
  3. 准备一个解析好的域名，请解析至主VPS的公网IP。
  4. 准备好一键安装脚本：[2021 搭建 Xray 服务器最新教程](<https://www.idleleo.com/12/4876.html>)

### 主VPS搭建步骤

连接到主VPS，运行[一键脚本](<https://www.idleleo.com/12/4876.html>)。

![](/images/wp-content/uploads/2021/04/20210408210030.jpg)

选择安装 Xray (Nginx+ws+tls)，期间会跳出多个可自定义选项，根据实际需求选择是否需要修改。一切顺利的话，会弹出配置信息。

![](/images/wp-content/uploads/2021/04/20210407222204.jpg)

请记下几个重要的参数，**用户id (UUID)、伪装路径 (path)** ，准备后续使用。

到此，主VPS的安装就结束了。其实主VPS的安装很简单，过程就是简单的搭建使用ws协议的Xray而已。其中最大的难点在于域名解析上，需要确保域名解析与VPS的公网IP一致。其他步骤即便全程无脑回车键，也能正常搭建完成。

### 后端VPS搭建步骤

首先要说的是后端VPS的选择问题。笔者建议大家选择后端VPS与主VPS在同一个私网下，这样能很好的解决一定的安全问题，并且能够让访问延迟更低。同时考虑到成本问题，选用配置较低的VPS即可。

之后的操作步骤较主VPS的搭建更为简单。运行[一键脚本](<https://www.idleleo.com/12/4876.html>)，选择安装 Xray (ws ONLY)模式。

![](/images/wp-content/uploads/2021/04/20210408210031.jpg)

根据提示输入之前记下的主VPS的用户id (UUID)与伪装路径 (path)。之后输入自定义端口 (port)，此端口 (port)需要记下，之后要使用，建议端口选择为高位端口 (>10000)。

![](/images/wp-content/uploads/2021/04/20210407222207.jpg)

完成后记下此后端VPS的私网IP地址或者公网IP地址 (host)、端口 (port)即可。

后端VPS的搭建很简单。如果选择的是安装 Xray (ws ONLY)模式，搭建还非常快。但是需要注意的是，****用户id (UUID)、伪装路径 (path)** 必须与主VPS一致**。

当然，其实还有一个隐藏办法，可以选择安装 Xray (XTLS+Nginx)模式。此模式中包含了后端VPS的搭建，可以同时tcp+XTLS与ws共存。这里笔者就不再详细说明了，小伙伴可以自行尝试一下。

### 配置Nginx负载均衡

这个功能也可以借助[一键脚本](<https://www.idleleo.com/12/4876.html>)，脚本集成了简单的Nginx负载均衡搭建。

当完成主VPS与后端VPS搭建的两个步骤后，登录**主VPS** ，运行[一键脚本](<https://www.idleleo.com/12/4876.html>)，选择追加 Nginx 负载均衡。

![](/images/wp-content/uploads/2021/04/20210407222208.jpg)

根据提示输入后端VPS的私网IP/公网IP (host)、端口 (port)、权重 (weight)。注意，这里的端口 (port)是之前搭建后端VPS输入的自定义端口 (port)；这里的权重 (weight)需要输入数字，数字越大，使用的概率越大。主VPS的权重是50，可以根据后端VPS实际连接情况选择大于或者小于。

到这里，一个后端的负载均衡就做好啦！如果你是土豪，有非常多的VPS，可以重复最后的两个操作，将更多的后端VPS加入进去！

## 实际测试

毫无疑问，加入后端负载均衡后连接速度大涨，尤其对于配置较低的VPS而言。

YouTube实测：

![](/images/wp-content/uploads/2021/04/202104061725-1024x370.jpg)

以上测试环境为两个1核/1G内存的VPS组成的负载均衡。实测还是很可以的，不差钱的小伙伴可以试试啦~

## 推荐阅读

搭建 Xray 服务器最新教程：[2021 搭建 Xray 服务器最新教程](<https://www.idleleo.com/12/4876.html>)
