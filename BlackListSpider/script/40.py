# encoding=utf8
#date:2017-10-19
#domain type
#source :http://www.nothink.org/blacklist/blacklist_malware_dns.txt
#source_id:40

import download

source = '40'
stamp  = 'malware'
url    = 'http://www.nothink.org/blacklist/blacklist_malware_dns.txt'
download.download_ip(source, stamp, url)