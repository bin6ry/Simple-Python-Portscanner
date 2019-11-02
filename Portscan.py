#!/usr/bin/env python
# Simple Portscanner
# Created By bin6ry
# Usage: python Portscan.py 
import socket
import subprocess
import sys
from datetime import datetime
 
subprocess.call('clear', shell=True)
 
remoteServer    = raw_input("\x1b[1;32mPlease Enter The Host You Wish To Scan:\x1b[1;37m ")
remoteServerIP  = socket.gethostbyname(remoteServer)

subprocess.call('clear', shell=True)
 
print "\x1b[1;32mPlease Wait, Scanning Remote Host:\x1b[1;37m", remoteServerIP
 
t1 = datetime.now()

try:
    for port in range(1,65535):  
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex((remoteServerIP, port))
        if result == 0:
            print "\x1b[1;35m[\x1b[1;36mOPEN-PORT\x1b[1;35m]:\x1b[1;37m {}".format(port)
        sock.close()
 
except KeyboardInterrupt:
    print "\x1b[1;32mScan Has Been Stopped"
    sys.exit()
 
except socket.gaierror:
    print '\x1b[1;32mHostname could not be resolved'
    sys.exit()
 
except socket.error:
    print "\x1b[1;32mCouldn't Connect To Server"
    sys.exit()
 
t2 = datetime.now()
 
total =  t2 - t1
 
print '\x1b[1;32mScan Completed In:\x1b[1;37m', total