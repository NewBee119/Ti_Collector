BlackListSpider

1. run.py ：通过指令 python run.py  ，调用scrip目录下的脚本文件，通过脚本将feed下的威胁情报录入数据库。

2. script目录下：（1）相关feed的爬虫脚本；
		（2）feed_id.txt 相关feed与数据库中存储的source_id的对照；
		（3）采用MySQL数据库收录威胁情报，在使用本系统采集数据时，请自行修改1.py脚本和download.py脚本内与数据库有关的语句和参数。
		
3. MySQL-sql：TiDB.sql文件，构建数据库以及数据库表格。

Python依赖库：
MySQLdb
sys 
time
re
urlib
urllib2
threading
datetime
Queue
json
socket
os


# Ti_Collecter
  我们收集了一些开源的黑名单网站,把这些网站中的数据爬取整理存储下来。
## BlackListSpier
  一个爬取开源黑名单网站的爬虫，该网站为https://iplists.firehol.org 
  
  我们爬取了它的所有黑名单，共计900000+条。该网站中的黑名单更新频率高、可信度高，是一个很好的来源。
## ThreatArticleSpiders.py
  用来爬取https://badcyber.com 该网站不定期发布与安全相关的文章，我们主要爬取了这个网站上的有关其他网站的链接，通过这些链接发现新的威胁情报来源。
## request.py
  是查询dns记录的脚本 使用时要将dns_sniffer生成的待查文件放入同一个文件夹中。直接运行该脚本即可。
## dns_sniffer
  是捕获DNS请求包的程序，可以使用run.py启动
  其整个流程如下图所示。
  ![流程图](https://github.com/scu-igroup/Ti_Collecter/raw/master/images/流程.png)
  
  最后的结果如下图所示。
  
  ![结果](https://github.com/scu-igroup/Ti_Collecter/raw/master/images/fin.png)
  
  同时会生成一个文件，把匹配到的结果存储在其中。
