import platform
import os
#import win32api

s=platform.system()

if   cmp(s,"Windows")==0:
     #win32api.ShellExecute(0,'open','.\dns_sniffer.exe','','',1)
     os.system(".\\Windows\\DNS\\Release\\DNS.exe")
elif cmp(s,"Linux")==0:
     os.system(".//Linux//dns")
