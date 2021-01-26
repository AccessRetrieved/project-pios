from tkinter import *
import tkmacosx # Helper for designing

# Template for creating custom apps to use with  Project-Pios
# import_app function is needed to initiate the app
# quit_app is needed to return to home screen

def import_app(window): # customize app here
    global NSAppView
    NSAppView = Frame(window) # Make sure to use NSAppView as main window, ex. root, or master
    NSAppView.pack(fill=BOTH, expand=True)
    
    # Define functions here



    
    # Add widgets and modules here
    Label(NSAppView, text='app 1').place(relx=0.5, rely=0.5, anchor=CENTER)


def quit_app():
    NSAppView.destroy()