import platform
import os
#import win32api

s=platform.system()

if   cmp(s,"Windows")==0:
     #win32api.ShellExecute(0,'open','.\dns_sniffer.exe','','',1)
     os.system("dns_sniffer.exe")
elif cmp(s,"Linux")==0:
     os.system("./dns")
