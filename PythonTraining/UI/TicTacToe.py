from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from random import randint
ActivePlayer=1
p1=[]
p2=[]
root=Tk()
root.title("TicTacToe:Player1")
b1=ttk.Button(root,text='')
b1.grid(row=0,column=0,sticky='snew',ipadx=40,ipady=40)
b1.config(command=lambda :ButtonClk(1))

b2=ttk.Button(root,text='')
b2.grid(row=0,column=1,sticky='snew',ipadx=40,ipady=40)
b2.config(command=lambda :ButtonClk(2))

b3=ttk.Button(root,text='')
b3.grid(row=0,column=2,sticky='snew',ipadx=40,ipady=40)
b3.config(command=lambda :ButtonClk(3))

b4=ttk.Button(root,text='')
b4.grid(row=1,column=0,sticky='snew',ipadx=40,ipady=40)
b4.config(command=lambda :ButtonClk(4))

b5=ttk.Button(root,text='')
b5.grid(row=1,column=1,sticky='snew',ipadx=40,ipady=40)
b5.config(command=lambda :ButtonClk(5))

b6=ttk.Button(root,text='')
b6.grid(row=1,column=2,sticky='snew',ipadx=40,ipady=40)
b6.config(command=lambda :ButtonClk(6))

b7=ttk.Button(root,text='')
b7.grid(row=2,column=0,sticky='snew',ipadx=40,ipady=40)
b7.config(command=lambda :ButtonClk(7))

b8=ttk.Button(root,text='')
b8.grid(row=2,column=1,sticky='snew',ipadx=40,ipady=40)
b8.config(command=lambda :ButtonClk(8))

b9=ttk.Button(root,text='')
b9.grid(row=2,column=2,sticky='snew',ipadx=40,ipady=40)
b9.config(command=lambda :ButtonClk(9))

def ButtonClk(ID):
    global ActivePlayer
    global p1
    global p2
    if(ActivePlayer==1):
        root.title("TicTacToe:Player2")
        SetLayout(ID,"X")
        p1.append(ID)
        print("P1:{}".format(p1))
        ActivePlayer = 2
        AutoPlay()
    elif(ActivePlayer==2):
        ActivePlayer = 1
        root.title("TicTacToe:Player1")
        SetLayout(ID, "0")
        p2.append(ID)
        print("P2:{}".format(p2))
    CheckWin()


def SetLayout(ID,Sym):
    if(ID==1):
        b1.config(text=Sym)
        b1.state(['disabled'])
    elif(ID==2):
        b2.config(text=Sym)
        b2.state(['disabled'])
    elif(ID==3):
        b3.config(text=Sym)
        b3.state(['disabled'])
    elif(ID==4):
        b4.config(text=Sym)
        b4.state(['disabled'])
    elif(ID==4):
        b4.config(text=Sym)
        b4.state(['disabled'])
    elif(ID==5):
        b5.config(text=Sym)
        b5.state(['disabled'])
    elif(ID==6):
        b6.config(text=Sym)
        b6.state(['disabled'])
    elif(ID==7):
        b7.config(text=Sym)
        b7.state(['disabled'])
    elif(ID==8):
        b8.config(text=Sym)
        b8.state(['disabled'])
    elif(ID==9):
        b9.config(text=Sym)
        b9.state(['disabled'])
def CheckWin():
    Win=-1
    if((1 in p1) and (2 in p1) and (3 in p1)):
        Win=1
    if((1 in p2) and (2 in p2) and (3 in p2)):
        Win = 2
    if ((4 in p1) and (5 in p1) and (6 in p1)):
        Win = 1
    if ((4 in p2) and (5 in p2) and (6 in p2)):
        Win = 2
    if ((7 in p1) and (8 in p1) and (9 in p1)):
        Win = 1
    if ((7 in p2) and (8 in p2) and (9 in p2)):
        Win = 2
    if ((1 in p1) and (4 in p1) and (7 in p1)):
        Win = 1
    if ((7 in p2) and (4 in p2) and (1 in p2)):
        Win = 2
    if ((2 in p1) and (5 in p1) and (8 in p1)):
        Win = 1
    if ((2 in p2) and (8 in p2) and (5 in p2)):
        Win = 2
    if ((3 in p1) and (6 in p1) and (9 in p1)):
        Win = 1
    if ((3 in p2) and (6 in p2) and (9 in p2)):
        Win = 2
    if(Win==1):
        messagebox.showinfo(title="Congrats",message="Player 1 is winner")
    if (Win == 2):
        messagebox.showinfo(title="Congrats", message="Player 2 is winner")
def AutoPlay():
    global p1
    global p2
    EmptyCells=[]
    for cell in range(9):
        if(not((cell+1 in p1) or(cell+1 in p2))):
            EmptyCells.append(cell+1)
    RandIndex=randint(0,len(EmptyCells)-1)
    ButtonClk(EmptyCells[RandIndex])





root.mainloop()