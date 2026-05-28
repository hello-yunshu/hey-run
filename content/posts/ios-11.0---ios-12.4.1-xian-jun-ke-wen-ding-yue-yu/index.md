+++
title = "iOS 11.0 - iOS 12.4.1 现均可稳定越狱"
date = 2019-08-20T11:20:12+08:00
draft = true
description = "现在iOS可越狱版本已经提高至iOS 12.4.1。此次越狱并非完美越狱，在重启手机后需要再次进入app激活。由于苹果越来越开放，越狱本身价值在一步步的减少。但如果你需要破解内购，安装不经过签名的app等不寻常的操作，那么越狱是你的必然选择。"
slug = "ios-11.0---ios-12.4.1-xian-jun-ke-wen-ding-yue-yu"
featureimage = "/images/posts/ios-11.0---ios-12.4.1-xian-jun-ke-wen-ding-yue-yu/cover.avif"
+++

![](/images/posts/ios-11.0---ios-12.4.1-xian-jun-ke-wen-ding-yue-yu/cover.avif)

现在iOS可越狱版本已经提高至iOS 12.4.1。此次越狱并非完美越狱，在重启手机后需要再次进入app激活。由于苹果越来越开放，越狱本身价值在一步步的减少。但如果你需要破解内购，安装不经过签名的app等不寻常的操作，那么越狱是你的必然选择。

## 越狱方法

下载unc0ver app以及Cydia Impactor（不同操作系统对应不同的版本）。

打开Cydia Impactor，注意必须装有iTunes才可。

![](/images/posts/ios-11.0---ios-12.4.1-xian-jun-ke-wen-ding-yue-yu/01.avif)

将下载的unc0ver app（.ipa文件）拖入红框中。软件会要求输入Apple ID以及密码。这是必须的过程，是为了申请临时证书。当然如果你有开发者证书可以跳过此步骤直接安装这个app。

![](/images/posts/ios-11.0---ios-12.4.1-xian-jun-ke-wen-ding-yue-yu/02.avif)

如上所述。由于使用临时证书，此app只有7天的使用时间。若是想继续使用，可以通过越狱后安装插件自动刷新证书，或者直接重装使用。

安装app后，在手机中直接打开并点击最显眼的按钮，非专业人士不需要去碰其他设置。

注意：此越狱支持iOS 11.0-12.4.1上的所有设备（A12-A12X运行iOS 12.1.3-12.4.1已经支持），支持iPhone 5S/SE/6/6P/6S/6SP/7/7P/8/8P/iPhone X(A12机型 Xr/Xs/XsMax现已经支持)

**V3.7.0~b1版本暂时有bug，在部分手机上可能会导致重启，建议使用其他版本。**

## 下载地址

unc0ver GitHub：[点我前往](https://github.com/pwn20wndstuff/Undecimus)

unc0ver官网：[点我前往](https://unc0ver.dev)

unc0ver工具下载： [点我下载](https://github.com/pwn20wndstuff/Undecimus/releases) V3.8.x正式版（英文原版）11.0-12.4.1

Cydia Impactor：[点我下载](http://cloud.abcydia.com/jailbreak/abcydia_Impactor_0.9.52.zip)   Win 0.9.52 (个人版安装工具)

Cydia Impactor：[点我下载](http://cloud.abcydia.com/jailbreak/abcydia_Impactor_0.9.52.dmg)   Mac 0.9.52 (个人版安装工具)

## 更新日志

v3.8.0 Pre-Release

  1. 添加对A12 iPhone的iOS 12.4.1支持（当前不支持iPad）

v3.5.3

  1. 在iOS 12.1.3,12.1.4,12.2和12.4上为A12-A12X设备添加WIP部分支持，支持将HSP＃4设置为TFP0，设置kernel_task信息，导出kernel_task端口，转储APTicket，记录KASLR shift和ECID以及禁用自动更新

V3.3.8

  1. 使用重写的SockPort 2.0漏洞，具有~100％的可靠性，~100毫秒的运行时间，并支持iOS 11.0-12.2上的所有设备（A12-A12X上的12.1.3-12.2除外）。
  2. 修复iOS 12.2 iPhone和iPod上的越狱。

V3.3.7

  1. 提高4K设备上Sock Port内核利用的可靠性。
