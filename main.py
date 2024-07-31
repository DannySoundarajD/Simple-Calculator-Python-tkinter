from tkinter import *
root = Tk()
root.title("Simple Calculator")
root.iconbitmap('Calc_icon.ico')
root.configure(bg="pink")

ent = Entry(root, width=50,borderwidth=10)
ent.grid(row = 0,column = 0,columnspan = 4,padx = 20,pady = 20)
ent.get()

def button_input(number):
    new_number = ent.get()
    ent.delete(0,END)
    ent.insert(0,str(new_number)+str(number))

def button_clear():
    ent.delete(0,END)


def Add():
    global math
    math = "Add"
    first_number = ent.get()
    global f_num
    f_num = int(first_number)
    ent.delete(0,END)

def Sub():
    global math
    math = "Sub"
    first_number = ent.get()
    global f_num
    f_num = int(first_number)
    ent.delete(0,END)

def Mul():
    global math
    math = "Mul"
    first_number = ent.get()
    global f_num
    f_num = int(first_number)
    ent.delete(0,END)

def Div():
    global math
    math = "Div"
    first_number = ent.get()
    global f_num
    f_num = int(first_number)
    ent.delete(0,END)

def button_equal():
    second_number = int(ent.get())
    ent.delete(0,END)
    if math == "Add":
        sum = f_num + second_number
        ent.insert(0,sum)

    if math == "Sub":
        sum = f_num - second_number
        ent.insert(0,sum)

    if math == "Mul":
        sum = f_num * second_number
        ent.insert(0,sum)

    if math == "Div":
        sum = f_num / second_number
        ent.insert(0,sum)

button_1 = Button(root, text=1,width = 15,background="yellow",fg="black",command=lambda :button_input(1))
button_2 = Button(root, text=2,width = 15,background="yellow",fg="black",command=lambda :button_input(2))
button_3 = Button(root, text=3,width = 15,background="yellow",fg="black",command=lambda :button_input(3))

button_4 = Button(root, text=4,width = 15,background="yellow",fg="black",command=lambda :button_input(4))
button_5 = Button(root, text=5,width = 15,background="yellow",fg="black",command=lambda :button_input(5))
button_6 = Button(root, text=6,width = 15,background="yellow",fg="black",command=lambda :button_input(6))

button_7 = Button(root, text=7,width = 15,background="yellow",fg="black",command=lambda :button_input(7))
button_8 = Button(root, text=8,width = 15,background="yellow",fg="black",command=lambda :button_input(8))
button_9 = Button(root, text=9,width = 15,background="yellow",fg="black",command=lambda :button_input(9))


button_0 = Button(root, text=0,width = 15,background="yellow",fg="black",command=lambda :button_input(0))
button_clear = Button(root, text="Clear",background="red",fg="black",width=32,command=button_clear)


button_add = Button(root, text="+",width = 15,bg="green",fg="white",command=Add)
button_sub = Button(root, text="-",width = 15,bg="green",fg="white",command=Sub)
button_mul = Button(root, text="x",width = 15,bg="green",fg="white",command=Mul)


button_div = Button(root, text="/",width = 15,bg="green",fg="white",command=Div)
button_eq = Button(root, text="=",width = 15,height=3,bg="blue",fg="black",command=button_equal)

button_exit = Button(root,text="Exit the Programme",width=49,bg="orange",command=root.quit)

button_1.grid(row= 1, column = 0)
button_2.grid(row= 1, column = 1)
button_3.grid(row= 1, column = 2)

button_4.grid(row= 2, column = 0)
button_5.grid(row= 2, column = 1)
button_6.grid(row= 2, column = 2)

button_7.grid(row= 3, column = 0)
button_8.grid(row= 3, column = 1)
button_9.grid(row= 3, column = 2)


button_0.grid(row= 4, column = 0)
button_clear.grid(row = 4,column = 1,columnspan=2)

button_add.grid(row=5,column = 0)
button_sub.grid(row=5,column=1)
button_eq.grid(row=5,column=2,rowspan=2)


button_div.grid(row=6,column=0)
button_mul.grid(row=6,column=1)

button_exit.grid(row=7,column=0,columnspan = 3)

root.mainloop()
