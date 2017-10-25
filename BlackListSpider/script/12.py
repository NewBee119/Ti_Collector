# encoding=utf8
#source:  https://raw.githubusercontent.com/firehol/blocklist-ipsets/master/cruzit_web_attacks.ipset
#source ID : 10
#date:2017-10-19
#ip type

import download
source = '10'
url = 'http://cybersweat.shop/iprep/iprep_ramnode.txt'
stamp = 'BlackList'
download.download_ip(source,stamp,url)