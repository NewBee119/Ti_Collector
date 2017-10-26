# ThreatFeedSpider
# run.py 
	通过指令 python run.py  ，调用scrip目录下的脚本文件，通过脚本将feed下的威胁情报录入数据库。

# script目录下：
	（1）相关feed的爬虫脚本；
	（2）feed_id.txt 相关feed与数据库中存储的source_id的对照；
	（3）采用MySQL数据库收录威胁情报，在使用本系统采集数据时，请自行修改1.py脚本和download.py脚本内与数据库有关的语句和参数。
		
# Sql：
	TiDB.sql文件，构建数据库以及数据库表格。

# Python依赖库：
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
