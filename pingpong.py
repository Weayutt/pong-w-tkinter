from tkinter import *
import math

def animation():
    global canvas; global rect
    global dx; global dy
    width = int(canvas.cget('width'))
    height = int(canvas.cget('height'))
    x1, y1, x2, y2 = canvas.coords(ball)
    bounce()
    if x2 > width or x1 < 0: 
        dx = - dx
    if y2 > height or y1 < 0:
        dy = - dy
    canvas.move(ball, dx, dy)
    canvas.after(10, animation)

def bounce():
    bx1, by1, bx2, by2 = canvas.coords(ball)
    px1, py1, px2, py2 = canvas.coords(paddle)
    global dy
    bx, by = 0,0
    L, R = int(px1), int(px2)
    Y1, Y2 = 0,0

    if dy == 1:                       #if ball is descending, range being checked it set to slightly above paddle
        bx, by = (bx1+14), (by2)
        Y1, Y2 = 215, 220
    if dy == -1:
        bx, by = (bx1+14), (by1)     #if ball is descending, range being checked is set to slightly below paddle
        Y1, Y2, = 220, 225

    if by in range(Y1, Y2):  #if ball is near paddle, check distance between ball and paddle edges
        for val in range(L, R):
            if abs(val - bx) == 0:
                dy = dy *-1


def left(event):
    global px1, py1, px2, py2
    x = -10
    y = 0
    canvas.move(paddle, x, y)
    px1, py1, px2, py2 = canvas.coords(paddle)


def right(event):
    global px1, py1, px2, py2
    x = 10
    y = 0
    canvas.move(paddle, x, y)
    px1, py1, px2, py2 = canvas.coords(paddle)


# main program
gui = Tk() 
canvas = Canvas(gui)
gui.title("Use left and right arrow keys !")
ball = canvas.create_oval(100,100,125,125,fill="red")
paddle = canvas.create_rectangle(50,220, 150, 230, fill= "blue")


bx1, by1, bx2, by2 = canvas.coords(ball)
px1, py1, px2, py2 = canvas.coords(paddle)

gui.bind("<Left>", left)
gui.bind("<Right>", right)

canvas.pack()
dx, dy = 1, 1
animation()
mainloop() 