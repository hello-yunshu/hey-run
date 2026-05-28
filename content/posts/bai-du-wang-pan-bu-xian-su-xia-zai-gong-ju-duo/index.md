+++
title = "百度网盘 不限速下载工具 (多)"
date = 2019-03-07T23:49:38+08:00
draft = true
description = "百度网盘相信大家用的又爱又恨，其资源丰富，但是下载若不开启vip限速严重。百度vip价格并不便宜。为了互联网的开放精神，今天笔者（其实就是站长TAT）给大家带来几个简单的不限速下载工具。 在使用前，笔者不得不提醒一句，由于下载工具是对百度网盘的破解；又因为百度网盘自身限制部分文件下载需要登陆。故存在"
slug = "bai-du-wang-pan-bu-xian-su-xia-zai-gong-ju-duo"
featureimage = "/images/posts/bai-du-wang-pan-bu-xian-su-xia-zai-gong-ju-duo/cover.avif"
+++

百度网盘相信大家用的又爱又恨，其资源丰富，但是下载若不开启vip限速严重。百度vip价格并不便宜。为了互联网的开放精神，今天笔者（其实就是站长TAT）给大家带来几个简单的不限速下载工具。

在使用前，笔者不得不提醒一句，由于下载工具是对百度网盘的破解；又因为百度网盘自身限制部分文件下载需要登陆。故存在账号**被封** 的风险。所谓被封，即用几次后破解失效。故部分下载方式不推荐，您可以自行判断。

#### Proxyee Down

Proxyee Down 是一款开源的免费 HTTP 高速下载器，底层使用`netty`开发，支持自定义 HTTP 请求下载且支持扩展功能，可以通过安装扩展实现特殊的下载需求。 

![](/images/posts/bai-du-wang-pan-bu-xian-su-xia-zai-gong-ju-duo/cover.avif)

### 项目地址：

<https://github.com/proxyee-down-org/proxyee-down>

