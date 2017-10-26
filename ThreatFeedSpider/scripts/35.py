# encoding=utf8
#date:2017-10-19
#domain type
#source:https://reputation.alienvault.com/reputation.generic
#source_id:37

import download

stamp  = 'BlackList'
source = '37'
url    = 'https://reputation.alienvault.com/reputation.generic'
download.download_ip_2(source, stamp, url)