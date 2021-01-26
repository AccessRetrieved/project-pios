from tkinter import *
import subprocess
import tkmacosx # Helper for designing

# Template for creating custom apps to use with  Project-Pios
# import_app function is needed to initiate the app
# quit_app is needed to return to home screen

def import_app2(window): # customize app here
    global NSApp2View
    NSApp2View = Frame(window) # Make sure to use NSAppView as main window, ex. root, or master
    NSApp2View.pack(fill=BOTH, expand=True)
    
    # Define functions here
    def we():
        subprocess.call(['open', '/Applications/WeChat.app'])

    def su():
        subprocess.call(['open', '/Applications/WeChat.app/Contents/MacOS/WeChat'])


    
    # Add widgets and modules here
    Label(NSApp2View, text='Testing', font=("Futura", 25)).place(relx=0.5, rely=0.1, anchor=CENTER)

    wechat = tkmacosx.Button(NSApp2View, text='WeChat', borderless=1, activebackground='black', activeforeground='white', command=we)
    wechat.place(relx=0.5, rely=0.2, anchor=CENTER)

    subwechat = tkmacosx.Button(NSApp2View, text='Sub-WeChat', borderless=1, activebackground='black', activeforeground='white', command=su)
    subwechat.place(relx=0.5, rely=0.3, anchor=CENTER)


def quit_app2():
    NSApp2View.destroy()