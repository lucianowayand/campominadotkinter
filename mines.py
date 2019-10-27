from tkinter import *
from functools import partial
import random

class Coord:
    def __init__(self,x,y):
        self.x = x
        self.y = y

class Botao():
    def __init__(self, x, y, valor):
        self.coord = Coord(x,y)
        self.bt = Button(text=" ",width=3,command=partial(click,self.coord))
        self.valor = valor

def arrayToMatrix(size,i,j):
    return (size.y*i+j)

def click(coord):
    global bt, size
    if bt[arrayToMatrix(size,coord.x,coord.y)].bt['text']==" ":
        bt[arrayToMatrix(size,coord.x,coord.y)].bt['text']="F"
    elif bt[arrayToMatrix(size,coord.x,coord.y)].bt['text']=="F":
        bt[arrayToMatrix(size,coord.x,coord.y)].bt['text']=1
    else:
        bt[arrayToMatrix(size,coord.x,coord.y)].bt['text']=" "

    print(bt[arrayToMatrix(size,coord.x,coord.y)].valor)

size = Coord(10,10)

vetor = []

for i in range (size.x):
    for j in range (size.y):
        vetor.append(Coord(i,j))

main = Tk()
main.geometry("370x410")
main.title("Campo minado")
main.resizable(width=FALSE,height=FALSE)

bombs=[]
for i in range (len(vetor)):
    if i < 30:
        bombs.append("Bomb")
    else:
        bombs.append("")

random.shuffle(bombs)

bt=[]
for i in range (len(vetor)):
    bt.append(Botao(vetor[i].x,vetor[i].y,bombs[i]))
    bt[i].bt.config(text=bombs[i])
    bt[i].bt.place(x=((vetor[i].x)*35)+10,y=((vetor[i].y)*40)+10)


main.mainloop()
