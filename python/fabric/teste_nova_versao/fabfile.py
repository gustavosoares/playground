from fabric.api import *
from services import *
from setup import *



## FIM STAGES ##

@roles('web')
def deploy():
	'''Deploy para o ambiente escolhido com o comando fab [AMB] deploy'''
	sudo('pwd')
	sudo('ls')
    
def teste():
	'''Teste'''
	print env.application
	stop()
