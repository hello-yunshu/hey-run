+++
title = "WordPress后台加速 - 使用CDN替代本地小文件"
date = 2021-01-21T00:06:47+08:00
draft = true
description = "搭过网站的小伙伴应该知道CDN的作用，不仅可以有效的提高网站的访问速度，还能降低对网站服务器的性能影响。而对于CDN提供商，小网站的CDN请求解决了浪费剩余资源的问题，也成为了盈利的一种方式，可谓是双赢之举。为了方便还未了解CDN的小伙伴，这里说一下CDN的基础知识： CDN是什么 CDN的全称是C"
slug = "wordpresshou-tai-jia-su"
featureimage = "https://cdn.idleleo.com/wp-content/uploads/2021/01/202101202331.jpg"
+++

搭过网站的小伙伴应该知道CDN的作用，不仅可以有效的提高网站的访问速度，还能降低对网站服务器的性能影响。而对于CDN提供商，小网站的CDN请求解决了浪费剩余资源的问题，也成为了盈利的一种方式，可谓是双赢之举。为了方便还未了解CDN的小伙伴，这里说一下CDN的基础知识：

#### CDN是什么

CDN的全称是Content Delivery Network，即内容分发网络。CDN是构建在现有网络基础之上的智能虚拟网络，依靠部署在各地的边缘服务器，通过中心平台的负载均衡、内容分发、调度等功能模块，使用户就近获取所需内容，降低网络拥塞，提高用户访问响应速度和命中率。CDN的关键技术主要有内容存储和分发技术。——百度百科

#### WordPress的CDN使用问题

对于WordPress网站而言，情况有些特殊。这主要与WordPress的设计有关系，WordPress拥有前台、后台两种界面，最常为大家熟知的是前台界面。前台往往是静态或者伪静态的页面，这样的好处是访问速度能尽量不受服务器的性能的影响。同时，这样做也能使一些js、css、字体等资源实现静态化，更好的为CDN或本地缓存，进一步降低服务器的开销，进一步加速访问速度。（这当然也是无主界的策略）

![](/images/wp-content/uploads/2021/01/202101202331.jpg)

前端静态化，这无可厚非，但问题在于WordPress的后台。WordPress后台一般开放于权限更高的用户，当然有些WordPress网站后台也会直接对普通用户开放。WordPress后台与前台的不同在于后台是动态的。由于WordPress后台可以对整个网站进行调整，因此后台作为动态页面亦无可厚非。但问题就在于，即便使用了全站CDN，在访问WordPress后台时，为了保证动态访问，所有的js、css等小文件都是根据每次访问而请求一次的。这无疑加剧了网站服务器的开销，比如随便的一个WordPress网站后台，居然有上百个小文件请求：

![](/images/wp-content/uploads/2021/01/202101202332-1024x607.gif)来自wp-china.org测试

那么有没有办法把一些小文件不再从源服务器请求？当然是有的，但这里要考虑一些问题：

  1. 从CDN请求后，小文件能不能随着WordPress的版本更新而即时更新？
  2. 这些小文件对WordPress后台的运行至关重要，CDN是否有被投毒的风险？

