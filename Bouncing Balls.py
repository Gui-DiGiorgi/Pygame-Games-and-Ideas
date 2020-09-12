import pygame
import random
import copy
from pygametexting import pyg_text

dev = False

clock_time = 60

balls = 50

grav = 10

trans_cons = 1

elas = 0.95

fric = 0.1

W = 1000

H = 600

pygame.init()

wind=pygame.display.set_mode((W,H))

pygame.display.set_caption("Bouncing Balls")

txt = pyg_text(20,(255,255,255),"comicsansms",Win=wind)

back_color = (0,0,0)

clock = pygame.time.Clock()

circles = []

error_message = False

pause = False

run = True

class circle(object):
    
    def __init__(self,radius):
    
        self.radius = radius
        self.x = pygame.mouse.get_pos()[0]
        self.y = pygame.mouse.get_pos()[1]
        self.mouse_on = True
        self.color = (0,0,255)
        self.y_vel = 0
        self.x_vel = 0
        self.time = 0

    def draw(self,window):
        pygame.draw.circle(window,self.color,(self.x,self.y),self.radius)
        

while run:
    
    clock.tick(clock_time)
    
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            run = False
            
        if event.type == pygame.MOUSEBUTTONUP and len(circles)<balls and not error_message:
            create_count=0
            for item in circles:
                if not item.mouse_on:
                    create_count += 1
            if create_count == len(circles):
                circles.append(circle(20))
            
        if event.type == pygame.KEYDOWN:
            
            if event.key == pygame.K_ESCAPE or event.key == pygame.K_q:
                run = False    
            
            if event.key == pygame.K_r:
                circles = []
                error_message = False
                
            if event.key == pygame.K_p:
                if not pause:
                    pause = True
                elif pause:
                    pause = False
                     
            
    
    wind.fill(back_color)
        
    checks = copy.deepcopy(circles)
    
    if not pause: 
        
        for index1,item,f_item in zip(range(len(circles)),circles.copy(),checks):

            for index2,target,f_target in zip(range(len(circles)),circles.copy(),checks):

                dist_x = (f_item.x-f_target.x)**2
                dist_y = (f_item.y-f_target.y)**2
                dist = dist_x+dist_y

                if index1==index2:
                    pass  

                elif dist<=(item.radius+target.radius)**2:


                    if (f_item.y-f_target.y)*(f_item.y_vel)<0:
                        y_pos_const = 1
                    else:
                        y_pos_const = -1

                        item.y -= round(f_item.y_vel)*(y_pos_const)
                        target.y += round(f_item.y_vel)*(y_pos_const)

                    if (f_item.x-f_target.x)*(f_item.x_vel)<0:
                        x_pos_const = 1
                    else:
                        x_pos_const = -1

                        item.x -= round(f_item.x_vel)*(x_pos_const)
                        target.x += round(f_item.x_vel)*(x_pos_const)


                    if f_item.y_vel>0:
                        y_dir_const = 1
                    else:
                        y_dir_const = -1

                    try:

                        item.y_vel -= (0.5)*trans_cons*((dist_y/dist)**2)*abs(f_item.y_vel)*(y_pos_const)*(y_dir_const)
                        target.y_vel += (0.5)*trans_cons*((dist_y/dist)**2)*abs(f_item.y_vel)*(y_pos_const)*(y_dir_const)

                        if f_item.x-f_target.x!=0:

                            item.y_vel -= trans_cons*((dist_y*dist_x)/dist**2)*abs(f_item.y_vel)*(y_dir_const)

                            if f_item.x-f_target.x>0:

                                x_side_const = 1

                            else:

                                x_side_const =-1

                            item.x_vel += (0.5)*trans_cons*((dist_y*dist_x)/dist**2)*abs(f_item.y_vel)*(x_side_const)*(y_dir_const)
                            target.x_vel -= (0.5)*trans_cons*((dist_y*dist_x)/dist**2)*abs(f_item.y_vel)*(x_side_const)*(y_dir_const)

                    except:
                        circles=[]
                        error_message=True



                    if f_item.x_vel>0:
                        x_dir_const = 1
                    else:
                        x_dir_const = -1

                    try:

                        item.x_vel -= (0.5)*trans_cons*((dist_x/dist)**2)*abs(f_item.x_vel)*(x_pos_const)*(x_dir_const)
                        target.x_vel += (0.5)*trans_cons*((dist_x/dist)**2)*abs(f_item.x_vel)*(x_pos_const)*(x_dir_const)

                        if f_item.y-f_target.y!=0:

                            item.x_vel -= trans_cons*((dist_y*dist_x)/dist**2)*abs(f_item.x_vel)*(x_dir_const)

                            if f_item.y-f_target.y>0:

                                y_side_const = 1

                            else:

                                y_side_const = -1

                            item.y_vel += (0.5)*trans_cons*((dist_x*dist_y)/dist**2)*abs(f_item.x_vel)*(y_side_const)*(x_dir_const)
                            target.y_vel -= (0.5)*trans_cons*((dist_x*dist_y)/dist**2)*abs(f_item.x_vel)*(y_side_const)*(x_dir_const)

                    except:
                        circles=[]
                        error_message=True



            if (item.y+item.radius)>=H:

                item.y=H-item.radius

                if abs(item.y_vel)>1.5:
                    item.y_vel = -(elas*item.y_vel)
                else:
                    item.y_vel = 0

                if abs(item.x_vel)>0.001:
                    item.x_vel = (1-fric)*item.x_vel
                else:
                    item.x_vel = 0

            else:
                item.y_vel += (grav/clock_time)


            item.y += round(item.y_vel)
            item.x += round(item.x_vel)
        
            if item.x>(W+item.radius) or item.x<-item.radius:
                try:
                    circles.remove(item)
                except:
                    pass


            if not dev:
                item.time+=1
                if (item.time/clock_time)>15:
                    try:
                        circles.remove(item)
                    except:
                        pass
                    
                    
    for item in circles:            
        if ((item.x-pygame.mouse.get_pos()[0])**2 + (item.y-pygame.mouse.get_pos()[1])**2)>(2*item.radius)**2:
            item.mouse_on = False
        else:
            item.mouse_on = True
                    
        item.draw(wind)
        
        
    if dev:
        
        init_y = 50
        
        for item in circles:
        
            info1 = "Item {0} y: {1} Item {0} x: {2} Item {0} y vel: {3} Item {0} x vel: {4}".format(circles.index(item), item.y, item.x, 
                                                                       round(item.y_vel), round(item.x_vel))
            txt.screen_text_initpos(info1,10,init_y)
            
            init_y += 25
    
        
    if error_message:
        error_txt = "Something went wrong, press R to Restart"
        txt.screen_text_centerpos(error_txt,W/2,H/2)
        
    if pause:
        pause_text = "Pause: On"
    else:
        pause_text = "Pause: Off"
        
    txt.screen_text_initpos(pause_text,10,10)
    
    if circles == [] and not error_message:
        
        start_txt = ["Welcome to the this little bouncing balls simulator",
                    "You can click anywhere to create a little blue ball",
                     "But you can't create a ball inside another ball",
                     "Each ball lasts about 15 seconds",
                     "You can reset with r and pause with p",
                     "To quit, simply press q or ESC",
                     "Have fun!"]
        
        start_init_y = 200
        
        for text in start_txt:
            
            txt.screen_text_centerpos(text,W/2,start_init_y)
            
            start_init_y += 25
            
    
    balls_txt = "Active Balls: {}/{}".format(len(circles),balls)
    
    mouse_position = "Mouse location (x/y): {}/{}".format(pygame.mouse.get_pos()[0],pygame.mouse.get_pos()[1])
    
    txt.screen_text_limitpos(balls_txt,W-50,32)
    txt.screen_text_limitpos(mouse_position,W-50,54)
        
    pygame.display.update()
    
pygame.quit()
