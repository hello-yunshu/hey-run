+++
title = "利用内存加速系统 - PrimoCache 破解版"
date = 2019-05-04T18:22:39+08:00
draft = true
description = "笔者当时买电脑的时候，突发奇想，买了个16G内存的电脑。两年过去了，这16G内存除了在运行AE的时候勉强全部用完，平常根本用不到50%以上。这么大的内存对于在研究虚拟化系统的笔者来说，实在是浪费。于是，笔者又双叒叕突发奇想：既然Windows自带ReadyBoost这类功能加速HDD，那么为何不能利"
slug = "li-yong-nei-cun-jia-su-xi-tong---primocache-po-jie-ban"
featureimage = "/images/posts/li-yong-nei-cun-jia-su-xi-tong---primocache-po-jie-ban/cover.avif"
+++

笔者当时买电脑的时候，突发奇想，买了个16G内存的电脑。两年过去了，这16G内存除了在运行AE的时候勉强全部用完，平常根本用不到50%以上。这么大的内存对于在研究虚拟化系统的笔者来说，实在是浪费。于是，笔者又双叒叕突发奇想：既然Windows自带ReadyBoost这类功能加速HDD，那么为何不能利用大内存加速HDD甚至SSD呢？

![](/images/posts/li-yong-nei-cun-jia-su-xi-tong---primocache-po-jie-ban/cover.avif)

事实当然是可以的。众所周知，内存的速度远远快于硬盘的速度。但是内存数据断电即消失，因此不适合作为硬盘。其实内存也可以做硬盘，本文中的Primo Ramdisk便是将内存作为硬盘，只需在关机时重新将内存数据写入磁盘便可。当然数据安全性难以保证。

话不多说，咱们切入主题，下面便是两个利用大内存加速系统的软件，重点推荐PrimoCache，笔者自己用的也很开心。

## Primo Ramdisk

Primo Ramdisk 具有一系列强大的功能和选项以最大化性能，并使软件具有广泛的应用性。它提供了独特的内存管理特性，强大的文件系统支持以及完善的镜像文件功能，可以更好地满足各种需求。Primo Ramdisk 可应用于多个领域，尤其对于服务器系统、大型图像图形处理系统、实时监控分析系统等要求快速处理海量数据的应用环境效果显著。

## PrimoCache

### 功能介绍

PrimoCache是一款可以将物理内存、SSD硬盘或闪存盘等虚拟成硬盘缓存的软件。它可以自动将硬盘中读取的数据存入物理内存等速度较快的设备，当系统再次需要该数据时它可以很快从缓存设备中读取，而无需再次访问速度较慢的硬盘，从而有效提升物理硬盘的访问性能。PrimoCache支持将SSD硬盘作为传统机械硬盘的缓存，并且支持永久保持缓存内容，即计算机关机后缓存内容不会丢失。这个特性可以显著提升计算机的启动时间并加速应用程序的运行。 

PrimoCache也支持缓写功能，即可以将系统请求写入的数据先存入缓存设备中，在一定时间后再将数据从缓存设备写入物理硬盘中。缓写功能使系统的写入请求可以快速完成，从而极大地提升硬盘的写入性能。此外，PrimoCache支持使用系统未识别内存作为缓存设备，从而克服部分Windows操作系统对内存总量的限制（例如32位桌面Windows系统最大仅支持4GB内存），充分利用全部物理内存。 PrimoCache实现了多种缓存策略以及灵活的缓存设置，您可轻松为您的物理硬盘创建缓存，提高硬盘的读写性能。 

### 实际测试

经过笔者实际测试，笔者电脑为SSD盘做系统，外加HDD储存文件。在以SSD为主系统，使用4G的内存作为加速，效果明显。打开Chrome、PS等软件的速度提升明显。系统整体相应也得到了提高。

![](/images/posts/li-yong-nei-cun-jia-su-xi-tong---primocache-po-jie-ban/01.avif)

利用CrystalDiskMark进行磁盘基准测试，其结果令人咋舌。

![](/images/posts/li-yong-nei-cun-jia-su-xi-tong---primocache-po-jie-ban/02.avif)

笔者并没有配置二级缓存，据网友测试，开启二级缓存可以使命中率提高至99%，推荐大家试一试。

## 关于使用风险

对于内存来说，由于内存的特性，内存颗粒寿命远远大于SSD内存的寿命，因此根本不需要担心读写频率的增加影响内存寿命。

而对于SSD寿命而言，由于SSD的特性，对其影响最多的是写入量。有个网友做了测试：“我SSD用做二级缓写缓读经过计算一年也超不过5TB，而我SSD的寿命是300TB左右，这样的二级单纯计算读写保守都可以用75年。(我的是科普特500G,SSD)” 

诚如这位网友所说，由于均是类似4K的小文件，写入读取虽然频繁但整体量不大。大家完全可以放心使用。

## 破解下载

下载地址（PrimoCache v3.0.2、Primo Ramdisk 5.7.0）：

[login] 

正常版：

<https://pan.baidu.com/s/13RjVyS-IGoQF-1PgwW10Yw>

密码：5252 

server版：

<https://pan.baidu.com/s/1Z184tVL6leXtLavaQOp5eg>

密码：k79a

[/login] 

**破解方式已附在下载文件中！**
