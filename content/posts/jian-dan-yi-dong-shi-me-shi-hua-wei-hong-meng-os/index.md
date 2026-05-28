+++
title = "简单易懂：什么是华为「鸿蒙 OS」"
date = 2019-08-09T23:03:01+08:00
draft = true
description = "2019年8月9日是笔者和傻梁在一起一周年的日子。 笔者和傻梁一起开开心心的出去玩，回家一看，错过了一个重要的事情。"
slug = "jian-dan-yi-dong-shi-me-shi-hua-wei-hong-meng-os"
featureimage = "/images/posts/jian-dan-yi-dong-shi-me-shi-hua-wei-hong-meng-os/cover.avif"
+++

2019年8月9日是笔者和傻梁**在一起一周年** 的日子。

![](/images/posts/jian-dan-yi-dong-shi-me-shi-hua-wei-hong-meng-os/cover.avif)

笔者和傻梁一起开开心心的出去玩，回家一看，错过了一个重要的事情。

2019年8月9日下午，华为正式发布了旗下的鸿蒙 OS。

![](/images/posts/jian-dan-yi-dong-shi-me-shi-hua-wei-hong-meng-os/01.avif)

笔者一开始觉得鸿蒙很可能仅仅是在Linux内核基础上改进的系统。

但没想到这鸿蒙是一个理念新颖、具有实力对抗已有系统的不可忽视的创举。

那么，究竟鸿蒙 OS 是什么呢？(以下部分来自互联网)

![](/images/posts/jian-dan-yi-dong-shi-me-shi-hua-wei-hong-meng-os/02.avif)

正如之前余承东所言，鸿蒙 OS 是**第一个打通全平台的系统** 。

不光电脑可用、手表可用、汽车可用、智能家居可用。

**如果未来安卓不再可用，手机上也随时可用。**

而且从安卓迁移到鸿蒙，只需 1-2 天时间。

对于为何要开发鸿蒙系统，余承东表示：

> 现有的安卓系统和各种分裂的 IoT 系统，并不能很好的适应 5G 时代下万物互联的背景。现在，我们迫切需要一个更强大的 OS 系统。它要适用所有设备、足够安全、足够快、足够简单易用。

## 全设备

这是华为鸿蒙 OS 的架构图，最底层是内核，上面是基础服务层和程序框架等。

通过这些东西，鸿蒙 OS 可以支撑不同的设备，运行不同的程序。

![](/images/posts/jian-dan-yi-dong-shi-me-shi-hua-wei-hong-meng-os/03.avif)

  * 一套系统、对应不同的设备。
  * 不同的设备又有性能强弱分别。

这就要求鸿蒙 OS 的内核极为精简。

在今天，不管是苹果 iOS 还是安卓，他们都基于 Linux、Unix 。

这样的内核极为庞大，安卓的操作系统有 1 亿行代码，仅内核一项，就超过 2000 万，非常复杂。

平常我们真正用的，只有 8% 的代码，如此庞大的设计很难保证流畅。

**所以，鸿蒙 OS 使用了微内核架构，以满足不同的设备。**

当然，这里的全平台并不仅仅指，鸿蒙 OS 可以在不同的设备上运行。

**还意味着，鸿蒙 OS 可以让这些设备连动起来。**

![](/images/posts/jian-dan-yi-dong-shi-me-shi-hua-wei-hong-meng-os/04.avif)

比如，我们的手表上没有摄像头，那就用手机的摄像头。

我们觉得 PC 上的摄像头不好，那就用手机上的。

**一个账户共享互用** ，系统硬件解耦，弹性部署。

简单来说，就是“苹果 iPhone、ipad、iMac、AirPods等设备协同”的升级版。

![](/images/posts/jian-dan-yi-dong-shi-me-shi-hua-wei-hong-meng-os/05.avif)

使用华为鸿蒙 OS ，也能做到。

## 更安全

使用微内核架构带来的好处还不止这些。微内核还会带来内核级安全体验。

传统系统在进行形式化验证时有个问题：

  * 编一行程序，形式化代码 100 行。
  * 那么 2000 万的宏内核，就是 20 亿形式化代码。

![](/images/posts/jian-dan-yi-dong-shi-me-shi-hua-wei-hong-meng-os/06.avif)

根本没法做，所以无法全面保证系统的安全。

