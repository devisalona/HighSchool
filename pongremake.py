from functools import *
from itertools import *
from Tkinter import *
from string import *
from random import *
from Queue import *
from math import *
from time import *
from sys import *

def disk(x,y,r,kolor):
    return canvas.create_oval(x-r,y-r,x+r,y+r,width = 1,fill = kolor)
def key(evnt):
    temp = canvas.coords(obj1)
    mid = (temp[3]+temp[1])/2
    if mid-10 >= 0 and mid-10 <= 780:
         canvas.move(obj1,0,-14)
def keyP2(evnt):
    temp = canvas.coords(obj2)
    mid = (temp[3]+temp[1])/2
    if mid-10 >= 0 and mid-10 <= 780:
         canvas.move(obj2,0,-14)
def key2(evnt):
    temp = canvas.coords(obj1)
    mid = (temp[3]+temp[1])/2
    if mid+10 >= 0 and mid+10 <= 780:
         canvas.move(obj1,0,14) 
def key2P2(evnt):
    temp = canvas.coords(obj2)
    mid = (temp[3]+temp[1])/2
    if mid+10 >= 0 and mid+10 <= 780:
         canvas.move(obj2,0,14) 
def paddle(evnt):
    temp = canvas.coords(obj1)
    mid = (temp[3]+temp[1])/2
    if evnt.y >= 0 and evnt.y <= 780:
        if evnt.y > mid:
        	canvas.move(obj1,0,5)
	elif evnt.y <mid:
		canvas.move(obj1,0,-5)
def paddleP2(evnt):
    temp = canvas.coords(obj2)
    mid = (temp[3]+temp[1])/2
    if evnt.y >= 0 and evnt.y <= 780:
	if evnt.y > mid:
        	canvas.move(obj2,0,5)
	elif evnt.y <mid:
		canvas.move(obj2,0,-5)

def move():
    global xInc,yInc,countR,countL,canvas, counterR,counterL
    temp = canvas.coords(ball1)
    temp2 = canvas.coords(obj1)
    temp3 = canvas.coords(obj2)
    midy = (temp[3]+temp[1])/2
    midx = (temp[0]+temp[2])/2
        
    if  temp[0] > 1270 or temp[2] > 1270 :
        xInc = -xInc
        yInc = yInc
        canvas.move(ball1,xInc,yInc)
        counterR += 1
        canvas.itemconfigure(countR,text = str(counterR))
    if midy<temp2[3] and midy>temp2[1] and midx == (temp2[0]):
        xInc = -xInc
        yInc = yInc
        canvas.move(ball1,xInc,yInc)
    if midy<temp3[3] and midy>temp3[1] and midx == (temp3[0]):
        xInc = -xInc
        yInc = yInc
        canvas.move(ball1,xInc,yInc)
    if temp[2] <0:
        xInc = -xInc
        yInc = yInc
        canvas.move(ball1,xInc,yInc)
        counterL += 1
        canvas.itemconfigure(countL,text = str(counterL))

    elif temp[1] < 0 or temp[1] > 780 or temp[3] <0 or temp[3] > 780:
        xInc = xInc
        yInc = -yInc
        canvas.move(ball1,xInc,yInc)
    else:
        canvas.move(ball1,xInc,yInc)

    canvas.after(10,move)




root = Tk()
counterR = 0
counterL = 0
canvas = Canvas(root, width = 1270, height = 780, bg = 'black')
canvas.pack(expand = YES, fill = BOTH)
countR = canvas.create_text(500,250,text = str(counterR), fill= 'white',font = ('Helvetica',20))
countL = canvas.create_text(700,250,text = str(counterL), fill = 'white', font = ('Helvetica',20))
ball1 = disk(100,100,10,'red')
obj1 = canvas.create_line(80,10,80,80,width = 7, fill = 'green')
root.bind('<B1-Motion>',paddle)
#root.bind('<Up>',key)
#root.bind('<Down>',key2)
obj2 = canvas.create_line(1200,10,1200,80,width = 7, fill = 'green')
root.bind('<Up>',keyP2)
root.bind('<Down>',key2P2)
xInc = 2; yInc = 2

canvas.after(0,move)
root.mainloop()
