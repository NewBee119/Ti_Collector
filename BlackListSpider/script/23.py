# encoding=utf8
#aurhor :LiMengming
#date:2017-10-19
#domain type
#source = https://ransomwaretracker.abuse.ch/downloads/RW_URLBL.txt
#source_id = 23

import download

stamp = 'BalckList'
source ='23'
url = 'https://ransomwaretracker.abuse.ch/downloads/RW_URLBL.txt'
download.download_url(source, stamp, url)