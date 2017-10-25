# encoding=utf8
#aurhor :LiMengming
#date:2017-10-19
#domain type
#source = https://raw.githubusercontent.com/firehol/blocklist-ipsets/master/sslproxies_1d.ipset
#source_id =29

import download
source = '29'
stamp ='anoymizers'
url = 'https://raw.githubusercontent.com/firehol/blocklist-ipsets/master/sslproxies_1d.ipset' 
download.download_ip(source, stamp, url)