import turtle

# main
wn = turtle.Screen()
wn.title("Pong by @ME")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)
# skore
score_a = 0
score_b = 0
# paddle hrace c.1
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)
# paddle hrace c.2
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)
# míč
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.1
ball.dy = 0.1
# zobrazeni skore
player_1 = "Player 1"
player_2 = "Player 2"
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write(f"{player_1}: 0 {player_2}: 0", align="center", font=("Courier", 24, "bold"))


# funkce pro pohyb paddles
def paddle_a_up():
    y = paddle_a.ycor()
    y += 40
    paddle_a.sety(y)


def paddle_a_down():
    y = paddle_a.ycor()
    y -= 40
    paddle_a.sety(y)


def paddle_b_up():
    y = paddle_b.ycor()
    y += 40
    paddle_b.sety(y)


def paddle_b_down():
    y = paddle_b.ycor()
    y -= 40
    paddle_b.sety(y)


# ovladani paddles
wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")

while True:
    wn.update()
    #
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
    # pohyb mice
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
    # skorovani hrace
    if ball.xcor() > 350:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write(f"{player_1}: {score_a} {player_2}: {score_b}", align="center", font=("Courier", 24, "bold"))
        if score_a == 10:
            quit()
    if ball.xcor() < -350:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write(f"{player_1}: {score_a} {player_2}: {score_b}", align="center", font=("Courier", 24, "bold"))
        if score_b == 10:
            quit()
    # odraz mice od paddles
    if (340 < ball.xcor() < 350) and (paddle_b.ycor() + 40 > ball.ycor() > paddle_b.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1
        ball.dy *= 1.1
        ball.dx *= 1.1

    if (-340 > ball.xcor() > -350) and (paddle_a.ycor() + 40 > ball.ycor() > paddle_a.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1
        ball.dy *= 1.1
        ball.dx *= 1.1
