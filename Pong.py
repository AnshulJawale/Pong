import turtle
import time
import random

#todo Setup the main screen
win = turtle.Screen()                                           #? Setting Screen
win.title("Pong")                                               
win.bgcolor("black")
win.setup(width=800, height=600)
win.tracer()

# Scoring
score_a = 0
score_b = 0
#? Design
#todo Design 2 paddle and 1 ball 
#* Left Paddle
paddle_left = turtle.Turtle()
paddle_left.speed(0)
paddle_left.shape("square")
paddle_left.color("white")
paddle_left.penup()
paddle_left.goto(-350, 0)
paddle_left.shapesize(stretch_wid=5, stretch_len=1)                #? Increases the width 5x

#* Right Paddle
paddle_right = turtle.Turtle()
paddle_right.speed(0)
paddle_right.shape("square")
paddle_right.color("white")
paddle_right.penup()
paddle_right.goto(350, 0)
paddle_right.shapesize(stretch_wid=5, stretch_len=1)

#* Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.shapesize(stretch_wid=1, stretch_len=1)
ball.dx = 5
ball.dy = random.randrange(2, 10)

#* Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("cyan")
pen.penup()
pen.hideturtle()
def start():
    for i in range(0, 6):
        pen.clear()
        pen.goto(0, 100)
        pen.write(f"Your game starts in {5-i}", align="center", font=("Courier", 14, "normal"))
        time.sleep(1)
        pen.clear()
start()
pen.goto(0, 260)
pen.write(f"Player A : {score_a}       Player B : {score_b}", align="center", font=("Courier", 24, "normal"))

#? Functions
def paddle_up(paddle:turtle.Turtle):
    y = paddle.ycor()
    y += 20
    paddle.sety(y)                                              

def paddle_down(paddle:turtle.Turtle):
    y = paddle.ycor()
    y -= 20
    paddle.sety(y)

#? Bindin with keyboard
paddle = paddle_left or paddle_right
win.listen()
win.onkeypress(fun=lambda : paddle_up(paddle), key="Up")
win.onkeypress(fun=lambda : paddle_down(paddle), key="Down")

#? Main Game loop
if __name__ == "__main__":
    try:
        while True:
            win.update()
            if ball.dx > 0:
                paddle = paddle_right
            else:
                paddle = paddle_left
            ball.setx(ball.xcor() + ball.dx)
            ball.sety(ball.ycor() + ball.dy)
            if ball.ycor() > 290:
                ball.dy *= -1
            if ball.ycor() < -290:
                ball.dy *= -1
            if ball.xcor() > 390:
                ball.goto(0, 0)
                score_a += 1
                ball.dx *= -1
                pen.clear()
                pen.write(f"Player A : {score_a}       Player B : {score_b}", align="center", font=("Courier", 24, "normal"))
            if ball.xcor() < -390:
                ball.goto(0, 0)
                ball.dx *= -1
                score_b += 1
                pen.clear()
                pen.write(f"Player A : {score_a}       Player B : {score_b}", align="center", font=("Courier", 24, "normal"))

            if (ball.xcor() > 340 and ball.xcor() < 350)and (ball.ycor() < paddle_right.ycor() + 40 and ball.ycor() > paddle_right.ycor() - 40):
                ball.setx(340)
                ball.dx *= -1
                
            if (ball.xcor() < -340 and ball.xcor() < 350) and (ball.ycor() < paddle_left.ycor() + 40 and ball.ycor() > paddle_left .ycor()- 40):
                ball.setx(-340)
                ball.dx *= -1
    except:
        print("Game Over")