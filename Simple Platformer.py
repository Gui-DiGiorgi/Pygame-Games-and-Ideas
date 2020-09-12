import pygame
import random
import time
import numpy
from pygametexting import pyg_text

back_color = (0,0,0)

clock = pygame.time.Clock()

clock_time = 60

grav = 50

pygame.init()

W = 1000
H = 600

win=pygame.display.set_mode((W,H))

pygame.display.set_caption("Platformer")

txt = pyg_text(20,(255,255,255),"comicsansms",Win=win)

class player(object):
    
    def __init__(self,x,y):
        self.width = 20
        self.height = 20
        self.x = x
        self.y = y
        self.x_vel = 5
        self.y_vel = 0
        self.jump_str = 15
        self.on_block = False
        self.color = (255,0,0)
        self.distance = 0
        self.time = time.time()
        
    def draw(self,window):
        pygame.draw.rect(win,self.color,(self.x,self.y,self.height,self.width))
    
    def right(self):
        self.distance+=self.x_vel
        


class block(object):
    
    def __init__(self,x,y,width):
    
        self.width = width
        self.height = 20
        self.x = x
        self.y = y
        self.color = (128,128,128)

    def draw(self,window):
        pygame.draw.rect(win,self.color,(self.x,self.y,self.width,self.height))
        

def start_restart():
    global p1, blocks
    init_x = 0
    init_y = random.randint(50,H-20)
    blocks = []
    blocks_n = round(W/150)
    for create in range(blocks_n):
        blocks.append(block(init_x,init_y,50))
        init_x+=150
        a=random.randint(1,2)
        if a==1 and init_y-150>10:
            init_y -= random.randint(50,150)
        else:
            init_y = random.randint(init_y,H-20)
#The player block is always going to be 3 (the 4th block)
    p1=player(blocks[3].x,(blocks[3].y-20))

run = True

b_distance = 0

start_restart()
        
while run:
    clock.tick(clock_time)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    win.fill(back_color)
    
    on_block = 0
    for b in blocks:
        if p1.y+p1.height>=b.y and p1.y+p1.height<b.y+b.height and p1.x+p1.width>=b.x and p1.x<=b.x+b.width:
            p1.y=b.y-p1.height
            on_block = 1
            
        elif p1.y+p1.height<b.y and p1.y+p1.height+p1.y_vel>b.y+b.height and\
        ((p1.x+p1.width>=b.x and p1.x<=b.x+b.width and not forward) or\
        (p1.x+p1.width+p1.x_vel>=b.x and p1.x+p1.x_vel<=b.x+b.width and forward)):
            p1.y=b.y-p1.height
            on_block = 1
            
        elif p1.y+p1.height>b.y and p1.y<b.y+b.height:
            if p1.x<b.x and p1.x+p1.width>b.x:
                p1.x = b.x - p1.width
            elif p1.x<b.x+b.width and p1.x+p1.width>b.x+b.width:
                p1.x = b.x+b.width
                
        if on_block == 1:
            break
            
    if on_block == 1:
        p1.on_block = True
        p1.y_vel = 0
    else:
        p1.on_block = False
    
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_ESCAPE]:
        run = False
        
    if keys[pygame.K_r]:
        pygame.time.delay(200)
        start_restart()
    
    if keys[pygame.K_RIGHT]:
        p1.right()
        for b in blocks:
            b.x-=p1.x_vel
        forward = True
    else:
        forward = False
        
    if keys[pygame.K_UP] and p1.on_block:
        p1.y_vel-=p1.jump_str
    
    if not p1.on_block:
        p1.y_vel += grav/60
    
    p1.y+=round(p1.y_vel)
    
    
    if blocks[-1].x <= W-150:
        a=random.randint(1,2)
        if a==1 and blocks[-1].y-150>10:
            new_y = blocks[-1].y - random.randint(50,150)
        else:
            new_y = random.randint(blocks[-1].y,H-20)
        blocks.append(block(blocks[-1].x+150,new_y,50))
        
    if blocks[0].x + blocks[0].width == 0:
        blocks.remove(blocks[0])
        
    for b in blocks:
        b.draw(win)

        
    p1.draw(win)
    
    if p1.y<W and round(time.time()-p1.time,1)<20:
        stats = "Distance: {} Time: {}s".format(p1.distance,round(time.time()-p1.time,1))
        game_on = True
    else: 
        if game_on:
            
            start_restart()
            game_on = False
    txt.screen_text_limitpos(stats,W-20,40)
    
    #x_on_block = (blocks[3].x+blocks[3].width)-p1.x
    #x_next_block = (blocks[4].x+blocks[4].width)-p1.x
    #y_next_block = blocks[4].y-(p1.y+p1.height)
    #
    #variables = "X On Block: {} X Next Block: {} Y Next Block: {} Y Vel: {}".format(x_on_block,x_next_block,y_next_block,round(p1.y_vel))
    #txt.screen_text_limitpos(variables,W-20,65)
    
    if b_distance<p1.distance:
        b_distance = p1.distance
    b_stats = "Best Distance: {}".format(b_distance)
    txt.screen_text_limitpos(b_stats,W-20,90)
    
    

    pygame.display.update()
    
pygame.quit()
