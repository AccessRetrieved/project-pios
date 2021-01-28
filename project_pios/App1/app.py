from tkinter import *
import os
from PIL import Image, ImageTk
import tkmacosx # Helper for designing

# Template for creating custom apps to use with  Project-Pios
# import_app function is needed to initiate the app
# quit_app is needed to return to home screen

def import_app(window, launch_screen_time=1000): # customize app here
    '''
    Param launch_screen_time is time for launch screen in milliseconds.
    '''
    global NSAppView
    NSAppView = Frame(window) # Make sure to use NSAppView as main window, ex. root, or master
    NSAppView.pack(fill=BOTH, expand=True)
    
    # Define functions here
    global a, b, c
    a = 0
    b = 0
    c = 0
    
    def start():
        global a, b, c
        NSStart.config(state = DISABLED)
        NSStart['bg'] = 'white'
        NSStop.config(state = NORMAL)
        NSStop['text'] = 'Stop'
        NSStop['bg'] = 'red'
        NSStop.config(command=stop)

        c += 1
        NSDisplayTime['text'] = '{}:{}:{}'.format(a, b, c)
        if c == 60:
            c = 0
            b += 1
            NSDisplayTime['text'] = '{}:{}:{}'.format(a, b, c)
        elif b == 60:
            b = 0
            a += 1
            NSDisplayTime['text'] = '{}:{}:{}'.format(a, b, c)

        global count
        count = NSAppView.after(ms=1000, func=start)

    def stop():
        NSStart.config(state = NORMAL)
        NSStart['bg'] = 'green'
        NSStop['text'] = 'Reset'
        NSStop['bg'] = 'white'

        global count
        NSAppView.after_cancel(count)
        NSStop.config(command=reset)

    def reset():
        global a, b, c
        a = 0
        b = 0
        c = 0
        NSDisplayTime['text'] = '0:0:0'
        
        NSStart.config(state = NORMAL)
        NSStop.config(state = DISABLED)
        NSStop.config(command=stop)

    # Add widgets and modules here
    NSDisplayTime = Label(NSAppView, text='0:0:0', font=("Futura", 40))
    NSDisplayTime.place(relx=0.5, rely=0.3, anchor=CENTER)

    NSStart = tkmacosx.CircleButton(NSAppView, text='Start', bg='green', activebackground='white', activeforeground='green', borderless=1, command=start)
    NSStart.place(relx=0.7, rely=0.5, anchor=CENTER)

    NSStop = tkmacosx.CircleButton(NSAppView, text='Stop', bg='white', activebackground='white', activeforeground='red', borderless=1, state = DISABLED, command=stop)
    NSStop.place(relx=0.3, rely=0.5, anchor=CENTER)

    # Customize launch screen here
    img = Image.open(os.getcwd() + '/project_pios/App1/launch/launch.png')
    pic = ImageTk.PhotoImage(img)

    def launch_app():
        NSLaunchScreen.destroy()
    NSLaunchScreen = Label(window, text='', image=pic)
    NSLaunchScreen.image = pic
    NSLaunchScreen.place(relx=0.5, rely=0.5, anchor=CENTER)

    NSAppView.after(launch_screen_time, launch_app)

def quit_app(): # Quit app function
    NSAppView.destroy()