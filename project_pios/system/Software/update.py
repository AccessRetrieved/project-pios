from subprocess import call, Popen
from getpass import getuser
from tkinter import *
from tkinter import ttk
import tkmacosx
import zipfile
import threading
import requests
import os

def update():
    update_win = Tk()
    update_win.geometry('500x400')
    update_win.title('Project-Pios 更新小助手')

    max = IntVar()
    current_chunk = StringVar()
    current_chunk.set("Current chunk: 0")

    url = 'https://github.com/AccessRetrieved/Project-Pios/archive/main.zip'
    file_name = "/Users/jerryhu/Desktop/Project-Pios.zip"

    def start():
        with open(file_name, 'wb') as f:
            response = requests.get(url, stream=True)
            total_length = response.headers.get('content-length')

            if total_length is None:
                f.write(response.content)
            else:
                global dl
                dl = 0
                total_length = int(total_length)
                max.set(int(total_length))
                pbar['maximum'] = max.get()
                for data in response.iter_content(chunk_size=1000):
                    dl += len(data)
                    current_chunk.set('Current chunk: {}'.format(str(dl)))
                    pbar['value'] = dl
                    f.write(data)
                    done = int(50 * dl / total_length)

    def start_download(event):
        global submit, dl

        update_win.attributes('-topmost', True)
        update_win.attributes('-alpha', 0.8)
        update_win.attributes('-fullscreen', True)

        pbar['value'] = 0
        start_btn.place_forget()
        alert.place(relx=0.5, rely=0.8, anchor=CENTER)
        submit = threading.Thread(target=start)
        submit.daemon = True
        submit.start()
        update_win.after(1, check)

    def check():
        if submit.is_alive():
            update_win.after(1, check)
        else:
            print(max.get())
            pbar['value'] = max.get()
            with zipfile.ZipFile('/Users/{}/Desktop/Project-Pios.zip'.format(getuser()), 'r') as zip_ref:
                zip_ref.extractall('/Users/{}/Desktop'.format(getuser()))
                os.rename('/Users/{}/Desktop/Project-Pios-main'.format(getuser()), '/Users/{}/Desktop/Project-Pios'.format(getuser()))

                update_win.attributes('-topmost', False)
                update_win.attributes('-alpha', 1)
                update_win.attributes('-fullscreen', False)
                update_win.geometry('500x400')

                try:
                    call('pip3 install -r r.txt', cwd='/Users/{}/Desktop/Project-Pios'.format(getuser()), shell=True)
                    Popen('python3 main.py', cwd='/Users/{}/Desktop/Project-Pios/project_pios'.format(getuser()), shell=True)

                    os.remove('/Users/{}/Desktop/Project-Pios.zip'.format(getuser()))
                except:
                    call('pip install -r r.txt', cwd='/Users/{}/Desktop/Project-Pios'.format(getuser()), shell=True)
                    Popen('python3 main.py', cwd='/Users/{}/Desktop/Project-Pios/project_pios'.format(getuser()), shell=True)
                    
                    os.remove('/Users/{}/Desktop/Project-Pios.zip'.format(getuser()))

    pbar = ttk.Progressbar(update_win, mode="determinate")
    pbar.place(relx=0.5, rely=0.5, anchor=CENTER, relwidth=0.8)

    display_chunks = Label(update_win, textvariable=current_chunk)
    display_chunks.place(relx=0.5, rely=0.45, anchor=CENTER)

    remaining_time = Label(update_win, text='Less than one minute, 小于一分钟', font=("Arial", 17))
    remaining_time.place(relx=0.5, rely=0.2, anchor=CENTER)

    start_btn = tkmacosx.Button(update_win, text='Start Update/开始更新', command=lambda: start_download(None), borderless=1)
    start_btn.place(relx=0.5, rely=0.8, anchor=CENTER)

    alert = Label(update_win, text='Please don\'t exit out/请不要退出程序')
    alert.place(relx=0.5, rely=0.87, anchor=CENTER)

    update_win.mainloop()