# encoding=utf8
#aurhor :LiMengming
#source    = https://ransomwaretracker.abuse.ch/downloads/RW_DOMBL.txt
#source_id = 21 

import download

source = '21'
stamp  = 'BlackList'
url    = 'https://ransomwaretracker.abuse.ch/downloads/RW_DOMBL.txt'

download.download_domain(source, stamp, url)