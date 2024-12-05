"by using grid we can establish different elements in we can say the row and column number of any element"\
"number of elements is directly proportional to the number of row and column"

from tkinter import *

root = Tk()

for i in range(16):
    l = Label(text=str(i),font=("Verdana",16))
    l.grid(row=i//4,column=i%4)
    label.append(l)

label1.grid(row=0,column=0,rowspan=2)
label2.grid(row=0,column=1)
label2.grid(row=0,column=1,columnspan=2)
label2.grid(row=0,column=0)
label2.grid(row=0,column=2)

mainloop()