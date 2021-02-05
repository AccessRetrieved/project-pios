from subprocess import call, Popen
from getpass import getuser

def update():
    call('git clone https://github.com/AccessRetrieved/Project-Pios', cwd='/Users/{}/Desktop'.format(getuser()), shell=True)
    try:
        call('pip3 install -r r.txt', cwd='/Users/{}/Desktop/Project-Pios'.format(getuser()), shell=True)
        Popen('python3 main.py', cwd='/Users/{}/Desktop/Project-Pios/project_pios'.format(getuser()), shell=True)
    except:
        call('pip install -r r.txt', cwd='/Users/{}/Desktop/Project-Pios'.format(getuser()), shell=True)
        Popen('python3 main.py', cwd='/Users/{}/Desktop/Project-Pios/project_pios'.format(getuser()), shell=True)