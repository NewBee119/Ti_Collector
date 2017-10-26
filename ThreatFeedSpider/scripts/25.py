# encoding=utf8
#aurhor :LiMengming
#date:2017-10-19
#domain type
#source :https://report.cs.rutgers.edu/DROP/attackers
#source_id = 25

import download
source = '25'
stamp  = 'attacker'
url    = 'https://report.cs.rutgers.edu/DROP/attackers'
download.download_ip(source, stamp, url)