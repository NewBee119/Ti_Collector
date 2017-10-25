#coding:utf-8
#'https://badcyber.com'
import urllib2
import Queue
import re
from bs4 import BeautifulSoup
import threading
import time
import json

ret =list()
thnum = 0
page = '' #存放被打开的网页
DownList = Queue.Queue()
queueLocker = threading.Lock()

def GetThePage(url,name,time,fm):
	headers = {'User-Agent' : 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'}
	request = urllib2.Request(url, None, headers)
	try:
		response = urllib2.urlopen(request,timeout=20)
	except urllib2.HTTPError as e:
		pass
	except urllib2.URLError as e:
		print e.reason
		pass
	else:
		global page
		page = response.read()
		FILE = open("%s.%s"%(name,fm),'wb+')
		FILE.write(page)


def DisposePage(PageName):
	pattern = re.compile('2017\/$')
	count = 0
	soup = BeautifulSoup(open(PageName),'lxml')
	for link in soup.find_all('a'):
		downurl = link.get('href')
		goal = pattern.search(downurl)
		if goal:
			name = '%s'%count
			count += 1
			time = '0'
			doc = {'name':name,'downurl':downurl,'time':time}
			DownList.put(doc)
		else:
			pass

def DisposePage1(PageName):
	soup = BeautifulSoup(open(PageName),'lxml')
	for link in soup.find_all('ol'):
		for child in link.descendants:
			a = child.find('a')
			try:
				url = a.get('href')
			except:
				pass
			else:
				name = child.string
				doc1 = {'name':name,'url':url}
				ret.append(doc1)

class DownFile(threading.Thread):
	"""docstring for DownFile"""
	def __init__(self):
		threading.Thread.__init__(self)
		self.queue = DownList
	def run(self):
		global thnum
		while True:
			if not self.queue.empty():
				queueLocker.acquire()
				DownDoc = DownList.get()
				queueLocker.release()
				try:
					GetThePage(DownDoc['downurl'],DownDoc['name'],DownDoc['time'],'html')
				except:
					thnum -= 1
					print thnum
					print 'timeout'
					break
			else:
				thnum -= 1
				print thnum
				break

if __name__ == '__main__':
	global page
	global thnum
	global ret
	GetThePage('https://badcyber.com','basepage','20171011','html')
	DisposePage('basepage.html')
	
	for i in xrange(0,10):
		t = DownFile()
		thnum += 1
		try:
			t.start()
			print 'start'
		except:
			pass
	while True:
		time.sleep(5)
		if thnum == 0:
			break

	for x in xrange(0,50):
		pagename = '%s.html'%x
		try:
			DisposePage1(pagename)
		except:
			pass

	nub = 0
	while nub < len(ret):
		nub2 = nub + 1
		if nub2 == len(ret):
			break
		while nub2 < len(ret)-1:
			if cmp(ret[nub],ret[nub2])==0:
				del ret[nub2]
			else:
				nub2 += 1
		nub += 1
	RET = json.dumps(ret)
	File = open('ret.json','w')
	File.write(RET)
	File.close
