#TODO: importar o modulo de forma diferente
import deploy_util
#from deploy_util import *
from fabric.api import *


def config():
	env.application = "puppet"
	env.project = "gerencia-configuracao"
	env.user = "puppet"
	env.grupo = "puppet"
	env.deploy_be_dir = "/mnt/projetos/deploy-be/_geral"
	env.filer_dir = "%s/%s" % (env.deploy_be_dir, env.application)
	env.log_dir = "/opt/puppet/log/"
	env.htdocs_dir = "/opt/generic/httpd-worker/htdocs"
	env.conf_host_be = [ 'puppet', 'httpd-worker-local' ]
	env.apachectl_be = "/etc/init.d/httpd-worker_genericctl"


@roles('web')
def setup_be():
	'''######### Setup master server'''
	#setup_filer()
	sudo("yum -y install git_globo")
	sudo("yum -y install augeas-libs")
	sudo("yum -y install ruby_globo")
	sudo("yum -y install rubygems_globo")
	sudo("yum -y install puppet_globo")
	if env.stage == 'staging':
		sudo("yum -y install simpledns_globo")
		
	print 'Criando docroot do apache'
	sudo("mkdir -p %s" % env.htdocs_dir)
	sudo("chown -R %s:%s  %s" % (env.user, env.grupo, env.htdocs_dir))
	sudo("chown -R %s:%s  /etc/puppet" % (env.user, env.grupo))


##TODO: CHECK
@roles('web')
def check_be():
	'''###### Backend environments checks'''
	deploy_util.rpm('git_globo')
	deploy_util.rpm('augeas-libs')
	deploy_util.rpm('ruby_globo')
	deploy_util.rpm('rubygems_globo')
	deploy_util.rpm('puppet_globo')
	if env.stage == 'staging':
		deploy_util.rpm("simpledns_globo")

	for host in env.conf_host_be:
		deploy_util.is_entry_at_host(host)