笔者最近在研究[jsdelivr.com](http://jsdelivr.com)网站以及最近较火的[WP-China-Yes插件](https://wp-china.org/)时，找出了一个好的解决方案。

#### 利用jsdelivr加速WordPress后台

### jsdelivr简介

jsdelivr可能还有一些小伙伴比较陌生，这是一个公共加速平台。国外是cloudflare代理，而国内是网宿代理，仅仅从速度而言完全没有问题。

今天要说的不仅是jsdelivr速度，jsdelivr与其他CDN相比最与众不同的功能是它可以加速GitHub与WordPress。这种加速不是一般的某些公共大型项目的加速，而是平台所有的公共项目的加速！这就厉害了，WordPress在GitHub上是有独立项目的，而只需要按照jsdelivr的规则，完全可以无缝替代本地的小文件。

### jsdelivr加速规则

Load any GitHub release, commit, or branch:

```
https://cdn.jsdelivr.net/gh/user/repo@version/file
```

Load any plugin from the WordPress.org plugins SVN repo:

```
https://cdn.jsdelivr.net/wp/plugins/project/tags/version/file
```

上述规则不仅可以加速GitHub内容，还能加速WordPress的插件内容。现在有了基础，就要提到WP-China-Yes插件的一个后台加速功能了。

### 加速后台代码

以下是来自插件WP-China-Yes的后台加速代码：

```php
add_action('init', function () {
    ob_start(function ($buffer) {
        return preg_replace('~'.home_url('/').'(wp-admin|wp-includes)/(css|js)/~', sprintf('https://a2.wp-china-yes.net/WordPress@%s/$1/$2/', $GLOBALS['wp_version']), $buffer);
    });
});
```

利用上述的jsdelivr的加速方式后，就是如下的加速代码：

```php
add_action('init', function () {
     ob_start(function ($buffer) {
         $buffer = preg_replace('~'.home_url('/').'(wp-admin|wp-includes)/(css|js)/~', sprintf('//cdn.jsdelivr.net/gh/WordPress/WordPress@%s/$1/$2/', $GLOBALS['wp_version']), $buffer);
         return $buffer;
     });
 });
```

选择以上的**两段代码其中之一** 直接放入主题/插件中即可立即生效。（**注意：请勿对测试版加速！** ）后台访问速度直接翻翻！

![](/images/wp-content/uploads/2021/01/202101202330-1024x607.gif)来自wp-china.org测试

也许又小伙伴会问为什么会有两段差不多的代码呢？不能直接用WP-China-Yes插件提供的吗？要解答，我们需要回到上面提出的两个问题。

### 两个问题的解答

还记得上述的两个问题吗？

  1. 从CDN请求后，小文件能不能随着WordPress的版本更新而即时更新？
  2. 这些小文件对WordPress后台的运行至关重要，CDN是否有被投毒的风险？

由于GitHub的项目特性，往往先会发布Releases，在面对普通用户推送新版本。因此使用jsdelivr（根据其策略）小文件是会随着WordPress的版本更新而即时得到更新的。而WP-China-Yes插件提供的CDN情况未知。

再者，对于WP-China-Yes插件来说（这里没有贬低的意思），毕竟WP-China-Yes插件是后起之秀。对于CDN来说，最基本的稳定，安全，对于一个才刚刚出现不到两年的CDN来说，的确还要时间检验。而对于jsdelivr这类老牌的CDN，相对更容易获得信任。当然，即便是jsdelivr也有被投毒的历史，可见这类安全问题更难被忽略。

![](/images/wp-content/uploads/2021/01/202101202334.jpg)

最后由于jsdelivr不仅仅用于加速WordPress后台，它还能加速很多公共库。因此在访问角度看，如果你的网站已经启用了jsdelivr加速（比如无主界哈哈），那么选择jsdelivr作为后台加速显然是明智的选择。

#### 等等，还有？

对你没看错，这里笔者提了这么多的jsdelivr绝不仅仅局限于此。试想，jsdelivr可以加速GitHub，而很多WordPress插件在GitHub上开源...

对了，除去加速WordPress的后台，还能加速WordPress的插件！话不多说，直接上代码：

```php
add_action('init', function () {
     ob_start(function ($buffer) {
         $buffer = preg_replace('~'.home_url('/').'(wp-admin|wp-includes)/(css|js)/~', sprintf('//cdn.jsdelivr.net/gh/WordPress/WordPress@%s/$1/$2/', $GLOBALS['wp_version']), $buffer);
         if (is_plugin_active('woocommerce/woocommerce.php')) {
             $plugin_data = get_plugin_data(WP_PLUGIN_DIR . '/woocommerce/woocommerce.php');
             $buffer = preg_replace('~'.home_url('/').'wp-content/plugins/woocommerce/(.*).(css|js|woff|woff2|jpg|png|svg|webp)~', sprintf('//cdn.jsdelivr.net/gh/woocommerce/woocommerce@%s/$1.$2', $plugin_data['Version']), $buffer);
         }
         if (is_plugin_active('autoptimize/autoptimize.php')) {
             $plugin_data = get_plugin_data(WP_PLUGIN_DIR . '/autoptimize/autoptimize.php');
             $buffer = preg_replace('~'.home_url('/').'wp-content/plugins/autoptimize/(.*).(css|js|woff|woff2|jpg|png|svg|webp)~', sprintf('//cdn.jsdelivr.net/gh/futtta/autoptimize@%s/$1.$2', $plugin_data['Version']), $buffer);
         }
         return $buffer;
     });
 });
```

上述代码只是简单加速了woocommerce与autoptimize两个插件。用的是GitHub的仓库加速方式，当然也可以改成WordPress SVN的方式：

```php
add_action('init', function () {
     ob_start(function ($buffer) {
         $buffer = preg_replace('~'.home_url('/').'(wp-admin|wp-includes)/(css|js)/~', sprintf('//cdn.jsdelivr.net/gh/WordPress/WordPress@%s/$1/$2/', $GLOBALS['wp_version']), $buffer);
         if (WOOCOMMERCE_VERSION) {
             $buffer = preg_replace('~'.home_url('/').'wp-content/plugins/woocommerce/(.*).(css|js|woff|woff2|jpg|png|svg|webp)~', sprintf('//cdn.jsdelivr.net/wp/plugins/woocommerce/tags/%s/$1.$2', WOOCOMMERCE_VERSION), $buffer);
         }
         if (AUTOPTIMIZE_PLUGIN_VERSION) {
             $buffer = preg_replace('~'.home_url('/').'wp-content/plugins/autoptimize/(.*).(css|js|woff|woff2|jpg|png|svg|webp)~', sprintf('//cdn.jsdelivr.net/wp/plugins/autoptimize/tags/%s/$1.$2', AUTOPTIMIZE_PLUGIN_VERSION), $buffer);
         }
         return $buffer;
     });
 });
```

很显然，此类加速方式不会局限于这两个插件，只会局限于大家的想象力！（**注意：请勿对测试版插件加速！** ）。

#### 还有插件？！

现在，笔者直接把代码集成到了插件[Wp Admin Boost](https://github.com/paniy/WP-Admin-Boost)中，**此插件集成了上述的所有功能，还可以加速全部WordPress后台插件！同时，还能自行选择禁用那些不需要加速的插件！**

插件截图：

![](/images/wp-content/uploads/2021/01/20210122203422-1024x507.jpg)

详情可见这篇文章：[《插件 WP Admin Boost 正式发布！》](https://www.idleleo.com/01/5040.html)

现在笔者把已知所有的好办法都给大家啦~快来试试吧~
