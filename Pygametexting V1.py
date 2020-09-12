class pyg_text():
    
    def __init__(self,Size,Color,Font,Win=None):
        
        self.Win = Win
        self.Size = Size
        self.Color = Color
        self.Font = Font
        if Win!=None:
        	self.Win = Win
    
    def screen_text_centerpos(self,text, x_pos, y_pos, size=None, color=None, font=None, win=None):
        import pygame
        import sys
        
        if win==None:
        	win=self.Win
        if size==None:
            size=self.Size
        if color==None:
            color=self.Color
        if font==None:
            font=self.Font
        
        font = pygame.font.SysFont(font, size) 
        rendered_text = font.render(str(text), True, color)
        textRect = rendered_text.get_rect()
        textRect.center = (x_pos, y_pos)
        win.blit(rendered_text, textRect)
        
    def screen_text_initpos(self,text, x_pos, y_pos, size=None, color=None, font=None, win=None):
        import pygame
        import sys
        
        if win==None:
        	win=self.Win
        if size==None:
            size=self.Size
        if color==None:
            color=self.Color
        if font==None:
            font=self.Font
        
        font = pygame.font.SysFont(font, size) 
        rendered_text = font.render(str(text), True, color)
        textRect = rendered_text.get_rect()
        textRect.x = x_pos
        textRect.y = y_pos
        win.blit(rendered_text, textRect)
        
    def screen_text_limitpos(self,text, x_pos, y_pos, size=None, color=None, font=None, win=None):
        import pygame
        import sys
        
        if win==None:
        	win=self.Win        
        if size==None:
            size=self.Size
        if color==None:
            color=self.Color
        if font==None:
            font=self.Font
        
        font = pygame.font.SysFont(font, size) 
        rendered_text = font.render(str(text), True, color)
        textRect = rendered_text.get_rect()
        textlist=list(textRect[2:4])
        x_init= x_pos - textlist[0]
        y_init= y_pos - textlist[1]
        textRect.x = x_init
        textRect.y = y_init
        win.blit(rendered_text, textRect)
        

