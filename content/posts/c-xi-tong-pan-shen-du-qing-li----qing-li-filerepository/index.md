+++
title = "C(系统)盘深度清理——清理FileRepository"
date = 2017-12-17T23:26:38+08:00
draft = true
description = "引言 许多朋友都会发现，Windows系统(以下简称Win系统)刚安装的时候，所占的体积不大；然而使用了一段时间后，系统盘的剩余空间就越来越小了，各种清理工具也未必能够把空间清出来。为什么Win系统所占体积会越来越大？其实除了大家熟知的缓存文件外，还有很多老旧的驱动文件，而这些驱动文件，系统自带的清"
slug = "c-xi-tong-pan-shen-du-qing-li----qing-li-filerepository"
featureimage = "/images/posts/c-xi-tong-pan-shen-du-qing-li----qing-li-filerepository/cover.avif"
+++

#### 引言

许多朋友都会发现，Windows系统(以下简称Win系统)刚安装的时候，所占的体积不大；然而使用了一段时间后，系统盘的剩余空间就越来越小了，各种清理工具也未必能够把空间清出来。为什么Win系统所占体积会越来越大？其实除了大家熟知的缓存文件外，还有很多老旧的驱动文件，而这些驱动文件，系统自带的清理功能，以及很多第三方清理工具，都是不会删掉的。

[![](/images/posts/c-xi-tong-pan-shen-du-qing-li----qing-li-filerepository/cover.avif)](/images/posts/c-xi-tong-pan-shen-du-qing-li----qing-li-filerepository/cover.avif)Win系统的老驱动会放到FileRepository目录中，体积可能出乎你意料

#### 体积大的原因

Win系统对于驱动文件，有这样的一个机制。Win系统会把第三方的驱动都放入到“C:WindowsSystem32DriverStoreFileRepository”目录中，当你安装新驱动的时候，新的驱动也会安装到这个目录。然而，用户安装新驱动的同时，Win系统并不会清理掉之前的老驱动，而是保留老驱动的文件，方便出问题的时候回滚到原来的版本。

![](/images/posts/c-xi-tong-pan-shen-du-qing-li----qing-li-filerepository/04.avif)图中标记的就为老驱动，而它实际占用800多m空间！

Win保留老驱动方便出问题回滚，这令驱动体积越来越大，虽然系统的可靠性提高了，但如果驱动更新得比较频繁，旧驱动文件所占的空间就会非常可观。例如如图NV的显卡驱动可能一个月更新两三次，每次都会残留数百M的老驱动文件，很多硬盘空间就被这样子占去了。如果想要删掉老驱动文件，又不能直接删掉FileRepository的文件，直接删FileRepository目录的文件很容易出问题。怎么办？

#### 解决办法

方法还是有的，原理很简单，如果我们能找出已经不用的老驱动，直接删除就完事了，但怎么找，删哪些就是问题，其实Win系统本身就有一个pnputil.exe工具，可以用来删掉FileRepository目录的老驱动。但这是一个命令行工具，使用很麻烦。所幸的是，有开发者为这个工具做了一个图形界面，名叫“**DriverStore Explorer** ”（下载见文末）。利用这个工具，很轻松就可以清掉系统盘的老驱动，一起来看看怎么用吧。

#### 如何使用

DriverStore Explorer是一个开源绿色软件，解压后，可以看到其中有一个“Rapr.exe”的文件，这个就是DriverStore Explorer的本体了。不过，不要直接运行这个文件，这个文件需要点击右键，选择“以管理员身份运行”，DriverStore Explorer才能够发挥作用。[![](/images/posts/c-xi-tong-pan-shen-du-qing-li----qing-li-filerepository/01.avif)](/images/posts/c-xi-tong-pan-shen-du-qing-li----qing-li-filerepository/01.avif)

DriverStore Explorer开启后，会自动扫描FileRepository目录下的文件，然后把驱动通通整理出来。在DriverStore Explorer界面中，可以看到各种驱动的不同版本，这些驱动对应的硬件、开发商、版本号、日期以及体积大小等信息，都会罗列出来。[![](/images/posts/c-xi-tong-pan-shen-du-qing-li----qing-li-filerepository/02.avif)](/images/posts/c-xi-tong-pan-shen-du-qing-li----qing-li-filerepository/02.avif)

想要删除老驱动，只需要点击界面左上角“Select Old”按钮，然后点击“Delete Package”按钮就可以了。如果删除失败，可以勾选“Force Deletion”。如果不确定目前系统正在使用的是哪个版本的驱动，可以通过设备管理器查询一下驱动的版本号或者看一下驱动对应的发行时间。

[![](/images/posts/c-xi-tong-pan-shen-du-qing-li----qing-li-filerepository/03.avif)](/images/posts/c-xi-tong-pan-shen-du-qing-li----qing-li-filerepository/03.avif)

删除后，你会发现Win系统大幅的减小，而站长我，也用这个办法清除了整整14G的垃圾文件。

_本文摘自互联网，部分内容paniy进行了修改完善。_

#### 相关下载

DriverStoreExplorer最新版下载：

<https://github.com/lostindark/DriverStoreExplorer/releases>
