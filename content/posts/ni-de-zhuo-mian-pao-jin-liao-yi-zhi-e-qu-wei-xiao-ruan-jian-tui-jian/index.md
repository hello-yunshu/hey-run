+++
title = "你的桌面跑进了一只鹅！趣味小软件推荐"
date = 2020-04-03T20:14:33+08:00
draft = true
description = "今天笔者给大家推荐一款电脑的趣味小插件——DesktopGoose。就如软件名称“桌面鹅”所说，这款软件是一个桌面宠物养成类的小软件。话不多说，我们一起来看看这款软件到底是怎么样的吧。 软件简介 软件分为Windows版和MacOS版，不需要安装，直接下载运行即可。这里以Windows版本为例："
slug = "ni-de-zhuo-mian-pao-jin-liao-yi-zhi-e-qu-wei-xiao-ruan-jian-tui-jian"
featureimage = "https://cdn.idleleo.com/wp-content/uploads/2020/04/20200403191034-1024x510.jpg"
+++

今天笔者给大家推荐一款电脑的趣味小插件——DesktopGoose。就如软件名称“桌面鹅”所说，这款软件是一个桌面宠物养成类的小软件。话不多说，我们一起来看看这款软件到底是怎么样的吧。

## 软件简介

软件分为Windows版和MacOS版，不需要安装，直接下载运行即可。这里以Windows版本为例：

![](/images/wp-content/uploads/2020/04/20200403191034-1024x510.jpg)

运行图中`GooseDesktop.exe`文件即可，运行后会在电脑后台自动运行此程序。注意，这个程序不会以出现窗口或者任务栏图标。需要关闭这程序只能调用任务管理器或者运行上图中的`Close Goose.bat`文件。（是不是有小伙伴想到了恶搞同伴的办法。。嘿嘿🤭）

![](/images/wp-content/uploads/2020/04/20200403191705.jpg)

运行完后，桌面就会出现如图的一个鹅（鸭？）啦~ 那么重点来了，这只看上去萌萌的鹅能做什么呢？放心，这只鹅要是只能傻站在哪里，负责任的笔者怎么会推荐给大家呢。

![](/images/wp-content/uploads/2020/04/20200403192322-1024x455.jpg)偶尔拖出一个文本框

![](/images/wp-content/uploads/2020/04/20200403192147-1024x454.jpg)追着鼠标跑

这头蠢萌的鹅看上去人畜无害，但却并不好惹。有时候它会拖出一些奇奇怪怪的文本框和图片，如果你把那些无故出现的窗口关掉，这头蠢鹅就会追着你的鼠标跑，你以为就只是追着鼠标跑就完事了吗？并不是，如果它追上你的鼠标，还会咬着你的鼠标平移！对，你没看错，它会让你无法控制你的鼠标。

## 自定义配置

看到这里大家是不是想试一试这头“可爱”的鹅了呢？根据笔者进一步的研究，这款小软件可以一定程度的定制内容。定制的功能在`config.ini`文件中。下面是文件的代码，笔者稍微翻译了一下：
[code] 
    Version_DoNotEdit=1 //笔者也不知道是啥
    EnableMods=False //是否开启mod(鹅会变成🌈鹅)
    SilenceSounds=False //是否静音
    Task_CanAttackMouse=True //是否攻击鼠标
    AttackRandomly=False //是否随机攻击鼠标
    UseCustomColors=False //自定义鹅的颜色(以下修改需要先改此条)
    GooseDefaultWhite=#ffffff //鹅的身体颜色
    GooseDefaultOrange=#ffa500 //鹅的橘黄色
    GooseDefaultOutline=#d3d3d3 //鹅的边框颜色
    MinWanderingTimeSeconds=20 //最小闲逛时间
    MaxWanderingTimeSeconds=40 //最大闲逛时间
    FirstWanderTimeSeconds=20 //最初闲逛时间
[/code]

大家快来让自己的桌面成为养鹅厂吧~

## 更新内容

**0.3更新：**

- **新的官方改装API  ！**加入Discord**[discord.gg/xZFRmPT](<https://t.co/DP3C2342uT?amp=1>)** 并检查#goose-mods频道以获取更多有关此信息:-D

- **您自己未发表的文字！** 添加任何您想要的记事本短语，鹅就会把它们拉起来！

- **新的配置切换！** 进一步自定义鹅的行为，使音频静音，等等！

**从0.2开始：**

- 无限模因！将任何所需的模因放入资产文件夹中！鹅会带来它们。

- 添加了GIF支持！

- 配置鹅！更改config.goos文件中的属性（在记事本中打开它）以调整他的攻击性!)

## 资源下载

作者官网下载：

<https://samperson.itch.io/desktop-goose>

网盘下载：

<https://www.lanzous.com/iaw9n9i>
