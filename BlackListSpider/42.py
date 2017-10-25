# encoding=utf8
#date:2017-10-19
#domain type
#source :http://www.nothink.org/blacklist/blacklist_malware_irc.txt
#source_id:42

import download

source = '42'
stamp  = 'malware'
url    = 'http://www.nothink.org/blacklist/blacklist_malware_irc.txt'
download.download_ip(source, stamp, url)