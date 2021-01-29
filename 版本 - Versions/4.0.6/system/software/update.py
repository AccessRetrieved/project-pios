from subprocess import call
from getpass import getuser

def update():
    call('git clone https://github.com/AccessRetrieved/Project-Pios', cwd='/Users/{}/Desktop'.format(getuser()), shell=True)
    try:
        call('pip3 install -r r.txt', cwd='/Users/{}/Desktop/Project-Pios'.format(getuser()), shell=True)
        pass
    except:
        call('pip install -r r.txt', cwd='/Users/{}/Desktop/Project-Pios'.format(getuser()), shell=True)
        pass