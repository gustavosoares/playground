from fabric.api import *

def stop():
	'''stop'''
	local('echo \"stop %s\"' % env.apachectl_be)

