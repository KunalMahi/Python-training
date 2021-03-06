from tkinter import *
from tkinter import ttk

root=Tk()

def key_pressed(event):
    print("Event type:{}".format(event.type))

Bu=ttk.Button(root,text="Click me")
Bu.pack()
root.bind("<ButtonPress>",key_pressed)
root.bind("<Control-c>",key_pressed)
root.mainloop()