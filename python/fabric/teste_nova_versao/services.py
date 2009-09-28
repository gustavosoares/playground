from fabric.api import *
import time

def stop_puppetmaster():
	'''####### stop puppet master'''
	sudo('%s stop' % env.apachectl_be)

def start_puppetmaster():
	'''####### start puppet master'''
	sudo('%s start' % env.apachectl_be)

def restart_puppetmaster():
	'''####### restart puppet master'''
	stop_puppetmaster()
	time.sleep(5)
	start_puppetmaster()

