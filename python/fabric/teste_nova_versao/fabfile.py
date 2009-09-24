from fabric.api import *

env.roledefs = {
    'web': ['riovld48.globoi.com'],
    'filer': ['riovld48.globoi.com']
}

def dev():
#    env.hosts = ['riovld48.globoi.com']
    env.user = 'puppet'

def prod():
#    env.hosts = ['riovld48.globoi.com']
    env.user = 'puppet'

@roles('web')
def deploy():
    run('pwd')
    run('ls -l')
    sudo('pwd')
    sudo('ls')
