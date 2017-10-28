# encoding=utf8
#date:2017-10-24
#function : request the data using domain

import MySQLdb

import warnings

import sys 
reload(sys) 
sys.setdefaultencoding('utf8') 
warnings.filterwarnings("ignore")
def Parse_DnsFile(dnsfile,domainfile):
	try:
		DnsFile= open(dnsfile,'r')
	except:
		print 'DNS file not found'
		print 'The file can be generate from the file DNS-Sniffer/RunSniffer.py'
	Domain_Collect = open(domainfile,'w')		
	for line in DnsFile:
		line = line.strip('\n')
		#avoid top of the file and the space
		if len(line)<2:
			continue
		else:
			if 'IP Source              Dns Server ' in line :
				continue
		line = line.strip()
		line_parameter = line.split()
		domain = line_parameter[3]
		Domain_Collect.write(domain+'\n')
	DnsFile.close()
	Domain_Collect.close()
	return True

def request_domain(DomainFile,ResultFile):
	domain_file = open(DomainFile,'r')
	result_file = open(ResultFile,'w')
	result_file .write("Domain 		  				stamp 				      source 						 			update_time")
	db = MySQLdb.connect(user='root',db='TiDB',passwd='123456',host='192.168.9.12',charset='utf8')
	cursor = db.cursor()
	for domain in domain_file:
		domain = domain.strip('\n').strip()
		domain_option = "select * from domain_table where domain = '%s';"%domain
		cursor.execute(domain_option)
		raw_reply = cursor.fetchall()
		if raw_reply == ():
			continue
		reply = raw_reply[0]
		result = []
		for each in reply:
			result.append(each.encode('utf-8'))
		domain      = result[0]
		update_time = result[1]
		source      = result[2]
		stamp       = result[3]
		print '#**********************************************************************************#'
		print ''
		print 'warning :suspicous domain'
		print 'domain  :',domain
		print 'stamp   :',stamp
		print 'source  :',source
		print 'data update time :',update_time
		print ''
		print '#**********************************************************************************#'
		Result = "%s 		  				%s 				      %s 						 			%s"%(domain,stamp,source,update_time)
		result_file.write(Result)
	db.close()
	domain_file.close()
	result_file.close()
	return True
if __name__ == '__main__':
	s = "输入DNS_Sniffer生成的文件（当前路径下），如‘DNS.txt’"
	print s.decode('utf-8').encode('gbk')
	rawfile = raw_input(">")
	s =  '开始解析--------------->>>>>>>'
	print s.decode('utf-8').encode('gbk')
	if Parse_DnsFile(rawfile,'domain_file.txt'):
		request_domain('domain_file.txt','Result.txt')


