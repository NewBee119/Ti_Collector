# encoding=utf8
#date:2017-10-19
#domain type
#source = https://raw.githubusercontent.com/firehol/blocklist-ipsets/master/sslproxies_1d.ipset
#source_id =31

import download
source = '31'
stamp ='Tor node'
url = 'http://www.urlvir.com/export-hosts/' 
download.download_ip(source, stamp, url)