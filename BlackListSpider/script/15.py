# encoding=utf8
#source: http://blocklist.greensnow.co/greensnow.txt
#source ID : 20
#date:2017-10-19
#ip type

import download

url    = 'http://blocklist.greensnow.co/greensnow.txt'
stamp  = 'BlackList'
source = '15'


download.download_ip(source, stamp, url)