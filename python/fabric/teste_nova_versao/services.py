from fabric.api import *

@roles('web')
def stop():
	'''####### stop'''
	local('echo \"stop %s\"' % env.apachectl_be)

