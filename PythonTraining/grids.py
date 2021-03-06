from tkinter import *
from tkinter import ttk
root=Tk()
style=ttk.Style()
style.theme_use('classic')
l1=ttk.Label(root,text='Green',background='Green').grid(row=0,column=0,padx=5,pady=5,sticky='snew')
l2=ttk.Label(root,text='Red',background='Red').grid(row=0,column=1,ipadx=5,ipady=5,sticky='snew')
l3=ttk.Label(root,text='Yellow',background='Yellow').grid(row=0,column=2,rowspan=2,sticky='snew')
l4=ttk.Label(root,text='Blue',background='Blue').grid(row=1,column=0,columnspan=2,sticky='snew')
root.rowconfigure(0,weight=2)
root.rowconfigure(1,weight=1)
root.columnconfigure(1,weight=1)
root.columnconfigure(2,weight=2)
root.mainloop()