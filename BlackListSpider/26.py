# encoding=utf8
#aurhor :LiMengming
#date:2017-10-19
#domain type
#source :http://sblam.com/blacklist.txt
#source_id = 26

import download
source = '26'
stamp  = 'email spammer'
url    = 'http://sblam.com/blacklist.txt'
download.download_ip(source, stamp, url)