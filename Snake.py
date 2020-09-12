# Snake Game
import pygame
import random
import copy
from pygametexting import pyg_text

back_color = (0,0,0)

clock = pygame.time.Clock()

clock_time = 15

size_all = 20

snake_color = (0,255,0)

fruit_color = (255,0,0)

game_over = False

game_start = False

pygame.init()

W = 500
H = 500

win=pygame.display.set_mode((W,H))

pygame.display.set_caption("Snake")

txt = pyg_text(20,(255,255,255),"comicsansms",Win=win)

class snake_head(object):
    
    def __init__(self,size,color):
        self.size = size
        self.color = color
        
    def new(self):
        self.x = self.size*((W/2)//self.size)
        self.y = self.size*((H/2)//self.size)
        
    def up(self):
        self.y -= self.size
        
    def down(self):
        self.y += self.size
        
    def left(self):
        self.x -= self.size
        
    def right(self):
        self.x += self.size
        
    def draw(self,window):
        pygame.draw.rect(win,self.color,(self.x,self.y,self.size,self.size))
        
class snake_body(object):
    
    def __init__(self,size,color,x,y):
        self.size = size
        self.x = x
        self.y = y
        self.color = color
        
    def draw(self,window):
        pygame.draw.rect(win,self.color,(self.x,self.y,self.size,self.size))
        
class fruit(object):
    def __init__(self,size,color):
        self.size = size
        self.color = color
        
    def new(self):
        self.x = self.size*(random.randint(0,W-self.size)//self.size)
        self.y = self.size*(random.randint(0,H-self.size)//self.size)
        
    def draw(self,window):
        pygame.draw.rect(win,self.color,(self.x,self.y,self.size,self.size))

p1 = snake_head(size_all,snake_color)

apple = fruit(size_all,fruit_color)

modes = [p1.up,p1.down,p1.left,p1.right]

loser_move = [[0,1],[1,0],[2,3],[3,2]]

n_all_x = (W-size_all)//size_all
n_all_y = (H-size_all)//size_all

all_spaces = []

for x,y in zip(range(n_all_x),range(n_all_y)):
    all_spaces.append([x,y])

run = True

while run:
    
    clock.tick(clock_time)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    
    control_keys = [keys[pygame.K_w],keys[pygame.K_s],keys[pygame.K_a],keys[pygame.K_d]]
    
    win.fill(back_color)
    
    if not game_start:
        if keys[pygame.K_SPACE]:
            game_start = True
            p1.new()
            apple.new()
            snake_whole_body = []
            mode = modes[3]
            points = 0
        if game_over:
            old_points = "Game Over - You managed to get {0} points".format(points)
            txt.screen_text_centerpos(old_points, W/2, 20)
        txt.screen_text_centerpos("Press SPACE to start",W/2,H/2)
    
    else:
        
        old_mode = mode
    
        for i in range(len(control_keys)):
            if control_keys[i]:
                mode = modes[i]
                

        if p1.x == apple.x and p1.y == apple.y:
            points += 1
            point_made = True
            if len(snake_whole_body) == 0:
                snake_whole_body.append(snake_body(size_all,snake_color,p1.x,p1.y))
            else:
                last_snake_x = snake_whole_body[len(snake_whole_body)-1].x
                last_snake_y = snake_whole_body[len(snake_whole_body)-1].y
                snake_whole_body.append(snake_body(size_all,snake_color,last_snake_x,last_snake_y))
        else:
            point_made = False
                
        snake_copy = copy.deepcopy(snake_whole_body)
        
        if points>0:
            if point_made:
                for i in range(1,len(snake_whole_body)-1):
                    snake_whole_body[i].x = snake_copy[i-1].x
                    snake_whole_body[i].y = snake_copy[i-1].y
                    
            else:
                for i in range(1,len(snake_whole_body)):
                    snake_whole_body[i].x = snake_copy[i-1].x
                    snake_whole_body[i].y = snake_copy[i-1].y

            snake_whole_body[0].x = p1.x
            snake_whole_body[0].y = p1.y
            
        mode()
        
        if (p1.x<0 or p1.x>W-p1.size or p1.y<0 or p1.y>H-p1.size):
            pygame.time.delay(100)
            game_over = True
            game_start = False
            
        if points>0:
            for i in loser_move:
                if mode == modes[i[0]] and old_mode == modes[i[1]]:
                    pygame.time.delay(100)
                    game_over = True
                    game_start = False
            
        for i in snake_whole_body:
            if (p1.x==i.x and p1.y==i.y):
                pygame.time.delay(100)
                game_over = True
                game_start = False
                
        if points>0 and point_made:
            
            snake_spaces = []
            free_spaces = []

            for i in snake_whole_body:
                snake_spaces.append([(i.x/20),(i.y/20)])

            for i in all_spaces:
                if i not in snake_spaces:
                    free_spaces.append(i)
                    
            next_apple = free_spaces[random.randint(0,len(free_spaces)-1)]
            
            apple.x = 20*next_apple[0]
            apple.y = 20*next_apple[1]
                        
        apple.draw(win)
        
        p1.draw(win)
            
        for i in snake_whole_body:
            i.draw(win)
        
        true_points = "Current Points: {0}".format(points)

        txt.screen_text_centerpos(true_points,W/2,10)
    
    pygame.display.update()
    
pygame.quit()
