# encoding=utf8
#date:2017-10-19
#domain type
#source:https://zeustracker.abuse.ch/blocklist.php?download=compromised
#source_id:35

import download

stamp  = 'BlackList'
source = '35'
url    = 'https://zeustracker.abuse.ch/blocklist.php?download=compromised'
download.download_ip_2(source, stamp, url)
