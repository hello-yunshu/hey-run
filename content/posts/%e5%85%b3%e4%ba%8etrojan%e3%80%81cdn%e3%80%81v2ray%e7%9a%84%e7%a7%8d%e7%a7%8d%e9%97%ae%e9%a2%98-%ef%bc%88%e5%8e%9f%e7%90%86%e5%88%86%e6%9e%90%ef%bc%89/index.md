+++
title = "关于Trojan、CDN、V2Ray的种种问题 （原理分析）"
date = 2020-03-11T23:48:57+08:00
draft = true
slug = "%e5%85%b3%e4%ba%8etrojan%e3%80%81cdn%e3%80%81v2ray%e7%9a%84%e7%a7%8d%e7%a7%8d%e9%97%ae%e9%a2%98-%ef%bc%88%e5%8e%9f%e7%90%86%e5%88%86%e6%9e%90%ef%bc%89"
featureimage = "/images/posts/%e5%85%b3%e4%ba%8etrojan%e3%80%81cdn%e3%80%81v2ray%e7%9a%84%e7%a7%8d%e7%a7%8d%e9%97%ae%e9%a2%98-%ef%bc%88%e5%8e%9f%e7%90%86%e5%88%86%e6%9e%90%ef%bc%89/cover.avif"
+++

最近笔者鼓捣了一段时间Trojan，对Trojan有了些新的认知。在笔者的《[V2Ray / Trojan 传输方式哪个好？(原理对比)](https://www.idleleo.com/02/4064.html)》的文章中，已经一定程度的对Trojan有了初步的认知。现在我们用提问的方式来一起更加“深入”的了解Trojan的本质吧~

#### Trojan能使用CDN吗？

答：不能。

很不幸，Trojan开发者非常明确的说明了不支持反向代理连接到Trojan。由于这种特性，导致Trojan无法直接隐藏在反向代理之后，同时亦不能使用反向代理达到多个不同协议的同时使用。因此对于CDN而言，由于使用了反向代理的技术，Trojan自然亦不支持套用CDN。这点笔者觉得甚是可惜。

![](/images/posts/%e5%85%b3%e4%ba%8etrojan%e3%80%81cdn%e3%80%81v2ray%e7%9a%84%e7%a7%8d%e7%a7%8d%e9%97%ae%e9%a2%98-%ef%bc%88%e5%8e%9f%e7%90%86%e5%88%86%e6%9e%90%ef%bc%89/cover.avif)

笔者知道大家在想什么，如果不支持反向代理，那么是否会使得Trojan容易被识别呢？答：不至于。因为Trojan不支持反向代理只是局限于对自身的协议而言。对于普通协议，Trojan是支持反向代理的。也就是说，对于访问网站这类流量，即便使用了CDN，依然可以正常访问。

那么为什么不支持呢？笔者查找了所有已知公开文档，并没有找到原因说明（估计也不会有哈哈）。笔者推测，在流量经过反向代理后失去了一部分Trojan的特征信息；或者在经过反向代理后，由于增加了部分信息而导致Trojan判断为其他流量。总之，无论何种情况，一旦Trojan处于反向代理的后端，那么Trojan将变为一个性能低下的实打实的“web服务器”，这也就失去了它的真正功能。

#### Trojan与V2Ray可以共存吗？

答：可以。

刚刚笔者说明了Trojan是无法作为反向代理后端的。但是，Trojan本身一定程度起到了“反向代理”的功能。因此可以通过Trojan使其他流量发送至另外的`HTTP`服务器或者V2Ray，也就是下图中的`remote_addr`、`remote_port`两处配置。

![](/images/posts/%e5%85%b3%e4%ba%8etrojan%e3%80%81cdn%e3%80%81v2ray%e7%9a%84%e7%a7%8d%e7%a7%8d%e9%97%ae%e9%a2%98-%ef%bc%88%e5%8e%9f%e7%90%86%e5%88%86%e6%9e%90%ef%bc%89/01.avif)

通过这种方式，可以利用Trojan将流量转发至nginx再经由nginx转发至V2Ray，实现Trojan、网站、V2Ray三者共存的情况。但就如笔者《[V2Ray / Trojan 传输方式哪个好？(原理对比)](https://www.idleleo.com/02/4064.html)》一文中的描述，Trojan由于多一个判断和转发过程，使得被转发的V2Ray和网站性能低下。根据实际测试，V2Ray表现明显下降。因此，虽然这种方式在理论上完全行得通，但是实际体验并不友好，笔者不推荐。

#### Trojan与V2Ray协议是否一致？

答：几乎完全一致。

笔者对Trojan、V2Ray以及正常的网站访问进行了抓包。

首先为Trojan：

![](/images/posts/%e5%85%b3%e4%ba%8etrojan%e3%80%81cdn%e3%80%81v2ray%e7%9a%84%e7%a7%8d%e7%a7%8d%e9%97%ae%e9%a2%98-%ef%bc%88%e5%8e%9f%e7%90%86%e5%88%86%e6%9e%90%ef%bc%89/02.avif)Trojan

其次为V2Ray：

![](/images/posts/%e5%85%b3%e4%ba%8etrojan%e3%80%81cdn%e3%80%81v2ray%e7%9a%84%e7%a7%8d%e7%a7%8d%e9%97%ae%e9%a2%98-%ef%bc%88%e5%8e%9f%e7%90%86%e5%88%86%e6%9e%90%ef%bc%89/03.avif)V2Ray

最后为正常网站：

![](/images/posts/%e5%85%b3%e4%ba%8etrojan%e3%80%81cdn%e3%80%81v2ray%e7%9a%84%e7%a7%8d%e7%a7%8d%e9%97%ae%e9%a2%98-%ef%bc%88%e5%8e%9f%e7%90%86%e5%88%86%e6%9e%90%ef%bc%89/04.avif)正常网站

不难看出，三者在握手、连接、传输的过程中几乎找不出差别。由于笔者懒得进行中间人攻击哈哈，因此没有对`TLS`解包，所以传输内部封装情况还是暂时未知。不过根据已知的协议设计可知，Trojan与V2Ray的协议设计差别是很大的。Trojan内部封装的协议类似于`SOCKS5`，这也就解释了为什么Trojan客户端需要使用`SOCKS5`的原因。

#### Trojan究竟是什么？

答：笔者觉得，Trojan在作为服务器的部分更像是一个只处理`TLS`协议的nginx web服务器。在服务器上，对所设定端口（一般为443）的`TLS`协议进行握手、连接、转发。除去本身特殊作用外，与普通的web服务器的行为几乎无差别，这和其团队宣传的内容一致，笔者觉得是值得肯定的。但Trojan对普通流量的处理和反向代理的支持做的并不完善。从服务器安全角度看，未来可能会针对这两点进行识别。

![](/images/posts/%e5%85%b3%e4%ba%8etrojan%e3%80%81cdn%e3%80%81v2ray%e7%9a%84%e7%a7%8d%e7%a7%8d%e9%97%ae%e9%a2%98-%ef%bc%88%e5%8e%9f%e7%90%86%e5%88%86%e6%9e%90%ef%bc%89/05.svg)Trojan工作原理

Trojan在作为协议部分则更像是`SOCKS5`，这是本身设计使然。因此，若`TLS`加密失效（无论是量子计算机未来的量子霸权或是中间人攻击），都会对Trojan协议带来致命的打击。当然若是本地客户端就有对协议的监控则更为简便。**从协议安全角度看，未来从客户端内部对Trojan进行拦截可能是最简单最可靠的方案。**

#### 总结

截至目前发表日期，笔者觉得Trojan整体还是一个非常“年轻”的方案。笔者认为无论是服务端还是客户端均不能达到稳定日常使用的水平。但是，Trojan安装配置的便利以及设计的巧妙还是值得持续关注的。欢迎大家多多关注无主界的最新动态~

  

#### 推荐阅读

如何部署Trojan：[替代V2Ray？- Trojan搭建教程](https://www.idleleo.com/02/3899.html)

如何部署V2Ray：[2020 搭建 V2Ray 最新教程](https://www.idleleo.com/10/2148.html)

Trojan、V2Ray传输方式对比：[V2Ray / Trojan 传输方式哪个好？(原理对比)](https://www.idleleo.com/02/4064.html)

V2Ray传输协议哪个好：[V2Ray / SSR 传输协议哪个好? (各种协议对比)](https://www.idleleo.com/05/2071.html)

更好的了解TLS：[揭秘密码背后的原理](https://www.idleleo.com/03/1703.html)、[在浏览器地址栏输入一个URL回车后，究竟会发生什么？](https://www.idleleo.com/05/2017.html)
