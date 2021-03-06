from tkinter import *
from tkinter import ttk

root=Tk()
style=ttk.Style()
style.configure('TButton',bbackground='blue',foreground='red',font=('arial',18))
entry=ttk.Entry(root,width=100)
entry.pack()
button=ttk.Button(root,text="click me")
button.pack()
logo=PhotoImage(file="login-gif-images-12.gif")
button.config(image=logo,compound=LEFT)
ResizeLogo=logo.subsample(10,10)
button.config(image=ResizeLogo)
def BCLk():
    print(entry.get())
    entry.delete(0,END)
    entry.insert(0,"NNNNNNNNNNNNYYYYYYYYYYYYYYYYYYYCCCCCCCCCCCCCCEEEEEEEEEEEEEEEEEEEEE")

button.config(command=BCLk)


root.mainloop()