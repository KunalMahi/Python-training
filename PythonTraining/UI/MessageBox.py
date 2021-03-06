from tkinter import *
from tkinter import ttk
from tkinter import messagebox
root=Tk()
root.title("Login")
root.resizable(False,False)
l1=ttk.Label(root,text="UserName")
et1=ttk.Entry(root,width=20)
l2=ttk.Label(root,text="Password")
et2=ttk.Entry(root,width=20)
BClk=ttk.Button(root,text="Login")
l1.grid(row=0,column=0)
et1.grid(row=0,column=1)
l2.grid(row=1,column=0)
et2.grid(row=1,column=1)
BClk.grid(row=2,column=1)
et2.config(show='*')

def Click():
    print("UserName:{} Password:{}".format(et1.get(),et2.get()))
    if(et1.get()=="Admin" and et2.get()=="1234"):
        messagebox.showinfo(title="Login info",message="Welcome to Python App")
    else:
        messagebox.showerror(title="Error",message="Invalid username and password")

BClk.config(command=Click)

root.mainloop()

