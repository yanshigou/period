## 前言

为了监测nginx服务器，我使用了很多个方法(之前的文章都有写到)，例如Netdata实时监测，ngxtop分析log(也可以实时监测)，但我想在nginx服务器挂掉的时候立马给我发邮件，通知我及时重新启动。

所以我写了一个脚本，定时去访问以下某个链接，看是否挂掉或者其他问题（这个方法特别的愚蠢）

但总不能一直启动脚本吧

所以，就使用了celery的定时任务来执行，这次是完全独立的，不依赖于Django了



## 目录结构



![](https://raw.githubusercontent.com/yanshigou/yanshigou.github.io/master/img/t/period.png)