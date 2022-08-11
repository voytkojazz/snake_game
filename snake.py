from turtle import Turtle



MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    x = 0 
    y = 0
    def __init__(self):
        self.snakes = []
        self.create_snake()
        self.head = self.snakes[0]

    def create_snake(self):      
        for i in range(3):
            self.add_snake((Snake.x, Snake.y))
            Snake.x -= 20
    
    def add_snake(self, position):
        snake = Turtle('square')
        snake.color('white')
        snake.penup()
        snake.goto(position[0], position[1])
        self.snakes.append(snake)

    def extend(self):
        self.add_snake(self.snakes[-1].position())

    def move(self):
        for i in range(len(self.snakes)-1, 0, -1):
            new_x = self.snakes[i-1].xcor()
            new_y = self.snakes[i-1].ycor()
            self.snakes[i].goto(new_x, new_y)
        self.snakes[0].forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
    
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading != LEFT:
            self.head.setheading(RIGHT)

    def __repr__(self) -> list:
        return self.snakes

    def __len__(self):
        return len(self.snakes)  