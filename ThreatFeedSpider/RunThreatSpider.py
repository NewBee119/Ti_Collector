#date:2017-10-26

import os
path = os.getcwd()
path = path+'/scripts'
filelist = os.listdir(path)
filelist.remove('download.py')
try:
	filelist.remove('download.pyc')
except:
	pass
try:
	filelist.remove('feed_id.txt')
except:
	pass
try:
	filelist.remove('tmp.txt')
except:
	pass
for each_py in filelist:
	try:
		command = 'python scripts/%s'%each_py
		print command
		os.system(command)
	except:
		print 'error in script :',each_py
		print 'run another script'