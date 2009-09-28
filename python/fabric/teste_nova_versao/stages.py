from fabric.api import *
import setup

setup.config()

## STAGES ##
def dev():
	'''Seta configuracoes de dev'''
	#config()
	env.stage = 'dev'
	env.roledefs = {
    	'web': ['riovld48.globoi.com'],
    	'filer': ['riovld48.globoi.com']
	}

def prod():
#    env.hosts = ['riovld48.globoi.com']
	env.stage = 'prod'

    
## FIM STAGES ##
