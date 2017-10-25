# Ti_Collecter
我们收集了一些开源的黑名单网站如下。

https://www.badips.com/get/list/any/2?age=7d
https://raw.githubusercontent.com/firehol/blocklist-ipsets/master/botscout_1d.ipset
http://danger.rulez.sk/projects/bruteforceblocker/blist.php
http://cinsscore.com/list/ci-badguys.txt
https://raw.githubusercontent.com/firehol/blocklist-ipsets/master/cruzit_web_attacks.ipset
http://cybersweat.shop/iprep/iprep_ramnode.txt
https://isc.sans.edu/feeds/suspiciousdomains_Low.txt
http://blocklist.greensnow.co/greensnow.txt
https://malc0de.com/bl/ZONES
https://www.malwaredomainlist.com/hostslist/hosts.txt
https://myip.ms/files/blacklist/htaccess/latest_blacklist.txt
https://openphish.com/feed.txt
https://ransomwaretracker.abuse.ch/downloads/RW_DOMBL.txt
https://ransomwaretracker.abuse.ch/downloads/RW_IPBL.txt
https://ransomwaretracker.abuse.ch/downloads/RW_URLBL.txt
https://raw.githubusercontent.com/firehol/blocklist-ipsets/master/ri_web_proxies_30d.ipset
https://report.cs.rutgers.edu/DROP/attackers
http://sblam.com/blacklist.txt
https://raw.githubusercontent.com/firehol/blocklist-ipsets/master/socks_proxy_7d.ipset
https://raw.githubusercontent.com/firehol/blocklist-ipsets/master/sslproxies_1d.ipset
https://check.torproject.org/cgi-bin/TorBulkExitList.py?ip=1.1.1.1
http://www.urlvir.com/export-hosts/
http://vxvault.net/URL_List.php
https://zeustracker.abuse.ch/blocklist.php?download=domainblocklist
https://zeustracker.abuse.ch/blocklist.php?download=badips
https://zeustracker.abuse.ch/blocklist.php?download=compromised
https://reputation.alienvault.com/reputation.generic
http://www.ciarmy.com/list/ci-badguys.txt
http://talosintel.com/files/additional_resources/ips_blacklist/ip-filter.blf
https://reputation.alienvault.com/reputation.generic
http://www.nothink.org/blacklist/blacklist_malware_dns.txt
http://www.nothink.org/blacklist/blacklist_malware_http.txt
http://www.nothink.org/blacklist/blacklist_malware_irc.txt
http://www.nothink.org/blacklist/blacklist_ssh_all.txt
# BlackListSpier
  一个爬取开源黑名单网站的爬虫，该网站为https://iplists.firehol.org 
  我们爬取了它的所有黑名单，共计900000+条。该网站中的黑名单更新频率高、可信度高，是一个很好的来源。
# ThreatArticleSpiders
  用来爬取https://badcyber.com 该网站不定期发布与安全相关的文章，我们主要爬取了这个网站上的有关其他网站的链接，通过这些链接发现新的威胁情报来源
# request.py
  是查询dns记录的脚本 使用时要将dns_sniffer生成的待查文件放入同一个文件夹中。直接运行该脚本即可
# dns_sniffer
  是捕获DNS请求包的程序，可以使用run.py启动
