# encoding=utf8
#date:2017-10-24
#function : request the data using domain

import MySQLdb

import warnings
warnings.filterwarnings("ignore")


def Parse_DnsFile(dnsfile,domainfile):
	DnsFile= open(dnsfile,'r')
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

def request_domain(Domain_File):
	domain_file = open(Domain_File,'r')
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
	db.close()
	domain_file.close()
	return True
if __name__ == '__main__':
	if Parse_DnsFile('dns_sample.txt','domain_file.txt'):
		request_domain('domain_file.txt')


