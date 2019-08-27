# coding: utf-8

import turtle
import tkSimpleDialog
import math
import random

FI = 360 / 7
R = 50

def goto_xy(x,y):
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()

def draw_circle(r,color):
    turtle.fillcolor(color)
    turtle.begin_fill()
    turtle.circle(r)
    turtle.end_fill()

def new_List():
    turtle.clear()
    goto_xy(0, 0)
    turtle.circle(80)
    goto_xy(0, 160)
    draw_circle(5, "red")

    for i in range(0, 7):
        fi_r = FI * i * math.pi / 180.0
        goto_xy(math.sin(fi_r) * R, math.cos(fi_r) * R + 60)
        draw_circle(22, "white")



turtle.speed(0)

new_List()

answer = ''
Start = 0

while answer != 'n':
    answer = tkSimpleDialog.askstring('Будем играть в Русскую рулетку?',"y/n")

    if answer == 'y':

        if Start == 0:
            new_List()

			for i in range(Start, random.randrange(7,100)):
				fi_r = FI * i * math.pi / 180.0
				goto_xy(base_x + math.sin(fi_r) * R, base_y + math.cos(fi_r) * R + 60)
				draw_circle(22,"green")
				draw_circle(22,"white")
		
			goto_xy(base_x + math.sin(fi_r) * R, base_y + math.cos(fi_r) * R + 60)
			draw_circle(22, "green")
		
			Star = i % 7 
        
        if Start == 0:
            goto_xy(-150,250)
            turtle.write("БАХ!!! Проиграли!!!")



