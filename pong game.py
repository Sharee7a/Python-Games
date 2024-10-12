import turtle

# creating the window
window = turtle.Screen()
window.title('Ping Pong Game')
window.bgcolor('black')
window.setup(800, 600)
window.tracer(0)  # stop the window from updating automatically

# creating the first bat
bat1 = turtle.Turtle()  # initialize the game object
bat1.speed(0) # set the speed of the animation
bat1.shape('square')
bat1.color('yellow')
bat1.shapesize(stretch_wid=5, stretch_len=1)   # set the size of the object
bat1.penup()  # stop the object from drawing lines
bat1.goto(-350,0)  # set the position of the object

# creating the second bat
bat2 = turtle.Turtle()
bat2.speed(0)
bat2.shape('square')
bat2.color('blue')
bat2.shapesize(stretch_wid=5, stretch_len=1)
bat2.penup()
bat2.goto(350,0)

# creating the ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape('circle')
ball.color('white')
ball.penup()
ball.goto(0,0)
ball.dx = 0.2
ball.dy = 0.2

# creating the score board
score1 = 0
score2 = 0
score = turtle.Turtle()
score.speed(0)
score.color('white')
score.penup()
score.hideturtle()
score.goto(0, 250)
score.write("Player 1: 0 Player 2: 0", align='center', font=('Arial',24,'normal'))


# defining functions to move the bats up and down
def bat1_up():
    y = bat1.ycor()  # get the y coordinates of the first bat
    y += 20  # set the y to increase to be +20
    bat1.sety(y)  # set the y of the bat1 to the new y coordinates

def bat1_down():
    y = bat1.ycor()
    y -= 20
    bat1.sety(y)

def bat2_up():
    y = bat2.ycor()
    y += 20
    bat2.sety(y)

def bat2_down():
    y = bat2.ycor()
    y -= 20
    bat2.sety(y)

window.listen()
window.onkeypress(bat1_up,'w')
window.onkeypress(bat1_down, 's')
window.onkeypress(bat2_up, 'Up')
window.onkeypress(bat2_down, 'Down')


# the main game loop
while True:
    window.update()  # update the game each time the game runs

    # move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # border check
    if ball.ycor() > 290:  # if the ball at the top border
        ball.sety(290)  # set Y coordinates to 290
        ball.dy *= -1  # reverse direction, making  +2,5 ---> -2,5

    if ball.ycor() < -290: # if the ball at the bottom border
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390: # if the ball at the right border
        ball.goto(0,0) # return thr ball to the center
        ball.dx *= -1 # reverse the direction of the ball to -x
        score1 += 1
        score.clear()
        score.write("Player 1: {} Player 2: {}".format(score1,score2), align='center', font=('Arial', 24, 'normal'))

    if ball.xcor() < -390: # if the ball at the left border
        ball.goto(0,0)
        ball.dx *= -1
        score2 += 1
        score.clear()
        score.write("Player 1: {} Player 2: {}".format(score1, score2), align='center', font=('Arial', 24, 'normal'))

    # ball collision with the bats
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < bat2.ycor() + 40 and ball.ycor() > bat2.ycor() -40):
        ball.setx(340)
        ball.dx *= -1

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < bat1.ycor() + 40 and ball.ycor() > bat1.ycor() -40):
        ball.setx(-340)
        ball.dx *= -1






