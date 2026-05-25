+++
title = "安全、免费激活Windows 10 - 激活方式讨论"
date = 2019-02-25T23:11:35+08:00
draft = true
description = "Windows 10（以下简称Win10）自从推出已经过去了接近5年。在Win10推出之初，由于主打服务而非单一销售，微软通过免费升级的办法吸引用户主动升级至Win10，并且整整提供了将近2年的免费升级服务。即便到现在，装有Windows 7（以下简称Win7）的童鞋仍旧可以通过某些方法免费升级至W"
slug = "an-quan-mian-fei-ji-huo-windows-10---ji-huo-fang-shi-tao-lun"
featureimage = "https://cdn.idleleo.com/wp-content/uploads/2019/02/20190225213942-1024x751.png"
+++

Windows 10（以下简称Win10）自从推出已经过去了接近5年。在Win10推出之初，由于主打服务而非单一销售，微软通过免费升级的办法吸引用户主动升级至Win10，并且整整提供了将近2年的免费升级服务。即便到现在，装有Windows 7（以下简称Win7）的童鞋仍旧可以通过某些方法免费升级至Win10。但是，近年才买电脑的童鞋此方法几乎行不通。因为，近年的电脑根本不再支持安装Win10以下的系统，即便通过各种方式成功安装，其体验也远远逊色于Win10。

抛开未激活的系统不提，Win10系统激活后便可高枕无忧吗？显然不是，电脑可能由于重装、更换关键硬件等原因导致激活失效，此时除去非常不划算的购买正版外，**安全** 又**免费** 的激活方式便是我们喜闻乐见的。

#### 激活Win10的普通办法

以下罗列几种最常见的激活方式，各有优缺，可自行参考。

### KMS激活

KMS，全称Key Management Service。KMS是微软官方认可的一种系统激活方式。这个激活方式主要用于企业计算机的批量激活。

具体什么是KMS激活？打个比方，某公司买了3000台一模一样的台式机，然而都是空机没有内置OEM系统。怎么办？这时便需要一个系统管理员（System Administrator），由这个系统管理员购买一个批量激活密钥（也就是大家经常看到的Volume Key，Vol密钥）。然而有这个密钥还是不够的，总不见得3000台机器一台一台开机设置输入密钥激活吧？这时KMS的优势就体现了。管理员设置一个激活服务器（Activation Server），并在每一个客户机上安装KMS的客户端，就可以进行批量激活和管理。也就是说，管理员不光可以远程激活你的电脑，还能够远程取消激活乃至控制你的电脑。

以上便是KMS的激活方式的描述，此种激活方式非常普遍，几乎从网络找到的所有方式本质都是如此。当然很多企业和学校也在用KMS的激活方式激活Windows以及Office等软件。

![](/images/wp-content/uploads/2019/02/20190225213942-1024x751.png) 某网站提供的KMS激活工具

KMS方式确实流行，但是就如上文所说，激活方式并不安全。实际上是非常不安全。因为我们没有办法保证这个管理员会做什么。操纵电脑作为肉鸡还只是小事，如果涉及重要文件，后果难以预料。实际上，一旦成功激活，我们就可以在计算机系统属性中发现我们已经加入了一个工作组，这个工作组是没有办法改变的。如图：

![](/images/wp-content/uploads/2019/02/20190225211515.png)

除去不安全，KMS的激活方式亦不稳定。由于KMS本身性质决定，其激活时长为180天，过了180天便需要重新再次激活。因此，在KMS激活时，会创建一个开机启动的服务或者程序，其目的就在于进行检测激活的有效性。但出于各种原因，KMS的激活程序时常被认为病毒，因此容易被各种杀毒软件拦截。这便容易造成激活失效。并且由于无法保证激活服务器的可靠性，因此其激活并不稳定。

对于KMS的激活方式，笔者我非常不推荐。试想，一个批量激活密钥价值不菲，免费提供者的收入来源在哪？在此笔者不会提供这类激活方式，若实在需求，可以直接在搜索引擎搜索KMS激活即可。

### 网店便宜的激活码

此类激活码非常之多，而且价格较之正版动辄几千来说，可谓是非常便宜。那么问题来了，便宜有好货吗？

