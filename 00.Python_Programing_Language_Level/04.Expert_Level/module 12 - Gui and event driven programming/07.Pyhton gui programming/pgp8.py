"Desktop program Age calculation"

from tkinter import *
from datetime import datetime

root = Tk()
# to keep birthyear,birthmonth,age
year = 0
month = 0
day = 0
age = 0
age_msg_str = StringVar()
age_msg_str.set("")

# showing it with label and entry box
font = "Verdana",16
msg1 = Label(text="Enter your date of birth here:", font=font)
msg1.grid(row=0,column=0,columnspan=2)


year_label = Label(text="Year",font=font,width=10)
month_label = Label(text="Month",font=font,width=10)
day_label = Label(text="Day",font=font,width=10)

year_label.grid(row=1,column=0)
month_label.grid(row=2,column=0)
day_label.grid(row=3,column=0)


year_entry = Entry(font=font,width=10)
month_entry = Entry(font=font,width=10)
day_entry = Entry(font=font,width=10)

year_entry.grid(row=1,column=1)
month_entry.grid(row=2,column=1)
day_entry.grid(row=3,column=1)

# callback function to calculate age
def callback():
    global age # 
    year = int(year_entry.get())
    month = int(month_entry.get())
    day = int(day_entry.get())

    current_day = datetime.now()
    age = current_day.year - year
    if (current_day.month,current_day.day) < (month,day):
        age -= 1
    age_msg_str.set("You are {} years Old".format(age))

# setting a button and label for calculating age
calc_age_button = Button(text="Calculate My age",font=font,command=callback)
calc_age_button.grid(row=4,column=1)

age_msg_label = Label(font=font,textvariable=age_msg_str)
age_msg_label.grid(row=5,column=0,columnspan=2)

mainloop()