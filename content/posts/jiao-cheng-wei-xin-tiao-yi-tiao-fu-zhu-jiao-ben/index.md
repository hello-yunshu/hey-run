+++
title = "教程：微信跳一跳辅助脚本"
date = 2018-01-02T21:26:37+08:00
draft = true
description = "游戏模式 2017 年 12 月 28 日下午，微信发布了 6.6.1 版本，加入了「小游戏」功能，并提供了官方 DEMO「跳一跳」。这是一个 2.5D 插画风格的益智游戏，玩家可以通过按压屏幕时间的长短来控制这个「小人」跳跃的距离。分数越高，那么在好友排行榜更加靠前。通过 Python 脚本自动运"
slug = "jiao-cheng-wei-xin-tiao-yi-tiao-fu-zhu-jiao-ben"
featureimage = "/images/posts/jiao-cheng-wei-xin-tiao-yi-tiao-fu-zhu-jiao-ben/cover.avif"
+++

## 游戏模式

2017 年 12 月 28 日下午，微信发布了 6.6.1 版本，加入了「小游戏」功能，并提供了官方 DEMO「跳一跳」。这是一个 2.5D 插画风格的益智游戏，玩家可以通过按压屏幕时间的长短来控制这个「小人」跳跃的距离。分数越高，那么在好友排行榜更加靠前。通过 Python 脚本自动运行，让你轻松霸榜。 [![](/images/posts/jiao-cheng-wei-xin-tiao-yi-tiao-fu-zhu-jiao-ben/cover.avif)](/images/posts/jiao-cheng-wei-xin-tiao-yi-tiao-fu-zhu-jiao-ben/cover.avif)   可能刚开始上手的时候，因为时间距离之间的关系把握不恰当，只能跳出几个就掉到了台子下面。**如果能利用图像识别精确测量出起始和目标点之间测距离，就可以估计按压的时间来精确跳跃。**

## 原理说明

  1. 将手机点击到《跳一跳》小程序界面
  2. 用 ADB 工具获取当前手机截图，并用 ADB 将截图 pull 上来

`adb shell screencap -p /sdcard/autojump.png adb pull /sdcard/autojump.png .`

  3. 计算按压时间

  * 手动版：用 Matplotlib 显示截图，用鼠标先点击起始点位置，然后点击目标位置，计算像素距离；
  * 自动版：靠棋子的颜色来识别棋子，靠底色和方块的色差来识别棋盘；

  4. 用 ADB 工具点击屏幕蓄力一跳

`adb shell input swipe x y x y time(ms)`

## 安卓手机或模拟器操作步骤

