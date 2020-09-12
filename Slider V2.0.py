# A new version of the slider class, that makes it possible to hold ans drag the slider easier, click where the slider goes right away,
# and press the up and down buttom for a slower slider manipulation. the pygtxt and its font addition makes it possible for the buttoms to
# appear as they should.

import pygame
from pygametexting import pyg_text

pygtxt=pyg_text(20,(255,255,255),"msmincho",wind)

class slider():
    def __init__(self, x, y, width, height, size):
        
        slider.g_selected = False
        
#         Buttom config:
        self.size = size
    
#         Slider config
        self.width = width
        self.height = height
        self.s_x = x
        self.s_y = y
        self.color = (200,200,200)
#         Block config
        self.selected = False
        self.clicked = False
        self.block = width
        self.x = x
        self.y = y
        self.block_color = (100,100,100)
        
    def click(self,mouse_x,mouse_y,mouse_p):
        
        if mouse_p and not slider.g_selected:
            if self.s_x<=mouse_x<=self.s_x+self.width and self.s_y<=mouse_y<=self.s_y+self.height:
                self.selected = True
                slider.g_selected = True
                
        elif not mouse_p:
            self.selected = False
            slider.g_selected = False
            
        if pygtxt.screen_button_initpos("▲", self.s_x, self.s_y - self.size):
            
            self.clicked = True
            self.y -= 1
            
        elif pygtxt.screen_button_initpos("▼", self.s_x, self.s_y + self.height):
            
            self.clicked = True
            self.y += 1
            
        else:
            
            self.clicked = False
            
    def move(self, mouse_x, mouse_y):
        
        if self.selected:
        
            self.y = mouse_y - self.block//2
            
        if self.selected or self.clicked:

            if self.y < self.s_y:
                self.y = self.s_y

            if self.y > self.s_y + self.height - self.block:
                self.y = self.s_y + self.height - self.block

    def draw(self,window):
        pygame.draw.rect(window,self.color,(self.s_x,self.s_y,self.width,self.height))
        pygame.draw.rect(window,self.block_color,(self.x,self.y,self.block,self.block))
