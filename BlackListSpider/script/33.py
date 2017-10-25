# encoding=utf8
#aurhor :LiMengming
#date:2017-10-19
#domain type
#source   :https://zeustracker.abuse.ch/blocklist.php?download=domainblocklist
#source_id:33

import download

source = '33'
stamp  = 'BlackList'
url    = 'https://zeustracker.abuse.ch/blocklist.php?download=domainblocklist'
download.download_domain(source, stamp, url)