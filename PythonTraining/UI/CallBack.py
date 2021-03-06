from tkinter import *
from tkinter import ttk
root=Tk()
def BClk(ID):
    print("ID={}".format(ID))

ttk.Button(root,text="Click Button",command=lambda :BClk(10)).pack()

root.mainloop()