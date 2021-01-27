from tkinter import *
from app import import_app, quit_app
from app2 import import_app2, quit_app2

root = Tk()
root.geometry('400x800')

import_app2(root)

root.mainloop()