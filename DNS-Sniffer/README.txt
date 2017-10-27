Windows及Linux下的Dns嗅探器：在相应环境进入RunSniffer.py所在文件下（windows直接双击RunSniffer.py,Linux输入命令python RunSniffer.py)，运行后根据命令行提示选择网卡，之后就可以在当前目录下看到新生产的DNS域名文件dns.txt。
Linux和Windows中都有源码，如何编译生成看下面说明。


1.Windows环境
安装Winpcap，正常电脑基本都安装了，没有安装的可在Windows文件夹下找到它的安装文件WinPcap_4_1_2.exe(64)或者自行百度下载。
VS中需配置项目属性 详情请参看：http://www.cnblogs.com/laddielan/p/5405534.html。
编译：安装Winpcap并配置好项目属性后，打开源码用VS2013及以上版本直接编译生成即可。

2.Linux环境
安装libcap库，Ubuntu输入命令apt-get install libpcap-dev即可安装，
CentOS参考http://www.cnblogs.com/wawahaha/p/3821486.html
编译：安装好库后，进入Linux文件夹下执行make就可生成可执行文件dns。


注意：Winpcap和Libpcap这两个是必须安装的，不然既无法运行而且也无法编译源码生成可执行文件，python需要2.x版本，3.x版本运行RunSniffer.py会报错，需要的可直接修改RunSniffer.py（很简单的）。Windows下电脑电源设置为从不休眠，因为休眠后会关闭嗅探器。
