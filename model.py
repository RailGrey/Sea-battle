import pygame
import random
from objects import *

def modul(mod):
    if mod >= 0:
        return  mod
    else:
        return -mod
    
def sign(sig):#int
    if sig==0:
        return 0
    else:
        return int(sig/modul(sig))

intXboard=10
intYboard=10
MaxPalubn=4
def placement_of_ship(grid):
    ###!!! тут номерация с 0, но переводится в итоге с 1 как и требуется в других частях кода
    ShipsPositions=[]
    Positions_list=[(i * 10 ** len(str(max(intXboard, intYboard) - 1)) + j) for i in range(intXboard) for j in range(intYboard)]
    for m in range(MaxPalubn-1,-1,-1):
        n=0
        #Spawn (m+1)-x
        while n<=MaxPalubn-1-m:
            position=random.randint(0,len(Positions_list)-1)
    
            x=Positions_list[position]//(10**len(str(max(intXboard,intYboard)-1)))
            y=Positions_list[position]-10**len(str(max(intXboard,intYboard)-1))*x
    
            popit=0
            while popit == 0:
                rot1 = random.randint(1, 4)                     #Change rotation 1-up,2-right,3-down,4-left
                rot2 = random.randint(0, 1)
                rotY = int((1 - (-1) ** rot1) * (0.5 - rot2))
                rotX = int((1 - (-1) ** (rot1 - 1)) * (0.5 - rot2))
                popit = 1
                if 0 <= (x + m * rotX) <= intXboard - 1 and 0 <= (y + m * rotY) <= intYboard - 1:

                    try:
                        Positions_list.index((x+m*rotX)*(10**len(str(max(intXboard,intYboard)-1)))+(y+m*rotY))
                    except ValueError:
                        popit=0
                        #print("исключения есть")
                    else:
                        popit=1
                        #print("исключений нет")

                else:
                    popit=0
                    #print("исключения есть")


            Yaround=-1-m*(1-sign(rotY+0.5))//2
            Xaround=-1-m*(1-sign(rotX+0.5))//2


            Del_list=[-1 for i in range(3*(3+m))]
            i = 0
            while Xaround<=1+(1+(m-1)*modul(rotX))*(1+sign(rotX))//2:               #Что удаляем из возможных позиций
                    while Yaround<=1+(1+(m-1)*modul(rotY))*(1+sign(rotY))//2 and i<=3*(3+m)-1:
                        #print(x+Xaround,y+Yaround)
                        if 0<=x+Xaround<=intXboard-1 and 0<=y+Yaround<=intYboard-1:
                            Del_list[i]=(x+Xaround)*(10**len(str(max(intXboard,intYboard)-1)))+y+Yaround
                            Yaround+=1
                            i+=1
                        else:
                            Del_list[i]=-1
                            Yaround+=1
                            i += 1
                    Xaround+=1
                    Yaround=-1-m*(1-sign(rotY+0.5))//2
       
            Yaround=-m*(1-sign(rotY+0.5))//2
            Xaround=-m*(1-sign(rotX+0.5))//2
            i = 0
            S=[]
            while Xaround<=(1+(m-1)*modul(rotX))*(1+sign(rotX))//2:               #Что добавляем в позиции вражеских кораблей
                while Yaround<=(1+(m-1)*modul(rotY))*(1+sign(rotY))//2:
                    S+=[(x+Xaround+1,y+Yaround+1)]
                    
                    Yaround+=1
                Xaround+=1
                Yaround=-m*(1-sign(rotY+0.5))//2
          
 
            ShipsPositions.append(Ship(grid,S))
            i=0
            while i<=(len(Del_list)-1):
                if Del_list[i]!=-1:
                    try:
                        Positions_list.remove(int(Del_list[i]))
                        i+=1
                    except ValueError:i+=1
                else: i+=1
            n+=1
    #end of Spawn (m+1)-x
    #popitshipplacement=1 
    grid.ships = ShipsPositions
    
    
    
    