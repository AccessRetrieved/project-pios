from tkinter import *
from App1.app import import_app, quit_app
from App2.app2 import import_app2, quit_app2

root = Tk()
root.geometry('400x800')
root.title('Project-Pios Simulator')

import_app(root, 500)

root.mainloop()
