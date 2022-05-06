from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
import time

PADDLE_HIT_BOX = 320

screen = Screen()
game_is_on = True
screen.tracer(0)
paddle_one = Paddle((350, 0))
paddle_two = Paddle((-350, 0))
ball = Ball()
score = ScoreBoard()

screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title('Pong')
screen.listen()
screen.onkeypress(fun=paddle_one.up, key="Up")
screen.onkeypress(fun=paddle_one.down, key="Down")
screen.onkeypress(fun=paddle_two.up, key="w")
screen.onkeypress(fun=paddle_two.down, key="s")

while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()
    if ball.ycor() + 10 >= 290 or ball.ycor() - 10 <= -290:
        ball.bounce()
    if ball.distance(paddle_one) < 50 and ball.xcor() > PADDLE_HIT_BOX or \
            ball.distance(paddle_two) < 50 and ball.xcor() < -PADDLE_HIT_BOX:
        ball.bounce_paddle()
    if ball.xcor() > 360:
        ball.reset_position()
        score.left_score_update()
        time.sleep(0.5)
        ball.go_towards_left()
    elif ball.xcor() < -360:
        ball.reset_position()
        score.right_score_update()
        time.sleep(0.5)
        ball.go_towards_right()
    if score.game_over():
        game_is_on = False

screen.exitonclick()
