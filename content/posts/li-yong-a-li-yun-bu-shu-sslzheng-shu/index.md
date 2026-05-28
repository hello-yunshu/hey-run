+++
title = "利用阿里云部署ssl证书"
date = 2017-10-16T15:20:49+08:00
draft = true
description = "首先你最好用阿里云的解析方案，这样能直接帮你自动生成证书解析等。 之后，进入阿里云，点击产品-安全-CA证书服务，如图： 点击立即购买，选择免费型DV SSL（一般个人站点选此即可，其他根据实际情况自行选择）： 然后完成支付后按以下流程进行即可："
slug = "li-yong-a-li-yun-bu-shu-sslzheng-shu"
featureimage = "/images/posts/li-yong-a-li-yun-bu-shu-sslzheng-shu/cover.avif"
+++

首先你最好用阿里云的解析方案，这样能直接帮你自动生成证书解析等。 之后，进入阿里云，点击产品-安全-CA证书服务，如图： ![](/images/posts/li-yong-a-li-yun-bu-shu-sslzheng-shu/cover.avif) 点击立即购买，选择免费型DV SSL（一般个人站点选此即可，其他根据实际情况自行选择）： ![](/images/posts/li-yong-a-li-yun-bu-shu-sslzheng-shu/01.avif) 然后完成支付后按以下流程进行即可： ![](/images/posts/li-yong-a-li-yun-bu-shu-sslzheng-shu/02.avif) **注意** ，在签发证书后，需要将指定证书下载至服务器部署，同时，阿里云亦支持上传已有的证书。若部署证书出现问题可以参考：[关于：启用Include conf/extra/httpd-ssl.conf出错](https://www.idleleo.com/2017/10/16/关于：启用include-confextrahttpd-ssl-conf出错/)
