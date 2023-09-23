# TODO Extract Colors from a specific image
# from colorgram import colorgram
# image_colors = colorgram.extract('the hirst Image.jpg', 30)#this will give me tuple that containg r gand b colors
# all_colors = []#creating an empty list to add all the colors in it
# for i in range(len(image_colors)):#the loop will iterate with the number of colors is extracted from image_colors
#     colors = image_colors[i]#it will iterate on each index of the color for 0 till end #https://pypi.org/project/colorgram.py/
#     r = colors.rgb.r#extracting each color alone and put it in new tuple (new_color)
#     b = colors.rgb.b
#     g = colors.rgb.g
#     new_colors =  (r, g, b) # creating a tuple
#     all_colors.append(new_colors)
# print(all_colors, '\n',  len(all_colors))
import turtle
# TODO After extracting the colors and puttingit a list we need to draw the dots
from turtle import Turtle,Screen
import  random
timmy = Turtle()
timmy.speed(0)
turtle.colormode(255)
color_list = [ (132, 166, 205), (221, 148, 106), (32, 42, 61), (199, 135, 148), (166, 58, 48), (141, 184, 162), (39, 105, 157), (237, 212, 90), (150, 59, 66), (216, 82, 71), (168, 29, 33), (235, 165, 157), (51, 111, 90), (35, 61, 55), (156, 33, 31), (17, 97, 71), (52, 44, 49), (230, 161, 166), (170, 188, 221), (57, 51, 48), (184, 103, 113), (32, 60, 109), (105, 126, 159), (175, 200, 188), (34, 151, 210), (65, 66, 56)]
number_of_dots = 100
timmy.setheading(225) # to know why 225 watch Play 174. The Hirst Painting Project Part 2 - Drawing the Dots
timmy.penup()
timmy.forward(300)
timmy.setheading(0)

for  count in range(1, number_of_dots+1):#here i add 1 in order to loop for 100 which is the number of dots needed
    timmy.dot(20,random.choice(color_list))#drawing dot with radius 20
    timmy.penup()
    timmy.forward(50)
    timmy.pendown()
    if count % 10 == 0:#since we need to draw in a dimention 10 so when the modulus remainder becom 0 the turtle will start drawing the next line
        timmy.setheading(90)
        timmy.penup()
        timmy.forward(50)
        timmy.setheading(180)
        timmy.forward(500)
        timmy.setheading(0)
timmy.hideturtle()




screen = Screen()
screen.exitonclick()