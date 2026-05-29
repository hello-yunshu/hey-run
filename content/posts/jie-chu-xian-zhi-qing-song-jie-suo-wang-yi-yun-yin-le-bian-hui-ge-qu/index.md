+++
title = "解除限制，轻松解锁网易云音乐变灰歌曲~"
date = 2019-06-15T20:53:20+08:00
draft = true
description = "由于版权意识的加强，现在听歌变得越来越麻烦。从产业角度看，版权意识的加强是利大于弊的。而对于我们个人来说，却是越来越麻烦。 网易云音乐是非常多的网友的选择，虽然音乐收入丰富，但是有些歌曲涉及到了版权的问题依然无法播放。这多少让人觉得麻烦。 下面介绍一个开源项目，来解决这个问题。笔者亲测可以使用。 项"
slug = "jie-chu-xian-zhi-qing-song-jie-suo-wang-yi-yun-yin-le-bian-hui-ge-qu"
featureimage = "/images/posts/jie-chu-xian-zhi-qing-song-jie-suo-wang-yi-yun-yin-le-bian-hui-ge-qu/cover.png"
+++

由于版权意识的加强，现在听歌变得越来越麻烦。从产业角度看，版权意识的加强是利大于弊的。而对于我们个人来说，却是越来越麻烦。

网易云音乐是非常多的网友的选择，虽然音乐收入丰富，但是有些歌曲涉及到了版权的问题依然无法播放。这多少让人觉得麻烦。

下面介绍一个开源项目，来解决这个问题。笔者亲测可以使用。

## 项目地址

<https://github.com/nondanee/UnblockNeteaseMusic>

## 功能特点

解锁网易云音乐客户端变灰歌曲！

使用网易云旧链 / QQ / 虾米 / 百度 / 酷狗 / 酷我 / 咕咪 / JOOX 音源替换变灰歌曲链接 (默认仅启用前四)。

为请求增加  X-Real-IP 参数解锁海外限制，支持指定网易云服务器 IP，支持设置上游 HTTP / HTTPS 代理。

完整的流量代理功能 (HTTP / HTTPS)，可直接作为系统代理 (同时支持 PAC)。

## 安装部署

如果自己有云服务器可以在服务器上部署。如果你只是在PC上听歌，那你可以按照下面的教程使用。

### Linux

依次执行一下命令即可。

`curl -o- https://raw.githubusercontent.com/creationix/nvm/v0.33.0/install.sh | bash`

`nvm install 10.16.0`

`git clone https://github.com/nondanee/UnblockNeteaseMusic.git`

`cd UnblockNeteaseMusic`

`npm install pm2 -g`

`npm install`

`pm2 start app.js`

这里不再多说明了。

### Windows

1）下载安装nodejs （官方地址：<https://nodejs.org/en/>）

2）安装完成后检查是否成功。

Win + R  然后输入 `cmd` 点击【确定】

然后输入 node -v 会显示nodejs版本号，有显示就说明nodejs安装成功了。

![](/images/posts/jie-chu-xian-zhi-qing-song-jie-suo-wang-yi-yun-yin-le-bian-hui-ge-qu/cover.png)

![](/images/posts/jie-chu-xian-zhi-qing-song-jie-suo-wang-yi-yun-yin-le-bian-hui-ge-qu/01.png)

3）下载项目源码到本地。

可以用git（需要安装git） 也可以直接下载zip包。

下载地址：<https://github.com/nondanee/UnblockNeteaseMusic/archive/master.zip>

将压缩包所有文件解压到任何一个目录，比如 D:/aaa（**注意记住路径** ）若只出现一个文件夹，则将文件夹内文件全部复制到创建的目录。

4）再次启动cmd,  注意这次一定要用管理员模式启动，因为还安装依赖包。

![](/images/posts/jie-chu-xian-zhi-qing-song-jie-suo-wang-yi-yun-yin-le-bian-hui-ge-qu/02.avif)

5）启动后，依次输入下面的命令来安装依赖包并启动服务。

（**若打开为Windows PowerShell(管理员)** 请先运行命令: `cmd`）

`cd D:aaa //"D:aaa"为刚刚压缩包解压的目录`

`npm install`

`node app.js -p 18080`

6）弹出提示  HTTP Server running @ http:_//0.0.0.0:18080  _就是启动成功了。

## 软件设置

1）下载安装网易云音乐客户端~

2）右上角【⚙】 – 【工具】 – 【Http代理】 – 点击【自定义代理】 – 下拉框选择【HTTP代理】

分别输入 服务器 和 端口 点击怕【确定】即可，会提示要重启客户端，重启即可。

![](/images/posts/jie-chu-xian-zhi-qing-song-jie-suo-wang-yi-yun-yin-le-bian-hui-ge-qu/03.avif)

3）使用前后结果对比。

![](/images/posts/jie-chu-xian-zhi-qing-song-jie-suo-wang-yi-yun-yin-le-bian-hui-ge-qu/04.avif)

![](/images/posts/jie-chu-xian-zhi-qing-song-jie-suo-wang-yi-yun-yin-le-bian-hui-ge-qu/05.avif)
