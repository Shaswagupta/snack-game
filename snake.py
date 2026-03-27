from  turtle import Turtle,Screen
SEGEMENT_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTENCE = 20
segment = []
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
class Snack :
    def __init__(self):
        self.segment = []
        self.create_snack()
        self.head = self.segment[0]
    def create_snack (self):
        for position in SEGEMENT_POSITION:
            self.addSegement(position)

    def  addSegement(self , position):
        segment_new = Turtle("square")
        segment_new.color("white")
        segment_new.penup()
        segment_new.goto(position)
        self.segment.append(segment_new)

    def extend (self):
        self.addSegement(self.segment[-1].position())

    def move(self):
        for seg_num in range(len(self.segment) - 1, 0, -1):
            new_x = self.segment[seg_num - 1].xcor()
            new_y = self.segment[seg_num - 1].ycor()
            self.segment[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTENCE)
    def up(self):
         if self.head.heading() != DOWN :
             self.head.setheading(UP)
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)








