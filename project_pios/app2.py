from tkinter import *
import os
from PIL import Image, ImageTk
from datetime import *
import tkmacosx # Helper for designing

# Template for creating custom apps to use with  Project-Pios
# import_app function is needed to initiate the app
# quit_app is needed to return to home screen

def import_app2(window): # customize app here
    global NSApp2View
    NSApp2View = Frame(window) # Make sure to use NSApp2View as main window, ex. root, or master
    NSApp2View.pack(fill=BOTH, expand=True)
    
    # Define functions here
    def update():
        orig = str(datetime.now())
        fil = orig[11:19]
        time['text'] = fil

        NSApp2View.after(ms=1000, func=update)


    # Add widgets and modules here
    Label(NSApp2View, text='custom app 1').place(relx=0.5, rely=0.5, anchor=CENTER)

    time = Label(NSApp2View, text='', font=("Futura", 15))
    time.place(relx=0.5, rely=0.2, anchor=CENTER)
    update()


    # Launch screen
    img = Image.open(os.getcwd() + '/project_pios/apps/launch/1.png')
    pic = ImageTk.PhotoImage(img)

    def launch_app():
        NSLaunchScreen2.destroy()

    # Customize launch screen here
    NSLaunchScreen2 = Label(window, text='', image=pic)
    NSLaunchScreen2.image = pic
    NSLaunchScreen2.place(relx=0.5, rely=0.5, anchor=CENTER)

    NSApp2View.after(1500, launch_app)

def quit_app2(): # Quit app function
    NSApp2View.destroy()