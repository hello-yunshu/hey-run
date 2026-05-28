+++
title = "Edge浏览器(基于Chromium)正式稳定版泄露——浅谈浏览器"
date = 2019-08-22T21:00:01+08:00
draft = true
description = "如果你一直关心无主界的话，也许你觉得笔者最近“发了疯”，在疯狂的推送几乎同样的新闻。这不是没有原因的，最近关于Edge浏览器(基于Chromium)的新闻实在更新太快，导致笔者都来不及改文章内容。这不，刚刚发布了Beta版本的Edge浏览器马上就有正式版泄露出来了。 几个月前，微软收购了GitHub"
slug = "edgeliu-lan-qi-ji-yu-chromium-zheng-shi-wen-ding-ban-xie-lu----qian-tan-liu-lan-qi"
featureimage = "/images/posts/edgeliu-lan-qi-ji-yu-chromium-zheng-shi-wen-ding-ban-xie-lu----qian-tan-liu-lan-qi/cover.avif"
+++

如果你一直关心无主界的话，也许你觉得笔者最近“发了疯”，在疯狂的推送几乎同样的新闻。这不是没有原因的，最近关于Edge浏览器(基于Chromium)的新闻实在更新太快，导致笔者都来不及改文章内容。这不，刚刚发布了Beta版本的Edge浏览器马上就有正式版泄露出来了。

![](/images/posts/edgeliu-lan-qi-ji-yu-chromium-zheng-shi-wen-ding-ban-xie-lu----qian-tan-liu-lan-qi/cover.avif)

几个月前，微软收购了GitHub网站。正当笔者在考虑这笔收购有何益处时，没过多久，微软就宣布将基于Chromium开发新一代Edge浏览器。

![](/images/posts/edgeliu-lan-qi-ji-yu-chromium-zheng-shi-wen-ding-ban-xie-lu----qian-tan-liu-lan-qi/01.avif)

这个消息也许对普通人来说可能不算什么，但对于网站浏览器行业来说是意味深长。毕竟对于整个浏览器市场，已经许久没有新鲜血液的注入了。至于为什么说浏览器行业许久没有大动作，这需要从浏览器的历史说起。

#### 什么是Chromium

> Chromium是一个由Google主导开发的网页浏览器。以BSD许可证等多重自由版权发行并开放源代码。Chromium的开发可能早自2006年即开始，设计思想基于简单、高速、稳定、安全等理念，在架构上使用了Apple发展出来的WebKit排版引擎、Safari的部份源代码与Firefox的成果，并采用Google独家开发出的V8引擎以提升解译JavaScript的效率，而且设计了“沙盒”、“黑名单”、“无痕浏览”等功能来实现稳定与安全的网页浏览环境。Chromium是Google为发展自家的浏览器Google Chrome（以下简称Chrome）而开启的计划，所以Chromium相当于Chrome的工程版或称实验版（尽管Chrome自身也有β版阶段），新功能会率先在Chromium上实现，待验证后才会应用在Chrome上，故Chrome的功能会相对落后但较稳定。Chromium的更新速度很快,每隔数小时即有新的开发版本发布，而且可以免安装，下载zip封装版后解压缩即可使用（Windows下也有安装版）。Chrome虽然理论上也可以免安装，但Google仅提供安装版。 

事实上，即便很多国产浏览器不会主动告知用户它们使用的是Chromium，但大多都是基于它进行开发的。比如大名鼎鼎的360极速浏览器、世界之窗极速版、傲游浏览器和UC浏览器电脑版等。搜狗高速浏览器和QQ浏览器虽然官方不承认，但经过测试也极有可能用的是Chromium。

![](/images/posts/edgeliu-lan-qi-ji-yu-chromium-zheng-shi-wen-ding-ban-xie-lu----qian-tan-liu-lan-qi/02.avif)

所以我们不难发现，浏览器看似多种多样，功能也各有千秋。但回到根本，它们的核心均大同小异，唯一的区别在于Chromium的版本不同罢了。其实，如果你观察仔细，你很容易就会发现这类游览器呈现的页面十分类似，原因就是它们本身就是一个“母亲”的多个“儿子”。

#### 主流的几个浏览器内核

