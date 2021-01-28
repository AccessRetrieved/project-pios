from subprocess import call
from getpass import getuser

def update():
    call('git clone https://github.com/AccessRetrieved/Project-Pios', cwd='/Users/{}/Desktop'.format(getuser()), shell=True)