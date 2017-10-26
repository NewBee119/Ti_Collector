# encoding=utf8
#aurhor :LiMengming
#date:2017-10-20
#source =https://ransomwaretracker.abuse.ch/downloads/RW_IPBL.txt
#source_id = 22

import download

stamp  = 'BlakList'
source = '22'
url    = 'https://ransomwaretracker.abuse.ch/downloads/RW_IPBL.txt'
download.download_ip(source, stamp, url)