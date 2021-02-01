from tkinter import *
from App1.app import import_app, quit_app
from App2.app2 import import_app2, quit_app2

root = Tk()
root.geometry('400x800')

import_app2(root, 500)

def see():
    print('success!')

root.mainloop()