![](/images/wp-content/uploads/2019/02/20190225214252-1024x652.jpg) 某购物网站售卖的win 10密钥

答案是：没有。

首先我们要明白Windows密匙分这几种：零售（Retail License）、制造商（OEM License）、教育系统（校园先锋、dreamspark）、大客户批量授权（Volume License，包含KMS、MAK）、开发者（MSDN）。

这部分低价贩卖的密钥主要是教育和开发者两个渠道“弄出来”的激活秘钥。比如批量获得edu邮箱账号，大量注册申请获得Windows/Office激活秘钥，或者是盗用MSDN订阅用户的账号（或其他手段）非法获取。

此类密钥虽然较之KMS安全的多，但是一旦重装系统激活秘钥就不再有效。这是教育系统/MSDN渠道获得的激活秘钥的特点之一，说白了就是一次性激活而已。另外，如果更换主板也会要求重新激活（更换硬盘Office也需重新激活），也就是秘钥会失效。 同时也不排除微软吊销密钥的可能。因此此类密钥稳定性甚至不及KMS。

也就是说这类密钥确确实实是接近正版的，是较为安全的，不必冒着被他人操控电脑的风险。但是稳定性就欠佳了，一但电脑出现故障便需要重装、更换硬件，便需要再花钱去购买。

## 安全、免费的激活方式

以下推荐两种安全且免费的激活方式。

#### 利用Win7申请数字许可证激活

此类激活方式其实较多，现在笔者并不能保证此类激活方式有效。利用Win7的激活方式适用于仍在使用Win7的童鞋，若您的电脑已经为Win10则可以参考下一种方式。

### 什么是“数字权利激活”

什么是“数字权利激活”？数字许可证激活是Win10中新加入的激活方式，是一种授权方法的分类。

数字许可证会记录您的硬件设备信息，只要在CPU和主板设备没有更换的情况下就可以连接微软服务器自动永久性的激活系统，重新安装系统时无需再次输入产品密钥，安装后会自动永久激活。

“数字权利激活”在不更换电脑硬件的情况下一直有效，无论您安装的系统是正式版还是预览版，不影响永久激活效果。

### 激活步骤

  1. 首先保证你的当前Win7是永久激活状态的（盗版正版无所谓都可以，激活工具网上一大把）
  2. 然后下载和你当前Win7版本对应的Win10镜像，（纯净版官方原版镜像可以去i tell you下载）
  3. 在 Win10 镜像里的 Sources 文件夹下找到名为「gatherosstate.exe」复制到Win7的电脑运行 稍等片刻，会生成一个「GenuineTicket.xml」的文件 保存这个文件
  4. 然后正常方法安装Win10系统，安装过程中无需输入序列号 直接跳过。
  5. 安装完成后按将上面生成的「GenuineTicket.xml」复制到 ProgramDataMicrosoftWindowsClipSVCGenuineTicket

![](/images/wp-content/uploads/2019/02/20190225220714-1024x596.png)

放入此文件夹中之后，重启系统即可完成激活！

![](/images/wp-content/uploads/2019/02/20190225220736.jpg)

### 注意事项

  1. 此类激活为数字许可证激活， 更换了电脑的主板或硬盘可能导致激活失效，此时需登录你的微软帐户运行“设置 - 更新和安全 - 激活”界面的Activation Troubleshooter（疑难解答）工具即可重新激活设备。
  2. 若您的Win7是家庭版，那么与之对应的Win10也要装家庭版。若Win7是旗舰版或专业版，那么Win10就要装Win10专业版。
  3. 可以通过各种方式包括升级、重装等方式激活Win10。

#### 通过HWIDGen申请数字许可证

HWIDGen是一款由国外Nsane论坛会员s1ave77制作的Win10数字权利激活工具，这款Win10数字权利获取工具，可以自动获取Win10 数字许可证激活，无需产品密钥，以最简单的方式非KMS的方式申请数字许可证。

### 手动激活

安全放心的激活方式。。

1. Get GatherOsState.exe from Windows 10 17134 ISO

2. Get latest version of slshim from https://github.com/vyvojar/slshim/releases

3. Extract slshim32.dll (for gatherosstate from x86 ISO) or slshim64.dll (for gatherosstate from x64 ISO)

