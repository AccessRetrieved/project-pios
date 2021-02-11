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


    # Add widgets and modules here
    Label(NSAppView, text='Chat App is on the way', font=("Arial", 20)).place(relx=0.5, rely=0.4, anchor=CENTER)


    # Customize launch screen here
    img = Image.open(os.getcwd() + '/App1/launch/launch.png')
    pic = ImageTk.PhotoImage(img)

    def launch_app():
        NSLaunchScreen.destroy()
    NSLaunchScreen = Label(window, text='', image=pic)
    NSLaunchScreen.image = pic
    NSLaunchScreen.place(relx=0.5, rely=0.5, anchor=CENTER)

    NSAppView.after(launch_screen_time, launch_app)

def quit_app(): # Quit app function
    NSAppView.destroy()