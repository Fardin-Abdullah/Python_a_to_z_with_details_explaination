# to show any text on tkinter we have to create label type object then we have to show it

from tkinter import *
root = Tk()

label1 = Label(text = "Hello thre!",font=("Verdana",16))  # telling the font using a tuple
label2 = Label(text = "How are you doing?")

# while creating object of label() class txt,font

label1.grid(row=0,column=0)
label2.grid(row=1,column=0) # for showing the label on window we called grid function here we are telling where it will be showed on window



mainloop()