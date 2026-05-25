+++
title = "[敛火成丹]Win11Dev-25236.1010专业工作站版-微调"
date = 2022-11-22T15:01:00+08:00
draft = true
slug = "lian-huo-cheng-dan-win11dev-25236."
featureimage = "https://tva4.sinaimg.cn/large/0073r2KBly1h82dqw1b73j30so0ls0uw.jpg"
+++

本文来自[@zxgu183](<https://t.me/zxgu183>)投稿！感谢[@zxgu183](<https://t.me/zxgu183>)！

近来研究了下Win11的各个版本，发现Dev的调度相当激进，在Server2025上也有所体现，它和专工是孪生版本，于是乎整了这个镜像给老师  
如果使用此系统发现任何问题请回帖留言，我将于放假时回应并尽力修复。

配方文件公开于网盘，也可根据自己需求进行修改，开学了也希望有人能够替我更新，用MSMG（或其改版）和NTLite（免费版）就好，DISM++可调

部分集成来源于MSMG，部分优化来源于MDL和论坛，感谢各位坛友的支持！

以UUP为母盘微调优化制作，仅专业工作站版，可自行修改为其他版本

**VM虚拟机** 测试请使用**单U单核** ，虽然性能如图所示的降低但是可以开机而不会蓝屏提示不支持的平台

此版本暂未发现官方BUG之外的问题，已经**拆除时间限制和弹窗，** 但保留水印以明确版本，请自行测试各类软件，若异常可以回本帖探讨解决方案

提供ISO镜像，带UIA为**无人值守非内置****管理员账户** 版本（即**UIA,** 无人值守版本无WinRE

提供镜像原始winre.wim和常用注册表恢复、打印机共享修复、新旧右键菜单切换

网盘里有Restore.zip，需要MPO、幽灵熔断防护等都可在此恢复。不希望看到多余的右键菜单，分享链接有提供右键菜单管理工具.Net3.5版，可自行关闭或删除  

**不封装 ，**保留原味驱动**，保留绝大部分功能组件和附件，可更新**

**资源直达：**

  1. Cloudreve公益盘：share.nite07.com/s/PKDtn  

  2. 京服隧道：pan.huang1111.cn/s/bmZ9hY  

  3. OneDrive国际版：liuxiane5-my.sharepoint.com/:f:/g/personal/zxgu183_e5_liuxianl_com/EkAlhcrW3b1PjQ0hdqlbCbQBFnEh46QFDLlAEKU3D2DQWg?e=PVtRhY 

系统状态截图  
![](https://tva4.sinaimg.cn/large/0073r2KBly1h82dqw1b73j30so0ls0uw.jpg)  
系统信息旁边的开始菜单应用和Win+V  
![](https://tva4.sinaimg.cn/large/0073r2KBly1h56si2nasoj31bq0pqn44.jpg)  
**集成与启用**

  1. 集成.NET 3.5框架  

  2. 集成WTG  

  3. 集成常用VC运行库  

  4. 启用Windows投影文件系统 (ProjFS)  

  5. 启用NFS功能  

  6. 允许DirectPlay安装  

  7. 启用LPD与LPR打印服务  

  8. 启用SMB 1.0/CIFS文件共享  

  9. 启用XPS文档写入  

  10. 启用Telent远程支持  

  11. 启用虚拟机平台支持  

  12. Win32计算器顶替UWP计算器并替换来自MDL的Metro皮肤  

  13. 照片查看器顶替UWP图片并替换来自MDL的Metro皮肤（非无人值守版MediaPlayer也为Metro）  

  14. IE顶替Edge并在桌面显示图标  

  15. Notepad2顶替传统记事本并卸载UWP记事本（UIA集成Notepad3并自动适配深色模式）  

  16. 桌面右键新增传统个性化、一键息屏  

  17. 此电脑右键添加编辑Hosts  

  18. 此电脑Shift右键添加上帝模式、系统配置、组策略、经典属性面板、注册表编辑器菜单  

  19. DLL、OCX右键菜单添加注册/反注册  

  20. 右键菜单添加管理员取得所有权  

  21. 回收站右键菜单清除DNS缓存  

  22. Shift 右键添加“复制路径”和隐藏菜单  

  23. UIA非极限版集成静默安装7z、MPC-BEx64UWP、Notepad3（适配深色模式） 

  
**保留这些应用**  
**![](https://tvax3.sinaimg.cn/large/0073r2KBly1h4w0zdtk22j31bq0pqaig.jpg)**  
正常的截图快捷键和暗影主题  
![](https://tva4.sinaimg.cn/large/0073r2KBly1h4w0zdx778j30t10m7myw.jpg)  
**优化调整**

  1. Edge禁用SmartScreen  

  2. IE11开启企业模式  

  3. IE不提示默认浏览器，不检查下载程序的签名  

  4. IE允许活动内容在我的电脑的文件运行  

  5. IE开启ClearType  

  6. IE开启兼容显示并跳过首次引导关闭升级  

  7. IE禁用建议的网站  

  8. Winlogin自动重连  

  9. 不主动检测联网，防止打开浏览器占用  

  10. 不再请求我的反馈  

  11. 不要上报感染信息  

  12. 关联照片查看器  

  13. 关闭Edge用户反馈  

  14. 关闭MPO，防止GPU拖前台后腿  

  15. 关闭RPC隐私保护以解决打印机共享11b  

  16. 关闭Smartscreen应用筛选器  

  17. 关闭VBS，防止CPU拖后腿  

  18. 关闭WindowsInk推荐应用  

  19. 关闭WindowsMessenger客户体验改差计划  

  20. 关闭上传用户活动  

  21. 关闭仅限管理员安装驱动程序  

  22. 关闭偶尔在开始菜单中显示建议  

  23. 关闭写入调试信息  

  24. 关闭在设置应用中为我显示建议的内容  

  25. 关闭备胎共享  

  26. 关闭小娜搜索、WD记录  

  27. 关闭幽灵(Spectre)与熔断(Meltdown)  

  28. 关闭打开程序警告  

  29. 关闭搜索框建议 (关闭Bing在线搜索和广告)  

  30. 关闭数据采集遥测  

  31. 关闭新版记事本提示  

  32. 关闭显示受保护文件时警告提示  

  33. 关闭更新后以及登录后显示Windows欢迎体验以显示新增功能和建议内容  

  34. 关闭查找我的设备  

  35. 关闭火狐数据上传  

  36. 关闭系统推荐  

  37. 关闭系统自动调试功能  

  38. 关闭网络内容评估  

  39. 关闭量身腚制的体验  

  40. 关闭驱动签名验证  

  41. 删除SmartScreen进程启动项  

  42. 删除启用安全中心通知  

  43. 去除USB3以上部分询问，常用于解决USB3刷机  

  44. 去除Win11升级检测  

  45. 去除硬件不符水印  

  46. 启用FMP3专业解码器  

  47. 启用Resetbase  

  48. 启用应用程序预读  

  49. 屏蔽防病毒软件监控  

  50. 应用使用广告ID-关  

  51. 强制关闭篡改防护  

  52. 微软拼音候选词9个  

  53. 忽略安装更新预定时间  

  54. 我的电脑Shift右键组策略  

  55. 打开开发人员模式  

  56. 文件系统长路径显示  

  57. 显示所有文件扩展名加快UI速度最高壁纸质量去除快捷方式副本后缀  

  58. 查看诊断数据-关  

  59. 禁止体验共享  

  60. 禁止创建内存调试文件  

  61. 禁止在重新启动时覆盖内存  

  62. 禁止登录后创建成功登录报告功能  

  63. 禁止网络搜索无关联文件方式  

  64. 禁用EdgeV9钓鱼网站过滤  

  65. 禁用MSOffice记录和遥测  

  66. 禁用VisualStudio遥测  

  67. 禁用Windows客户体验改差计划  

  68. 禁用内容交付管理器订阅  

  69. 禁用功能更新的保护措施  

  70. 禁用在线提示  

  71. 禁用提交数据样本和间谍报告  

  72. 禁用组件堆栈和更新解压模块日志  

  73. 禁用计划的系统维护  

  74. 禁用诊断中心标准收集器服务  

  75. 禁用诊断反馈相关  

  76. 禁用诊断策略服务  

  77. 禁用通用遥测客户端  

  78. 禁用错误报告  

  79. 禁用错误报告服务  

  80. 经典系统属性添加接口  

  81. 自动释放多余DLL  

  82. 解除驱动安装弹窗  

  83. 设置默认保留带宽为0  

  84. 诊断数据-基本  

  85. 跳WindowsMediaPlayer首次使用并设置本地策略  

  86. 错误报告不再记录  

  87. 阻止手写数据共享  

  88. 阻止手写错误报告  

  89. 驱动器Shift右键优化驱动器  

  90. 驱动器Shift右键磁盘清理 

**精简列表**

  1. （仅无人值守版精简此条）简体中文之外的其他语言和无用字体、Windows Media Player  

  2. Windows安全中心和Defender  

  3. EdgeChromium  

  4. EdgeWebView  

  5. GameExplorer  

  6. SpeechRecognition  

  7. WinSAT  

  8. WindowsTIFFIFilter  

  9. WindowsMail  

  10. CEIP  

  11. KernelDebugging  

  12. UnifiedTelemetryClient  

  13. WindowsErrorReporting  

  14. WindowsInsiderHub  

  15. OneDrive  

  16. Cortana  

  17. EasyTransfer  

  18. Narrator  

  19. CBSPreview  

  20. ContentDeliveryManager  

  21. Edge  

  22. EdgeDevToolsClient  

  23. WindowsReaderPDF  

  24. ECApp  

  25. MapControl  

  26. NarratorQuickStart  

  27. ParentalControls  

  28. PeopleExperienceHost  

  29. RetailDemoContent  

  30. SkypeORTC  

  31. SmartScreen  

  32. WebcamExperience  

  33. WindowsMixedReality  

  34. MixedRealityPortal  

  35. 3DViewer  

  36. SkypeApp  

  37. 其他部分可卸载重装应用 

  
NTLite见配方  

  

优化主要是注册表

DISM++自己看

> 桌面壁纸和锁屏壁纸来源：Pixiv画师banishment作品

  

如果有更好的优化方案和建议或我做的哪里不好，请在帖子下不吝指点，感谢各位看官支持！