既然都谈到了Chromium，站长兼笔者觉得应该科普一下浏览器的内核。其实站长早就想科普一下浏览器的种种知识了，因为这不仅十分影响网站体验，还对上网的安全起到至关重要的作用。

### 什么是浏览器内核？

根据百度百科：浏览器最重要或者说核心的部分是“Rendering Engine”，可大概译为“渲染引擎”，不过我们一般习惯将之称为“浏览器内核”。负责对网页语法的解释（如标准通用标记语言下的一个应用HTML、JavaScript）并渲染（显示）网页。 所以，通常所谓的浏览器内核也就是浏览器所采用的渲染引擎，渲染引擎决定了浏览器如何显示网页的内容以及页面的格式信息。不同的浏览器内核对网页编写语法的解释也有不同，因此同一网页在不同的内核的浏览器里的渲染（显示）效果也可能不同，这也是网页编写者需要在不同内核的浏览器中测试网页显示效果的原因。

![](/images/posts/edgeliu-lan-qi-ji-yu-chromium-zheng-shi-wen-ding-ban-xie-lu----qian-tan-liu-lan-qi/03.avif)

简单说，网站只是一堆代码和些许富媒体文件。浏览器内核便是负责把这些代码、文件组合编译，最终以一种符合网站设计者要求的形态展示给访问者的工具。所以，大家明白了。为什么说一个浏览器核心很重要，就是这个原因。如果没有一个可靠、安全、快速的浏览器内核。不仅对于开发者来说是个灾难，对于普通用户来说，也是糟糕的体验。

### 有几种主流内核？

**Trident内核**

听上去好像大家完全不明所以。但是如果告诉它的成品，大家就会恍然大悟了。

Trident内核是微软在Mosaic代码的基础之上修改而来的。基于它，微软开发了IE浏览器。这个内核曾经风光无限，直到Windows 8都能见到它的身影（IE11），可以说是昔日王者。随着时间的推移，微软的懈怠逐渐导致内核性能已经跟不上时代发展。2005年，新一代W3C标准颁布，Trident再次错过，这成了IE浏览器被淘汰的导火索。接着，Trident内核的长期不更新导致安全事件频发，并逐渐消磨了开发者、用户的耐心，最终，出现了另一个重要的内核——Gecko。

**Gecko内核**

Gecko内核是一个完全开源的内核，其主要使用的浏览器是大名鼎鼎的Mozilla FireFox(火狐浏览器)。此内核由于开源特性使得它能很好的适配新的网页特性，因此获得了众多用户。

即便今天，Chromium一支独大。Gecko凭借Firefox仍能占领一部分市场份额。这是因为Gecko的渲染能力的确令人赞叹。作为站长，站长是推荐Firefox作为Chromium的第一替补浏览器的。

**Webkit内核**

可能大家都不会想到，这个不起眼的内核居然占领了手机端浏览器份额的大半。它是苹果公司自己研发的内核。iPhone、Mac上的自带浏览器Safari浏览器用的就是Webkit。

不得不说，这个浏览器内核效果也十分不错。有趣的是上述说到的Chromium一开始便是基于Webkit内核的，而无论Android亦是iOS，自带的浏览器均是基于Webkit内核，这便解释了为什么Webkit内核能占据移动端浏览器份额的半壁江山。

**Blink内核**

2013年谷歌宣布Chromium不再使用Webkit内核，转而使用自研的Blink内核。这一举动，直接或间接的使得Chromium成功问鼎。至于Blink内核怎么样，相信笔者已经无须赘述。如果你是一位网民，看到这里会发现自己或多或少的使用过Blink内核吧。

#### 微软的反击——Edge浏览器

以上对Trident内核的描述中，大家不难发现，微软似乎经历了浏览器的滑铁卢。事实确实如此，IE浏览器可谓是昨日黄花，市场份额与日俱减。作为曾经的老大哥，微软自然不能坐视不管。因此在Windows 10发布的同时，Edge浏览器进入大家的视野。

![](/images/posts/edgeliu-lan-qi-ji-yu-chromium-zheng-shi-wen-ding-ban-xie-lu----qian-tan-liu-lan-qi/04.avif)

