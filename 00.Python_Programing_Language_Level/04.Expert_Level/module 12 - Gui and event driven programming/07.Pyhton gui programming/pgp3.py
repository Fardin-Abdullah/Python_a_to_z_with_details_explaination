from tkinter import *

root = Tk()

font1 = ("Verdana",16)
font2 = ("Comic Sans MS",16,"underline")
font3 = ("Arial",16,"bold")

label1 = Label(text="This is a good day", font=font1,foreground="red",background="orange")
label2 = Label(text="This is a good day", font=font2,foreground="#5F2F2F",background="#FFDFDF")
label3 = Label(text="This is a good day", font=font3,foreground="black",background="#DFDFFF")

label1.grid(row=0,column=0)
label2.grid(row=1,column=0)
label3.grid(row=2,column=0)

# sometimes we need to change writing of label to do this

label1.configure(text="This is a sunny day!",font=("Times New Roman",16))

# if we want we can bind string variable with label 
# then which string is in variable that string will be shown in label but in this case instead of using python string we have to use StringVar() class object 
s = StringVar()
s.set("Good Morning!")
label = Label(textvariable=s,font=('Verdana',16))
label.grid(row=0,column=0)

# now if we change the value of s string the labal will be changed also and we have to use set()

s.set("Nice to meet you!")
s.set("You have done well")
mainloop()