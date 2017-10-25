import os
path = os.getcwd()
filelist = os.listdir(path)
filelist.remove('run.py')
filelist.remove('download.py')
filelist.remove('TiDB.sql')
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
	command = 'python %s'%each_py
	print command
	os.system(command)


print filelist