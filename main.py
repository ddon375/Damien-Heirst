# import colorgram
#
# colours = colorgram.extract('hirst.jpg', 20)
#
# color_list = []
# for i in colours:
#     r = i.rgb.r
#     g = i.rgb.g
#     b = i.rgb.b
#     rgb_colour = (r, g, b)
#     color_list.append(rgb_colour)
# print(color_list)

from turtle import Turtle, Screen
import random
turtle.colormode(255)
damien_colours = [(141, 165, 183), (24, 117, 173), (202, 140, 166), (238, 212, 62), (221, 158, 90), (123, 73, 97),
                  (138, 20, 38), (191, 173, 20), (21, 140, 58), (68, 27, 33), (191, 70, 32), (224, 171, 197),
                  (54, 32, 29), (25, 170, 185), (118, 188, 142), (3, 109, 61)]

my_turtle = Turtle()
my_screen = Screen()
my_turtle.penup()
my_turtle.hideturtle()
my_turtle.speed("fastest")


def choose_color():
    first_choice = random.choice(damien_colours)
    r = first_choice[0]
    g = first_choice[1]
    b = first_choice[0]
    return r,g,b


def draw_spot(x_cor, y_cor):
    my_turtle.setpos(x_cor, y_cor)
    for i in range(10):
        my_turtle.dot(20, choose_color())
        my_turtle.penup()
        my_turtle.fd(50)
        my_turtle.pendown()


x_cor = -270
y_cor = -250
count = 0
karen = True
while karen:
    draw_spot(x_cor, y_cor)
    my_turtle.penup()
    y_cor += 50
    count += 1
    if count == 10:
        karen = False

my_screen.exitonclick()