# Funções necessárias
from tkinter import * #interface gráfica
from functools import partial #utilizada para passar parametros à função usada no botão
import random #para fazer o shuffle

def arrayToMatrix(size,i,j): #auxilia o uso de vetores que representam matrizes
    return (size.y*i+j)

def click(coord):
    global bt, size #referencia o botao e lê o size sem precisar de referencia

    c = 0 
    for i in range (3):
        for j in range (3):
            if bt[arrayToMatrix(size,(coord.x-1)+i,(coord.y-1)+j)].valor == "Bomb":
                c+=1 #contador de bombas

    if bt[arrayToMatrix(size,coord.x,coord.y)].bt['text']==" ":
        bt[arrayToMatrix(size,coord.x,coord.y)].bt['text']="F"

    elif bt[arrayToMatrix(size,coord.x,coord.y)].bt['text']=="F":
        bt[arrayToMatrix(size,coord.x,coord.y)].bt['text']= c
    
# Determinam-se classes utilizadas
class Coord:
    def __init__(self,x,y):
        self.x = x
        self.y = y

class Botao():
    def __init__(self, x, y, valor):
        self.coord = Coord(x,y) #posicao do botao
        self.bt = Button(text=" ",width=3,command=partial(click,self.coord))
        self.valor = valor

# Determina-se o tamanho do jogo
size = Coord(10,10)

# Armazenam-se as coordenadas de botão de modo a posicionalos posteriormente
vetor = []
for i in range (size.x):
    for j in range (size.y):
        vetor.append(Coord(i,j))

# Configurações de janela e inicio do loop
main = Tk()
main.geometry("370x410")
main.title("Campo minado")
main.resizable(width=FALSE,height=FALSE)

# Cria-se um vetor que armazena o numero de bombas de jogo, ele é depois embaralhado para randomizar as posições de cada bomba
bombs=[]
for i in range (len(vetor)):
    if i < 30:
        bombs.append("Bomb")
    else:
        bombs.append(" ")

random.shuffle(bombs)

# Colocam-se os botoes na tela com as informações passadas
bt=[]
for i in range (len(vetor)):
    bt.append(Botao(vetor[i].x,vetor[i].y,bombs[i]))
    bt[i].bt.config(text=bombs[i])
    bt[i].bt.place(x=((vetor[i].x)*35)+10,y=((vetor[i].y)*40)+10)


main.mainloop()
