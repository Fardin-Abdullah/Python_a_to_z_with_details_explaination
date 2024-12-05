"to take different types of command we use differnettypes of buttons after clicking bitton create Tk() window"
"create an event which is called event firing"
"after firing an event what we want to do we make a function for this and bind it with the event and also we can do this with button"
"when we click the button the function will be called which is binded with the button this type of function is called callback function"


from tkinter import *
root = Tk()

font = "Verdana",16
clicked_label = Label(text="Not clicked",font=font,width=20)
clicked_label.grid(row=0,column=0)

# after clicking the button this function will be called
def callback():
    clicked_label.configure(text="Button was clicked")

clicker_button = Button(text="Click here",font=font,width=10,command=callback)
clicker_button.grid(row=1,column=0)

mainloop()