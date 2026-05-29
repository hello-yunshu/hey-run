+++
title = "MySQL导入数据出错的解决办法"
date = 2020-04-13T15:37:07+08:00
draft = false
description = "最近笔者在折腾MySQL的时候出现些问题，在备份结构与数据时，导出简单轻松没什么问题，但将导出的数据再导入时，会出现如下表无法创建的情况。 问题复现"
slug = "mysqldao-ru-shu-ju-chu-cuo-de-jie-jue-ban-fa"
featureimage = "/images/posts/mysqldao-ru-shu-ju-chu-cuo-de-jie-jue-ban-fa/cover.avif"
categories = ["教程"]
tags = ["MySQL", "数据库", "故障排查"]
+++
> 旧文归档：本文记录的是一次 MySQL 导入失败的具体排查。不同 MySQL/MariaDB 版本的 SQL mode、字符集和默认约束可能不同，实际处理前请先备份数据，并根据当前报错逐项确认。

最近笔者在折腾MySQL的时候出现些问题，在备份结构与数据时，导出简单轻松没什么问题，但将导出的数据再导入时，会出现如下表无法创建的情况。

![](/images/posts/mysqldao-ru-shu-ju-chu-cuo-de-jie-jue-ban-fa/cover.avif)

## 问题复现

一开始，笔者很自然的觉得是在导出数据库时出现了问题，但几次导出并导入均无法顺利导入，而且奇怪的情况是每次导出导入时出错的表还不同。

遇到这种令人头大的问题时，笔者觉得可能是遇到MySQL的bug了。这就比较尴尬了，如果是MySQL的bug所致，那么短时间内恐怕是没什么办法修改更换MySQL了。

不过好在笔者发现之前在导出数据时均是选择的是数据+结构，而笔者在仅备份数据时却没有遇到这样的问题。于是，笔者就懂了，笔者打开了导出的数据，仔细研究了一下出错的表的的特征，笔者发现了下面一些不正常的数据：

![](/images/posts/mysqldao-ru-shu-ju-chu-cuo-de-jie-jue-ban-fa/01.avif)

如果对MySQL有一定研究的小伙伴一定会想到原因，没错sql_mode的严格模式。是这么回事，如果设置了严格模式，MySQL就无法插入0值的日期和时间，也就是NO_ZERO_IN_DATE、NO_ZERO_DATE产生的效果，由于导出的数据含有值为0的日期和时间，所以自然也就没法成功导入了。

## 解决办法

解决办法非常简单，在MySQL的配置文件中加入以下一行：
[code] 
    sql_mode='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION'
[/code]

如果不知道是否处于严格模式可以运行以下命令查询：
[code] 
    show variables like 'sql_mode';
[/code]

是不是很简单。。
