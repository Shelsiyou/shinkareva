#turtle2
#задание 1
import turtle as tp
import numpy as np
import math as mt
from random import *

# tp.shape('circle')
# while True:
#     tp.forward((random())*30)
#     a=randint(1,2)
#     if a==1:
#         tp.left(random()*360)
#     elif a==2:
#         tp.right(random()*360)
    
#задание 2
# tp.shape('circle')

# poch=[1,4,1,7,0,0]
# n=len(poch)
# def cif(n):
#     lg=0
#     x=0
#     y=0
#     for i in range(n):
#         if poch[lg] == 1:
#             tp.penup()
#             tp.goto(x,(y+21))
#             tp.pendown()
#             tp.left(45)
#             tp.forward(29)
#             tp.right(135)
#             tp.forward(42)
#             tp.left(90)
#         elif poch[lg] == 4:
#             tp.penup()
#             tp.goto(x,(y+42))
#             tp.pendown()
#             tp.right(90)
#             tp.forward(21)
#             tp.left(90)
#             tp.forward(20)
#             tp.left(90)
#             tp.forward(21)
#             tp.left(180)
#             tp.forward(42)
#             tp.left(90)
#         elif poch[lg] == 7:
#             tp.penup()
#             tp.goto(x,(y+42))
#             tp.pendown()
#             tp.forward(20)
#             tp.right(135)
#             tp.forward(29)
#             tp.left(45)
#             tp.forward(21)
#             tp.left(90)
#         elif poch[lg] == 0:
#             tp.penup()
#             tp.goto(x,y)
#             tp.pendown()
#             tp.forward(20)
#             tp.backward(20)
#             tp.left(90)
#             tp.forward(42)
#             tp.right(90)
#             tp.forward(20)
#             tp.right(90)
#             tp.forward(42)
#             tp.left(90)
#         tp.penup()
#         x+=25
#         tp.goto(x,y)
#         tp.pendown()
#         lg+=1
# cif(n)

#задание файл

        
#задание 3
# tp.shape('circle')
# y=200
# x=0
# Vx=1
# Vy=2
# dt=1
# ay=-2
# while True:
#     if y<=-200:
#         Vy=-Vy
#     x+=Vx*dt
#     y+=Vy*dt-((ay*dt)**2)/2
#     Vy+=ay*dt
#     tp.goto(x,y)
    
# задание 4 газ
# tp.penup()
# tp.goto(200,200)
# tp.pendown()
# for i in range(4):
#     tp.right(90)
#     tp.forward(400)
# pool = [tp.Turtle(shape='circle') for i in range(20)]
# for unit in pool:
#     unit.penup()
#     unit.speed(100)
#     unit.goto(randint(-200, 200), randint(-200, 200))

# for i in range(1000):
#     for unit in pool:
#         tp.speed(100)
#         unit.forward((random())*10)
#         a=randint(1,2)
#         if a==1:
#             unit.left(random()*360)
#         elif a==2:
#             unit.right(random()*360)
        # не совсем понимаю как добавить условие на координаты, так как нет координат для каждой штуки
        
            


