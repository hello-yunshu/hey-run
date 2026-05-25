+++
title = "Xray进阶玩法 - 使用gRPC协议"
date = 2021-05-09T23:25:07+08:00
draft = false
description = "在Xray 1.4.0版本中，gRPC作为新的一种传输协议被引进，并在之后的版本中逐渐得到完善。现今，随着脚本Xray_bash_onekey引进了gRPC协议，那么是时候说一说这个协议了。 什么是gRPC gRPC是一个高性能、开源和通用的RPC框架，面向移动和HTTP/2设计。gRPC基于HTT"
slug = "xrayjin-jie-wan-fa---shi-yong-grpcxie-yi"
featureimage = "https://cdn.idleleo.com/wp-content/uploads/2021/05/20210508154552-1024x536.jpg"
+++

在Xray 1.4.0版本中，gRPC作为新的一种传输协议被引进，并在之后的版本中逐渐得到完善。现今，随着脚本[Xray_bash_onekey](<https://www.idleleo.com/12/4876.html>)引进了gRPC协议，那么是时候说一说这个协议了。

## 什么是gRPC

gRPC是一个高性能、开源和通用的RPC框架，面向移动和HTTP/2设计。gRPC基于HTTP/2标准设计，带来诸如双向流、流控、头部压缩、单TCP连接上的多复用请求等特。这些特性使得其在移动设备上表现更好，更省电和节省空间占用。

![](/images/wp-content/uploads/2021/05/20210508154552-1024x536.jpg)

简单来说，可以认为gRPC是HTTP/2的高级版。HTTP/2有的特性gRPC也有，与此同时gRPC还解决了HTTP/2一些传输过程中的痛点，比如效率低、延迟高等。本来，笔者是不希望支持这个协议的，因为HTTP/2传输效果一般，比起已有的WebSocket协议来说，HTTP/2不适合用作某些特殊用途，但考虑到延迟低的特性，决定还是尝试一下。至于效果如何，先卖个关子。哈哈

## 如何搭建

[一键脚本](<https://www.idleleo.com/12/4876.html>)已经比较好的支持了gRPC协议，搭建方式与ws协议别无二致，具体步骤完全可以按照脚本说明一步一步安装。这里需要说明的是以下几点：

### serviceName参数

此参数类似于ws协议的path（路径），但并不完全相同。在ws协议中，path是需要加上“/”的，其实它的意思就是域名后面跟着的路径，如[www.idleleo.com/helloworld](<http://www.idleleo.com/helloworld>)这段域名中的“/helloworld”的意思。而gRPC略有差别，**在客户端配置中，serviceName这一栏中是不需要填写“/”这个符号的。**

![](/images/wp-content/uploads/2021/05/20210508163732.jpg)

实际上。在Nginx做路径分流时，gRPC的配置方式与ws也几乎完全一致，两者区别不是很大。既然如此，gRPC的serviceName为什么要与ws的path搞出区分别来实在有些难以理解，兴许之后的Xray版本会统一两者在加不加“/”上的问题。

### 负载均衡

如同ws协议一般，gRPC是可以使用负载均衡的。启用方法，也和ws协议一模一样，可以参考这篇文章：[XRay进阶玩法 – 搭建后端服务器负载均衡](<https://www.idleleo.com/04/5136.html>)，注意在选择协议时选择gRPC即可。

![](/images/wp-content/uploads/2021/05/20210508154551.jpg)

### 启用CloudFlare

对，没错！如同WebSocket、HTTP/2一般，gRPC也可以套用CDN。

这里稍微说一下脚本设计的想法，模式一主要是用于放在CDN后的，也推荐大家这么做，这么做是迄今为止最安全的传输方式之一，只是性能一般；模式二主要用于直连，性能强劲，但安全性一般；那么模式三，也就是组件负载均衡则是集两者优势为一体，若再使用CF的优选IP（[PassWall进阶玩法 – 自动替换优选IP](<https://www.idleleo.com/04/5199.html>)），那效果是真·芜湖起飞！

当然，在套用CF时需要注意，**在CF的控制面板->网络中启用gRPC** 。否则，将无法使用gRPC协议。

![](/images/wp-content/uploads/2021/05/20210508155436-1024x276.jpg)

## 实际体验

传输速度与ws没有太大的差别，速度上硬要说有区别的话，ws比gRPC性能更好。。毕竟gRPC是以HTTP/2设计的，还是有它的瓶颈所在，但是，这并不代表gRPC没有了价值，其最大的特点在于它的延迟。gRPC比ws延迟低了200ms左右，效果还是很明显。实际测试下来（套用CF），效果更加明显：

![](/images/wp-content/uploads/2021/05/202105081620010.jpg)

如果之前用的是[一键脚本](<https://www.idleleo.com/12/4876.html>)搭建的服务器，更新脚本后是可以无缝添加gRPC协议的（注意之前的配置）。gRPC协议可能会根据不同的网络环境有不同的延迟情况，不管怎么样。大家赶紧试试吧~
