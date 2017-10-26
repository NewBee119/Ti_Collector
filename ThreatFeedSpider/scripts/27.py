# encoding=utf8
#aurhor :LiMengming
#date:2017-10-19
#domain type
#source = https://raw.githubusercontent.com/firehol/blocklist-ipsets/master/socks_proxy_7d.ipset
#source_id =27

import download
source = '27'
stamp ='anoymizers'
url = 'https://raw.githubusercontent.com/firehol/blocklist-ipsets/master/socks_proxy_7d.ipset' 
download.download_ip(source, stamp, url)