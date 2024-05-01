from turtle import Screen, Turtle
import time
from snake import Snake
from food import Food
from scoreboard import Score


def display_level_features():
    screen.clear()
    screen.bgcolor("white")

    title = Turtle()
    title.penup()
    title.hideturtle()
    title.color("Blue")
    title.goto(0, 200)
    title.write("Snake Game", align="center", font=("Times New Roman", 28, "bold"))

    # Level 1 features
    level1 = Turtle()
    level1.penup()
    level1.hideturtle()
    level1.color("black")
    level1.goto(-200, 100)
    level1.write("Level 1:", align="left", font=("Fixedsys", 16, "normal"))
    level1_features = [
        "Pass through walls",
        "Slow snake speed"
    ]
    for i, feature in enumerate(level1_features):
        level1.goto(-180, 70 - i * 30)
        level1.write(feature, align="left", font=("Fixedsys", 12, "normal"))


    level2 = Turtle()
    level2.penup()
    level2.hideturtle()
    level2.color("black")
    level2.goto(-200, -50)
    level2.write("Level 2:", align="left", font=("Fixedsys", 16, "normal"))
    level2_features = [
        "Collision with walls",
        "Faster snake speed"
    ]
    for i, feature in enumerate(level2_features):
        level2.goto(-180, -80 - i * 30)
        level2.write(feature, align="left", font=("Fixedsys", 12, "normal"))

    instructions = Turtle()
    instructions.penup()
    instructions.hideturtle()
    instructions.color("Red")
    instructions.goto(0, -220)
    instructions.write("Press '1' for Level 1 or '2' for Level 2.", align="center",
                       font=("Times New Roman", 14, "normal"))

    screen.update()


def select_level(level):
    screen.clear()
    screen.bgcolor("black")
    screen.tracer(0)

    snake = Snake(level)
    food = Food()
    scoreboard = Score()

    screen.listen()
    screen.onkey(snake.up, "Up")
    screen.onkey(snake.down, "Down")
    screen.onkey(snake.left, "Left")
    screen.onkey(snake.right, "Right")

    game_on = True
    while game_on:
        screen.update()
        time.sleep(0.1 / level)

        snake.move()

        if snake.head.distance(food) < 15:
            food.refresh()
            scoreboard.increment()
            snake.extend()

        if level == 2:
            if (
                    abs(snake.head.xcor()) > 290
                    or abs(snake.head.ycor()) > 290
            ):
                scoreboard.reset()
                snake.reset()
        elif level == 1:
            if snake.head.xcor() > 290:
                snake.head.goto(-290, snake.head.ycor())
            elif snake.head.xcor() < -290:
                snake.head.goto(290, snake.head.ycor())
            elif snake.head.ycor() > 290:
                snake.head.goto(snake.head.xcor(), -290)
            elif snake.head.ycor() < -290:
                snake.head.goto(snake.head.xcor(), 290)

        for segment in snake.my_list[1:]:
            if snake.head.distance(segment) < 10:
                scoreboard.reset()
                snake.reset()


screen = Screen()
screen.setup(width=600, height=600)
screen.title("Snake Game")

display_level_features()

screen.listen()
screen.onkey(lambda: select_level(1), "1")
screen.onkey(lambda: select_level(2), "2")

screen.mainloop()
