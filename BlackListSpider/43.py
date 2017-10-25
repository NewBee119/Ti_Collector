# encoding=utf8
#date:2017-10-19
#domain type
#source :http://www.nothink.org/blacklist/blacklist_ssh_all.txt
#source_id:43

import download

source = '43'
stamp  = 'BlackList'
url    = 'http://www.nothink.org/blacklist/blacklist_ssh_all.txt'
download.download_ip(source, stamp, url)