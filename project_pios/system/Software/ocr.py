from subprocess import call
from getpass import getuser
import os

def download_ocr():
    if os.path.exists(os.getcwd() + '/project_pios/system/Library/Helpers') == True:
        call('git clone https://github.com/AccessRetrieved/OCR', cwd=os.getcwd() + '/project_pios/system/Library/Helpers', shell=True)
    else:
        os.mkdir(os.getcwd() + '/project_pios/system/Library/Helpers')
        call('git clone https://github.com/AccessRetrieved/OCR', cwd=os.getcwd() + '/project_pios/system/Library/Helpers', shell=True)