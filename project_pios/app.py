from tkinter import *
from tkinter import messagebox
import tkmacosx

# Template for creating custom apps for Project-Pios
# import_app function is needed to initiate the app
# quit_app is needed to return to home screen

def import_app(window): # You can customize your app here
    global NSAppView
    NSAppView = Frame(window) # Make sure to use NSAppView as window
    NSAppView.pack(fill=BOTH, expand=True)

    
    
    # Define functions here
    def show_alert():
        messagebox.showinfo(message='Custom App executed successfully.')
    
    
    
    # Add widgets and modules here
    tkmacosx.Button(NSAppView, text='Click here', bg='black', fg='white', activebackground='white', activeforeground='black', borderless=1, command=show_alert).place(relx=0.5, rely=0.5, anchor=CENTER)


def quit_app():
    NSAppView.destroy()