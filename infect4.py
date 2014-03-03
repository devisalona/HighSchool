from Tkinter import *
from random import *
from math import *
from time import *
import os
import sys

def setUpCanvas(root):
    global a
    root.title("Virus")
    canvas = Canvas(root,width = 1270, height = 780, bg = 'black')
    canvas.pack(expand = YES,fill = BOTH)
    return canvas
def createMatrix():
    global a
    for i in xrange(35):
        a.append([])
        for j in xrange(74):
            t = random()
            if t <=.25:
                a[i].append(0)
            else:
                a[i].append(1)
def printMatrix(canvas):
    global a
    ch = ''
    for r in xrange(35):
        for c in xrange(74):
                if a[r][c] == 1:
                    ch = 'X'
                    canvas.create_text(c*17+13,r*22+15,text = ch,fil= 'green', font = ('Helvetica',20,'bold'))
                elif a[r][c] == 0:
                    ch = ' '
                    canvas.create_text(c*17+13,r*22+15,text = ch,fil= 'green', font = ('Helvetica',20,'bold'))
                elif a[r][c] == 2:
                    ch = 'X'
                    canvas.create_text(c*17+13,r*22+15,text = ch,fil= 'red', font = ('Helvetica',20,'bold'))
    canvas.update()

def printCell(canvas,r,c):
    global a
    ch = ''
    if a[r][c] == 1:
        ch = 'X'
        canvas.create_text(c*17+13,r*22+15,text = ch,fil= 'green', font = ('Helvetica',20,'bold'))
    elif a[r][c] == 0:
        ch = ' '
        canvas.create_text(c*17+13,r*22+15,text = ch,fil= 'green', font = ('Helvetica',20,'bold'))
    elif a[r][c] == 2:
        ch = 'X'
        canvas.create_text(c*17+13,r*22+15,text = ch,fil= 'red', font = ('Helvetica',20,'bold'))
    canvas.update()
    sleep(0.02)
                
def infect(srow,scol):
    global a
    global canvas
    ilist = [(srow,scol)]
    i = 0
    while i < len(ilist):
        r,c = ilist[i]
        #print ilist
        a[r][c] = 2
        printCell(canvas,r,c)
        if r+1 <35 and a[r+1][c] == 1:
            a[r+1][c]=-1
            ilist.append((r+1,c))           
        if r-1 >= 0 and a[r-1][c] == 1:
            a[r-1][c] = -1
            ilist.append((r-1,c))
        if c+1 < 74 and a[r][c+1] == 1:
            a[r][c+1] = -1
            ilist.append((r,c+1))
        if c-1 >=0 and a[r][c-1] == 1:
            a[r][c-1] = -1
            ilist.append((r,c-1))
        i += 1
    return 

        
sys.setrecursionlimit(500000)
a = []
root = Tk()
canvas = setUpCanvas(root)
createMatrix()
printMatrix(canvas)
infect(16,35)
printMatrix(canvas)
root.mainloop()
