import turtle
import winsound

# Turtle center is (0,0)
wn  = turtle.Screen()
wn.title("Pong")
wn.bgcolor("black")
height  = 600
width   = 800
wn.setup(width, height)
wn.tracer(0)

# Score
scoreA = 0
scoreB = 0

# Paddle A
paddleA = turtle.Turtle()
paddleA.speed(0)            # Animation speed, 0 sets to max
paddleA.shape("square")     # 20px X 20px by default
paddleA.color("white")
paddleA.shapesize(stretch_wid=5, stretch_len=1)
paddleA.penup()
paddleA.goto(-350, 0)


# Paddle B
paddleB = turtle.Turtle()
paddleB.speed(0)            # Animation speed, 0 sets to max
paddleB.shape("square")     # 20px X 20px by default
paddleB.color("white")
paddleB.shapesize(stretch_wid=5, stretch_len=1)
paddleB.penup()
paddleB.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)            # Animation speed, 0 sets to max
ball.shape("square")     # 20px X 20px by default
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.1
ball.dy = 0.1

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)

def paddleAUp():
    y   = paddleA.ycor()
    y  += 20
    paddleA.sety(y)

def paddleADwn():
    y   = paddleA.ycor()
    y  -= 20
    paddleA.sety(y)

def paddleBUp():
    y   = paddleB.ycor()
    y  += 20
    paddleB.sety(y)

def paddleBDwn():
    y   = paddleB.ycor()
    y  -= 20
    paddleB.sety(y)

# Keyboard binding
wn.listen()
wn.onkeypress(paddleAUp, "w") # When W is pressed call the function paddleAUP
wn.onkeypress(paddleAUp, "W") # When W is pressed call the function paddleAUP
wn.onkeypress(paddleADwn, "s")
wn.onkeypress(paddleADwn, "S")
wn.onkeypress(paddleBUp, "Up") # When W is pressed call the function paddleAUP
wn.onkeypress(paddleBDwn, "Down")

pen.write("Player A: {}  Player B: {}".format(scoreA, scoreB), align="center", font=("Courier", 24, "normal"))
# Mail game loop
while True:
    wn.update()

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border checking
    if ball.ycor() > height/2-10:
        ball.sety(height/2-10)
        ball.dy*= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    elif ball.ycor() < -height/2+10:
        ball.sety(-height/2+10)
        ball.dy*= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    if ball.xcor() > width/2-10:
        ball.goto(0, 0)
        ball.dx*= -1
        scoreA += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(scoreA, scoreB), align="center", font=("Courier", 24, "normal"))
    elif ball.xcor() < -width/2+10:
        ball.goto(0, 0)
        ball.dx*= -1
        scoreB += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(scoreA, scoreB), align="center", font=("Courier", 24, "normal"))

    # Paddle and ball collision
    if (ball.ycor() < paddleB.ycor() + 40 and ball.ycor() > paddleB.ycor() -40) and (ball.xcor() > 340  and ball.xcor() < 350) :
        ball.setx(340)
        ball.dx *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    elif (ball.ycor() < paddleA.ycor() + 40 and ball.ycor() > paddleA.ycor() -40) and (ball.xcor() < -340  and ball.xcor() > -350) :
        ball.setx(-340)
        ball.dx *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
