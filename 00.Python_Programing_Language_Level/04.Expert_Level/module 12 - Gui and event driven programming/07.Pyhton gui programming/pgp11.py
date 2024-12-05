"Digital watch"
from tkinter import *
from datetime import datetime

root = Tk()
root.title("Digital Clock") # using title function to to give title to window
root.minsize(520,100) # setting minimum size of window

# important label to show hour,minute,sec

font_1 = "Cursed Timer ULil",72 # You can use your desired font here
font_2 = "Cursed Timer ULil",48

time_str = StringVar()
sec_str = StringVar()

time_str.set("00:00")
sec_str.set("00")

time_label = Label(textvariable=time_str,font=font_1)
sec_label = Label(textvariable=sec_str,font=font_2)

# establishing label on grid
time_label.grid(row=0,column=0,sticky="S")
sec_label.grid(row=0,column=1,sticky="S")

# now we will show current time and also it will update time
def update():
    now = datetime.now()
    hour = now.hour
    minute = now.minute
    second = now.second
    # formated string 
    time_str.set("{:02d}:{:02d}".format(hour,minute))
    sec_str.set("{:02d}".format(second))
    root.after(1000,update) # here we are telling after every 1000 ms or 1 sec call update function
    # last

    if time_format.get() == 1:
        if hour>12:
            am_pm_str.set("PM")
            hour %= 12
        else:
            am_pm_str.set("AM")
    else:
        am_pm_str.set("")


# now if we want we can add menu here

menu = Menu()
root.configure(menu=menu)

file_menu = Menu(menu,tearoff=0)
menu.add_cascade(label="File",menu=file_menu)



# settings function 
def settings():
    global time_format
    settings_win = Toplevel()
    settings_win.title("Settings")
    twentyfour = Radiobutton(settings_win,text,text="24-hour format",var=time_format,value=0)
    twelve = Radiobutton(settings_win,text="AM/PM format",var=time_format,value=1)
    twentyfour.grid(row=0,column=0)
    twelve.grid(row=0,column=1)


file_menu.add_command(label="Settings",command=settings)
file_menu.add_separator()
file_menu.add_command(label="Exit",command=root.destroy)

# time format

time_format = IntVar()
time_format.set(0)

font_3 = "Verdana",72
am_pm_str = StringVar()
am_pm_str.set("")
am_pm_label = Label(textvariable=am_pm_str,font=font_3,width=3)
am_pm_label.grid(row=0,column=3,sticky="S")


# settings function 
def settings():
    global time_format
    settings_win = Toplevel()
    settings_win.title("Settings")
    twentyfour = Radiobutton(settings_win,text,text="24-hour format",var=time_format,value=0)
    twelve = Radiobutton(settings_win,text="AM/PM format",var=time_format,value=1)
    twentyfour.grid(row=0,column=0)
    twelve.grid(row=0,column=1)

file_menu.add_command(label="Settings",command=settings)
file_menu.add_separator()
file_menu.add_command(label="Exit",command=root.destroy)



# last
update()
mainloop()