+++
title = "下载网页无法下载的富媒体"
date = 2018-02-05T21:14:04+08:00
draft = true
description = "绪论 本文介绍一个You-Get小程序。 You-Get 乃一小小哒命令行程序，提供便利的方式来下载网络上的媒体信息。 利用[code]you-get[/code]下载这个网页<"
slug = "xia-zai-wang-ye-wu-fa-xia-zai-de-fu-mei-ti"
featureimage = "https://cdn.idleleo.com/wp-content/uploads/2018/02/201825-300x154.jpg"
+++

#### 绪论

本文介绍一个[You-Get](<https://you-get.org/>)小程序。 [You-Get](<https://you-get.org/>) 乃一小小哒命令行程序，提供便利的方式来下载网络上的媒体信息。 [![](/images/wp-content/uploads/2018/02/201825-300x154.jpg)](</images/wp-content/uploads/2018/02/201825.jpg>) 利用[code]you-get[/code]下载[这个网页](<http://www.fsf.org/blogs/rms/20140407-geneva-tedx-talk-free-software-free-society>)的视频: 
[code] 
    $ you-get http://www.fsf.org/blogs/rms/20140407-geneva-tedx-talk-free-software-free-society
    Site:       fsf.org
    Title:      TEDxGE2014_Stallman05_LQ
    Type:       WebM video (video/webm)
    Size:       27.12 MiB (28435804 Bytes)
    
    Downloading TEDxGE2014_Stallman05_LQ.webm ...
    100.0% ( 27.1/27.1 MB) ├████████████████████████████████████████┤[1/1]   12 MB/s
[/code]

为什么你要好好的用You-get： 

  * 你欢喜于互联网上的富媒体内容，并为个人寻欢而储存
  * 你喜悦观看的视频，然而不得保存；对个人设备无从控制，此乃违背开放互联网之行为
  * 你寻求解脱于闭源软件或JavaScript代码，并禁止Flash运行
  * 你为黑客精神与自由软件而欣喜

[code]you-get[/code]之功用: 
  * 下载流行网站之音视频，例如YouTube, Youku, Niconico,以及更多. (查看[完整支持列表](<https://github.com/soimort/you-get/wiki/%E4%B8%AD%E6%96%87%E8%AF%B4%E6%98%8E#supported-sites>))
  * 于您心仪的媒体播放器中观看在线视频，脱离浏览器与广告
  * 下载您喜欢的网页上的图片
  * 下载任何非HTML内容，例如二进制文件

心动? [现在安装](<https://github.com/soimort/you-get/wiki/%E4%B8%AD%E6%96%87%E8%AF%B4%E6%98%8E#installation>) 并 [查看使用范例](<https://github.com/soimort/you-get/wiki/%E4%B8%AD%E6%96%87%E8%AF%B4%E6%98%8E#getting-started>). 使用Python编程？敬请查看 [源代码](<https://github.com/soimort/you-get>) 并fork! 

#### 安装

### 绪论

以下乃必要依赖，需要单独安装，除非于Windows下使用预包装包: 

  * **[Python 3](<https://www.python.org/downloads/>)**
  * **[FFmpeg](<https://www.ffmpeg.org/>)** (强烈推荐) or [Libav](<https://libav.org/>)
  * (可选) [RTMPDump](<https://rtmpdump.mplayerhq.hu/>)

### 选项 1: 通过pip安装

[code]you-get[/code]之官方版本通过[PyPI](<https://pypi.python.org/pypi/you-get>)分发, 可从PyPI镜像中通过[pip](<https://en.wikipedia.org/wiki/Pip_(package_manager)>) 包管理器安装. 须知您务必使用版本3的 [code]pip[/code]: 
[code]
    [code]$ pip3 install you-get[/code]
[/code]

### 选项 2: 使用预装包(仅供Windows)

[code]exe[/code] (单独文件) 或 [code]7z[/code] (包括所有依赖) 可从<https://github.com/soimort/you-get/releases/latest> 下载. 

### 选项 3: 于GitHub下载

您可选择[稳定版](<https://github.com/soimort/you-get/archive/master.zip>) (与PyPI最新版等同) 或 [开发版](<https://github.com/soimort/you-get/archive/develop.zip>) (更多的热补丁与不稳定功能)的[code]you-get[/code]. 解压并将含有[code]you-get[/code]的目录加入[code]PATH[/code]. 或者, 运行 
[code]
    [code]$ make install[/code]
[/code]

以安装[code]you-get[/code] 于永久路径. [code]$ git clone git://github.com/soimort/you-get.git[/code]
[/code]

将目录加入 [code]PATH[/code], 或运行 [code]make install[/code] 以安装[code]you-get[/code] 于永久路径. 

#### 升级

考虑到 [code]you-get[/code] 安装方法之差异, 请使用: 
[code]
    [code]$ pip3 install --upgrade you-get[/code]
[/code]

或下载最新更新: 
[code]
    [code]$ you-get https://github.com/soimort/you-get/archive/master.zip[/code]
[/code]

#### 开始

### 下载视频

当观赏感兴趣之视频，您可以使用 [code]--info[/code]/[code]-i[/code] 以查看所有可用画质与格式、s: 
[code]
    $ you-get -i 'https://www.youtube.com/watch?v=jNQXAC9IVRw'
    site:                YouTube
    title:               Me at the zoo
    streams:             # Available quality and codecs
        [ DEFAULT ] _________________________________
        - itag:          43
          container:     webm
          quality:       medium
          size:          0.5 MiB (564215 bytes)
        # download-with: you-get --itag=43 [URL]
    
        - itag:          18
          container:     mp4
          quality:       medium
        # download-with: you-get --itag=18 [URL]
    
        - itag:          5
          container:     flv
          quality:       small
        # download-with: you-get --itag=5 [URL]
    
        - itag:          36
          container:     3gp
          quality:       small
        # download-with: you-get --itag=36 [URL]
    
        - itag:          17
          container:     3gp
          quality:       small
        # download-with: you-get --itag=17 [URL]
[/code]

标有[code]DEFAULT[/code] 为默认画质。如认同，可下载: 
[code]
    $ you-get 'https://www.youtube.com/watch?v=jNQXAC9IVRw'
    site:                YouTube
    title:               Me at the zoo
    stream:
        - itag:          43
          container:     webm
          quality:       medium
          size:          0.5 MiB (564215 bytes)
        # download-with: you-get --itag=43 [URL]
    
    Downloading zoo.webm ...
    100.0% (  0.5/0.5  MB) ├████████████████████████████████████████┤[1/1]    7 MB/s
    
    Saving Me at the zoo.en.srt ...Done.
[/code]

(如YouTube视频带有字幕，将被一同下载，以SubRip格式保存.) 或，如您希望其他格式(mp4)，请使用其他提示选项: 
[code]
    [code]$ you-get --itag=18 'https://www.youtube.com/watch?v=jNQXAC9IVRw'[/code]
[/code]

**注意:**

  * 目前，格式选择没有大规模铺开；默认选项为最高画质.
  * [code]ffmpeg[/code]为必要依赖，以下载流式视频以及合并分块视频(例如，类似Youku), 以及YouTube的1080p或更高分辨率.
  * 如不希望[code]you-get[/code]合并视频，使用[code]--no-merge[/code]/[code]-n[/code].

### 下载其他内容

如你有URL，可以直接使用: 
[code]
    $ you-get https://stallman.org/rms.jpg
    Site:       stallman.org
    Title:      rms
    Type:       JPEG Image (image/jpeg)
    Size:       0.06 MiB (66482 Bytes)
    
    Downloading rms.jpg ...
    100.0% (  0.1/0.1  MB) ├████████████████████████████████████████┤[1/1]  127 kB/s
[/code]

或者, [code]you-get[/code]将自动检查网页，下载一切有可能感兴趣的内容: 
[code]
    $ you-get http://kopasas.tumblr.com/post/69361932517
    Site:       Tumblr.com
    Title:      kopasas
    Type:       Unknown type (None)
    Size:       0.51 MiB (536583 Bytes)
    
    Site:       Tumblr.com
    Title:      tumblr_mxhg13jx4n1sftq6do1_1280
    Type:       Portable Network Graphics (image/png)
    Size:       0.51 MiB (536583 Bytes)
    
    Downloading tumblr_mxhg13jx4n1sftq6do1_1280.png ...
    100.0% (  0.5/0.5  MB) ├████████████████████████████████████████┤[1/1]   22 MB/s
[/code]

**注意:**

  * 此功能为测试性，远未完成。对于类似Tumblr和Blogger的大图有效，但是没有办法为所有网站建立通用格式.

### 在Google Videos搜索并下载

[code]you-get[/code]可以吃任何东西. 如果不是合法的URL, [code]you-get[/code]将在Google查找并下载最相关视频. (可能不是最心仪的，但是很有可能) 
[code]
    [code]$ you-get "Richard Stallman eats"[/code]
[/code]

### 暂停与恢复下载

可以使用`Ctrl`+`C` 暂停下载. 临时的[code].download[/code]文件将保存于输出目录。下次使用[code]you-get[/code]传入相同参数时，下载将从上次继续开始. 如果下载已经完成 (临时的[code].download[/code] 扩展名消失), [code]you-get[/code]将忽略下载. 用[code]--force[/code]/[code]-f[/code]强行重下载. (**注意:** 将覆盖同名文件或临时文件!) 

### 设置输出文件名或路径

使用[code]--output-dir[/code]/[code]-o[/code] 设定路径, [code]--output-filename[/code]/[code]-O[/code] 设定输出文件名: 
[code]
    [code]$ you-get -o ~/Videos -O zoo.webm 'https://www.youtube.com/watch?v=jNQXAC9IVRw'[/code]
[/code]

**提示:**

  * 如果原视频标题含有与系统不兼容字符，十分有效.
  * 也可以帮助使用脚本批量下载于指定目录和文件名.

### 代理设置

使用 [code]--http-proxy[/code]/[code]-x[/code]为[code]you-get[/code]设置HTTP代理: 
[code]
    [code]$ you-get -x 127.0.0.1:8087 'https://www.youtube.com/watch?v=jNQXAC9IVRw'[/code]
[/code]

然而系统代理 (即系统变量[code]http_proxy[/code]) 自动使用. 使用[code]--no-proxy[/code]强行关闭. **提示:**

  * 如果经常使用代理 (网络封锁了部分网站), 考虑将[code]you-get[/code]和 [proxychains](<https://github.com/rofl0r/proxychains-ng>) 一同使用，并设置[code]alias you-get="proxychains -q you-get"[/code] (于命令行).
  * 对于某些网站(例如Youku), 如果你需要下载仅供中国大陆观看的视频, 可以使用 [code]--extractor-proxy[/code]/[code]-y[/code]单独为解析器设置代理. 可以使用 [code]-y proxy.uku.im:8888[/code] (鸣谢： [Unblock Youku](<https://github.com/zhuzhuor/Unblock-Youku>) 项目).

### 观看视频

使用 [code]--player[/code]/[code]-p[/code] 将视频喂进播放器, 例如 [code]mplayer[/code] 或者 [code]vlc[/code],而不是下载: 
[code]
    [code]$ you-get -p vlc 'https://www.youtube.com/watch?v=jNQXAC9IVRw'[/code]
[/code]

或者你想在浏览器中观看而不希望看广告或评论区: 
[code]
    [code]$ you-get -p chromium 'https://www.youtube.com/watch?v=jNQXAC9IVRw'[/code]
[/code]

**提示:**

  * 可以使用 [code]-p[/code] 开启下载工具,例如 [code]you-get -p uget-gtk 'https://www.youtube.com/watch?v=jNQXAC9IVRw'[/code], 虽然有可能不灵.

### 加载cookie

并非所有视频可供任何人观看。如果需要登录以观看 (例如, 私密视频), 可能必须将浏览器cookie通过[code]--cookies[/code]/[code]-c[/code] 加载入 [code]you-get[/code]. **注意:**

  * 目前我们支持两种cookie格式：Mozilla [code]cookies.sqlite[/code] 和 Netscape [code]cookies.txt[/code].

### 复用解析数据

使用 [code]--url[/code]/[code]-u[/code] 获得页面所有可下载URL列表. 使用 [code]--json[/code]以获得JSON格式. **警告:**

  * 目前此功能**未定型** ,JSON格式未来有可能变化.

#### 支持网站

[table id=2 /] 对于不在列表的网站，通用解析器将寻找并下载感兴趣之内容. 

#### 站长实测

站长我测试了国内一些视频网站，实际情况不乐观，部分网站并不能使用。 [![](/images/wp-content/uploads/2018/02/2018251-1024x534.jpg)](</images/wp-content/uploads/2018/02/2018251.jpg>) **需要注意图中红圈位置，在Windows下运行时，不可以加入$符号。**

_资源取自互联网，由idleleo.com整理_
