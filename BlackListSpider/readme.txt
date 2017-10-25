1. run.py ：通过指令 python run.py  ，调用scrip目录下的脚本文件，通过脚本将feed下的威胁情报通过爬虫传入数据库
2. script目录下：（1）相关feed的爬虫脚本
				 （2）feed_id.txt 相关feed与数据库中存储的source_id的对照

3.MySQL-sql：TiDB.sql文件，构建数据库以及数据库表格