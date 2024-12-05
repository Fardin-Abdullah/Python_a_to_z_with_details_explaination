"Target make a program like where ww will click mouse on turtle screen mouse will reach there"
import turtle

turtle_screen = turtle.Screen()
nonte = turtle.Turtle()
nonte.shape("turtle")

def run_to_position(x,y):
    nonte.goto(x,y)
    print(x,y)

def exit():
    turtle_screen.bye()

turtle_screen.onclick(run_to_position)
turtle_screen.onkey(exit,"Escape")

turtle_screen.listen()
turtle_screen.mainloop()