### 环境安装

  1. Android 或 Android 模拟器使用 ADB 进行连接 
     * [ADB](https://developer.android.com/studio/releases/platform-tools.html) 驱动，可以到[这里](https://adb.clockworkmod.com/)下载
  2. 如果你是 Android + macOS，请参考下面的配置： 
     * 安装 [Python 3](https://www.python.org/)，选择对应的版本，比如win10 64位为：Windows x86-64 executable installer
     * 使用 brew 进行安装 [code]brew cask install android-platform-tools[/code]
     * 安装完后插入安卓设备且安卓已打开 USB 调试模式，终端输入 [code]adb devices[/code] ，显示如下表明设备已连接[code]List of devices attached xxxxx device [/code]
     * 部分新机型可能需要再另外勾上**允许模拟点击** 权限
     * 小米设备除了 USB 调试，还要打开底下的 USB 调试（安全）
     * USB 可能要设置成 MTP 模式
  3. 如果你是 Android + Windows，请参考下面的配置： 
     * 安装[Python 3](https://www.python.org/)，选择对应的版本，比如win10 64位为：Windows x86-64 executable installer
     * 安装 [ADB](https://adb.clockworkmod.com/) 后，请在**环境变量** 里将 adb 的安装路径保存到 PATH 变量里，确保 [code]adb[/code] 命令可以被识别到
     * 同 Android + macOS 测试连接
  4. 安装依赖文件（在cmd中运行，requirements.txt在[GitHub](https://github.com/wangshub/wechat_jump_game)下载，其中requirements.txt为此文件在电脑上的路径）`pip install -r requirements.txt`
  5. 在 windows 环境中添加 ADB 调试路径的问题可以尝试把所有文件拷贝到 [Tool文件夹](https://github.com/wangshub/wechat_jump_game/tree/master/Tools/adb)下运行 
     1. 按住 shift + 右键 选择在该文件夹下打开命令窗口
     2. 打开安卓手机的usb调试，并连接电脑，在终端输入 adb devices 进行测试，如果有连接设备号则表示成功
     3. 把[GitHub](https://github.com/wangshub/wechat_jump_game)中common文件夹和config相关文件下载在本地，注意config需要把config.json改名为default.json并放在config文件夹下
     4. 打开微信小游戏，然后运行代码 [code]python wechat_jump_py3.py[/code]，点击出现的图形起点和终点，棋子自动跳转 **注意** ：这里使用的是不需要配置的 adb 方式，需要在该文件下操作，至于如何自动跳转，只需改变执行脚本即可，这里只做演示

### 操作步骤

  1. 安卓手机打开 USB 调试，设置 > 开发者选项 > USB 调试
  2. 电脑与手机 USB 线连接，确保执行 [code]adb devices[/code] 可以找到设备 ID
  3. 界面转至微信跳一跳游戏，点击开始游戏
  4. 进入项目目录，运行 [code]python wechat_jump_auto.py[/code] 双击此文件即可，如果手机弹出界面显示 USB 授权，请点击确认
  5. 请按照你的机型或手机分辨率从 [code]./config/[/code]文件夹找到相应的配置，把对应的 [code]config.json[/code]拷贝到项目根目录，与 *.py 同级 
     * 如果屏幕分辨率能成功探测，会直接调用 config 目录的配置，不需要复制
     * 优先按机型去找，找不到再按分辨率
     * 如果都没有请找一个接近的自己，或者调节一下找到合适的参数

## 二、iOS 手机操作步骤

### 环境安装

  * 如果你是 iOS + macOS，请参考下面的配置 
    * 使用真机调试 WDA，参考 iOS 真机如何安装 [WebDriverAgent · TesterHome](https://testerhome.com/topics/7220)
    * 安装 [openatx/facebook-wda](https://github.com/openatx/facebook-wda)
  * 安装依赖文件（同上） 

`pip install -r requirements.txt`

### 操作步骤

  1. 运行安装好的 [code]WebDriverAgentRunner[/code]
  2. 将手机点击到《跳一跳》小程序界面
  3. 运行脚本。有两种模式可供选择：**手动辅助跳** 和**自动连续跳**
     * 手动辅助跳 
       * 命令行运行 [code]python3 wechat_jump_iOS_py3.py[/code]
       * 依次点击弹出的窗口中的起始位置和目标位置，会自动计算距离后起跳
       * 根据起跳的精准情况更改 [code]python3 wechat_jump_iOS_py3.py[/code] 中的 [code]time_coefficient[/code]参数，直到获得最佳取值
     * 自动连续跳 
       * 拷贝 [code]./config/iPhone[/code] 目录下对应的设备配置文件，重命名并替换到 [code]./config.json[/code]
       * 命令行运行 [code]python3 wechat_jump_auto_iOS.py[/code]
       * 会自动计算坐标并连续起跳，根据起跳的精准情况更改 [code]./config.json[/code] 中的 [code]press_coefficient[/code] 参数，直到获得最佳取值

### 运行效果

[![](/images/posts/jiao-cheng-wei-xin-tiao-yi-tiao-fu-zhu-jiao-ben/01.avif)](/images/posts/jiao-cheng-wei-xin-tiao-yi-tiao-fu-zhu-jiao-ben/01.avif)

_感谢wangshub的贡献，更多可见[wechat_jump_game](https://github.com/wangshub/wechat_jump_game)项目，idleleo.com整理_
