# encoding=utf8

import sys
import download

reload(sys) 
sys.setdefaultencoding('utf8')


source = '8'
url = 'http://danger.rulez.sk/projects/bruteforceblocker/blist.php'
stamp = 'BlackList'

download.download_ip_2(source, stamp, url)