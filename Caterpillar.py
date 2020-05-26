import turtle as tr
import random as rn
import time as ti

tr.bgcolor('yellow')
caterpillar = tr.Turtle()
caterpillar.speed(0)
poly = ((0,0),(10,-5),(0,10),(-10,-5))
tr.register_shape('arrow', poly)
caterpillar.shape('arrow')
caterpillar.color('red')
#caterpillar.penup()
caterpillar.hideturtle()

leaf = tr.Turtle()
leaf_shape = ((0,0),(14,2),(18,6),(20,20),(6,18),(2,14))

tr.register_shape('leaf', leaf_shape)
leaf.shape('leaf')
leaf.color('purple')
leaf.penup()
leaf.hideturtle()
leaf.speed()


game_started = False
text = tr.Turtle()
text.write('Press SPACE to start', align='center', font=('Arial',18,'bold'))
text.hideturtle()

score = tr.Turtle()
score.hideturtle()
score.speed(0)

def outside_window():
    left_wall = -tr.window_width() / 2
    right_wall = tr.window_width() / 2
    top_wall = tr.window_height() / 2
    bottom_wall = -tr.window_height() / 2
    (x, y) = caterpillar.pos()
    outside = x < left_wall or x > right_wall or y > top_wall or y < bottom_wall
    return outside

def place_leaf():
    leaf.hideturtle()
    leaf.setx(rn.randint(-200,200))
    leaf.sety(rn.randint(-200,200))
    leaf.showturtle()

def game_over():
    caterpillar.color('yellow')
    leaf.color('yellow')
    tr.penup()
    tr.hideturtle()
    tr.write('------> GAME OVER <------', align='center', font=('Arial', 30, 'bold'))


def display_score(current_score):
    score.clear()
    score.penup()
    x = (tr.window_width()/2) - 50
    y = (tr.window_height()/2) - 50
    score.setpos(x,y)
    score.write(str(current_score), align='right', font=('Arial', 40, 'bold'))


def start_game():
    global game_started
    if game_started:
        return
    game_started = True
    score = 0
    text.clear()
    caterpillar_speed = 1
    caterpillar_length = 3
    caterpillar.shapesize(1,caterpillar_length,1)
    caterpillar.showturtle()
    display_score(score)
    place_leaf()

    while True:
        caterpillar.forward(caterpillar_speed)
        if caterpillar.distance(leaf) < 20 :
            place_leaf()
            caterpillar_speed += 0.3
            caterpillar_length += 1
            caterpillar.shapesize(1,caterpillar_length,1)
            score += 10
            display_score(score)
        if outside_window():
            game_over()
            break

def move_up():
    if caterpillar.heading() == 0 or caterpillar.heading() == 180:
        caterpillar.setheading(90)

def move_down():
    if caterpillar.heading() == 0 or caterpillar.heading() == 180:
        caterpillar.setheading(270)
def move_right():
    if caterpillar.heading() == 90 or caterpillar.heading() == 270:
        caterpillar.setheading(0)
def move_left():
    if caterpillar.heading() == 90 or caterpillar.heading() == 270:
        caterpillar.setheading(180)





tr.onkey(start_game,'space')
tr.onkey(move_up, 'Up')
tr.onkey(move_down, 'Down')
tr.onkey(move_right, 'Right')
tr.onkey(move_left, 'Left')
tr.listen()
tr.mainloop()