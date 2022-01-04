# -*- coding: utf-8 -*-

import pygame

# import snakeElements as cp

from snakeElements import cuerpo as cp
from snakeElements import apple as ap


len_initial =  10 


def refresh(ventana):
    ventana.fill((0,0,0))
    footnote(ventana)
    comida.dibujar()

    for i in range(len(serpiente)):
        serpiente[i].dibujar()
        
        
def seguir_cabeza():
    for i in range(len(serpiente)-1):
        serpiente[len(serpiente)-i-1].x = serpiente[len(serpiente)-i-2].x 
        serpiente[len(serpiente)-i-1].y = serpiente[len(serpiente)-i-2].y 

def muerte():
    cabeza = serpiente[0]

    retorno = False
    check = True
    i =1
    while check:
        if i+1 > len(serpiente):
            check = False
        elif serpiente[i].x == cabeza.x and serpiente[i].y == cabeza.y:
            check= False
            retorno = True
        else:
            i+=1
    return retorno 

def game_over(ventana,i):
    ventana.fill((0,0,0))
    footnote(ventana,2)
    comida.dibujar()

    
    if i > len(serpiente):
        i = len(serpiente)
    for i in range(0,i):
        serpiente[i].dibujar(2)
    for i in range(i,len(serpiente)):
        serpiente[i].dibujar()

def restart():
    
    main()
    
    
def msg_texto(ventana,msg,color,colorfill,x,y):
    font = pygame.font.Font('freesansbold.ttf', 12)
    text = font.render(msg, True, color, colorfill)
    textRect = text.get_rect()
    textRect.center = (x, y)
    ventana.blit(text, textRect)
    
def footnote(ventana,color=1):
    black=(0,0,0)
    grey=(200,200,200)
    red= (255,0,0)
    if color == 1:
        color_barra=(0,255,255)
    else:
        color_barra=red
    pygame.draw.rect(ventana,color_barra,(0,410,400,10))
    pygame.draw.rect(ventana,grey,(0,420,400,90))
    
    
   
    nivel = "Nivel "+ str(level)
    msg_texto(ventana,nivel,black,grey,200,430)
    puntaje = "Puntaje " + str(puntos)
    msg_texto(ventana,puntaje,black,grey,200,450)
   
    if color != 1:
      restartmsj= "Presionar tecla N para Nuevo Juego"  
      msg_texto(ventana,restartmsj,red,grey,200,470)
    


def margin_check():
    if serpiente[0].x >= 400:
            serpiente[0].x=0
    if serpiente[0].x <0 :
        serpiente[0].x=390
    if serpiente[0].y >= 400:
        serpiente[0].y=0
    if serpiente[0].y < 0:
            serpiente[0].y=390
            
def control_lvl():
    global level , change_lvl
    change_lvl = change_lvl -1
    if change_lvl == 0:
        level += 1
        change_lvl=5
    

def main():
    global serpiente, comida, puntos, level , change_lvl
    puntos=0
    level=1 
    change_lvl = 5
  
    pygame.init()
           
               
    
    ventana = pygame.display.set_mode((400,500))
    ventana.fill((0,0,0))
   
    pygame.display.set_caption('la snake de python ')
    comida=ap(ventana)
    
    serpiente= [cp(ventana)]
    
#    len_initial =  10 
    for i in range(len_initial):
        serpiente.append(cp(ventana))

    
    
    
    
    run = True
    
    while run :
        for event in pygame.event.get():
            if event.type== pygame.QUIT:
                run =False
            if event.type == pygame.KEYDOWN:
                 if event.key == pygame.K_RIGHT:
                    serpiente[0].dir = 0
                 
                 if event.key == pygame.K_LEFT:
                    serpiente[0].dir = 1
                 
                 if event.key == pygame.K_UP:
                    serpiente[0].dir = 3
                    
                 if event.key == pygame.K_DOWN:
                    serpiente[0].dir = 2
        
        serpiente[0].mover_cuerpo()
        refresh(ventana)
        pygame.display.update()
        delay= 100 - ((level-1) *10 ) 
        pygame.time.delay(delay)
    
        
        comida.time -= 1
        
        # if comida.time==0:
        #       comida.new_apple()
        if muerte():
            run= False



        if serpiente[0].x ==comida.x and serpiente[0].y ==comida.y:
            comida.new_apple()
            puntos +=10
            control_lvl()
            serpiente.append(cp(ventana))
        
        margin_check()
        
                     
        seguir_cabeza()
    run = True
    i =0
    
    while run :
        for event in pygame.event.get():
            if event.type== pygame.QUIT:
                run =False
            if event.type == pygame.KEYDOWN:
                 if event.key == pygame.K_n :
                     run = False
                     restart()
        
 
       
               

        game_over(ventana,i)
        i+=1
        pygame.display.update()
        pygame.time.delay(200)
      

if __name__ == '__main__':
    main()
    pygame.quit()
    
