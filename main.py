from turtle import Turtle, Screen

miya = Turtle()
miya.shape('arrow')

def move_for():
    miya.forward(25)


screen = Screen()
screen.onkey(key='w', fun=move_for)

screen.listen()
screen.exitonclick()