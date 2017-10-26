import download

url = 'https://raw.githubusercontent.com/firehol/blocklist-ipsets/master/botscout_1d.ipset'
source =  '7'
stamp = 'abuse'
download.download_ip(source,stamp,url)