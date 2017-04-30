# IMPORTED MODULES

import turtle
from settings import *
import time
import sched

class SnakeGameIPX:
    """
        Class to handle the entire game.
    """
    def __init__(self):
        """
            Constructor
        """

        self.Window = turtle.Screen()
        self.__init_window__()

        self.Tails = [None] * 100
        self.TailSegments = 0

        self.Snake = turtle.Turtle()
        self.__init_snake__()

        self.Scheduler = sched.scheduler(time.time, time.sleep)

        self.test_counter = 0

        turtle.mainloop()

    def timed_event(self):
        self.snake_forward()
        self.Window.ontimer(self.timed_event, 200)

    def __init_snake__(self):
        """
            Init snake
        """
        self.Snake.color('pink')

        self.Snake.penup()
        self.Snake.setposition(INIT_SNAKE_POS_X, INIT_SNAKE_POS_Y)
        self.Snake.setheading(RIGHT)
        self.Snake.shape(SNAKE_HEAD_SHAPE_RIGHT)
        self.Snake.speed(0)
        self.__init_tail__(8)

        turtle.listen()
        turtle.onkey(self.set_snake_direction_left, "Left")
        turtle.onkey(self.set_snake_direction_right, "Right")
        turtle.onkey(self.set_snake_direction_up, "Up")
        turtle.onkey(self.set_snake_direction_down, "Down")

    def __init_tail__(self, number_of_tail_segment):
        """
            Add body segments to the snake
        """
        for i in range(number_of_tail_segment):
            self.Tails[i] = turtle.Turtle()
            self.Tails[i].shape(SNAKE_BODY_SEGMENT_SHAPE)
            self.Tails[i].penup()
            self.Tails[i].speed(0)
            self.Tails[i].setposition(INIT_SNAKE_POS_X - (SNAKE_FORWARD_DISTANCE * (i + 1)), INIT_SNAKE_POS_Y)
            self.Tails[i].setheading(RIGHT)
            self.TailSegments += 1

    def __init_window__(self):
        """
            Initiate game screen.
        """
        self.Window.bgcolor(SCREEN_BACKGROUND_COLOR)
        self.Window.title(SCREEN_TITLE)
        # full screen
        self.Window.setup(width=1.0, height=1.0)
        self.__draw_borders__()
        self.__register_shapes__()
        self.Window.ontimer(self.timed_event, 2000)

    def set_snake_direction_left(self):
        self.set_snake_direction(LEFT)
    def set_snake_direction_right(self):
        self.set_snake_direction(RIGHT)
    def set_snake_direction_up(self):
        self.set_snake_direction(UP)
    def set_snake_direction_down(self):
        self.set_snake_direction(DOWN)

    def set_snake_direction(self, direction):
        """
            Set direction of snake
        """
        # print("Function set_snake_direction called!")
        self.Snake.setheading(direction)

        if direction == LEFT:
            self.Snake.shape(SNAKE_HEAD_SHAPE_LEFT)
            return
        if direction == RIGHT:
            self.Snake.shape(SNAKE_HEAD_SHAPE_RIGHT)
            return
        if direction == UP:
            self.Snake.shape(SNAKE_HEAD_SHAPE_UP)
            return
        if direction == DOWN:
            self.Snake.shape(SNAKE_HEAD_SHAPE_DOWN)
            return

    def __register_shapes__(self):
        """
            Register images used in game
        """
        self.Window.register_shape(SNAKE_HEAD_SHAPE_UP)
        self.Window.register_shape(SNAKE_HEAD_SHAPE_DOWN)
        self.Window.register_shape(SNAKE_HEAD_SHAPE_RIGHT)
        self.Window.register_shape(SNAKE_HEAD_SHAPE_LEFT)
        self.Window.register_shape(SNAKE_BODY_SEGMENT_SHAPE)

    def __draw_borders__(self):
        """
            Draw borders for actuall game and for score panel
        """
        self.__draw_game_borders__()
        self.__draw_score_borders__()

    def __draw_game_borders__(self):
        """
            Draw the borders for game
        """

        # Draw game border

        # created border turtle
        border_pen = turtle.Turtle()
        # set it's speed
        border_pen.speed(BORDER_DRAWING_SPEED)
        # set it's color
        border_pen.color(BORDER_COLOR)
        # set it's width
        border_pen.pensize(BORDER_WIDTH)
        # disable drawing
        border_pen.penup()
        # set it's position
        border_pen.setposition(INIT_GAME_BORDER_POS_X, INIT_GAME_BORDER_POS_Y)
        # enable drawing
        border_pen.pendown()

        # draw the border
        border_pen.forward(GAME_BORDER_LENGHT)
        border_pen.left(90)
        border_pen.forward(GAME_BORDER_HEIGHT)
        border_pen.left(90)
        border_pen.forward(GAME_BORDER_LENGHT)
        border_pen.left(90)
        border_pen.forward(GAME_BORDER_HEIGHT)
        border_pen.left(90)

        # hide pen
        border_pen.hideturtle()

    def __draw_score_borders__(self):
        """
            Draw the borders for score panel
        """
        # Draw score border

        # created border turtle
        border_pen = turtle.Turtle()
        # set it's speed
        border_pen.speed(BORDER_DRAWING_SPEED)
        # set it's color
        border_pen.color(BORDER_COLOR)
        # set it's width
        border_pen.pensize(BORDER_WIDTH)
        # disable drawing
        border_pen.penup()
        # set it's position
        border_pen.setposition(INIT_SCORE_BORDER_POS_X, INIT_SCORE_BORDER_POS_Y)
        # enable drawing
        border_pen.pendown()

        # draw the border
        border_pen.forward(SCORE_BORDER_LENGHT)
        border_pen.left(90)
        border_pen.forward(SCORE_BORDER_HEIGHT)
        border_pen.left(90)
        border_pen.forward(SCORE_BORDER_LENGHT)
        border_pen.left(90)
        border_pen.forward(SCORE_BORDER_HEIGHT)
        border_pen.left(90)

        # hide pen
        border_pen.hideturtle()

    def snake_forward(self):

        x_list = []
        y_list = []

        x_list.append(self.Snake.xcor())
        y_list.append(self.Snake.ycor())

        self.Snake.forward(SNAKE_FORWARD_DISTANCE)

        for index in range(self.TailSegments):
            x_list.append(self.Tails[index].xcor())
            y_list.append(self.Tails[index].ycor())


        for index in range(self.TailSegments):
            self.Tails[index].setposition(x_list[index], y_list[index])

def test():
    x = SnakeGameIPX()

if __name__ == '__main__':
    test()
