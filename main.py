from turtle import Turtle, Screen


player=Turtle()
screen= Screen()

def move_up():
  player.setheading(90)
  player.forward(10)
  
def move_right():
  player.setheading(0)
  player.forward(10)

def move_down():
  player.setheading(270)
  player.forward(10)
  
def move_left():
  player.setheading(180)
  player.forward(10)
  
  
screen.listen()
screen.onkey(key="Up",fun=move_up)
screen.onkey(key="Right",fun=move_right)
screen.onkey(key="Down",fun=move_down)
screen.onkey(key="Left",fun=move_left)
screen.exitonclick()