Edge实际是浏览器的内核，同时它也是浏览器的名字。Edge在刚推出的时候，由于它前无古人的测试分数而闻名于网站开发者中。本来站长也被Edge描绘的未来所吸引，但事实无情的打了站长的脸。

随着正式版的推出，大家发现Edge并不像传闻中的那么美好。虽然Edge支持多种新特性，兼容过去的互联网协议，但正因为这种取舍导致了Edge“包袱”太重，在浏览网页时体验并不友好。其中最令人厌恶的就是打开网页的几秒白屏，严重影响了浏览体验。

于是随着时间的推移，这个雷声大雨点小的产品最终沦落为一款“pdf浏览器”、“用来下载Chrome”的工具。彻底丧失了它本身的作用。

#### Edge脱胎换骨的尝试

眼看Edge已然开始走起了IE的老路，微软开始有了新的动作。

这就要提到笔者在开篇所说的微软收购GitHub了。近期，最火的浏览器Chromium当之无愧。而Chromium的代码开源托管在GitHub上。微软又在近期收购了GitHub，这样一来似乎一切已经水到渠成。

**就在最近微软宣布以Chromium为基础开发新一代Edge浏览器。**

当笔者兼站长得知此消息时，也是吃惊了半天。因为这意味者Chromium的市场份额进一步上升、意味着未来微软可能会将一些Edge特性带入Chromium，最重要的，意味着Edge可能开始真正的好用了。

在宣布Edge基于Chromium打造后的一段时间，微软也正式开放了测试版的下载通道。

#### 基于Chromium的Edge简单测评

得知开放下载，笔者迫不及待的尝试一番。可以说，整体是令人满意的。

由于使用了Chromium，在网页渲染等各个方面较之原版Edge提升不止一点。又因为使用的Chromium版本要高于Chrome，因此在网上冲浪的体验上，笔者是认为优于Chrome的。

![](/images/posts/edgeliu-lan-qi-ji-yu-chromium-zheng-shi-wen-ding-ban-xie-lu----qian-tan-liu-lan-qi/05.avif)

又，大家都明白，由于政策的原因。Chrome在国内是不完整的体验。除非使用特殊手段，否则登陆谷歌账户都是问题，更别说跨平台同步之类的了。然而Edge没有这类的烦恼。由于使用的是微软账号，对于Windows用户十分友好，又因为基于Chromium，因此可以无缝从Chrome导入收藏甚至是密码（这有些可怕）。这是Chrome所达不到的。

综上所述，即便是测试版，站长在现阶段是推荐大家使用基于Chromium的Edge浏览器的。确实不错，站长自己也在用。**现在的Edge测试版及泄露出的正式版均已经完全支持中文。**

#### Edge最新正式稳定版下载

Chromium版Edge浏览器目前**已经提供了Beta版本** ，同时也有**正式版泄露** 出来，另外还有Dev和Canary版本。正式版最为稳定，但考虑到为泄露版本不一定能受到完整支持，因此Beta版本更为稳定，Dev版是一周时间里获得改进的版本，比Canary更稳定；Canary版本则几乎每天都会更新，可以最先体验最新进展，当然后两者稳定性通常不如Beta版本。

以下是微软官方下载地址。

下载：[点击链接](https://www.microsoftedgeinsider.com/en-us/download) 也有可以直接下载Beta版本：[点击链接](https://www.microsoftedgeinsider.com/zh-cn/)

**这里还有泄露的正式版** ：[点此链接](https://go.microsoft.com/fwlink/?linkid=2069324&Channel=Stable&language=cn)

![](/images/posts/edgeliu-lan-qi-ji-yu-chromium-zheng-shi-wen-ding-ban-xie-lu----qian-tan-liu-lan-qi/06.avif)

微软宣布Edge Beta版本提供以下功能：

  * 微软内置的Bing搜索功能可以智能地连接组织人员，文档，站点，位置和对话，从而减少在工作中寻找工作所花费的时间。
  * IE模式，通过将Internet Explorer 11兼容性直接引入Microsoft Edge浏览器，简化了当下通过两种不同浏览器查看Web体验，创建更加简单的体验。对于同时使用IE和其他浏览器的全球60％以上的组织而言，这是一项重要功能。
  * Windows Defender Application Guard有助于隔离企业定义的不受信任的站点，在员工浏览网络时保护公司。
