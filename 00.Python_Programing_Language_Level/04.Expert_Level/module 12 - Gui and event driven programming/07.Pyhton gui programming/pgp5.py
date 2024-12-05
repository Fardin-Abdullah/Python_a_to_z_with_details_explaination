"To take input from user we create entry type object to read value from entry we use get function"

from tkinter import *

root = Tk()

age_entry = Entry()
age_entry.grid(row=0,column=0)

age_string = Entry.get()
age_int = int(age_string)

# we can delete entry like this
age_entry.delete(0,END)
# and can insert like this
age_entry.insert(0,"Enter your age here")
# to show the text

mainloop()