from fabric.api import *
from services import *
from setup import *
import datetime

env.timestamp = datetime.datetime.now().strftime('%d_%m_%Y_%H_%M_%S')
env.release_sufix = 'releases/' + env.timestamp 

print env.timestamp

def default():
	update()

@roles('web')
def update_be():
	check()
	#criaco e upload
	local('pwd && ls -l')
	local('tar --exclude=*.unfiltered --exclude=*.rb --exclude=Capfile --exclude=deploy/* -czf /tmp/package-%s.tar.gz .' % env.application)
	env.deploy_release_dir = env.filer_dir + '/' + env.release_sufix + '/' + env.application
	run('umask 002 && mkdir -p %s' % env.deploy_release_dir)
	put('/tmp/package-%s.tar.gz' % env.application,'%s/package-%s.tar.gz' % (env.deploy_release_dir, env.application))
'''
    
    # Abrindo pacotes e criando links de current de cada um
    run "cd #{deploy_release_dir} && umask 002 && tar -xzf #{deploy_release_dir}/package-#{application}.tar.gz && rm -f #{deploy_release_dir}/package-#{application}.tar.gz"
    run "rm -f #{filer_dir}/current && umask 002 && ln -s #{deploy_release_dir} #{filer_dir}/current"

	# Copia para a pasta /etc/puppet conteudo da pasta current
	
    system "rm #{temp_dir}/package-#{application}.tar.gz"
    #system "rm #{temp_dir}/package-conf.tar.gz"
'''

    
@roles('web')
def deploy():
	'''Deploy para o ambiente escolhido com o comando fab [AMB] deploy'''
	update_be()
    
def teste():
	'''Teste'''
	print env.application
	stop()
	
	

