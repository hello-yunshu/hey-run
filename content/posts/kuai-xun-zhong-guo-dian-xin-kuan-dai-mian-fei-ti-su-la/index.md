+++
title = "快讯：中国电信宽带免费提速啦！！"
date = 2020-11-13T15:03:56+08:00
draft = true
description = "就在昨天，笔者在网上看到了电信宽带免费提速的消息，很快啊，笔者立刻起身，上来一个开电脑，再乱输一通命令，宽带速度居然真的立马就上去了。。。 如何提速 哈哈哈，不开玩笑了，确实有这么个活动。其实在之前疫情期间，电信就有免费的提速活动，后来疫情控制住了，也就没有了。没想到现在活动又出现了。这次有网友更是"
slug = "kuai-xun-zhong-guo-dian-xin-kuan-dai-mian-fei-ti-su-la"
featureimage = "/images/posts/kuai-xun-zhong-guo-dian-xin-kuan-dai-mian-fei-ti-su-la/cover.avif"
+++

就在昨天，笔者在网上看到了电信宽带免费提速的消息，很快啊，笔者立刻起身，上来一个开电脑，再乱输一通命令，宽带速度居然真的立马就上去了。。。

## 如何提速

哈哈哈，不开玩笑了，确实有这么个活动。其实在之前疫情期间，电信就有免费的提速活动，后来疫情控制住了，也就没有了。没想到现在活动又出现了。这次有网友更是直接把提速接口找到了，只需要在自家宽带的环境下，打开以下两个网址即可：

<http://znts.189.cn/xyface/xyspeedDev/isTs.jhtml>

<http://znts.189.cn/xyface/xyspeedDev/speedup.jhtml>

如果分别出现以下字段：
[code] 
    {"basicRateUp":"30","ip":"xxx","dialAcct":"xxxxx","basicRateDown":"200","state":0,"message":"提速预判成功"}
    {"state":1,"message":"提速成功"}
[/code]

这就意味着提速成功了。

也可以点击官方提供的网址：[点此链接参与提速](http://znts.189.cn/novfree/index.jsp)。

当然还有更加简单的办法啦。可以直接在电脑端输入以下命令：
[code] 
    curl -4 -c cookie.txt http://znts.189.cn/xyface/xyspeedDev/isTs.jhtml
    curl -4 -b cookie.txt http://znts.189.cn/xyface/xyspeedDev/speedup.jhtml
[/code]

如果有软路由或者Linux系统的小伙伴可以直接把命令添加到crontab，Windows系统的小伙伴可以添加计划任务，这样的话就可以无限免费提速啦！（Windows系统的小伙伴需要下载[curl的指令包](https://curl.se/windows/)喔~）

### **注意**

  * 一次操作只能提速7天，但可以无限重复操作。
  * 在IPv6环境下会失败，注意处在IPv4环境操作。
  * 必须是在需要提速的宽带网络下操作，否则是无效的。
  * 多线多播的请谨慎使用，根据网友反应提速反而会降低网速。。
  * 此次活动时间为2020年11月9日至12月31日。

## 实际测试

笔者家庭宽带速度为100M，经过提速下行速度可达到200M左右。根据网友测试，最快提速至500M，也就是说大于500M的宽带没有效果。

虽然下行提速力度一般，但上行就厉害了，笔者之前宽带上行速度20M，提速后达到100M，快了5倍！这对需要上传大文件的小伙伴简直是福音啊！

![](/images/posts/kuai-xun-zhong-guo-dian-xin-kuan-dai-mian-fei-ti-su-la/cover.avif)

大家快试试吧~~