### 下载

  1. ~~[官网下载](http://pdown.org/releases.html)~~  
目前官网带宽非常低所以下载很慢，推荐用**OneDriver** 下载。
  2. [OneDrive 下载](https://imhx-my.sharepoint.com/:f:/g/personal/pd_imhx_onmicrosoft_com/EnPrybHS3rVFuy_HdcP7RLoBwhb0k5ayJdIzwjU0hCM9-A?e=he0oIz)  

_注：windows 下分 x86 和 x64 版本，x86 对应 32 位操作系统而 x64 对应 64 位操作系统，请根据自己操作系统选择正确版本下载,Linux 操作系统参考下面的 Linux 运行教程。_

### [](https://github.com/proxyee-down-org/proxyee-down/wiki/%E8%BD%AF%E4%BB%B6%E4%B8%8B%E8%BD%BD%E4%B8%8E%E8%BF%90%E8%A1%8C#%E8%BF%90%E8%A1%8C)运行

  * Windows:  
下载 Windows 版本的压缩包以后，将压缩包解压至任意目录，执行文件夹里的`Proxyee Down.exe`文件即可。 _注：360 可能会报毒，请将报毒文件加入白名单，或者直接卸载 360_

![](/images/posts/bai-du-wang-pan-bu-xian-su-xia-zai-gong-ju-duo/01.png)

  * macOS:  
下载 `macOS` 版本的压缩包之后，解压至任意目录，将目录内的 `Proxyee Down` 应用复制到 `Application`（或者 `应用程序`，取决于系统版本以及语言设定）文件夹，双击运行即可。 _注：如果启动闪退，把 APP 复制到其他目录即可正常运行；因为  `macOS` 切换代理以及安装证书需要管理员权限，所以每次应用启动时都会提示输入用户密码_

![](/images/posts/bai-du-wang-pan-bu-xian-su-xia-zai-gong-ju-duo/02.avif)

  * Linux:  
Linux 系统目前没有打原生包，要[下载 jar](https://github.com/proxyee-down-org/proxyee-down/releases) 包运行，需安装 `JRE` 或 `JDK`(要求版本不低于 `1.8`)，下载完成后在命令行中运行：`java -jar proxyee-down-main.jar `_注：如果使用  _`_openjdk_` _  的话需要安装 _`_openjfx﻿_`

#### BaiduPCS-Go

仿 Linux shell 文件处理命令的百度网盘命令行客户端。简单说是用GO语言编写的百度网盘客户端。为命令行下载不太适合新手。

GitHub地址：<https://github.com/iikira/BaiduPCS-Go>

### 特色

  * 多平台支持, 支持 Windows, macOS, linux, 移动设备等。
  * 百度帐号多用户支持; 
  * 通配符匹配网盘路径和 Tab 自动补齐命令和路径, [通配符_百度百科](https://baike.baidu.com/item/%E9%80%9A%E9%85%8D%E7%AC%A6);
  * 下载网盘内文件, 支持多个文件或目录下载, 支持断点续传和单文件并行下载;
  * 上传本地文件, 支持上传大文件(>2GB), 支持多个文件或目录上传;
  * 离线下载, 支持http/https/ftp/电驴/磁力链协议。

### 下载/运行

Go语言程序, 可直接在[发布页](https://github.com/iikira/BaiduPCS-Go/releases)下载使用。

如果程序运行时输出乱码, 请检查下终端的编码方式是否为 `UTF-8`。

使用本程序之前, 建议学习一些 linux 基础知识 和 基础命令。

如果未带任何参数运行程序, 程序将会进入仿Linux shell系统用户界面的cli交互模式, 可直接运行相关命令。

cli交互模式下, 光标所在行的前缀应为 `BaiduPCS-Go >`, 如果登录了百度帐号则格式为 `BaiduPCS-Go:<工作目录> <百度ID>$`

程序会提供相关命令的使用说明。

[](https://github.com/iikira/BaiduPCS-Go#windows)**Windows**

程序应在 命令提示符 (Command Prompt) 或 PowerShell 中运行, 在 mintty (例如: GitBash) 可能会有显示问题。

也可直接双击程序运行, 具体使用方法请参见 [命令列表及说明](https://github.com/iikira/BaiduPCS-Go#%E5%91%BD%E4%BB%A4%E5%88%97%E8%A1%A8%E5%8F%8A%E8%AF%B4%E6%98%8E) 和 [初级使用教程](https://github.com/iikira/BaiduPCS-Go#%E5%88%9D%E7%BA%A7%E4%BD%BF%E7%94%A8%E6%95%99%E7%A8%8B)。

[](https://github.com/iikira/BaiduPCS-Go#linux--macos)**Linux / macOS**

程序应在 终端 (Terminal) 运行。

具体使用方法请参见 [命令列表及说明](https://github.com/iikira/BaiduPCS-Go#%E5%91%BD%E4%BB%A4%E5%88%97%E8%A1%A8%E5%8F%8A%E8%AF%B4%E6%98%8E) 和 [初级使用教程](https://github.com/iikira/BaiduPCS-Go#%E5%88%9D%E7%BA%A7%E4%BD%BF%E7%94%A8%E6%95%99%E7%A8%8B)。

[](https://github.com/iikira/BaiduPCS-Go#android--ios)**Android / iOS**

_An droid / iOS 移动设备操作比较麻烦, 不建议在移动设备上使用本程序。_

安卓, 建议使用 [Termux](https://termux.com/) 或 [NeoTerm](https://github.com/NeoTerm/NeoTerm) 或 终端模拟器, 以提供终端环境。

示例: [Android 运行本项目程序参考示例](https://github.com/iikira/BaiduPCS-Go/wiki/Android-%E8%BF%90%E8%A1%8C%E6%9C%AC%E9%A1%B9%E7%9B%AE%E7%A8%8B%E5%BA%8F%E5%8F%82%E8%80%83%E7%A4%BA%E4%BE%8B), 有兴趣的可以参考一下。

苹果iOS, 需要越狱, 在 Cydia 搜索下载并安装 MobileTerminal, 或者其他提供终端环境的软件。

示例: [iOS 运行本项目程序参考示例](https://github.com/iikira/BaiduPCS-Go/wiki/iOS-%E8%BF%90%E8%A1%8C%E6%9C%AC%E9%A1%B9%E7%9B%AE%E7%A8%8B%E5%BA%8F%E5%8F%82%E8%80%83%E7%A4%BA%E4%BE%8B), 有兴趣的可以参考一下。

具体使用方法请参见 [命令列表及说明](https://github.com/iikira/BaiduPCS-Go#%E5%91%BD%E4%BB%A4%E5%88%97%E8%A1%A8%E5%8F%8A%E8%AF%B4%E6%98%8E) 和 [初级使用教程](https://github.com/iikira/BaiduPCS-Go#%E5%88%9D%E7%BA%A7%E4%BD%BF%E7%94%A8%E6%95%99%E7%A8%8B).[](https://github.com/iikira/BaiduPCS-Go#%E5%91%BD%E4%BB%A4%E5%88%97%E8%A1%A8%E5%8F%8A%E8%AF%B4%E6%98%8E)命令列表及说明。

#### 速盘SpeedPan

速盘是一款基于aria2技术，辅助用户下载百度网盘资源的网盘下载工具。除了具有百度网盘官方客户端相同的功能外，还拥有不限速下载等几个特色功能。 

![](/images/posts/bai-du-wang-pan-bu-xian-su-xia-zai-gong-ju-duo/03.avif)

### 特色功能

  1. 免登录下载和搜索分享的资源，避免封号；
  2. 管理自己百度网盘的资源；
  3. 速盘独有的黑科技加速技术。

### 下载和安装

**下载速盘**

如果你使用的Windows xp系统，请一定下载xp专用版。

安装版 [免费版](https://www.speedpan.com/speedpan-free.html)

**安装速盘**

如果你下载的是安装版，只需要根据步骤提示就可以轻松安装速盘。建议：将速盘安装到非系统盘。

如果你下载的是便携版（绿色免安装版），将下载的压缩文件释放都指定的文件夹就可以了。

![](/images/posts/bai-du-wang-pan-bu-xian-su-xia-zai-gong-ju-duo/04.avif)

#### PanDownload

一个类似与前两个下载器的工具，简约方面。

### 更新日志

v2.1.3

更新时间: 2019-08-22

更新内容:

  1. 新增批量转存功能
  2. 支持多账号文件搜索
  3. 优化使用体验及bug修复

### 下载地址

  * [本地下载](http://pandownload.com/)
