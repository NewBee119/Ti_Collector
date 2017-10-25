# encoding=utf8
#aurhor :LiMengming
#date:2017-10-19
#domain type
#source:https://reputation.alienvault.com/reputation.generic
#source_id:37

import download
stamp  ='reputation'
source = '37'
url    = 'https://reputation.alienvault.com/reputation.generic'
download.download_ip(source, stamp, url)