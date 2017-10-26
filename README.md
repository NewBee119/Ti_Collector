# Ti_Collecter
  我们收集了一些开源的黑名单网站,把这些网站中的数据爬取整理存储下来。
# BlackListSpier.py
  一个爬取开源黑名单网站的爬虫，该网站为https://iplists.firehol.org 
  我们爬取了它的所有黑名单，共计900000+条。该网站中的黑名单更新频率高、可信度高，是一个很好的来源。
# ThreatArticleSpiders.py
  用来爬取https://badcyber.com 该网站不定期发布与安全相关的文章，我们主要爬取了这个网站上的有关其他网站的链接，通过这些链接发现新的威胁情报来源。
# request.py
  是查询dns记录的脚本 使用时要将dns_sniffer生成的待查文件放入同一个文件夹中。直接运行该脚本即可。
# dns_sniffer
  是捕获DNS请求包的程序，可以使用run.py启动
  其整个流程如下图所示。
  ![流程图](https://github.com/scu-igroup/Ti_Collecter/raw/master/流程.png)