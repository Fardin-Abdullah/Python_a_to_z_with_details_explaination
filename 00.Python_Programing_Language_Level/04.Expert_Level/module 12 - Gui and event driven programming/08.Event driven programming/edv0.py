# in every program it starts from the first line and executes every line one by one
# we press keys of keyboard we use mouse it is called event pressing any key or pressing mouse button is event
# for example text editor software waits for this type of event this software checks which key has been pressed
# and if in this software it is told that what it has to do if someone press this key it does that
# for this we need to do a programming which is called event driven programming
# if an event occurs what the program does is called event handle
# GUI based programs have to be event-driven where user have to give input and program will work according to the input
# Computer games ar event-driven

# let's see an easy event driven program
import turtle

turtle_screen = turtle.Screen()

monte = turtle.Turtle()
monte.shape("turtle")

def move_forward():
    monte.forward(30)

turtle_screen.onkey(move_forward,"Up")
# Up is the arrow key of keyboards after pressing it it will call the move_forward function

turtle_screen.listen()
turtle_screen.mainloop() # this will make the program to wait for event this is called event loop