# encoding=utf8
#date:2017-10-19
#domain type
#source :https://isc.sans.edu/feeds/suspiciousdomains_Low.txt
#source_id:14
#attention; cannot connected without VPN

import download

source = '14'
stamp  = 'BlackList'
url    = 'https://isc.sans.edu/feeds/suspiciousdomains_Low.txt'
download.download_ip(source, stamp, url)