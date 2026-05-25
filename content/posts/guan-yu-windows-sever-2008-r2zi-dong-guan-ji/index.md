+++
title = "关于Windows sever 2008 r2自动关机"
date = 2017-10-16T13:14:28+08:00
draft = true
description = "最近服务器老是宕机，检查了一下问题，发现是这两个导致的： 最近问题：刚刚建好网站后莫名其妙就连不上服务器，后来发现，服务器会自动关机，研究了一下发现是服务器系统激活问题。 以下一个可行的办法。 原因是Windows Licensing Monitoring Service服务 此服务是Windows"
slug = "guan-yu-windows-sever-2008-r2zi-dong-guan-ji"
featureimage = "https://cdn.idleleo.com/wp-content/uploads/2017/11/20171016124251.jpg"
+++

最近服务器老是宕机，检查了一下问题，发现是这两个导致的： **最近问题** ：刚刚建好网站后莫名其妙就连不上服务器，后来发现，服务器会自动关机，研究了一下发现是服务器系统激活问题。 以下一个可行的办法。[![](/images/wp-content/uploads/2017/11/20171016124251.jpg)](</images/wp-content/uploads/2017/11/20171016124251.jpg>) 原因是Windows Licensing Monitoring Service服务 此服务是Windows软件许可状态。任务管理器里是wlms.exe进程。此进程关闭了你的服务器。 利用PSTOOLS工具进入SYSTEM用户执行regedit.exe,修改WLSMS服务项，将启动类型由02（自动）改为04（禁用），并修改加载的服务程序位置，来解决问题。 相关工具：PSTOOLS，网上有下载的http://pstools.en.softonic.com/download;下载后将psexec.exe进程拷贝倒system32文件夹下，然后通过运行命令执行 命令格式：psexec.exe -d -i -s regedit.exe 后，选择agree，打开注册表定位到： [HKEY_LOCAL_MACHINESYSTEMCurrentControlSetServicesWLMS] 将start参数的值改成04即可，然后重启服务器，删除imagepath中的地址 重启电脑查看任务管理器是否还存在wlms.exe进程。 实测可行。当然还是推荐大家使用正版。 **长期问题** ：由于服务器在国外，故解析访问都不快，加之服务器容量小，服务器提供商本身也容易GG，故网站宕机可能性还挺大的。
