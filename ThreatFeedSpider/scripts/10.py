# encoding=utf8
#source:  https://raw.githubusercontent.com/firehol/blocklist-ipsets/master/cruzit_web_attacks.ipset
#source ID : 10
#date:2017-10-19
#ip type

import download
source = '10'
url = 'https://raw.githubusercontent.com/firehol/blocklist-ipsets/master/cruzit_web_attacks.ipset'
stamp = 'attack'
download.download_ip(source,stamp,url)