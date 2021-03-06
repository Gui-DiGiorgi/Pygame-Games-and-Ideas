import pygame
from pygametexting import pyg_text

story = []    

story_en = ["Welcome to the world","Now you will know the secret behind it all", "Be prepared",
        ".","..","...","It's Friday mah dudes!", "Yeaaaaaaah!!!"]

story_pt = ["Bem-Vindo ao mundo", "Agora você saberá o segredo por trás de tudo", "Esteja preparado",
           ".","..","...","É sexta, meus camaradas!", "Uooooooooooo!!!"]

screen_n=0

def shown_screen(obj,screen_n,story):
    
    obj.screen_text_centerpos(story[screen_n],250,250)
    

pygame.init()

win=pygame.display.set_mode((500,500))

pygtxt=pyg_text(20,(255,255,255),"comicsansms",win)

pygame.display.set_caption("Language")

happy_color=(0,220,220)

story_lan = ""

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            
    keys = pygame.key.get_pressed()
            
    mouse = pygame.mouse.get_pressed()
    
    # Quits
    if keys[pygame.K_ESCAPE]:
        run = False
        
    win.fill((0,0,0))
    
    if story_lan=="":
        
        pygtxt.screen_text_centerpos('English',250,100)
        if 217<pygame.mouse.get_pos()[0]<283 and 85<pygame.mouse.get_pos()[1]<114:
            pygtxt.screen_text_centerpos('English',250,100,color = (0, 200, 200))
            if mouse[0]:
                pygtxt.screen_text_centerpos('English',250,100,color = (0, 100, 100))
                pygame.display.update((217,85),(66,29))
                pygame.time.delay(100)
                story=story_en
                story_lan="en"
                
        pygtxt.screen_text_centerpos('Português',250,400)
        if 204<pygame.mouse.get_pos()[0]<295 and 385<pygame.mouse.get_pos()[1]<414:
            pygtxt.screen_text_centerpos('Português',250,400,color = (0, 200, 200))
            if mouse[0]:
                pygtxt.screen_text_centerpos('Português',250,400,color = (0, 100, 100))
                pygame.display.update((204,385),(91,29))
                pygame.time.delay(100)
                story=story_pt
                story_lan="pt"
        

    
    if story_lan!="":
    
        if screen_n!=0:

            pygtxt.screen_text_initpos("<-",50,450)
            if 50<pygame.mouse.get_pos()[0]<66 and 450<pygame.mouse.get_pos()[1]<479:
                pygtxt.screen_text_initpos("<-",50,450,color=happy_color)
                if mouse[0]:
                    pygtxt.screen_text_initpos('<-',50,450,color = (0, 100, 100))
                    pygame.display.update((50,450),(16,29))
                    pygame.time.delay(200)
                    screen_n-=1

        if screen_n!=(len(story)-1):

            pygtxt.screen_text_initpos("->",450,450)
            if 450<pygame.mouse.get_pos()[0]<466 and 450<pygame.mouse.get_pos()[1]<479:
                pygtxt.screen_text_initpos("->",450,450,color=happy_color)
                if mouse[0]:
                    pygtxt.screen_text_initpos('->',450,450,color = (0, 100, 100))
                    pygame.display.update((450,450),(16,29))
                    pygame.time.delay(200)
                    screen_n+=1


        shown_screen(pygtxt,screen_n,story)
    
#    screen_text_centerpos(pygame.mouse.get_pos(),250,450)
    
    
    pygame.display.update()

pygame.quit()
