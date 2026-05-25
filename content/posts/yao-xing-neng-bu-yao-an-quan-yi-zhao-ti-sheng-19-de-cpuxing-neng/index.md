+++
title = "要性能不要安全！一招提升19%的CPU性能"
date = 2020-02-22T16:11:57+08:00
draft = true
description = "去年5月份，英特尔处理器又双叒叕曝出了漏洞，僵尸负载漏洞（ZombieLoad）。利用该漏洞，恶意软件能直接从CPU窃取敏感信息。近期，僵尸负载漏洞又出现了变种升级版本，Zombieloadv2。"
slug = "yao-xing-neng-bu-yao-an-quan-yi-zhao-ti-sheng-19-de-cpuxing-neng"
featureimage = "https://cdn.idleleo.com/wp-content/uploads/2020/02/202002221556.jpg"
+++

去年5月份，英特尔处理器又双叒叕曝出了漏洞，僵尸负载漏洞（ZombieLoad）。利用该漏洞，恶意软件能直接从CPU窃取敏感信息。近期，僵尸负载漏洞又出现了变种升级版本，Zombieloadv2。

![](/images/wp-content/uploads/2020/02/202002221556.jpg)

对此，英特尔已经发布了微码更新，来缓解漏洞，而微软在2019年11月份系统更新中，将与漏洞相关的英特尔事务扩展技术（TSX）进行了禁用，虽然禁用了英特尔事务扩展技术（TSX）能够提高安全性，但是却会影响英特尔CPU的性能。对此，英特尔表示，修复了这个漏洞，只会导致CPU效能下滑19%，但是苹果在进行多线程负载测试和公共基准测试中，却发现性能降低高达40%。

这就有点坑爹了，2018年熔断和幽灵漏洞曝光的时候，修补也损失了些许性能，没想到一年过后相同的剧情又出现了。也许大家觉得系统越用越卡的原因就是在修补这些漏洞导致的性能下降。

![](/images/wp-content/uploads/2020/02/202002221559-1024x683.jpg)

那些CPU型号会受到影响呢？Haswell架构以前的处理器、低于45XX的处理器、R系列和K系列的处理器是**不受影响** 的，这些大概是2011年前的CPU，也就是说近几年市面上搭载英特尔处理器的电脑都会被降低性能。是不是很坑？对没错，就是很坑。

有没有办法把安装的补丁卸载而提高性能呢？有，这里就介绍一种办法。

## 具体操作步骤

1、win10用户右键开始菜单，选择“Windows PowerShell（管理员）”。

2、win7用户在开始菜单附件中，找到命令提示符，右键以管理员身份打开。

3、复制输入以下命令并回车，再重启下电脑，即可完成启用。
[code] 
    reg add "HKEY_LOCAL_MACHINESYSTEMCurrentControlSetControlSession ManagerMemory Management" /v FeatureSettingsOverride /t REG_DWORD /d 3 /f
    reg add "HKEY_LOCAL_MACHINESYSTEMCurrentControlSetControlSession ManagerMemory Management" /v FeatureSettingsOverrideMask /t REG_DWORD /d 3 /f/
[/code]

## 常见问题

**会不会影响安全？**

若使用的电脑涉及机密或者有人会想知道电脑内的秘密的话，不推荐吧。利用漏洞本身实现也不简单，再加上几乎大家的电脑没什么公网IP，普通朋友没什么必要担心安全。

**实际性能提高有多少？**

笔者的电脑在修改后，打开任务管理器时的CPU占用从100%下降到了93%了呢！
