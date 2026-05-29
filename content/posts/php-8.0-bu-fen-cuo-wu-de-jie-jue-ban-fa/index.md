+++
title = "PHP 8.0 部分错误的解决办法"
date = 2021-01-12T04:04:22+08:00
draft = false
description = "前段时间，一直关注的PHP 8终于放出了正式版本，于是迫不及待的编译并测试了下，发现bug极多，尤其是新特性JIT更是在特定情况下直接无法使用。 好在大多bug已经在PHP的官网得到了提出，要做的就是等待修复了。不过在"
slug = "php-8.0-bu-fen-cuo-wu-de-jie-jue-ban-fa"
featureimage = "/images/posts/php-8.0-bu-fen-cuo-wu-de-jie-jue-ban-fa/cover.avif"
categories = ["教程"]
tags = ["PHP", "PHP 8", "故障排查"]
+++
> 旧文归档：本文针对 PHP 8.0 刚发布时遇到的部分错误。PHP 版本、扩展兼容性和框架适配已经继续演进，排查问题时请先看当前 PHP 版本的错误日志与官方迁移说明。

前段时间，一直关注的PHP 8终于放出了正式版本，于是迫不及待的编译并测试了下，发现bug极多，尤其是新特性JIT更是在特定情况下直接无法使用。

![](/images/posts/php-8.0-bu-fen-cuo-wu-de-jie-jue-ban-fa/cover.avif)

好在大多bug已经在PHP的官网得到了提出，要做的就是等待修复了。不过在遇到的众多bug中，有一些却并不是由于PHP本身造成的，比如接下来要说的两个较为隐蔽的错误。

## PHP Warning

Warning: Only the first byte will be assigned to the string offset in /path/wp-includes/class.wp-scripts.php on line 492

![](/images/posts/php-8.0-bu-fen-cuo-wu-de-jie-jue-ban-fa/01.avif)

其中一个错误如上所示，这个警告指向的是wp-includes/class.wp-scripts.php文件，这是WordPress的一个核心文件。一开始，我想很多小伙伴会和我一样认为是WordPress自己的错误，但是WordPress在5.6版本就已经宣布全面支持PHP 8了，所以这个问题不应该是WordPress核心文件有问题。

要想解决这个问题，我们需要把报错的相关代码拿出来看：
[code] 
    $l10n[ $key ] = html_entity_decode( (string) $value, ENT_QUOTES, 'UTF-8' );
[/code]

上述代码，大家肯定和我一样看的莫名奇妙，感觉不到什么问题。但是如果结合它所在的`function`：
[code] 
    public function localize( $handle, $object_name, $l10n ) 
[/code]

大家是不是猜到了，很可能是在使用`wp_localize_script`这个`function`时出现了问题，而问题的关键就在于参数`$l10n`。

我们不妨从官网资料中看一下`$l10n`到底是个什么东西：

> $l10n (array) (Required) The data itself. The data can be either a single or multi-dimensional array.

原来，问题在于参数`$l10n`在函数`wp_localize_script`中接受到的应该是一个数组，如果没有接受到数组，只是接受到了字符串等非数组的值时，由于[PHP 8的新特性](https://www.php.net/manual/en/language.types.string.php#language.types.string.substr)，会报出一个警告。

### 解决办法

解决这问题其实相对简单，只需要在使用函数`wp_localize_script`：
[code] 
    wp_localize_script( string $handle, string $object_name, array $l10n )
[/code]

把上面参数`$l10n`改为数组即可。但是**需要注意修改后的使用** ，比如此函数的作用可为JavaScript提供一个参数，参数名字为`$object_name`。在函数修改后，参数`$object_name`将在JavaScript中成为一个对象。

## PHP Deprecated

Deprecated: Required parameter $xxx follows optional parameter $yyy in…

![](/images/posts/php-8.0-bu-fen-cuo-wu-de-jie-jue-ban-fa/02.avif)

这类报错在升级PHP 8后也非常常见。这类错误多是来自一些主题或者是插件。其实这类的错误早就存在多年，但是一直未受到太多重视，最终在[PHP 8的时候变成了Deprecated](https://www.php.net/manual/en/migration80.deprecated.php)报错。

以下是出现错误代码：
[code] 
    function xxxxx( $avatar, $id_or_email, $size=30, $default, $alt )
[/code]

其实出现的问题很简单，错误的点就在`$size=30`这个参数。由于PHP规定，在可选参数中，若有默认值的参数不在最后一个，将会直接忽视它的默认值。所以这样写根本没必要，直接把默认值删除即可：
[code] 
    function xxxxx( $avatar, $id_or_email, $size, $default, $alt )
[/code]

也许有人会担心是不是会导致一些问题，这大可不必。因为这个问题在PHP 8之前就存在，只是没有报错而已。这次PHP 8特地报了个Deprecated来解决这种不严谨的使用。当然，这也是为什么虽然只是个Deprecated，也拿出来说一说的原因。赶紧把一些历史遗留问题解决了把~
