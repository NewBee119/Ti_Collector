# encoding=utf8
#aurhor :LiMengming
#date:2017-10-26
#domain type

import MySQLdb
import sys
import time
import re
from urllib import urlopen

reload(sys) 
sys.setdefaultencoding('utf8')

def time_formation(time_str):
	#'2017-10-19 02:30:01 (UTC) 				#'
	date_pattern = re.compile(r'(\d+)-(\d+)-(\d+)')
	time_pattern = re.compile(r'(\d+):(\d+):(\d+)')
	date_result  = re.search(date_pattern,time_str)
	time_result  = re.search(time_pattern,time_str)
	time_orignal = date_result.group() + ' ' + time_result.group()
	timeArray = time.strptime(time_orignal, "%Y-%m-%d %H:%M:%S")
	timeStamp = int(time.mktime(timeArray))
	TIME = time.ctime(timeStamp).encode('utf-8')
	return TIME


def get_ip(string_ip):
	result = re.findall(r"\b(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\b", string_ip)
	if result:
		return result
	else:
		return 'None'




def download_domain(source,stamp,url):
	file = open('tmp.txt','w')
	#claw the web and download the web-file
	try:
		resp = urlopen(url)
		html_data = resp.read().decode('utf-8')
		file.write(html_data)
	except Exception,e:
		print 'ERROR :',e
		exit()
	file.close()
	#Parse the file and get eachline into the MySQL database
	update_time = time.ctime().encode( "utf-8")
	fo = open('tmp.txt','r')
	db = MySQLdb.connect(user='root',db='TiDB',passwd='123456',host='192.168.9.223',charset='utf8')
	cursor = db.cursor()
	for eachline in fo :
		#insert data into 'url_table' table
		if '#' in eachline:
			continue
		else:
			ipgroup = get_ip(eachline)
			if ipgroup !='None':
				for ip in ipgroup:
					if len(ip)<7:
						continue
					cursor.execute("REPLACE INTO ip_table(ip,update_time,source,stamp) VALUES('%s','%s','%s','%s')" % (ip,update_time,str(source),stamp))	
				continue
			try:
				eachline_parameter = eachline.split()[1]
				domain = eachline_parameter.strip('\n').strip()
				cursor.execute("REPLACE INTO domain_table(domain,update_time,source,stamp) VALUES('%s','%s','%s','%s')" % (domain,update_time,source,stamp))
			except:
				try:
					domain = eachline.strip()
					cursor.execute("REPLACE INTO domain_table(domain,update_time,source,stamp) VALUES('%s','%s','%s','%s')" % (domain,update_time,source,stamp))
				except:
					print 'error in :',eachline
	db.commit()
	db.close()
	fo.close()



def download_ip(source,stamp,url):
	file = open('tmp.txt','w')
	#claw the web and download the web-file
	try:
		resp = urlopen(url)
		html_data = resp.read().decode('utf-8')
		file.write(html_data)
	except Exception,e:
		print 'ERROR :',e
		exit()
	file.close()
	#Parse the file and get eachline into the MySQL database
	update_time = time.ctime().encode( "utf-8")
	fo = open('tmp.txt','r')
	db = MySQLdb.connect(user='root',db='TiDB',passwd='123456',host='192.168.9.223',charset='utf8')
	cursor = db.cursor()
	for eachline in fo :
		#insert data into 'url_table' table
		if '#' in eachline:
			if 'updated' in eachline:
				try:
					update_time = time_formation(eachline)
					print 'update_time',update_time
				except:
					print 'error in line :',eachline
					continue
		else:
			ipgroup = get_ip(eachline)
			for ip in ipgroup:
				if len(ip)<7:
					continue
				cursor.execute("REPLACE INTO ip_table(ip,update_time,source,stamp) VALUES('%s','%s','%s','%s')" % (ip,update_time,str(source),stamp))
	db.commit()
	db.close()
	fo.close()

def download_url(source,stamp,url):
	file = open('tmp.txt','w')
	#claw the web and download the web-file
	try:
		resp = urlopen(url)
		html_data = resp.read().decode('utf-8')
		file.write(html_data)
	except Exception,e:
		print 'ERROR :',e
		exit()
	file.close()
	#Parse the file and get eachline into the MySQL database
	update_time = time.ctime().encode( "utf-8")
	fo = open('tmp.txt','r')
	db = MySQLdb.connect(user='root',db='TiDB',passwd='123456',host='192.168.9.223',charset='utf8')
	cursor = db.cursor()
	for eachline in fo :
		eachline = eachline.strip('\n').strip()
		#insert data into 'url_table' table
		if '#' in eachline:
			if 'updated' in eachline:
				update_time = time_formation(eachline)
		else:
			url =eachline.replace("'", "\\\'")
			cursor.execute("REPLACE INTO url_table(url_index,url,update_time,source,stamp) VALUES('%s','%s','%s','%s','%s')" % (url[0:50],url,update_time,str(source),stamp))
	db.commit()
	db.close()
	fo.close()

def download_ip_2(source,stamp,url):
	file = open('tmp.txt','w')
	#claw the web and download the web-file
	try:
		resp = urlopen(url)
		html_data = resp.read().decode('utf-8')
		file.write(html_data)
	except Exception,e:
		print 'ERROR :',e
		exit()
	file.close()
	#Parse the file and get eachline into the MySQL database
	update_time = time.ctime().encode( "utf-8")
	fo = open('tmp.txt','r')
	db = MySQLdb.connect(user='root',db='TiDB',passwd='123456',host='192.168.9.223',charset='utf8')
	cursor = db.cursor()
	for eachline in fo :
		ipgroup = get_ip(eachline)
		if ipgroup == 'None':
			continue
		else:
			try:
				update_time = time_formation(eachline)
			except:
				pass
			for ip in ipgroup:
				if len(ip)<7:
					continue
				cursor.execute("REPLACE INTO ip_table(ip,update_time,source,stamp) VALUES('%s','%s','%s','%s')" % (ip,update_time,str(source),stamp))
	db.commit()
	db.close()
	fo.close()