4. Place gatherosstate and extracted slshim dll in the same directory

5. Rename slshim dll to slc.dll

6. Import this to registry:

6.1. Set the real value for %sku% from beneath list.
[code] 
    edition=Cloud
    sku=178
    
    edition=CloudN
    sku=179
    
    edition=Core
    sku=101
    
    edition=CoreCountrySpecific
    sku=99
    
    edition=CoreN
    sku=98
    
    edition=CoreSingleLanguage
    sku=100
    
    edition=Education
    sku=121
    
    edition=EducationN
    sku=122
    
    edition=Enterprise
    sku=4
    
    edition=EnterpriseN
    sku=27
    
    edition=EnterpriseS
    sku=125
    
    edition=EnterpriseSN
    sku=126
    
    edition=Professional
    sku=48
    
    edition=ProfessionalEducation
    sku=164
    
    edition=ProfessionalEducationN
    sku=165
    
    edition=ProfessionalN
    sku=49
    
    edition=ProfessionalWorkstation
    sku=161
    
    edition=ProfessionalWorkstationN
    sku=162
[/code]

Replace the ‘XXX’ with the needed sku value. If using REG make sure the string is 7 digits long, the CMD will take the value from above.

CMD:
[code] 
    reg add "HKLMSYSTEMTokens" /v "Channel" /t REG_SZ /d "Retail" /freg add "HKLMSYSTEMTokensKernel" /v "Kernel-ProductInfo" /t REG_DWORD /d XXX /freg add "HKLMSYSTEMTokensKernel" /v "Security-SPP-GenuineLocalStatus" /t REG_DWORD /d 1 /freg add "HKCUSOFTWAREMicrosoftWindows NTCurrentVersionAppCompatFlagsLayers" /v "C:gatherosstate.exe" /d "^ WIN7RTM" /f 
[/code]

Make shure the XXX are peplaced by shown ID from above SKUID list.

Adapt the above path to gatherosstate.exe to the actual path.

7. Enter default Retail/OEM key from products ini

Key list from 17134.1 products.ini:

Site: https://pastebin.com

ShareCode: /rYakstDc

if you have Enterprise N or LTSB 2016 N use this in elevated Powershell:
[code] 
    ::EnterpriseN
    ((Get-Content '.gatherosstate.exe') -replace "`0" | Select-String -Pattern "(.....-){4}C372T" -AllMatches).Matches | Select-Object -ExpandProperty Value
     
    ::EnterpriseSN
    ((Get-Content '.gatherosstate.exe') -replace "`0" | Select-String -Pattern "(.....-){4}VMJWR" -AllMatches).Matches | Select-Object -ExpandProperty Value
[/code]

this will gather the key from within gatherosstate.exe

8. Run gatherosstate. After a few seconds you should get GenuineTicket.xml

9. (optional) Remove HKEY_LOCAL_MACHINESYSTEMTokens from registry.

CMD:

[cc] reg delete "HKLMSYSTEMTokens" /f reg delete "HKCUSOFTWAREMicrosoftWindows NTCurrentVersionAppCompatFlagsLayers" /v "C:gatherosstate.exe" /f [/cc]

10. Place the created genuineticket at the root of c: and in admin CMD:
[code] 
    clipup -v -o -altto c:
[/code]

11. then force activation with:

[cc]cscript /nologo %windir%system32slmgr.vbs -ato[/cc]

### 自动激活

HWIDGen v62.01 汉化版

软件下载：

链接: <https://pan.baidu.com/s/1qqvZjR9uTFOsNziKpw1rDw>

提取码: phnj

操作方式如图：

![](/images/wp-content/uploads/2019/02/201902251027-1-1024x751.gif)

