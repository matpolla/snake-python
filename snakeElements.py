# -*- coding: utf-8 -*-

import pygame
import random


class cuerpo:
    def __init__(self, ventana):
        self.x=0
        self.y=0
        self.dir=0
        self.ventana = ventana
    
    
    def dibujar(self,color=1):
        if color == 1:
            color_cuerpo=(255,255,255)
        else:
            color_cuerpo=(255,0,0)
            
        pygame.draw.rect(self.ventana,color_cuerpo,(self.x,self.y,10,10))
        
    def mover_cuerpo(self):
        if self.dir==0:
            self.x +=10
        elif self.dir==1:
            self.x -=10
        elif self.dir==2:
            self.y +=10
        elif self.dir==3:
            self.y -=10
       
class apple:
    def __init__(self, ventana):
        self.x=random.randrange(40) * 10
        self.y=random.randrange(40) * 10
        self.time=30
        self.ventana = ventana
    
    
    def dibujar(self):
        pygame.draw.rect(self.ventana,(255,0,0),(self.x,self.y,10,10))
    
    def new_apple(self):
        self.x=random.randrange(40) * 10
        self.y=random.randrange(40) * 10
        self.time=30