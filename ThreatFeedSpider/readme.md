# ThreatFeedSpider
	通过python爬虫，对31个威胁情报源（feed）进行数据搜集并将结果存入MySQL数据库。
	这些数据大概包括1090000个ip地址，4600个域名，14000个url。
	测试计算机用的Ubuntu 16.04.1，python 2.7，MySQL 5.7.20
	IP地址为192.168.9.223，数据库密码：123456，测试及使用时请自行作出修改


## Python依赖库：
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
	warnings


## Sql：
	TiDB.sql文件，构建数据库以及数据库表格。

## scripts目录下：
	（1）相关feed的爬虫脚本；
	（2）feed_id.txt 相关feed与数据库中存储的source_id的对照；
	（3）采用MySQL数据库收录威胁情报，在使用本系统采集数据时，请自行修改1.py脚本和download.py脚本内与数据库有关的语句和参数。


## run.py 
	通过指令 python run.py  ，调用scrip目录下的脚本文件，通过脚本将feed下的威胁情报录入数据库。 
	由于网络问题，个别feed网站不可到达而出现timeout报错
	以下是run.py的运行结果
  ![image_run.py](https://github.com/scu-igroup/Ti_Collector/blob/master/Image/run.py%E6%88%AA%E5%9B%BE.png)

