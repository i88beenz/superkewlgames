import turtle
import time
import random

def preGameScreen():
    screen = turtle.Screen()
    screen.title("Snake Game - Settings")
    screen.bgcolor("black")
    screen.setup(width=600, height=600)
    screen.tracer(0)

    # Instructions text
    instructions = turtle.Turtle()
    instructions.color("white")
    instructions.penup()
    instructions.hideturtle()
    instructions.goto(0, 200)
    instructions.write("SNAKE GAME - Settings", align="center", font=("Arial", 24, "bold"))

    # Helper functions to create buttons
    def create_button(text, x, y, onClick):
        button = turtle.Turtle()
        button.shape("square")
        button.color("gray")
        button.penup()
        button.goto(x, y)
        button.write(text, align="center", font=("Arial", 12, "bold"))
        button.onclick(onClick)
        return button

    # Game options
    border_size = 300  # default border size
    snake_speed = 0.1  # default speed
    apple_count = 1    # default apple count

    # Functions to change settings
    def set_border_size_300(x, y):
        nonlocal border_size
        border_size = 300
        print("Border size set to 300")

    def set_border_size_400(x, y):
        nonlocal border_size
        border_size = 400
        print("Border size set to 400")

    def set_speed_slow(x, y):
        nonlocal snake_speed
        snake_speed = 0.15
        print("Snake speed set to slow")

    def set_speed_normal(x, y):
        nonlocal snake_speed
        snake_speed = 0.1
        print("Snake speed set to normal")

    def set_speed_fast(x, y):
        nonlocal snake_speed
        snake_speed = 0.05
        print("Snake speed set to fast")

    def set_apple_count_1(x, y):
        nonlocal apple_count
        apple_count = 1
        print("Apple spawn count set to 1")

    def set_apple_count_2(x, y):
        nonlocal apple_count
        apple_count = 2
        print("Apple spawn count set to 2")

    def set_apple_count_3(x, y):
        nonlocal apple_count
        apple_count = 3
        print("Apple spawn count set to 3")

    def start_game(x, y):
        print("Starting Game with settings:")
        print(f"Border size: {border_size}")
        print(f"Snake speed: {snake_speed}")
        print(f"Apple count: {apple_count}")
        gameScreen(border_size, snake_speed, apple_count)

    # Create buttons for settings
    create_button("Border Size 300", -150, 50, set_border_size_300)
    create_button("Border Size 400", 150, 50, set_border_size_400)
    create_button("Snake Speed Slow", -150, 0, set_speed_slow)
    create_button("Snake Speed Normal", 150, 0, set_speed_normal)
    create_button("Snake Speed Fast", -150, -50, set_speed_fast)
    create_button("Apple Count 1", 150, -50, set_apple_count_1)
    create_button("Apple Count 2", -150, -100, set_apple_count_2)
    create_button("Apple Count 3", 150, -100, set_apple_count_3)

    # Start button
    start_button = create_button("Start Game", 0, -150, start_game)

    # Keep the pregame screen open until the user clicks start
    turtle.done()

def gameScreen(border_size, snake_speed, apple_count):
    screen = turtle.Screen()
    screen.title("Snake Game")
    screen.bgcolor("black")
    screen.setup(width=600, height=600)
    screen.tracer(0)

    # draw the border
    border = turtle.Turtle()
    border.color("white")
    border.penup()
    border.goto(-border_size//2, border_size//2)
    border.pendown()
    border.pensize(3)
    for _ in range(4):
        border.forward(border_size)
        border.right(90)
    border.hideturtle()

    # snake head
    head = turtle.Turtle()
    head.shape("square")
    head.color("green")
    head.penup()
    head.goto(0, 0)
    head.direction = "stop"

    segments = []

    # food
    food = turtle.Turtle()
    food.shape("circle")
    food.color("red")
    food.penup()
    food.goto(0, 100)

    def move():
        for i in range(len(segments) - 1, 0, -1):
            x = segments[i - 1].xcor()
            y = segments[i - 1].ycor()
            segments[i].goto(x, y)

        if len(segments) > 0:
            x = head.xcor()
            y = head.ycor()
            segments[0].goto(x, y)

        if head.direction == "up":
            head.sety(head.ycor() + 20)

        if head.direction == "down":
            head.sety(head.ycor() - 20)

        if head.direction == "left":
            head.setx(head.xcor() - 20)

        if head.direction == "right":
            head.setx(head.xcor() + 20)

    # direction control
    def go_up():
        if head.direction != "down":
            head.direction = "up"

    def go_down():
        if head.direction != "up":
            head.direction = "down"

    def go_left():
        if head.direction != "right":
            head.direction = "left"

    def go_right():
        if head.direction != "left":
            head.direction = "right"

    # key bindings
    screen.listen()
    screen.onkey(go_up, "w")
    screen.onkey(go_down, "s")
    screen.onkey(go_left, "a")
    screen.onkey(go_right, "d")
    screen.onkey(go_up, "Up")
    screen.onkey(go_down, "Down")
    screen.onkey(go_left, "Left")
    screen.onkey(go_right, "Right")

    # score display
    score = 0
    pen = turtle.Turtle()
    pen.hideturtle()
    pen.color("green")
    pen.penup()
    pen.goto(0, 260)

    def update_score():
        pen.clear()
        pen.write(f"Score: {score}", align="center", font=("Arial", 24, "bold"))

    update_score()

    # main game loop
    while True:
        screen.update()
        move()

        # check for collision with food
        if head.distance(food) < 20:
            x = random.randint(-14, 14) * 20
            y = random.randint(-14, 14) * 20
            food.goto(x, y)

            # add a segment
            new_segment = turtle.Turtle()
            new_segment.shape("square")
            new_segment.color("green")
            new_segment.penup()
            segments.append(new_segment)

            # increase score
            score += 1
            update_score()

            # spawn additional food if needed
            if len(segments) >= apple_count:
                apple_count += 1

            # speed up game
            snake_speed = snake_speed - 0.000025

        # check for collision with walls
        if abs(head.xcor()) > border_size // 2 or abs(head.ycor()) > border_size // 2:
            head.goto(0, 0)
            head.direction = "stop"
            score = 0
            update_score()
            for segment in segments:
                segment.goto(1000, 1000)
            segments.clear()

        # check for collision with itself
        for segment in segments:
            if segment.distance(head) < 20:
                head.goto(0, 0)
                head.direction = "stop"
                score = 0
                update_score()
                for segment in segments:
                    segment.goto(1000, 1000)
                segments.clear()

        time.sleep(snake_speed)

# Start the game
preGameScreen()
