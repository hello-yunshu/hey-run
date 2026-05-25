+++
title = "插件 WP Admin Boost 正式发布！"
date = 2021-01-22T21:48:01+08:00
draft = true
description = "经过笔者也就是站长3个小时的努力，一个崭新的插件诞生啦！在此再次感谢WP中国本土化社区与jsdelivr.com，虽然没有主动为笔者提供帮助，但笔者“强行”获得了帮助哈哈。 插件项目 WP-Admin-Boost {{CO"
slug = "cha-jian-wp-admin-boost-zheng-shi-fa-bu"
featureimage = "https://img.shields.io/github/issues/paniy/WP-Admin-Boost"
+++

经过笔者也就是站长3个小时的努力，一个崭新的插件诞生啦！在此再次感谢[WP中国本土化社区](<https://wp-china.org/>)与[jsdelivr.com](<https://www.idleleo.com/go?url=http://jsdelivr.com>)，虽然没有主动为笔者提供帮助，但笔者“强行”获得了帮助哈哈。

## 插件项目

[WP-Admin-Boost](<https://github.com/paniy/WP-Admin-Boost>)

{{CODEshieldsio}}

[![GitHub issues](https://img.shields.io/github/issues/paniy/WP-Admin-Boost)](<https://github.com/paniy/WP-Admin-Boost/issues>)  [![GitHub forks](https://img.shields.io/github/forks/paniy/WP-Admin-Boost?color=%230885ce)](<https://github.com/paniy/WP-Admin-Boost/network>)  [![GitHub stars](https://img.shields.io/github/stars/paniy/WP-Admin-Boost?color=%230885ce)](<https://github.com/paniy/WP-Admin-Boost/stargazers>)  [![GitHub license](https://img.shields.io/github/license/paniy/WP-Admin-Boost)](<https://github.com/paniy/WP-Admin-Boost/blob/main/LICENSE>)

WordPress官方平台不肯认证，核心文件不允许外链。。哭了。

## 插件功能

使用jsdelivr加速WordPress的后台核心小文件与插件小文件，大幅提高后台访问速度。支持自定义加速插件。

使用的方法与上篇文章[《WordPress后台加速 – 使用CDN替代本地小文件》](<https://www.idleleo.com/01/4975.html>)所提供的代码类似，如果对原理有兴趣，欢迎点击访问。上篇文章描述非常详细。

## 安装方式

可以进入GitHub项目下载最新Release。在WordPress插件安装界面，选择安装插件—>上传插件，选择下载的最新Release，上传安装启用即可。

![](/images/wp-content/uploads/2021/01/20210122205901-1024x428.jpg)

卸载可以进入插件，找到WP Admin Boost，点击禁用再点击删除即可。

## 插件截图

![](/images/wp-content/uploads/2021/01/20210122203422-1024x507.jpg)

## 注意事项

此插件会直接加速后缀为css、js、woff、woff2、jpg、png、gif、svg、webp的全部文件，**请勿使用测试版** 插件，请仔细检查加速后是否兼容（比如一些不在WordPress官方平台上的）。可以通过浏览器的Console报错检查兼容性。

![](/images/wp-content/uploads/2021/01/20210122215425-1024x209.jpg)

如果在Console出现小文件下载报错，那说明此小文件所在的插件并不支持加速，请在插件的设置界面将插件禁用加速，再刷新即可。

此插件与jsdelivr无关，jsdelivr造成的意外损失与本插件无关。

## 文章推荐

[WordPress后台加速 – 使用CDN替代本地小文件](<https://www.idleleo.com/01/4975.html>)