class pyg_tesxt():
    
    def __init__(self,Size,Font):
        
        self.Size = Size
        self.Font = Font
        
    #Use print(xxx.method()) to print with the correct formatting
    
    def test_on_screen_center_text(self,text, x_center=0, y_center=0, size=None, font=None):
        import pygame
        import sys    
        
        if size==None:
            size=self.Size
        if font==None:
            font=self.Font

        pygame.init()
        font = pygame.font.SysFont(font, size) 
        rendered_text = font.render(str(text), True, (0,0,0))
        textRect = rendered_text.get_rect()
        textlist=list(textRect[2:4])
        x_to_y=textlist[0]/textlist[1]
        final_report="Total Rect width: {}, x init: {}, x limit: {}\n".format(int(textlist[0]), int(x_center-textlist[0]/2), int(x_center+textlist[0]/2))
        final_report+="Total Rect height: {}, y init: {}, y limit: {}\n".format(int(textlist[1]), int(y_center-textlist[1]/2), int(y_center+textlist[1]/2))
        final_report+="x/y: {}".format(x_to_y)
        pygame.quit()
        
        return final_report
    
    def test_on_screen_init_text(self,text, x_init=0, y_init=0, size=None, font=None):
        import pygame
        import sys    
        
        if size==None:
            size=self.Size
        if font==None:
            font=self.Font
        
        pygame.init()
        font = pygame.font.SysFont(font, size) 
        rendered_text = font.render(str(text), True, (0,0,0))
        textRect = rendered_text.get_rect()
        textlist=list(textRect[2:4])
        x_to_y=textlist[0]/textlist[1]
        final_report="Total Rect width: {}, x center: {}, x limit: {}\n".format(int(textlist[0]), int(x_init+textlist[0]/2), int(x_init+textlist[0]))
        final_report+="Total Rect height: {}, y center: {}, y limit: {}\n".format(int(textlist[1]), int(y_init+textlist[1]/2), int(y_init+textlist[1]))
        final_report+="x/y: {}".format(x_to_y)
        pygame.quit()
        
        return final_report
    
    def test_on_screen_limit_text(self,text, x_limit=0, y_limit=0, size=None, font=None):
        import pygame
        import sys    
        
        if size==None:
            size=self.Size
        if font==None:
            font=self.Font
        
        pygame.init()
        font = pygame.font.SysFont(font, size) 
        rendered_text = font.render(str(text), True, (0,0,0))
        textRect = rendered_text.get_rect()
        textlist=list(textRect[2:4])
        x_to_y=textlist[0]/textlist[1]
        final_report="Total Rect width: {}, x init: {}, x center: {}\n".format(int(textlist[0]), int(x_limit-textlist[0]), int(x_limit-textlist[0]/2))
        final_report+="Total Rect height: {}, y init: {}, y center: {}\n".format(int(textlist[1]), int(y_limit-textlist[1]), int(y_limit-textlist[1]/2))
        final_report+="x/y: {}".format(x_to_y)
        pygame.quit()
        
        return final_report
    
        
    def test_size_for_screen_x(self,text, x, font=None):
        import pygame
        import sys          
        
        if font==None:
            font=self.Font
        
        pygame.init()
        font = pygame.font.SysFont(font, 10) 
        rendered_text = font.render(str(text), True, (0,0,0))
        textRect = rendered_text.get_rect()
        textlist=list(textRect[2:4])
        x_to_y=textlist[0]/textlist[1]
        size_needed=int(x/x_to_y)
        pygame.quit()
        
        return size_needed
        
    # Examples    

    # from pygametexting import pyg_tesxt
    
    # tt=pyg_tesxt(20,"comicsansms")
        
    # print(tt.test_on_screen_center_text("ALOHA")):
    
    # Total Rect width: 70, x init: -35, x limit: 35
    # Total Rect height: 29, y init: -14, y limit: 14
    # x/y: 2.413793103448276
    
    # print(tt.test_on_screen_init_text("ALOHA")):
    
    # Total Rect width: 70, x center: 35, x limit: 70
    # Total Rect height: 29, y center: 14, y limit: 29
    # x/y: 2.413793103448276
    
    # print(tt.test_on_screen_limit_text("ALOHA")):
    
    # Total Rect width: 70, x init: -70, x center: -35
    # Total Rect height: 29, y init: -29, y center: -14
    # x/y: 2.413793103448276
    
    # print(test_size_for_screen_x("ALOHA",20)) --> 8


