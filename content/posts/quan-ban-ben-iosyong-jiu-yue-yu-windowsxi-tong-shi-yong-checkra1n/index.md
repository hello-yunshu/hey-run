+++
title = "全版本iOS永久越狱！Windows系统使用checkra1n"
date = 2020-02-16T22:35:46+08:00
draft = true
description = "其实checkra1n已经出了很久了，但是笔者一直都懒得说。原因一方面是iOS 12.4版本越狱有更加简单的办法，另一方面checkra1n的越狱需要用到macOS，虽然笔者家里有Mac，但很显然笔者更爱Windows。所以，就懒得提了。 但是，就在最近，checkra1n团队终于释放了Linux版"
slug = "quan-ban-ben-iosyong-jiu-yue-yu-windowsxi-tong-shi-yong-checkra1n"
featureimage = "/images/posts/quan-ban-ben-iosyong-jiu-yue-yu-windowsxi-tong-shi-yong-checkra1n/cover.avif"
+++

其实checkra1n已经出了很久了，但是笔者一直都懒得说。原因一方面是iOS 12.4版本越狱有更加简单的办法，~~另一方面checkra1n的越狱需要用到macOS，虽然笔者家里有Mac~~ ，但很显然笔者更爱Windows。所以，就懒得提了。

但是，就在最近，checkra1n团队终于释放了Linux版本的越狱工具。这下就简单了，其实偷偷告诉大家，笔者之前是用Windows模拟macOS给笔者iPhone越狱的。现在终于可以直接让自己的电脑运行Linux系统越狱了。Windows电脑运行Linux比运行macOS简单的多，所以笔者觉得是时候分享啦~

## 支持的版本

A5-A11的所有设备，也就是**iPhone 4S-iPhone X中的所有设备以及所有iOS版本** ，理论上之后的所有iOS版本也会支持，根据笔者实测iOS 14.6完美越狱。值得注意的是此次越狱设备重启后需要再越狱。

## 越狱使用的技术

这次用的是checkm8漏洞，这是一个Bootrom的漏洞，经常玩安卓的童鞋应该是对boot不陌生的。Bootrom漏洞是永久性，无法修补，要修复Bootrom的任何漏洞，都需要对硅芯片进行修正，这意味着对设备芯片组进行物理修改。如果没有回调或大规模替换，任何公司都无法修复。所以这次越狱就变成了永久性的，大家想升级iOS就升级，完全不用担心。

![](/images/posts/quan-ban-ben-iosyong-jiu-yue-yu-windowsxi-tong-shi-yong-checkra1n/cover.avif)

## 经常问的问题

**问：什么是checkra1n？**

答：checkra1n是一个社区项目，旨在基于['checkm8'bootrom](https://twitter.com/axi0mX/status/1177542201670168576)漏洞向所有人提供高质量的半[捆绑](https://twitter.com/axi0mX/status/1177542201670168576)式越狱。

**问：如何运作？**

答：[魔术。](http://iokit.racing/oneweirdtrick.pdf)

**问：如何使用？**

答：打开checkra1n应用程序，然后按照说明将设备置于DFU模式。从那时起，会自动神奇地产生危害，并且设备将启动进入越狱模式。如果您在没有Checkra1n的情况下重新启动设备，它将恢复为库存的iOS，并且您将无法使用已安装的任何第三方软件，直到您进入DFU并再次对设备进行Checkra1n。

**问：越狱安全吗？它会损害我的设备/清除我的数据吗？**

答：我们认为越狱是安全的，请采取预防措施以避免数据丢失。但是，与任何软件一样，可能会发生错误，并且* **不提供任何保修** *。我们建议您在运行checkra1n之前备份设备。

**问：我有一个问题要报告，我认为这与错误的调整无关。**

答：请[在此处](https://github.com/checkra1n/Bugreports/issues)检查并遵循错误报告模板。

**问：我丢失了密码。Checkra1n可以解密我的数据或访问锁定的设备吗？**

答：不可以。

**问：Windows支持何时发布？**

答：我们需要编写一个内核驱动程序来支持Windows（这是一段非常复杂的代码！），这将需要一些时间。不过请放心，我们正在为此努力。

## 简单越狱过程

这里笔者准备了非常简单的越狱方式。这个办法适合使用**Windows系统** 的电脑，若有Linux系统的电脑，直接去官网下载运行即可。

下载一键越狱文件夹中的所有东西。找一个8G容量以上的U盘。准备工作就做完了。

打开制作U盘启动.exe文件，第一个选择下载文件中的checkn1x-1.0.1.iso，第二个选择U盘（注意这个U盘会被清空所有内容）

![](/images/posts/quan-ban-ben-iosyong-jiu-yue-yu-windowsxi-tong-shi-yong-checkra1n/01.avif)

点击Flash！就可以自动开始制作带有Linux系统的U盘啦。

制作好之后重启电脑，进入BIOS界面，将启动顺序改为U盘先启动。

![](/images/posts/quan-ban-ben-iosyong-jiu-yue-yu-windowsxi-tong-shi-yong-checkra1n/02.avif)

大概就是上图的样子，不同的电脑有不同的启动方式，大家可以百度一下自己电脑的启动方式。选择刚刚制作的U盘启动，等待片刻就会直接进入checkra1n的界面，为了截图，笔者就给大家看虚拟机的画面吧~

![](/images/posts/quan-ban-ben-iosyong-jiu-yue-yu-windowsxi-tong-shi-yong-checkra1n/03.avif)

电脑接上需要越狱的iPhone，方向键选择start，按下回车键即可。注意之后需要根据提示进入DFU模式，相信大家还是有点英文基础的吧，笔者就不多说了。

越狱完成后桌面会有个checkra1n的应用，进入应用安装cydia越狱完成！

![](/images/posts/quan-ban-ben-iosyong-jiu-yue-yu-windowsxi-tong-shi-yong-checkra1n/04.avif)

若iPhone重启了，那么只需要再按照上述的越狱过程重新来一遍就行啦。确实有点麻烦哈，大家要是闲着没事可以直接安装个Linux双系统在电脑里面吧哈哈。

## 越狱工具下载

checkra1n(最新)：<http://dl.ix10.cn/EAC>

## 推荐阅读

[2020 iOS越狱软件源及插件推荐（自用）](https://www.idleleo.com/03/4485.html)
