import pygame
import math

pygame.init()

win=pygame.display.set_mode((600,600))

pygame.display.set_caption("car")

clock = pygame.time.Clock()

clock_time = 30

black = (0,0,0)

run = True

angle = 0

abs_center = [300,300]

angular_vel = 10

straight_vel = 10

while run:
    
    clock.tick(clock_time)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    
    win.fill(black)
    
    rainbow = pygame.Surface((30, 15))
    
    rainbow.fill(black, rect = (0,0,1,1))
    
    rainbow.fill((255,0,0), rect = (1,1,30,15))
    
    rainbow.fill((255,255,255), rect = (27,2,30,5))
    
    rainbow.fill((255,255,255), rect = (27,10,30,13))
    
    if keys[pygame.K_a]:
        pygame.time.delay(15)
        angle += angular_vel

        
    if keys[pygame.K_d]:
        pygame.time.delay(15)
        angle -= angular_vel

    if angle<=0:
        angle = 360
    if angle>360:
        angle = 0
    
    rainbow_angle = pygame.transform.rotate(rainbow,angle)
    
    rotator_pos = rainbow_angle.get_rect()
        
    radians = math.radians(angle)
    
    if keys[pygame.K_w]:
        pygame.time.delay(15)
        center_x = round(straight_vel*math.cos(radians))
        center_y = round(-straight_vel*math.sin(radians))
        
    elif keys[pygame.K_s]:
        pygame.time.delay(15)
        center_x = round(-straight_vel*math.cos(radians))
        center_y = round(straight_vel*math.sin(radians))
          
    else:
        center_x = 0
        center_y = 0 
        
    abs_center[0] += center_x
    abs_center[1] += center_y
    
    if abs_center[0]>600:
          abs_center[0] = 0
    if abs_center[0]<0:
          abs_center[0] = 600
    if abs_center[1]>600:
          abs_center[1] = 0
    if abs_center[1]<0:
          abs_center[1] = 600
    
    rotator_pos.center = (abs_center[0],abs_center[1])
    
    win.blit(rainbow_angle, rotator_pos)
    
    pygame.display.update()
    
pygame.quit()

