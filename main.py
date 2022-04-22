import turtle
import time
import random


def change_side(n):
    snake.speed(0)
    snake.hideturtle()
    if n == 0:
        snake.setx(-screen.window_width() * snake.move[n] / 2)
    else:
        snake.sety(-screen.window_height() * snake.move[n] / 2)
    snake.showturtle()
    snake.speed(1)


def change_direction(direction):
    snake.direction = direction
    if snake.direction == "up":
        snake.move = (0, 1)
    elif snake.direction == "down":
        snake.move = (0, -1)
    elif snake.direction == "left":
        snake.move = (-1, 0)
    elif snake.direction == "right":
        snake.move = (1, 0)
    else:
        snake.move = (0, 0)
    print(snake.direction)


def move_snake():
    x = snake.xcor() + (10 * snake.move[0])
    y = snake.ycor() + (10 * snake.move[1])
    snake.goto(x, y)
    if snake.xcor() > screen.window_width() / 2 or snake.xcor() < -screen.window_width() / 2:
        change_side(0)
    if snake.ycor() > screen.window_height() / 2 or snake.ycor() < -screen.window_height() / 2:
        change_side(1)


def set_food():
    food.hideturtle()
    food.setx(random.randint(int(-screen.window_width() / 2), int(screen.window_width() / 2)))
    food.sety(random.randint(int(-screen.window_height() / 2), int(screen.window_height() / 2)))
    food.showturtle()


def check_collision():
    if snake.distance(food) < 20:
        add_body()
        set_food()


def add_body():
    snake.score += 1
    txt.clear()
    txt.write(f"Score: {snake.score} Highscore: {snake.highscore}", align="center", font=("Courier", 24, "normal"))
    for _ in range(3):
        body = turtle.Turtle()
        body.hideturtle()
        body.speed(0)
        body.shape("square")
        body.color("green")
        body.penup()
        body.goto(last_pos)
        body.showturtle()
        snake.body.append(body)


def gameOver():
    global isAlive
    for part in snake.body:
        part.hideturtle()
    snake.body = []
    snake.home()
    change_direction("stop")
    isAlive = True
    if snake.score > snake.highscore:
        snake.highscore = snake.score
    snake.score = 0
    txt.clear()
    txt.write(f"Score: {snake.score} Highscore: {snake.highscore}", align="center", font=("Courier", 24, "normal"))
    game()


def game():
    global isAlive
    global last_pos
    while isAlive:
        screen.update()
        last_pos = snake.pos()
        move_snake()
        for part in snake.body:
            temp_pos = last_pos
            last_pos = part.pos()
            part.goto(temp_pos)
            if part.distance(snake) < 10:
                isAlive = False

        check_collision()
        time.sleep(delay)
    else:
        gameOver()


delay = 0.1

screen = turtle.Screen()
screen.bgcolor("gray")
screen.title("Snake game")

# Establece las dimensiones de la ventana
screen.setup(650, 650)

snake = turtle.Turtle()
snake.speed(0)
snake.penup()
snake.shape("square")
snake.color("green")
snake.move = (0, 0)
snake.score = 0
snake.highscore = 0
change_direction("stop")

screen.listen()
screen.onkeypress(lambda: change_direction("up"), "Up")
screen.onkeypress(lambda: change_direction("down"), "Down")
screen.onkeypress(lambda: change_direction("left"), "Left")
screen.onkeypress(lambda: change_direction("right"), "Right")

food = turtle.Turtle()
food.speed(0)
food.penup()
food.shape("circle")
food.color("red")
set_food()

snake.body = []
last_pos = (0, 0)

txt = turtle.Turtle()
txt.speed(0)
txt.penup()
txt.hideturtle()
txt.goto(0, -260)
txt.write(f"Score: {snake.score} Highscore: {snake.highscore}", align="center", font=("Courier", 24, "normal"))

isAlive = True
game()

turtle.done()
