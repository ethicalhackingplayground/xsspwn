#!/usr/bin/python
import os

def install():
	print("Installing the required modules..\n")
	os.system('pip install -r requirements.txt')
	os.system("apt-get install tor")
	os.system("apt-get install privoxy")
	if (os.path.exists('reports') == False):	
		print("Setting up some folders..\n")
		os.system('mkdir reports')

	print ("Done..")
install()
