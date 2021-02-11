from subprocess import call, Popen
from getpass import getuser
import os
from tkinter.messagebox import *

def download_ocr():
    if os.path.exists(os.getcwd() + '/system/Library/Helpers') == True:
        call('git clone https://github.com/AccessRetrieved/OCR', cwd=os.getcwd() + '/system/Library/Helpers', shell=True)
        if os.path.exists(os.getcwd() + '/system/Library/Helpers/OCR') == True:
            ask = askyesno(message='成功，运行?')
            if ask == True:
                Popen('%s' % os.getcwd() + '/system/Library/Helpers/OCR/ocr.py', shell=True)
            else:
                pass
        else:
            showerror(message='下载出错，请稍后重试')
    else:
        os.mkdir(os.getcwd() + '/system/Library/Helpers')
        call('git clone https://github.com/AccessRetrieved/OCR', cwd=os.getcwd() + '/system/Library/Helpers', shell=True)
        if os.path.exists(os.getcwd() + '/system/Library/Helpers/OCR') == True:
            ask = askyesno(message='成功，运行?')
            if ask == True:
                Popen('%s' % os.getcwd() + '/system/Library/Helpers/OCR/ocr.py', shell=True)
            else:
                pass
        else:
            showerror(message='下载出错，请稍后重试')

def download_qrcode():
    if os.path.exists(os.getcwd() + '/system/Library/Helpers') == True:
        call('git clone https://github.com/AccessRetrieved/Qr-Code-Scanner', cwd=os.getcwd() + '/system/Library/Helpers', shell=True)
        if os.path.exists(os.getcwd() + '/system/Library/Helpers/Qr-Code-Scanner') == True:
            ask = askyesno(message='成功， 运行？')
            if ask == True:
                Popen('python3 %s' % os.getcwd() + '/system/Library/Helpers/Qr-Code-Scanner/qr.py', shell=True)
            else:
                pass
        else:
            showerror(message='下载出错，请稍后重试')
    else:
        os.mkdir(os.getcwd() + '/system/Library/Helpers')
        call('git clone https://github.com/AccessRetrieved/Qr-Code-Scanner', cwd=os.getcwd() + '/system/Library/Helpers', shell=True)
        if os.path.exists(os.getcwd() + '/system/Library/Helpers/Qr-Code-Scanner') == True:
            ask = askyesno(message='成功， 运行？')
            if ask == True:
                Popen('python3 %s' % os.getcwd() + '/system/Library/Helpers/Qr-Code-Scanner/qr.py', shell=True)
            else:
                pass
        else:
            showerror(message='下载出错，请稍后重试')