#encoding=utf8

import download
source ='34'
stamp  ='badips' 
url    ='https://zeustracker.abuse.ch/blocklist.php?download=badips'
download.download_ip(source, stamp, url)