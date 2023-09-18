import turtle
import numpy as np
import math as mt

# turtle.shape('turtle')
# turtle.forward(50)
# turtle.left(90)
# turtle.forward(50)
# turtle.left(90)
# turtle.forward(50)
# turtle.right(90)
# turtle.forward(50)
# turtle.right(90)
# turtle.forward(50)

#Задание 3 квадрат
# turtle.shape( 'circle')
# turtle.forward(100)
# turtle.left(90)
# turtle.forward(100)
# turtle.left(90)
# turtle.forward(100)
# turtle.left(90)
# turtle.forward(100)

#задание 4 
# turtle.shape( 'circle')
# for i in range(360):
#     turtle.forward(1)
#     turtle.left(1)

#задание 5
# turtle.shape('circle')
# lg=8
# x=0
# y=0
# for i in range(10):
#     turtle.penup()
#     turtle.goto(x,y)
#     turtle.pendown()
#     for i in range(4):
#         turtle.forward(lg)
#         turtle.left(90)
#     lg+=8
#     x+=-4
#     y+=-4

#задание 6 Паук
# n= int(input())
# turtle.shape('circle')
# for i in range(n):
#     turtle.goto(0,0)
#     turtle.left(360/n)
#     turtle.forward(100)
#     turtle.stamp()

#my best child
# turtle.shape('circle')
# n=3
# c=100
# while True:
#     turtle.forward(n)
#     turtle.left(c)
#     n+=-2

#задание 8 квадратная спираль
# turtle.shape('circle')
# n=10
# c=100
# while True:
#     for i in range(2):
#         for i in range(2):
#             turtle.forward(n)
#             turtle.left(90)
#         n+=4    


# задание 9 многоугольник
# def mg(n):
#     # r=20/2*(np.sin(360/(2*n))- считает отрицательный
#     r= 40/(2*(np.sin((2*np.pi)/(2*n))))
#     turtle.shape('circle')
#     turtle.penup()
#     turtle.goto(0,-r)
#     turtle.pendown()
#     for i in range(n):
#          turtle.left(360/n)
#          turtle.forward(40)

# c=10
# n=3
# for i in range(c):
#     mg(n)
#     n+=1

#задание 10 цветок

# def cir(n):
#     turtle.shape('circle')
#     turtle.left(360/n)
#     for i in range(180):
#         turtle.forward(1)
#         turtle.left(2)

# n=5
# for i in range(n):
#     cir(n)
    
#задание 11 летающее масло
# def cir(n):
#      turtle.shape('circle')
#      for i in range(180):
#          turtle.forward(n)
#          turtle.left(2)
#      for i in range(180):
#          turtle.forward(n)
#          turtle.right(2)
        
        
# n=0.5
# while True:
#      cir(n)
#      n+=0.1

# задание 14 звезда...
# n=11
# m=5
# turtle.shape('circle')
# for i in range(n):
#     turtle.forward(100)
#     turtle.left(180-(180/n))
# turtle.penup()
# turtle.goto(100,0)
# turtle.pendown()
# for i in range(m):
#     turtle.forward(100)
#     turtle.left(180-(180/m))

# задание 7 спиралька
# turtle.shape('circle')
# for i in range(3000):
#     turtle.forward(i*0.01)
#     turtle.left(3)

# задание 12 пружинка
# turtle.shape('circle')
# turtle.left(90)
# x = 1
# while x <= 6:
#     turtle.circle(45, 180, 50)
#     turtle.circle(7, 180, 50)
#     x += 1

# задание 13 smile.jpeg
#body
# turtle.shape('circle')
# turtle.begin_fill()
# turtle.width(7)
# turtle.circle(100)
# turtle.color('red')
# turtle.end_fill()

# # eyes
# y=50
# for i in range(2):
#     turtle.penup()
#     turtle.goto(y,120)
#     turtle.pendown()
#     turtle.begin_fill()
#     turtle.width(4)
#     turtle.circle(20)
#     turtle.color('white')
#     turtle.end_fill()
#     y=-y

# x=50
# turtle.color('black')
# for i in range(2):
#     turtle.penup()
#     turtle.goto(x,130)
#     turtle.pendown()
#     turtle.begin_fill()
#     turtle.width(4)
#     turtle.circle(10)
#     turtle.end_fill()
#     x=-60
    
# #ротик
# turtle.penup()
# turtle.goto(-45,77)
# turtle.right (90)
# turtle.pendown()
# turtle.width(7)
# turtle.circle(50,180)





    

    
    
    

