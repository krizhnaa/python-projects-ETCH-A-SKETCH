from turtle import Turtle, Screen

miya = Turtle()
miya.shape('arrow')

def move_for():
    miya.forward(25)
def move_back():
    miya.back(25)
def turn_left():
    miya.left(10)
def turn_right():
    miya.right(10)

def clear_scr():
    miya.clear()
    miya.penup()
    miya.home()
    miya.pendown()

screen = Screen()
screen.onkey(key='w', fun=move_for)
screen.onkey(key='s', fun=move_back)
screen.onkey(key='a', fun=turn_left)
screen.onkey(key='d', fun=turn_right)
screen.onkey(key='c', fun=clear_scr)

screen.listen()
screen.exitonclick()