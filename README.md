# Ti_Collector  
----
   Ti_Collector为Threat Intelligence Collector，主要关注网上公开的信誉类威胁情报和事件类威胁情报。
   
   信誉类威胁情报主要来源于一些安全社区的分享；事件类威胁情报主要来源于安全企业的咨询分享。     
   
   这些威胁情报数据通过爬虫手段，经分类处理后自动存入到数据库中，以构建自身的威胁情报库。
   
   同时，我们提供一个捕获和查询本机DNS纪录中是否存在威胁行为的程序。
   
   整个流程如图所示。
   
   ![流程](https://github.com/scu-igroup/Ti_Collecter/raw/master/Images/流程.jpg)
  
# Code Introduction
---
## ThreatFeedSpider

* 说明
	
  		ThreatFeedSpider中包含了31个爬虫，爬取了31个不同的信誉类威胁情报来源，然后按类存放到数据库中。
  	
  		这些数据大概包括1090000个ip地址，4600个域名，14000个url。
  
  		scripts目录下：（1）存有相关feed的爬虫脚本；（2）feed_id.txt 存有相关feed与数据库中存储的source_id的对照
  
  
* 环境要求

  		测试计算机用的Ubuntu 16.04.1，python 2.7，MySQL 5.7.20
  
  		python依赖环境为：MySQLdb
  
 * 数据库
 
   		sql目录中的TiDB.sql文件，构建数据库以及数据库表格。
   
   		IP地址为192.168.9.223，数据库密码：123456，测试及使用时请自行作出修改。
   
 * 使用
 
   		首先要运行sql目录下的建库脚本。
   		
   		然后再运行RunThreatSpider.py之前，请自行修改1.py脚本和download.py脚本内与数据库有关的语句和参数。
   
  		通过命令 python RunThreatSpider.py，调用scripts目录下的脚本文件，通过脚本将feed下的威胁情报录入数据库。
   
  		注：由于网络问题，个别feed网站不可到达而出现timeout报错。

  
## ThreatArticleSpider
* 说明

  		处理事件类威胁情报，在现阶段只有一个爬取文章链接的爬虫ThreatArticleSpider.py后续会陆续增加爬取链接的脚本和从文章中提取相应IoC信息的脚本。
  
* 使用

  		直接运行命令 python ThreatArticleSpider.py 即可。

* 结果

  		运行过程中会存储大量的html文件，这些文件为链接的来源，不需要的可以自行删除。
  
  		运行完成后会生成一个ret.json文件存储网站上的链接，用户可自行判断其中的链接是否有进一步处理的价值。 
  
 	 	Result目录下存储的是我们整理的文章中的事件类威胁情报，以#开头的是来源和时间，其余的是IoC信息。

## DNS-Sniffer
* 说明

  		DNS-Sniffer是用来捕获DNS请求包的程序，用C写成，内涵源码和编译好的程序，在Linux和Windows环境下可以直接使用RunSniffer.py启动。Windows下也可以直接运行DNS.exe。运行时会生成一个Dns.txt文件来存储DNS记录。

  
* 环境要求

  1.Windows环境
  
 		该程序要用到Winpcap，一般情况下都已经安装了，如果没有安装可以在Windows文件夹下找到它的安装文件WinPcap_4_1_2.exe(64)
  		VS中需配置项目属性 详情请参看：http://www.cnblogs.com/laddielan/p/5405534.html。
  		安装Winpcap并配置好项目属性后，打开源码用VS2013及以上版本直接编译生成即可。
  	
  2.Linux环境
  
  		安装libcap库，Ubuntu输入命令apt-get install libpcap-dev即可安装。
		CentOS参考http://www.cnblogs.com/wawahaha/p/3821486.html
		编译：安装好库后，进入Linux文件夹下执行make就可生成可执行文件dns。
		
* 使用

  		直接在同一目录下运行RunSniffer.py即可。 Linux下需要以管理员权限运行
  
  		注意：
  
  		Winpcap和Libpcap这两个是必须安装的，不然既无法运行而且也无法编译源码生成可执行文件，python需要2.x版本，3.x版本运行RunSniffer.py会报错。

  		Windows下电脑电源设置为从不休眠，因为休眠后会关闭嗅探器。
  
## request.py

* 说明

  		用来判断NDS-Sniffer捕获到的DNS纪录中是否有威胁情报中记录的恶意行为。
  
  		在查询到有恶意DNS记录后会输出警告，脚本运行完后会生成一个结果文件Result.txt

* 环境要求

  		python：MySQLdb库
  
  		数据库的信息要自行设置

* 使用

  		使用时要将DNS-Sniffer生成的待查文件Dns.txt放入同一个目录下。进入该目录直接运行命令：python request.py即可。
  
  		如果用户修改了数据库的信息，要在request.py中的相应位置修改数据库信息。  
  
# Screenshots
---


ThreatFeedSpider

![run](https://github.com/scu-igroup/Ti_Collecter/raw/master/Images/run.py截图.png)

DNS-Sniffer生成的文件dns.txt

![dns.txt](https://github.com/scu-igroup/Ti_Collecter/raw/master/Images/dns.png)

request.py

![结果](https://github.com/scu-igroup/Ti_Collecter/raw/master/Images/fin.png)
  
