# encoding=utf8
#source:  https://openphish.com/feed.txt
#source ID : 20
#date:2017-9-22


import download

stamp = 'Phish'
source = '20'
url = 'https://openphish.com/feed.txt'
download.download_url(source, stamp, url)