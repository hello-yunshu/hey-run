+++
title = "教程：phpStudy Apache升级至最新版"
date = 2018-01-01T23:48:28+08:00
draft = true
description = "前言 用过phpStudy的同学应该知道，phpStudy的apache版本是2.4.23 (Win32)的，这个版本还是2016年的，很明显，已经很低了，而且还是32位的版本。 当paniy我看到这个的时候，我是很不爽的，强迫症的我决定升级！ 我在网上找了很多关于phpStudy升级apache的"
slug = "jiao-cheng-phpstudy-apachesheng-ji-zhi-zui-xin-ban"
featureimage = "https://cdn.idleleo.com/wp-content/uploads/2018/01/asf_logo.jpg"
+++

#### 前言

用过phpStudy的同学应该知道，phpStudy的apache版本是2.4.23 (Win32)的，这个版本还是2016年的，很明显，已经很低了，而且还是32位的版本。 [![](/images/wp-content/uploads/2018/01/asf_logo.jpg)](</images/wp-content/uploads/2018/01/asf_logo.jpg>) 当paniy我看到这个的时候，我是很不爽的，强迫症的我决定升级！ 我在网上找了很多关于phpStudy升级apache的办法，结果要么就是互相抄抄文章，要么就是不知所云的胡扯，我也奉劝大家一句，这个千万不要相信。不仅没啥用，而且有可能搞坏你的网站。 

#### 准备工作

首先上[apache官网](<http://httpd.apache.org/docs/current/platform/windows.html#down>)，随便找一个下载地址，比如第一个，下载最新的apache版本，现在最新的是2.4.29。 [![](/images/wp-content/uploads/2018/01/20180101223337-1024x372.jpg)](</images/wp-content/uploads/2018/01/20180101223337.jpg>) 下载完成后，停止本地的apache运行，在phpStudyPHPTutorial目录中，重命名Apache文件夹名字，比如Apache1，记住不要删掉。 将下载的最新apache版本解压到phpStudyPHPTutorial目录，重命名为Apache，到这里，你就基本完成了准备工作的最初阶段。 

#### 进阶准备

这个阶段，你需要进行文件修改了。 很明显，最最重要的文件就是Apacheconf目录下的httpd.conf[![](/images/wp-content/uploads/2018/01/20180101224409.jpg)](</images/wp-content/uploads/2018/01/20180101224409.jpg>) 首先你需要做的，就是比较httpd.conf最新版和phpStudy原版中的差异。将所有你添加的条目、删除的条目或者原版自带的条目加至新版httpd.conf文件中。这个工作至关重要，几乎一切的apache无法启动都来自httpd.conf文件配置问题。 为了方便大家我这边做好了基础版的httpd.conf修改文件，注：paniy我自己没有加减任何一条，只是迁移了phpStudy原版的内容。 在完成httpd.conf文件的修改后，别忘记把之前文件夹中的vhosts.conf复制到新版本相同目录下，还有一个非常重要的文件夹，你需要把Apacheconfextra目录下的所有新版本不包含的文件都复制到新版的apache同目录下。 [![](/images/wp-content/uploads/2018/01/20180101231235.jpg)](</images/wp-content/uploads/2018/01/20180101231235.jpg>) 至于这个文件夹有什么用，你打开就可以发现，这个文件是用来调用php等等，这是必须的文件夹。到了这步，整个准备工作就基本完成了。 

#### Apache的升级

首先你要做的，是卸载原来的apache。如果你是以系统服务运行的话，你首先要删除服务。 在cmd命令行中，输入[code]sc delete apache[/code]。 [![](/images/wp-content/uploads/2018/01/20180101230342.jpg)](</images/wp-content/uploads/2018/01/20180101230342.jpg>) 然后进入apache/bin目录运行命令行，（你可以输入cd ...PHPTutorialApachebin），在此目录下输入[code]httpd.exe -k install -n apache[/code]，当你一切运行正常的话，你会发现有一个如图错误 [![](/images/wp-content/uploads/2018/01/20180101230946-1024x187.jpg)](</images/wp-content/uploads/2018/01/20180101230946.jpg>) apache无法运行！这是为什么？仔细研究错误报告，喔！原来Apachemodulesmod_fcgid.so这个文件不存在，那么直接去原来的apache文件夹中复制过来？错！绝对不可以这么做，我们现在回到之前下载apache的网站，往下翻，你会发现这个： [![](/images/wp-content/uploads/2018/01/20180101231913.jpg)](</images/wp-content/uploads/2018/01/20180101231913.jpg>) 是的，你还需要下载这个！这就是为什么我说准备工作只是“基本”完成，其实压根还没完成。下载你需要的mod_fcgid.so版本，放入Apachemodules目录中，运行[code]sc delete apache[/code]命令后，再次运行[code]httpd.exe -k install -n apache[/code]，之后你就会看到这些反馈 [![](/images/wp-content/uploads/2018/01/20180101232851.jpg)](</images/wp-content/uploads/2018/01/20180101232851.jpg>) 注意最后一句话：Errors reported here must be corrected before the service can be started.难道这意味着还有问题，不不不，如果下面没有东西，恭喜你！你升级完毕！ 

#### 写在最后

其实回过去想想不知道你有没有和paniy我一样的想法，这差不多就是完全重装一下apache嘛！没错，就是重装一遍。当然最后我要再次提醒下： 一、我提供的改好的httpd.conf是其中的ServerRoot是我安装phpStudy的目录，如果目录不同，你需要修改这个。 

二、升级完成后你可能不能通过phpStudy控制apache的启动、停止等，你可以在我的另一篇文章中找到解决办法。 

#### 相关下载

[reply] 点击下载：[下载](<https://y.idleleo.com/httpd.conf>)[/reply]
