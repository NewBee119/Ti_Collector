# encoding=utf8
#source: https://www.malwaredomainlist.com/hostslist/hosts.txt
#source ID : 18
#date:2017-10-19
#domain type

import download

source = '18'
stamp  = 'malware'
url    = 'https://www.malwaredomainlist.com/hostslist/hosts.txt'

download.download_domain(source, stamp, url)