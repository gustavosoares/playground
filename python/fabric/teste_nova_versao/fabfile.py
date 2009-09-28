from fabric.api import *
from stages import *
#from services import *
#from setup import *
import services
import setup
import datetime
import time

env.timestamp = datetime.datetime.now().strftime('%d_%m_%Y_%H_%M_%S')
env.release_sufix = 'releases/' + env.timestamp 

 
@roles('web')
def deploy_be():
	'''###### Deploy para o ambiente escolhido com o comando fab [AMB] deploy'''
	#update_be()
	setup.check_be()
	#criaco e upload
	print local('pwd && ls -l')
	print local('cd ..;tar --exclude=.git/* --exclude=.git* --exclude=*.unfiltered --exclude=*.rb --exclude=Capfile --exclude=deploy/* --exclude=deploy* -cvzf /tmp/package-%s.tar.gz .' % env.application)
	env.deploy_release_dir = env.filer_dir + '/' + env.release_sufix + '/' + env.application
	print run('umask 002 && mkdir -p %s' % env.deploy_release_dir)
	print put('/tmp/package-%s.tar.gz' % env.application,'%s/package-%s.tar.gz' % (env.deploy_release_dir, env.application))
	
	#abrinco pacotes e criando links de current de cada um
	cmd = '''
		cd %s && umask 002 && 
		tar -xzf %s/package-%s.tar.gz && 
		rm -f %s/package-%s.tar.gz
	''' % (env.deploy_release_dir, env.deploy_release_dir, env.application, env.deploy_release_dir, env.application)
	run(cmd)

	cmd = '''
		rm -f %s/current && 
		umask 002 && 
		ln -s %s %s/current
	''' % (env.filer_dir, env.deploy_release_dir, env.filer_dir)
	run(cmd)
	local("rm /tmp/package-%s.tar.gz" % env.application)
	
	#copia para a pasta /etc/puppet conteudo da pasta current
	print 'parando o puppet master'
	services.stop_puppetmaster()
	time.sleep(5)
	run('rm -rf /etc/puppet/*')
	run('cp -rp %s/* /etc/puppet/' % env.deploy_release_dir)
	print 'arquivos atualizados'
	print run('ls -ltr /etc/puppet/')
	print 'iniciando o puppet master'
	services.start_puppetmaster()

@roles('web')
def releases():
	'''#### Lista os releases disponiveis no servidor'''
	run("ls -lad %s/current | awk -F 'releases/' '{print $2}' > /tmp/release.current; for x in `ls -r %s/releases`; do if [ \"$x\" == \"`cat /tmp/release.current`\" ]; then echo \"$x <- current\"; else echo $x; fi; done; rm /tmp/release.current" % (env.filer_dir, env.filer_dir))
	
def help():
	print ''
	print '#' * 60
	print ''
	print '#### Deploy para o backend'
	print '\tfab dev deploy_be'
	print '#### Setup no backend'
	print '\tfab dev setup_be'	
