+++
title = "Deepnude “脱” 衣原理分析及下载"
date = 2019-07-06T18:57:27+08:00
draft = true
description = "Deepnude前段时间可谓火的不行，虽然作者很快关闭了网站和app，但是其使用的原理是值得一探究竟的。再加上有些小伙伴可能也想深入了解相关技术，笔者便转载了相关文章以及下载地址供大家参考。 可以参考NVIDIA论文使用部分卷积和基于部分卷积的填充来修复不规则孔的图像。纸质代码部分转换。论文地址:"
slug = "deepnude-tuo-yi-yuan-li-fen-xi-ji-xia-zai"
featureimage = "/images/posts/deepnude-tuo-yi-yuan-li-fen-xi-ji-xia-zai/cover.avif"
+++

Deepnude前段时间可谓火的不行，虽然作者很快关闭了网站和app，但是其使用的原理是值得一探究竟的。再加上有些小伙伴可能也想深入了解相关技术，笔者便转载了相关文章以及下载地址供大家参考。

![](/images/posts/deepnude-tuo-yi-yuan-li-fen-xi-ji-xia-zai/cover.avif)

可以参考NVIDIA论文使用部分卷积和基于部分卷积的填充来修复不规则孔的图像。纸质代码部分转换。论文地址: <https://arxiv.org/abs/1804.07723和https://arxiv.org/abs/1811.11718>

![](/images/posts/deepnude-tuo-yi-yuan-li-fen-xi-ji-xia-zai/01.avif)

在Image_Inpainting实验测试（<https://api.isoyu.com/Deepnude/Image_Inpainting(NVIDIA_2018).mp4>)视频的图像界面中，您只需使用工具简单地涂抹图像中不需要的内容。即使形状非常不规则，NVIDIA的模型也可以非常逼真地“恢复”图像。图片填充了涂抹的空白。它可以被描述为一键式P图片，并且“没有ps痕迹”。该研究基于Nvidia的桂林刘大佬的团队。他们发布了一种可以编辑图像或重建已损坏图像的深度学习方法，即使图像穿了个洞或丢失了像素。这是目前2018国家最先进的方法。

### Pix2Pix(需要配对数据)

论文参考: <https://arxiv.org/abs/1611.07004>下面是训练Pix2Pix模型200个epochs后产生的输出。

![](/images/posts/deepnude-tuo-yi-yuan-li-fen-xi-ji-xia-zai/02.avif)

了解更多信息可以查看[https://github.com/tensorflow/docs/blob/master/site/en/r2/tutorials/generative/pix2pix.ipynb](https://blog.isoyu.com/go.php?url=https://github.com/tensorflow/docs/blob/master/site/en/r2/tutorials/generative/pix2pix.ipynb)

### CycleGAN（无需配对数据）

CycleGAN使用循环一致性损失函数来实现训练，而无需配对数据。换句话说，它可以从一个域转换到另一个域，而无需在源域和目标域之间进行一对一映射。这开启了执行许多有趣任务的可能性，例如照片增强，图像着色，样式传输等。只需要源和目标数据集。参考论文<https://arxiv.org/abs/1703.10593>

![](/images/posts/deepnude-tuo-yi-yuan-li-fen-xi-ji-xia-zai/03.avif)

了解更多信息<https://github.com/tensorflow/docs/blob/master/site/en/r2/tutorials/generative/cyclegan.ipynb>

## Windows版DeepNude使用过程

DeepNude可以真正实现图像到图像的目的，并且生成的图像更加真实。

![](/images/posts/deepnude-tuo-yi-yuan-li-fen-xi-ji-xia-zai/04.avif)

![](/images/posts/deepnude-tuo-yi-yuan-li-fen-xi-ji-xia-zai/05.avif)

![](/images/posts/deepnude-tuo-yi-yuan-li-fen-xi-ji-xia-zai/06.avif)

![](/images/posts/deepnude-tuo-yi-yuan-li-fen-xi-ji-xia-zai/07.avif)

PS: 删除deepnude根目录中的color.cp36-win_amd64.pyd文件，然后添加color.py(<https://api.isoyu.com/Deepnude/color.py>)文件以获取deepnude的高级版本。

## 对deepnude下架争取再重新上架的建议

1. **尺寸** 包括156M DeepNude_Windows_v2.0.0.zip和1.90G pyqtlib.rar。

2. **速度** 转换图片需要30秒。

3. **内容** 使用图像到图像神经网络自动从女性身上移除衣服以揭示她们的裸露。此应用程序适用于深度学习的错误应用。

* DeepNude可以使用Tensorflow实现，并使用模型压缩技术。

* DeepNude应该改变目前不尊重女性的做法。**总结** 实际上，可以不需要Image-to-Image。我们可以使用GAN直接从随机值生成图像或从文本生成图像。 

Obj-GAN: <https://github.com/jamesli1618/>

Obj-GANStoryGAN: <https://github.com/yitong91/StoryGAN>

微软人工智能研究院（Microsoft Research AI）开发的新 AI 技术可以理解自然语言描述、绘制草图、合成图像，然后根据草图框架和文字提供的个别单词细化细节。换句话说，这个网络可以根据描述日常场景的文字描述生成同样场景的图像。

![](/images/posts/deepnude-tuo-yi-yuan-li-fen-xi-ji-xia-zai/08.avif)

![](/images/posts/deepnude-tuo-yi-yuan-li-fen-xi-ji-xia-zai/09.avif)

当前最优的文本到图像生成模型可以基于单句描述生成逼真的鸟类图像。然而，文本到图像生成器远远不止仅对一个句子生成单个图像。给定一个多句段落，生成一系列图像，每个图像对应一个句子，完整地可视化整个故事。

![](/images/posts/deepnude-tuo-yi-yuan-li-fen-xi-ji-xia-zai/10.avif)

## Deepnude下载

网友提供： [magnet:?xt=urn:btih:7be4eb8d640742d2ffebd6495e9392e9e2c399bc](magnet:?xt=urn:btih:7be4eb8d640742d2ffebd6495e9392e9e2c399bc)

也有GitHub开源地址： <https://github.com/open-deepnude/open-deepnude>
