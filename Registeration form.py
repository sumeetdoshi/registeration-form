from tkinter import *
import tkinter.messagebox as tmsg
root=Tk()
def getvalues():
    print("{namevalue.get(),gendervalue.get(),phonevalue.get(),paymentvalue.get()}")
    with open("record.txt","a") as f :
        f.write(f"{namevalue.get(),gendervalue.get(),phonevalue.get(),paymentvalue.get()}\n")
    ask = tmsg.askquestion("save ", "Would you like to submit")
    if ask == "yes":
        msg = "We have submitted your details"
        tmsg.showinfo("submitted", msg)
    else:
        msg = "We will not submit you detials"
        tmsg.showinfo("not submitted", msg)




root.geometry("400x250")
root.title("REGISTERATION FORM")
#making labels
l1=Label(root,text="NAME",fg="black")
l2=Label(root,text="GENDER",fg="black")
l3=Label(root,text="PHONE ",fg="black")
l4=Label(root, text="PAYMENT METHOD",fg="black")
#packing labels
l1.grid(row=1,column=0)
l2.grid(row=2,column=0)
l3.grid(row=3,column=0)
l4.grid(row=4,column=0)
#making buttons
b1=Button(text="REGISTER",command=getvalues,bg="blue",fg="white")
b1.grid(row=8,column=2)
b2=Button(root, text="Exit",command=exit,padx=5,bg="grey",fg="white")
b2.grid(row=8,sticky=E,columnspan=7)
#making check button

#giving value
namevalue=StringVar()
gendervalue=StringVar()
phonevalue=StringVar()
paymentvalue=StringVar()
c1value=IntVar()
#making entries
e1=Entry(root, textvariable=namevalue)
e2=Entry(root, textvariable=gendervalue)
e3=Entry(root, textvariable=phonevalue)
e4=Entry(root, textvariable=paymentvalue)
#griding values
e1.grid(row=1,column=2)
e2.grid(row=2,column=2)
e3.grid(row=3,column=2)
e4.grid(row=4,column=2)
def  value ():
    print("chalgaya!!!")
def value1():
    vale=tmsg.askquestion("save ","Would you like to save")
    if vale=="yes":
        msg="We have saved your form"
        tmsg.showinfo("Thanks",msg)
    else:
        msg="We will not save you form"
        tmsg.showinfo("Sorry",msg)


m1 = Menu(root)
m2=Menu(m1,tearoff=0)
m2.add_command(label="Save",command=value1)
m2.add_command(label="Save As",command=value)
m2.add_command(label="Print",command=value)
m2.add_command(label="New Project",command=value)
m1.add_cascade(label="File",menu=m2)
m1.add_cascade(label="Exit",command=quit)
root.config(menu=m1)





root.mainloop()
