from cProfile import label
from ssl import SSLErrorNumber
from tkinter import *
from ast import Lambda
from tokenize import Floatnumber
from turtle import right
from numpy import insert
from tkinter import messagebox

root = Tk()
root.title('Calculator')
root.iconbitmap('icon.ico')
root.wm_resizable(width=0, height=0)

e = Entry(root, width=40, borderwidth=2,justify='right')
e.grid(row=0, column=0, columnspan=5, padx=10, pady=10)

# Functions


def button_click(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current)+str(number))
    return


def button_clear():
    e.delete(0, END)


def click_add():
    if e.get()== "":
        messagebox.askokcancel("Error","Enter a number to perform addition")
    else:
        fn = e.get()
        global fnum, math
        math = 'add'
        fnum = int(fn)
        e.delete(0, END)


def click_sub():
    if e.get()== "":
        messagebox.askokcancel("Error","Enter a number to perform substraction")
    else:
        fn = e.get()
        global fnum, math
        math = 'sub'
        fnum = int(fn)
        e.delete(0, END)


def click_mult():
    if e.get()== "":
        messagebox.askokcancel("Error","Enter a number to perform multiplication")
    else:
        fn = e.get()
        global fnum, math
        math = 'mult'
        fnum = int(fn)
        e.delete(0, END)


def click_div():
    if e.get()== "":
        messagebox.askokcancel("Error","Enter a number to perform division")
    else:
        fn = e.get()
        global fnum, math
        math = 'div'
        fnum = int(fn)
        e.delete(0, END)


def click_equal():
    if e.get()== "":
      messagebox.askokcancel("Error","Peform mathematics first") 
    else:
        sn = e.get()
        e.delete(0, END)
        if (math == 'add'):
            e.insert(0, fnum+int(sn))
        elif(math == 'sub'):
            e.insert(0, fnum-int(sn))
        elif(math == 'mult'):
            e.insert(0, fnum*int(sn))
        elif(math == 'div'):
            e.insert(0, fnum/int(sn))


# Creating Buttons

button1 = Button(root, text='1',bg='white', padx=30, pady=10,
                 command=lambda: button_click(1))
button2 = Button(root, text='2',bg='silver', padx=30, pady=10,
                 command=lambda: button_click(2))
button3 = Button(root, text='3',bg='white', padx=30, pady=10,
                 command=lambda: button_click(3))
button4 = Button(root, text='4',bg='white', padx=30, pady=10,
                 command=lambda: button_click(4))
button5 = Button(root, text='5',bg='silver', padx=30, pady=10,
                 command=lambda: button_click(5))
button6 = Button(root, text='6',bg='white', padx=30, pady=10,
                 command=lambda: button_click(6))
button7 = Button(root, text='7',bg='white', padx=30, pady=10,
                 command=lambda: button_click(7))
button8 = Button(root, text='8',bg='silver', padx=30, pady=10,
                 command=lambda: button_click(8))
button9 = Button(root, text='9',bg='white', padx=30, pady=10,
                 command=lambda: button_click(9))
button0 = Button(root, text='0',bg='silver', padx=30, pady=10,
                 command=lambda: button_click(0))

buttonadd = Button(root, text='+',bg='white', padx=20, pady=10,
                   command=click_add)
buttonclear = Button(root, text='c',bg='white', padx=20, pady=10,
                     command=button_clear)
buttonequal = Button(root, text='=',bg='white', padx=20, pady=10,
                     command=click_equal)
buttonsub = Button(root, text='-',bg='white', padx=20, pady=10,
                   command=click_sub)
buttonmult = Button(root, text='*',bg='white', padx=30, pady=10,
                    command=click_mult)
buttondiv = Button(root, text='/',bg='white', padx=30, pady=10,
                   command=click_div)

# Griding Buttons

button1.grid(row=3, column=0)
button2.grid(row=3, column=1)
button3.grid(row=3, column=2)

button4.grid(row=2, column=0)
button5.grid(row=2, column=1)
button6.grid(row=2, column=2)

button7.grid(row=1, column=0)
button8.grid(row=1, column=1)
button9.grid(row=1, column=2)

button0.grid(row=4, column=1)
buttonadd.grid(row=2, column=3)
buttonsub.grid(row=3, column=3)
buttonmult.grid(row=4, column=0)
buttondiv.grid(row=4, column=2)
buttonclear.grid(row=1, column=3)
buttonequal.grid(row=4, column=3)

# Start

root.mainloop()
