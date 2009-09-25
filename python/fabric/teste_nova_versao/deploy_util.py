from fabric.api import *

def rpm(name):
	'''testa se um rpm existe'''
	run("/opt/local/bin/testa_rpm.sh %s" % name)
