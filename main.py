import tkinter as tk
# from tkinter.ttk import Label, LabelFrame
from tkinter import *
import numpy as np
from scipy import stats
import datetime
from statistics import mean, median, mode, variance
from PIL import ImageTk,Image

root =Tk()
root.title("stastico for automated statistics")
root.configure(bg="azure")
my_img1 =ImageTk.PhotoImage(file="icon.ico")
root.iconphoto(False,my_img1)

x=datetime.datetime.now()
label=Label(root,text=f"this software focuses on mathematical calculations in statics developed in {x.strftime("%x")} by chris kent",padx=100,pady=10)
label2=Label(root,text="it focus on the numpy module")
frame2 =LabelFrame(root,text="inputs..")
frame2.pack(expand='yes',fill='both')
frame2.configure(bg="azure")


frame =LabelFrame(root,text="calculations..")
frame.pack(expand='yes',fill='both')




myLabel =Label(frame2,text="input your values ",bg="blue").grid(row=0,column=0)
e = Entry(frame2,fg="green",width=100,borderwidth=5)
e.grid(row=0,column=1)

global list_num
list_num = []
def myClick(number):
    current= e.get()
    e.delete(0,END)
    e.insert(0,str(current)+str(number))
def clear():
    e.delete(0,END) 

def add():
    global first
    first =int(e.get())
    list_num.append(first)
    update_label()
    e.delete(0,END)
    
def update_label():
    my_label1= Label(frame_1,text=str(list_num),padx=300,pady=20,fg="purple",width=200, anchor="w", justify="left",wraplength=800,font=(15)).place(y=100)
    # go =np.array(first)
def mean():
    global mean
    global go
    # go =list_num.append(int(e.get()))
    go= np.array(list_num)
    if len(go)<1:
        my_label1= Label(frame_1,text="not enough data",padx=300,pady=20,fg="purple",width=200, anchor="w", justify="left",wraplength=800,font=(15)).place(x=0,y=100)
    else:

        e.delete(0,END)
        mean= np.mean(go)
        e.insert(0,mean)
def mod():
    global mode
    global go
    # go =list_num.append(int(e.get()))
    go= np.array(list_num)
    if len(go)<1:
        my_label1= Label(frame_1,text="not enough data",padx=300,pady=20,fg="purple",width=200, anchor="w", justify="left",wraplength=800,font=(15)).place(x=0,y=100)
    else:
        e.delete(0,END)
        mode= mode(go)
        e.insert(0,mode) 
def median():
    global median
    global go
    # go =list_num.append(int(e.get()))
    go= np.array(list_num)
    if len(go)<1:
        my_label1= Label(frame_1,text="not enough data",padx=300,pady=20,fg="purple",width=200, anchor="w", justify="left",wraplength=800,font=(15)).place(x=0,y=100)
    else:
        e.delete(0,END)
        median= np.median(go)
        e.insert(0,median)
def sd():
    global sd
    global go
    # go =list_num.append(int(e.get()))
    go= np.array(list_num)
    if len(go)<1:
        my_label1= Label(frame_1,text="not enough data",padx=300,pady=20,fg="purple",width=200, anchor="w", justify="left",wraplength=800,font=(15)).place(x=0,y=100)
    else:
        e.delete(0,END)
        sd= np.std(go)
        e.insert(0,sd)
def var():
    global list_num
    go =np.array(list_num)
    if len(go)<1:
        my_label1= Label(frame_1,text="not enough data",padx=300,pady=20,fg="purple",width=200, anchor="w", justify="left",wraplength=800,font=(15)).place(x=0,y=100)
    else:
        e.delete(0,END)
        var=variance(go)
        e.insert(0,f"{var:.2f}")

def clearList():
    list_num.clear()
    update_label()

def pop():
    number = int(e.get())
    list_num.pop(number)
    update_label()    


button_1=Button(frame,padx=100,pady=20,text="1",bg="black",fg="white", command=lambda:myClick(1))
button_2=Button(frame,padx=100,pady=20,text="2",bg="black",fg="white", command=lambda:myClick(2))
button_3=Button(frame,padx=100,pady=20 ,text="3",bg="black",fg="white", command=lambda:myClick(3))
button_4=Button(frame,padx=100,pady=20 ,text="4",bg="black",fg="white", command=lambda:myClick(4))
button_5=Button(frame,padx=100,pady=20 ,text="5",bg="black",fg="white", command=lambda:myClick(5))
button_6=Button(frame,padx=100,pady=20 ,text="6",bg="black",fg="white", command=lambda:myClick(6))
button_7=Button(frame,padx=100,pady=20 ,text="7",bg="black",fg="white", command=lambda:myClick(7))
button_8=Button(frame,padx=100,pady=20 ,text="8",bg="black",fg="white", command=lambda:myClick(8))
button_9=Button(frame,padx=100,pady=20 ,text="9",bg="black",fg="white", command=lambda:myClick(9))
button_0=Button(frame,text="0",padx=100,pady=20 ,bg="black",fg="white", command=lambda:myClick(0))
button_append=Button(frame,text="Addtolist ",padx=75,pady=20,bg="black",fg="white",command=add)
button_clear=Button(frame,text="clear",padx=90,pady=20,bg="black",fg="white",command=clear)
button_listDelete=Button(frame,text="deleteitem(pop)",bg="black",fg="white",padx=70,pady=20,command=pop)
button_Deleteitem=Button(frame,text="deletedata ",bg="black",fg="white",padx=80,pady=20,command=clearList)
button_1.grid(row=1, column=0)
button_2.grid(row=1, column=1)
button_3.grid(row=1, column=2)

button_4.grid(row=1, column=3)
button_5.grid(row=2, column=0)
button_6.grid(row=2, column=1)

button_7.grid(row=2, column=2)
button_8.grid(row=2, column=3)
button_9.grid(row=3, column=0)
button_0.grid(row=3, column=1)
button_append.grid(row=3, column=2)
button_clear.grid(row=3, column=3)
button_Deleteitem.grid(row=4, column=0)
button_listDelete.grid(row=4, column=1)

# frame_1.config(bg="pink")
frame_1 =LabelFrame(root,text="operaions..")
frame_1.pack(expand='yes',fill='both')
frame_1.configure(bg="pink")
frame.configure(bg="pink")
button_A=Button(frame_1,text="MEAN",padx=100,pady=20,bg="black",fg="white", command=mean)
button_B=Button(frame_1,text="MODE",padx=100,pady=20,bg="black",fg="white", command=mod)
button_C=Button(frame_1,text="MED",padx=100,pady=20,bg="black",fg="white", command=median)
button_D=Button(frame_1,text="SD",padx=100,pady=20,bg="black",fg="white",command=sd)
button_E=Button(frame_1,text="VARIENCE",padx=100,pady=20,bg="black",fg="white", command=var)

button_A.grid(row=0,column=0)
button_B.grid(row=0,column=1)
button_C.grid(row=0,column=2)

button_D.grid(row=0,column=3)
button_E.grid(row=0,column=4)
my_label1= Label(frame_1,text=str(list_num),fg="purple",width=200, anchor="w", justify="left",wraplength=800,font=(15))
my_label1.place(x=0,y=100)

# myLabel =Label(frame_1,text="hello",bg="blue").pack()
# e = Entry(frame_1,fg="green",width=50)
# e.pack()


root.mainloop()