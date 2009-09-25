from deploy_util import *
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


def prod():
#    env.hosts = ['riovld48.globoi.com']
	env.stage = 'prod'

    
## FIM STAGES ##

@roles('web')
def setup_master():
	'''Setup master server'''
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
	sudo("chown %s:%s  %s" % (env.user, env.grupo, env.htdocs_dir))


##TODO: CHECK
@roles('web')
def check_be():
	'''Environments checks'''
	rpm('git_globo')
	rpm('augeas-libs')
	rpm('ruby_globo')
	rpm('rubygems_globo')
	rpm('puppet_globo')
	if env.stage == 'staging':
		rpm("simpledns_globo")

@roles('web')
def check():
	check_be()
'''
  desc "########## Verifica o ambiente backend ##########"
  task :check_be, :roles => :master do
    default_run_options[:pty] = true # or else you'll get "sorry, you must have a tty to run sudo"
    Environment.define :be, self do

	  #TODO: colocar check para a entrada do hosts para o apache
      #conf_host_be.to_a.each{|conf_hostname| hosts_entry conf_hostname}
      #connects_to solr_host, "80"
      
    end
    Environment.verify :be
  end

  desc "########## Checagem de todos os ambientes ##########"
  task :check do
    check_be
  end
'''