class pyg_button():
    
    #obj1 is the object name for the properties Size and Font
    #obj2 is the string version (used with "" or '') of obj1
    
    def __init__(self,obj1,obj2):
        
        self.Size = obj1.Size
        self.Font = obj1.Font
        self.Obj = obj2
        
    # Use print(xxx.method()) to print with the correct formatting
    # color1 is the color for the button selection
    # color2 is the color for the button press
        
    def center_button(self,text, x_center, y_center, color1, color2, size=None, font=None,obj=None):  

        import pygame
        import sys

        if size==None:
            size=self.Size
        if font==None:
            font=self.Font
        if obj==None:
            obj=self.Obj
        
            
        pygame.init()
        font = pygame.font.SysFont(font, size) 
        rendered_text = font.render(str(text), True, (0,0,0))
        textRect = rendered_text.get_rect()
        textlist=list(textRect[2:4])
        total_x=int(textlist[0])
        total_y=int(textlist[1])
        x_init=int(x_center-total_x/2)
        y_init=int(y_center-total_y/2)
        x_limit=int(x_center+total_x/2)
        y_limit=int(y_center+total_y/2)
        ifs = '''{11}.screen_text_centerpos(\'{0}\',{3},{4})
if {1}<pygame.mouse.get_pos()[0]<{5} and {2}<pygame.mouse.get_pos()[1]<{6}:
    {11}.screen_text_centerpos(\'{0}\',{3},{4},color = {9})
    if mouse[0]:
        {11}.screen_text_centerpos(\'{0}\',{3},{4},color = {10})
        pygame.display.update(({1},{2}),({7},{8}))
        pygame.time.delay(100)'''.format(text,x_init,y_init,x_center,y_center,x_limit,y_limit,total_x,total_y,color1,color2,obj)
        pygame.quit()
        
        return ifs
    
    def init_button(self,text, x_init, y_init, color1, color2, size=None, font=None,obj=None):  

        import pygame
        import sys

        if size==None:
            size=self.Size
        if font==None:
            font=self.Font
        if obj==None:
            obj=self.Obj
        
            
        pygame.init()
        font = pygame.font.SysFont(font, size) 
        rendered_text = font.render(str(text), True, (0,0,0))
        textRect = rendered_text.get_rect()
        textlist=list(textRect[2:4])
        total_x=int(textlist[0])
        total_y=int(textlist[1])
        x_center=int(x_init+total_x/2)
        y_center=int(y_init+total_y/2)
        x_limit=int(x_init+total_x)
        y_limit=int(y_init+total_y)
        ifs = '''{11}.screen_text_initpos(\'{0}\',{1},{2})
if {1}<pygame.mouse.get_pos()[0]<{5} and {2}<pygame.mouse.get_pos()[1]<{6}:
    {11}.screen_text_initpos(\'{0}\',{1},{2},color = {9})
    if mouse[0]:
        {11}.screen_text_initpos(\'{0}\',{1},{2},color = {10})
        pygame.display.update(({1},{2}),({7},{8}))
        pygame.time.delay(100)'''.format(text,x_init,y_init,x_center,y_center,x_limit,y_limit,total_x,total_y,color1,color2,obj)
        pygame.quit()
        
        return ifs
    
    def limit_button(self,text, x_limit, y_limit, color1, color2, size=None, font=None,obj=None):  

        import pygame
        import sys

        if size==None:
            size=self.Size
        if font==None:
            font=self.Font
        if obj==None:
            obj=self.Obj
        
            
        pygame.init()
        font = pygame.font.SysFont(font, size) 
        rendered_text = font.render(str(text), True, (0,0,0))
        textRect = rendered_text.get_rect()
        textlist=list(textRect[2:4])
        total_x=int(textlist[0])
        total_y=int(textlist[1])
        x_init=int(x_limit-total_x)
        y_init=int(y_limit-total_y)
        x_center=int(x_limit-total_x/2)
        y_center=int(y_limit-total_y/2)
        ifs = '''{11}.screen_text_limitpos(\'{0}\',{5},{6})
if {1}<pygame.mouse.get_pos()[0]<{5} and {2}<pygame.mouse.get_pos()[1]<{6}:
    {11}.screen_text_limitpos(\'{0}\',{5},{6},color = {9})
    if mouse[0]:
        {11}.screen_text_limitpos(\'{0}\',{5},{6},color = {10})
        pygame.display.update(({1},{2}),({7},{8}))
        pygame.time.delay(100)'''.format(text,x_init,y_init,x_center,y_center,x_limit,y_limit,total_x,total_y,color1,color2,obj)
        pygame.quit()
        
        return ifs
    
    # Examples:

    # from pygametexting import pyg_text, pyg_button
    
    # pgt=pyg_text(20,(255,255,255),"comicsansms")
    # pygb=pyg_button(pgt,"pgt")
    # print(pygb.center_button("Huehue",50,50,(0,100,200),(0,100,100)))
    
    # Results:
    
    # pgt.screen_text_centerpos('Huehue',50,50)
        # if 15<pygame.mouse.get_pos()[0]<84 and 35<pygame.mouse.get_pos()[1]<64:
            # pgt.screen_text_centerpos('Huehue',50,50,color = (0, 100, 200))
        # if mouse[0]:
            # pgt.screen_text_centerpos('Huehue',50,50,color = (0, 100, 100))
            # pygame.display.update((15,35),(69,29))
            # pygame.time.delay(100)
