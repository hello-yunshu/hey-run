+++
title = "IPv6 国内外优秀DNS推荐"
date = 2019-07-24T22:05:32+08:00
draft = true
description = "前段时间，笔者向大家介绍了如何启用IPv6：国内网络启用 IPv6 方法及注意事项。在文章中，笔者说明了如何开始IPv6隧道，其中便涉及到了IPv6 DNS的相关问题。现今，虽IPv6应用已然普遍，但IPv6的DNS发展却非常缓慢"
slug = "ipv6-guo-nei-wai-you-xiu-dnstui-jian"
featureimage = "/images/shared/201907151015.avif"
+++

![](/images/shared/201907151015.avif)

前段时间，笔者向大家介绍了如何启用IPv6：[国内网络启用 IPv6 方法及注意事项](https://www.idleleo.com/07/2596.html)。在文章中，笔者说明了如何开始IPv6隧道，其中便涉及到了IPv6 DNS的相关问题。现今，虽IPv6应用已然普遍，但IPv6的DNS发展却非常缓慢。因此，笔者便给大家罗列几个国内外优秀的DNS地址。

## IPv6 DNS列表

  * Google Public IPv6 DNS  
2001:4860:4860::8888  
2001:4860:4860::8844

  * Cloudflare IPv6 DNS  
2606:4700:4700::1111  
2606:4700:4700::1001

  * OpenDNS  
2620:0:ccc::2  
2620:0:ccd::2

  * Neustar UltraDNS IPv6  
2610:a1:1018::1  
2610:a1:1019::1  
2610:a1:1018::5

  * 北京邮电大学 IPv6 DNS 服务器  
2001:da8:202:10::36  
2001:da8:202:10::37

  * 上海交通大学 IPv6 DNS 服务器  
2001:da8:8000:1:202:120:2:100  
2001:da8:8000:1:202:120:2:101

  * 中科院网络信息中心 IPv6 DNS 服务器
  * Yeti DNS Project 注册的 IPv6 DNS 服务器  
2001:cc0:2fff:1::6666

  * 北京交通大学 IPv6 DNS 服务器
  * Yeti DNS Project 注册的 IPv6 DNS 服务器  
2001:da8:205:2060::188

  * 清华大学 IPv6 DNS 服务器
  * Yeti DNS Project 注册的 IPv6 DNS 服务器  
2001:da8:ff:305:20c:29ff:fe1f:a92a

  * 清华大学 TUNA 协会 IPv6 DNS 服务器  
2001:da8::666

  * 北京科技大学 IPv6 DNS 服务器  
2001:da8:208:10::6

  * 科技网 IPv6 DNS 服务器  
2001:cc0:2fff:2::6

  * 百度 IPv6 DNS  
2400:da00::6666

  * 下一代互联网北京研究中心  
Yeti DNS Project 注册的 IPv6 DNS 服务器  
240C::6666  
240C::6644

  * CNNIC IPv6 DNS 服务器  
2001:dc7:1000::1

## IPv6 DNS速度实测

测试数据来自互联网，测试环境为中国国内网络。

下一代互联网北京研究中心

240c::6666 20±ms

CNNIC IPv6 DNS 服务器

2001:dc7:1000::1 35±ms

百度 IPv6 DNS

2400:da00::6666 58±ms

科技网 IPv6 DNS 服务器

2001:cc0:2fff:2::6 超时

北京科技大学 IPv6 DNS 服务器

2001:da8:208:10::6 66ms

清华大学 TUNA 协会 IPv6 DNS 服务器

2001:da8::666 53±ms

清华大学 IPv6 DNS 服务器

Yeti DNS Project 注册的 IPv6 DNS 服务器

2001:da8:ff:305:20c:29ff:fe1f:a92a 超时

北京交通大学 IPv6 DNS 服务器

Yeti DNS Project 注册的 IPv6 DNS 服务器

2001:da8:205:2060::188 超时

中科院网络信息中心 IPv6 DNS 服务器

Yeti DNS Project 注册的 IPv6 DNS 服务器

2001:cc0:2fff:1::6666 超时

上海交通大学 IPv6 DNS 服务器

2001:da8:8000:1:202:120:2:100 81ms

北京邮电大学 IPv6 DNS 服务器

2001:da8:202:10::36 57ms

OpenDNS

2620:0:ccc::2 超时

Cloudflare IPv6 DNS

2606:4700:4700::1111 363±ms

Google Public IPv6 DNS

2001:4860:4860::8888 220±ms

国外测试环境数据不再展示，实际测试情况为：大多国内DNS服务延迟非常高，而国际DNS相对较低。因此，若是国内网络环境，推荐使用国内DNS；而国际环境的话，则使用国际DNS即可。**若使用tunnelbroker建议使用国际DNS** ，详见：[国内网络启用 IPv6 方法及注意事项](https://www.idleleo.com/07/2596.html)。
