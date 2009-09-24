from fabric.api import *

def config():
	env.application = "puppet"
	env.project = "gerencia-configuracao"
	env.usuario = "puppet"
	env.grupo = "puppet"
	env.deploy_be_dir = "/mnt/projetos/deploy-be/_geral"
	env.filer_dir = "%s/%s" % (env.deploy_be_dir, env.application)
	env.log_dir = "/opt/puppet/log/"
	env.htdocs_dir = "/opt/generic/httpd-worker/htdocs"
	env.conf_host_be = [ "puppet-local" ]
	env.apachectl_be = "/etc/init.d/httpd-worker_genericctl"

## STAGES ##
def dev():
	'''Seta configuracoes de dev'''
	config()
	env.roledefs = {
    	'web': ['riovld48.globoi.com'],
    	'filer': ['riovld48.globoi.com']
	}
	env.stage = 'dev'
	env.user = 'puppet'

def prod():
#    env.hosts = ['riovld48.globoi.com']
    env.user = 'puppet'
