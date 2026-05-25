+++
title = "Motrix - 无广告开源的全能下载器"
date = 2019-06-10T00:43:26+08:00
draft = true
description = "之前笔者介绍了一款老牌下载神器： Internet Download Manager (IDM) 破解版下载。现在笔者来介绍另一款适用于HTTP、FTP、BT、磁力链接以及下载百度网盘等资源的下载工具——Motrix。"
slug = "motrix---wu-guang-gao-kai-yuan-de-quan-neng-xia-zai-qi"
featureimage = "https://cdn.idleleo.com/wp-content/uploads/2019/06/Motrix-1.png"
+++

![](/images/wp-content/uploads/2019/06/Motrix-1.png)

之前笔者介绍了一款老牌下载神器： [Internet Download Manager (IDM) 破解版下载](<https://www.idleleo.com/05/2060.html>)。现在笔者来介绍另一款适用于HTTP、FTP、BT、磁力链接以及下载百度网盘等资源的下载工具——Motrix。

## Motrix介绍

Motrix界面设计的十分简约，对于追求简单，方便的用户是不可多得的软件。同时，Motrix支持多平台，Windows、macOS、Linux均支持。下载速度方面，经过笔者实测，以磁力链接为例，由于使用新技术，Motrix同比比特彗星、μTorrent等下载速度明显更快。尤其对于冷门资源，Motrix的下载速度甚至快于百度网盘的离线速度。

![](/images/wp-content/uploads/2019/06/20190609213838.jpg)

Motrix同时也支持下载百度网盘文件。下载方式通过安装Chrome插件实现。笔者在之前的文章：[百度网盘 不限速下载工具 (多)](<https://www.idleleo.com/03/1545.html>)中提过破解百度网盘限速的方式。现在可以通过Motrix达到下载的目的。

Motrix也支持暗黑模式，对于熬夜党来说是个不错的功能。

![](/images/wp-content/uploads/2019/06/20190609213903.jpg)

## 百度网盘插件

插件安装： [BaiduExporter.zip](<https://motrix.app/release/BaiduExporter.zip>)

下载 BaiduExporter.zip 之后，请解压到你喜欢的目录位置（以 ~/Documents 为例），解压到 ~/Documents/BaiduExporter 备用。

启动你的 Google Chrome，点击顶部菜单栏的「扩展程序」进入扩展程序管理页面；或者直接在地址栏输入 chrome://extensions/

点击右上角的「开发者模式」开关启用开发者模式

点击「加载已解压的扩展程序」，弹出目录选择框选择弹层，选择前面解压出来的 ~/Documents/BaiduExporter 目录。

确定之后，Google Chrome 会弹出桌面通知告诉你安装成功了。

打开百度网盘网页版，如果页面弹出“初始化成功！”的提示，并且在你的百度网盘网页版界面上还会出现一个「MO.app」的按钮，就说明浏览器扩展安装成功了。

## 支持 RPC 添加下载任务 

Motrix 默认开放了 Aria 2 的 JSON-RPC 支持，可以兼容所有支持 Aria2 的扩展插件或工具。默认的 RPC 端口为 16800，目前暂不支持修改。如果与其他应用的端口冲突，请避免同时使用，不然可能会无法正常使用 Motrix。

`URL: http://127.0.0.1:16800/jsonrpc`

`地址: 127.0.0.1 或者 localhost`

`端口: 16800`

`协议: HTTP`

## Motrix下载

官网地址： <https://motrix.app/>

Windows/Linux版下载：<https://github.com/agalwood/Motrix/releases>

macOS版使用brew安装：`brew update && brew cask install motrix`

由于官网下载太慢，也有百度网盘下载地址（需登录）：

[login]

链接：<https://pan.baidu.com/s/139Y_6I70KSuYWKSWShRg3A>

提取码：dcj9

[/login]
