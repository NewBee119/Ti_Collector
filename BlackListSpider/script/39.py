# encoding=utf8
#date:2017-10-19
#domain type
#original source:http://talosintel.com/files/additional_resources/ips_blacklist/ip-filter.blf
#source :http://talosintel.com/files/additional_resources/ips_blacklist/ip-filter.blf 
#source_id :39
#download the web using python urllib pack may be banned for some unknown reason

import download
stamp  = 'BlackList'
source = '39'
url    = 'https://talos-intelligence-site.s3.amazonaws.com/production/document_files/files/000/015/549/original/ip_filter.blf?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAIXACIED2SPMSC7GA%2F20171020%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20171020T121734Z&X-Amz-Expires=3600&X-Amz-SignedHeaders=host&X-Amz-Signature=adc4eb0c38e4b16ea72f28046592a108e1770881fe63f1ee64b145143359bcaa'
download.download_ip(source, stamp, url)