+++
title = "自给自足！各种在线文档下载小技巧"
date = 2019-12-26T19:40:34+08:00
draft = true
description = "前段时间，笔者发现很多下载在线文档的“小技巧”已经失效了。据某位开发者说，是一些非技术原因导致的。看来某些互联网企业实在看不下去被人挡住财路了，哈哈。现在，笔者在互联网找到这篇教材，适用范围有限，但的确可以解决一些问题。 这里的浏览器需要有开发者工具选项，现在一般的浏览器如谷歌、火狐、360浏览器等"
slug = "zi-gei-zi-zu-ge-zhong-zai-xian-wen-dang-xia-zai-xiao-ji-qiao"
featureimage = "https://cdn.idleleo.com/wp-content/uploads/2019/12/20191226002.gif"
+++

前段时间，笔者发现很多下载在线文档的“小技巧”已经失效了。据某位开发者说，是一些非技术原因导致的。看来某些互联网企业实在看不下去被人挡住财路了，哈哈。现在，笔者在互联网找到这篇教材，适用范围有限，但的确可以解决一些问题。

这里的浏览器需要有开发者工具选项，现在一般的浏览器如谷歌、火狐、360浏览器等都自带这个。

下面以360安全浏览器为例。****

## 方法1、以搜索引擎爬虫的身份访问网页。

在线文档平台为了让文档内容被搜索引擎收录，一般展示给搜索引擎和普通用户的界面会不一样，展示给搜索引擎的页面是能直接复制的文字。

以豆丁文档页面为例，按f12(或者右键选择“检测”或“审查元素”)，打开开发者工具栏。

选择“device toolbar”小按钮，网页界面会缩小，选择上方的“选择设备”列表，

第一次使用需要新建一个爬虫身份设备，点“编辑”，添加设备，设备名可以写“google”，useragent里填写为“googleBot”。 新建完成后，选择这个设备，刷新一下页面，页面文档内容区域就会出现文本形式的内容，可以直接复制。

第二次访问就只要两个步骤，按f12打开开发者工具栏，选项默认的，就只要敲下地址栏刷新，就是以爬虫的身份访问网页。

![](/images/wp-content/uploads/2019/12/20191226002.gif)

## 方法2、以移动手机端的身份访问网页。

在线文档平台为了让文档内容适配手机端，一般展示的手机端界面比pc端界面简单很多。

1、这里以百度文档页面为例。跟上面步骤一样，按f12打开开发者工具栏。

选择“device toolbar”小按钮，在设备列表里选择一个移动端的设备，这里选择“iphone6/7/8”。

敲一下地址栏重新访问，文档页面的界面一般会变化，变得简单很多，而且没多少广告。

![](/images/wp-content/uploads/2019/12/20191226004.gif)

点击“加载更多”，将所有的文档内容展开。

2、部分版本的360安全浏览器下，把“device toolbar”小按钮按回，就可以右键全选，文档内容直接可以复制，将内容粘贴到word里了。

![](/images/wp-content/uploads/2019/12/20191226006.gif)

![](/images/wp-content/uploads/2019/12/20191226008.gif)

以下非必需：

2.1、如果右键没法复制文字，将网页另存为保存到本地硬盘。然后将保存的网页拖到浏览器(建议改用ie或Safari)打开，看看可不可复制文字和图片。

2.2、如果本地的网页还不能复制文字，再打开开发者工具，在“Console”控制台里输入

`document.querySelectorAll('*').forEach(function(node){node.style.cssText += '-webkit-user-select:text;-moz-user-select:text;-ms-user-select:text;user-select:text;';});`

回车，看能不能复制。

![](/images/wp-content/uploads/2019/12/20191226010.gif)

如果是某丁的文档，不能右键显示菜单，再输入这个代码：

`var doc = document;var bd = doc.body;bd.onselectstart = bd.oncopy = bd.onpaste = bd.onkeydown = bd.oncontextmenu = bd.onmousemove = bd.onselectstart = bd.ondragstart = doc.onselectstart = doc.oncopy = doc.onpaste = doc.onkeydown = doc.oncontextmenu = null;`

上述2.1和2.2步骤没有先后顺序，可能都不需要，主要是为解除网页的右键复制，可以先输入代码看看能不能复制，再另存为网页打开试试。第一次跑通后，第二次操作就简单很多。

另外对于上面浮动的某些区域觉得碍眼，或者由于这个浮框导致保存到本地的页面不能展示全内容，可以点击开发者工具的箭头按钮，选到该区域，按delete键，可以把这个区域直接删除掉。

![](/images/wp-content/uploads/2019/12/20191226012.gif)

![](/images/wp-content/uploads/2019/12/20191226014.gif)

## 方法三、将网页打印以pdf预览。

这个方法对于禁止复制的网页来复制一些文字效果比较好，比如360doc的文章不能复制，可以用打印预览的方式复制文字。这个方法对于文档平台在pc形式的页面上使用效果已经不好了，可以在方法二的基础上试，记得把页眉和页脚去掉。

![](/images/wp-content/uploads/2019/12/20191226016.gif)

希望能帮助到大家。不过建议不要大规模分享，不然容易失效。
