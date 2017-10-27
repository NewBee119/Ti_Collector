# Ti_Collector  
----
   Ti_Collector为Threat Intelligence Collector，主要关注网上公开的信誉类威胁情报和事件类威胁情报。
   
   信誉类威胁情报主要来源于一些安全社区的分享；事件类威胁情报主要来源于安全企业的咨询分享。     
   
   这些威胁情报数据通过爬虫手段，经分类处理后自动存入到数据库中，以构建自身的威胁情报库。
   
   同时，我们提供一个捕获和查询本机DNS纪录中是否存在威胁行为的程序。
  
# Code Introduction
---
## ThreatFeedSpider
  包含了31个爬虫，爬取了31个不同的信誉类威胁情报来源，然后按类存放到数据库中。
  
  为了方便使用，我们提供建库脚本和批量运行爬虫的脚本。
## ThreatArticleSpider
  处理事件类威胁情报，在现阶段只有一个爬取文章链接的爬虫ThreatArticleSpider.py后续会陆续增加爬取链接的脚本和从文章中提取相应IoC信息的脚本。
  
## request.py
  是查询dns记录的脚本，使用时要将dns_sniffer生成的待查文件放入同一个文件夹中。直接运行该脚本即可。
  
  如果用户修改了数据库的信息，要在request.py中的相应位置修改数据库信息。
## DNS-Sniffer
  是捕获DNS请求包的程序，用C写成，内涵源码和编译好的程序，可以直接使用run.py启动。
  
  
# Screenshots
---
捕获和查询DNS纪录流程

  ![流程图](https://github.com/scu-igroup/Ti_Collecter/raw/master/Images/流程.png)

ThreatFeedSpider

![run](https://github.com/scu-igroup/Ti_Collecter/raw/master/Images/run.py截图.png)

dns_sniffer生成的文件dns.txt

![dns.txt](https://github.com/scu-igroup/Ti_Collecter/raw/master/Images/dns.png)

request.py

![结果](https://github.com/scu-igroup/Ti_Collecter/raw/master/Images/fin.png)
  
