import tkinter as tk
from random import randint
from time import sleep

def rd_color():
    rgb = hex(randint(0,255**3))[2:]
    while len(rgb) < 6:
        rgb += "0"
    return "#"+rgb


############################
LARGEUR, HAUTEUR = 1000, 600
NBR_POINTS = 10
RAYON_POINT = 4
MOVING_RANGE = 2
############################

root = tk.Tk()
root.geometry(f"{LARGEUR}x{HAUTEUR}")
canvas = tk.Canvas(root,background="black",width=LARGEUR-5,height=HAUTEUR-5)

canvas.grid()

points_list = []
for i in range(NBR_POINTS):
    x,y = randint(10,LARGEUR-10), randint(10,HAUTEUR-10)
    color = rd_color()
    point = canvas.create_oval(x+RAYON_POINT,y+RAYON_POINT,x-RAYON_POINT,y-RAYON_POINT,fill=color)
    points_list.append([point, randint(-MOVING_RANGE,MOVING_RANGE), randint(-MOVING_RANGE,MOVING_RANGE)])

GUI = True
while GUI:
    for indice, (point, x_mv, y_mv) in enumerate(points_list):
        x0,y0,_,_ = canvas.coords(point)
        x0 += x_mv-1
        y0 += y_mv-1
        if not(0<x0<LARGEUR):
            points_list[indice][1] = -points_list[indice][1]
        if not(0<y0<HAUTEUR):
            points_list[indice][2] = -points_list[indice][2]
        canvas.moveto(point,str(x0),str(y0))
    canvas.update()
    sleep(0.01)

###############