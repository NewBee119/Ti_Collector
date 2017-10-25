Windows及LinuxDns嗅探器：在相应环境中运行run.py，运行后根据命令行提示选择网卡，之后就可以在当前目录下看到新生产的DNS域名文件dns.txt。
code中的是源码有需要的可以看一下。


1.Windows环境
安装Winpcap，正常电脑基本都安装了，没有安装的自行百度下载。
VS中需配置项目属性 详情请参看：http://www.cnblogs.com/laddielan/p/5405534.html
编译：配置好项目属性后，打开源码用VS直接生成就行。

2.Linux环境
安装libcap库，Ubuntu参考http://blog.csdn.net/loverooney/article/details/38543191
CentOS参考http://www.cnblogs.com/wawahaha/p/3821486.html
编译：进入Linux文件夹下执行make就可生成。


注意：python需要2.x版本，Windows下电脑电源设置为从不休眠，因为休眠后会关闭嗅探器。