### 支持的系统

  * Windows 10 Cloud
  * Windows 10 CloudN
  * Windows 10 Core
  * Windows 10 CoreN
  * Windows 10 CoreCountrySpecific
  * Windows 10 CoreSingleLanguage
  * Windows 10 Education
  * Windows 10 EducationN
  * Windows 10 Enterprise
  * Windows 10 EnterpriseS / LTSB
  * Windows 10 EnterpriseN
  * Windows 10 EnterpriseSN / LTSBN
  * Windows 10 Professional
  * Windows 10 ProfessionalN
  * Windows 10 ProfessionalEducation
  * Windows 10 ProfessionalEducationN
  * Windows 10 ProfessionalWorkstation
  * Windows 10 ProfessionalWorkstationN
  * Windows 10 EnterpriseSN / LTSBN
  * Windows 10 Professional
  * Windows 10 ProfessionalN
  * Windows 10 ProfessionalEducation
  * Windows 10 ProfessionalEducationN
  * Windows 10 ProfessionalWorkstation
  * Windows 10 ProfessionalWorkstationN
  * Windows 10 EnterpriseSN / LTSBN
  * Windows 10 Professional
  * Windows 10 ProfessionalN
  * Windows 10 ProfessionalEducation
  * Windows 10 ProfessionalEducationN
  * Windows 10 ProfessionalWorkstation
  * Windows 10 ProfessionalWorkstationN

#### 类似HWIDGen的激活工具（优化）

优化了批处理执行逻辑，失败自动重试。

兼容大于等于 Win7(win server 2008) 的各个版本的激活信息(包括Office)查询，备份，还原。

自动激活(获取数字许可证)只支持Win10，以后重装只要联网就会自动激活,无需输入许可证密钥。

### 功能列表

  1. 自动激活并获取数字激活许可证。
  2. 删除(初始化)系统激活信息。
  3. 备份系统激活信息。
  4. 还原系统激活信息。
  5. 查看激活状态。
  6. 查看支持列表。

![](/images/wp-content/uploads/2019/02/201902251032.jpg) 这“死亡水印”...

### 下载地址

<https://moeclub.org/attachment/WindowsSoftware/>

链接: <https://pan.baidu.com/s/1S4c3dptqtZq6Mvva5USJ_g>

密码: ksrc

### 注意内容

激活时请保持电脑连网状态，否则无法顺利激活。

激活时请保持Windows Update服务为启动状态。

如果已使用密钥激活Office等产品，会丢失其激活状态。

建议: 备份激活信息后再操作。

#### 相应的系统下载

推荐前往[msdn i tell you](<https://msdn.itellyou.cn/>)下载相应的系统，以下是常见的系统下载：

### Windows 7 Ultimate with Service Pack 1 (x64)

文件名：cn_windows_7_ultimate_with_sp1_x64_dvd_u_677408.iso

SHA1：2CE0B2DB34D76ED3F697CE148CB7594432405E23

发布时间2011-05-12

文件大小：3.19GB

[ed2k://|file|cn_windows_7_ultimate_with_sp1_x64_dvd_u_677408.iso|3420557312|B58548681854236C7939003B583A8078|/](<http://ed2k://|file|cn_windows_7_ultimate_with_sp1_x64_dvd_u_677408.iso|3420557312|B58548681854236C7939003B583A8078|/>)

### Windows 10 (consumer edition), version 1809 (Updated Sept 2018) (x64)

文件名：cn_windows_10_consumer_edition_version_1809_updated_sept_2018_x64_dvd_f7b9c8a9.iso

SHA1：81766e9fe5793e8781c5336e513ebceedd2f7b90

文件大小：4.74GB

发布时间：2018-11-16

[ed2k://|file|cn_windows_10_consumer_edition_version_1809_updated_sept_2018_x64_dvd_f7b9c8a9.iso|5085956096|226AB51B290C3C0393A6A17096CB7497|/](<http://ed2k://|file|cn_windows_10_consumer_edition_version_1809_updated_sept_2018_x64_dvd_f7b9c8a9.iso|5085956096|226AB51B290C3C0393A6A17096CB7497|/>)

#### 一些激活码

**Office 2013**

N2XDC-FCV96-GX6FD-8JPVV-X7367

**Office 2019**

N9J9Q-Q7MMP-XDDM6-63KKP-76FPM

**Windows 8.1**

VRDJD-48XFR-PW8D3-DYVV4-WMQ6M

**Windows 10 2019 LTSC**

93MGM-NTFKD-6BK63-R6FYR-6Q9PB

**Windows 10 pro**

NX97R-FPXYV-TM9RD-498KX-GJF9M
