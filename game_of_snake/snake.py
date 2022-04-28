from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-15, 0), (-30, 0)]
MOVE_DISTANCE = 15
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
WIDTH_COEFF = 0.75
LENGTH_COEFF = 0.75


class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):  # making the snake to move in reverse order so that last segment takes the place of the previous one
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def add_segment(self, position):
        new_turtle = Turtle(shape='square')
        new_turtle.shapesize(stretch_len=WIDTH_COEFF, stretch_wid=LENGTH_COEFF)
        new_turtle.penup()
        new_turtle.goto(position)
        new_turtle.color('white')
        self.segments.append(new_turtle)

    def extend(self):
        # add a new segment to the snake
        self.add_segment(self.segments[-1].position())

    def reset_snake(self):
        for seg in self.segments: #sending the old snake somewhere off screen so it is not visible
            seg.goto(1000, 1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]


