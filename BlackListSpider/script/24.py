# encoding=utf8
#aurhor :LiMengming
#date:2017-10-20
#domain type

import download
url    = 'https://raw.githubusercontent.com/firehol/blocklist-ipsets/master/ri_web_proxies_30d.ipset'
stamp  = 'anonymizers'
source = '24'

download.download_ip(source, stamp, url)
