# encoding=utf8
#date:2017-10-19
#domain type
#source :http://www.nothink.org/blacklist/blacklist_malware_http.txt
#source_id:41

import download

source = '41'
stamp  = 'malware'
url    = 'http://www.nothink.org/blacklist/blacklist_malware_http.txt'
download.download_ip(source, stamp, url)