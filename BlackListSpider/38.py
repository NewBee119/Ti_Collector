# encoding=utf8
#date:2017-10-19
#domain type

#source :http://www.ciarmy.com/list/ci-badguys.txt
#source_id :38
import download
stamp  = 'BlackList'
source = '38'
url    = 'http://www.ciarmy.com/list/ci-badguys.txt'
download.download_ip(source, stamp, url)