但是微内核的内核小，可以实现形式化验证。确保每一行程序都能验证。

![](/images/posts/jian-dan-yi-dong-shi-me-shi-hua-wei-hong-meng-os/07.avif)

另外，微内核天然没有安卓系统一样的 Root 权限，所以在权限管理上更加优秀。

**鸿蒙系统内核、外核分离。** 图形、电源管理、内存管理等涉及安全的单独加锁。

就算你拿到了图像的“钥匙”，也拿不到内存管理的钥匙，更不能触及微核。

![](/images/posts/jian-dan-yi-dong-shi-me-shi-hua-wei-hong-meng-os/08.avif)

因此，鸿蒙 OS 能从源头提升安全级别。

按余承东的说法：目前操作系统安全级别一般是 2 级，最多 3-4 级。鸿蒙 OS 应该能达到 5 级，甚至 5+ 级。

## 更流畅

目前的安卓，沿用 Linux 内核的公平调度机制。

打个比方就是：货车、快车、自行车全都混乱的堵在公路上。很难保证用户体验。

![](/images/posts/jian-dan-yi-dong-shi-me-shi-hua-wei-hong-meng-os/09.avif)

但是鸿蒙 OS，通过确定时延引擎，可以实时匹配应用特征。

让快车去快车道、自行车到最慢的车道。优先响应低时延进程，保证用户流畅体验。

![](/images/posts/jian-dan-yi-dong-shi-me-shi-hua-wei-hong-meng-os/10.avif)

配合华为方舟编译器，安卓应用运行在鸿蒙 OS 上，**运行速度最快可提升 60%。**

![](/images/posts/jian-dan-yi-dong-shi-me-shi-hua-wei-hong-meng-os/11.avif)

同时，按华为的说法，鸿蒙 OS 的进程间通信效率，比现有系统高 3-5 倍。

![](/images/posts/jian-dan-yi-dong-shi-me-shi-hua-wei-hong-meng-os/12.avif)

## 更简单

目前，华为鸿蒙 OS 内核继承了 Linux 内核。

这意味着，鸿蒙 OS 可以运行现有的安卓程序，即拿即用。

![](/images/posts/jian-dan-yi-dong-shi-me-shi-hua-wei-hong-meng-os/13.avif)

通过华为提供的方舟编译器，多终端 IDE 环境，开发者还可**一次开发，可多终端部署。**

不需要开发完 A 品牌手机后，再适配 B 品牌手机。也不需要开发完手机应用后，再开发电脑应用。

举个例子：

  * 你在鸿蒙 OS 开发了一款手机音乐软件。
  * 放到汽车屏幕上，它就会自动横屏。
  * 放到更大的电视上，它会重新显示布局，自动适配。

![](/images/posts/jian-dan-yi-dong-shi-me-shi-hua-wei-hong-meng-os/14.avif)

这保证了鸿蒙生态能够健康发展。

## 鸿蒙的未来

鸿蒙从 2017 年开始做，直到今年，正式从内核变为 OS 。

它的首个使用产品将是明天发布的荣耀智慧屏。

![](/images/posts/jian-dan-yi-dong-shi-me-shi-hua-wei-hong-meng-os/15.avif)

到 2020 年，鸿蒙 OS 将升级为 2.0 版本。内核及应用架构均为自研。

应用产品为国产 PC 、手表手环、汽车。

![](/images/posts/jian-dan-yi-dong-shi-me-shi-hua-wei-hong-meng-os/16.avif)

2021 年后，鸿蒙 OS 3.0 将使用在音箱、耳机、VR 等产品。

从今天的发布会来看，鸿蒙 OS 在安全性、分布式能力、性能、面向未来的全场景方面，均强于现有安卓系统和 iOS 系统。

![](/images/posts/jian-dan-yi-dong-shi-me-shi-hua-wei-hong-meng-os/17.avif)

更重要的是，华为决定将鸿蒙 OS 开源。

![](/images/posts/jian-dan-yi-dong-shi-me-shi-hua-wei-hong-meng-os/18.avif)

看得出，华为想要汇聚全球开发者的力量。

曾经想要挑战现有系统的有很多，鸿蒙 OS 是理念最打动笔者的一个。

笔者在5G到来之初，便预言了新旧系统的洗牌时期已经到来。

现在看，也许，鸿蒙 OS 真的能成。
