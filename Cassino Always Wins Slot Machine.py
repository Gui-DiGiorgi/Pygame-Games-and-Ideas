# Controled prize giving slot machine

import pygame
from pygametexting import pyg_text
from time import time
from random import randint, choice, choices

def no_match(slots_design):
    # No match

    numbers = []

    randomness = [-1,0,1]

    numbers.append(randint(0,len(slots_design[0])-1))

    for i in range(1,len(slots_design)):
        numbers.append(0)

    for r in range(1,len(slots_design)):
        for s in range(len(slots_design[r])):
            if slots_design[r][s] == slots_design[r-1][numbers[r-1]]:
                numbers[r] = s + choice(allowed_moves)

                while numbers[r] >= len(slots_design[r]):
                    numbers[r] -= len(slots_design[r])
                    
    return numbers
                    
def two_symbol_match(slots_design,symbol):
    
    if type(symbol) == list:
        symbol = choice(symbol)

    numbers = []

    randomness = [-1,0,1]

    combo_breaker = [0,2]

    for r in slots_design:
        for s in range(len(r)):
            if r[s] == symbol:
                numbers.append(s)
                break

    pos_shift = choice(randomness)

    cb_author = choice(combo_breaker)

    cb_shift = choice(allowed_moves)

    for i in range(len(numbers)):
        numbers[i] += pos_shift

    numbers[cb_author] += cb_shift
    
    return numbers
    
def three_symbol_match(slots_design,symbol):
    
    # Three one symbol match
    
    if type(symbol) == list:
        symbol = choice(symbol)

    numbers = []

    randomness = [-1,0,1]

    for r in slots_design:
        for s in range(len(r)):
            if r[s] == symbol:
                numbers.append(s)
                break

    pos_shift = choice(randomness)

    for i in range(len(numbers)):
        numbers[i] += pos_shift
        
    return numbers

def play_n_win(slots_design,SSR_symbol,SR_symbol,R_symbol,chances,prizes):
    
    methods = [[three_symbol_match,SSR_symbol],[two_symbol_match,SSR_symbol],
           [three_symbol_match,SR_symbol],[two_symbol_match,SR_symbol],
           [three_symbol_match,R_symbol],[two_symbol_match,R_symbol],
           [no_match,0]]
    
    play = choices(prizes,chances)[0]
    
    intakes = [slots_design]
           
    for i in range(len(prizes)):
    
        if play == prizes[i]:
            
            if methods[i][1] == 0:
                pass
            else:
                intakes += [methods[i][1]]
                
            numbers = methods[i][0](*intakes)
            
            break
            
    for i in range(len(numbers)):
        while numbers[i] >= len(slots_design[i]):
            numbers[i] -= len(slots_design[i])
        while numbers[i] <= -len(slots_design[i]):
            numbers[i] += len(slots_design[i])
            
    return [numbers,play]

pygame.init()

win_size = 500

win=pygame.display.set_mode((win_size,win_size))

pygame.display.set_caption("Slot Machine")

slots_design = [["日", "月", "火", "水", "木", "金", "土", "銀", "星", "人"],
                ['人', '星', '銀', '土', '金', '木', '水', '火', '月', '日'],
                ["日", "月", "火", "水", "木", "金", "土", "銀", "星", "人"]]

n_blocks = len(slots_design[0])

size = 20

space = 30

move_range = (space+size)*(n_blocks-1)

pygtxt=pyg_text(size,(0,0,0),"msmincho",win)

class player():
    def __init__(self, id_n, y_vel, x, y, size):

        self.y = y
        self.x = x
        self.y_vel = y_vel
        self.size = size
        self.id_n = id_n
        self.color = (0,0,0)
    
    def action(self, y_start, y_range, space):
        
        self.y += self.y_vel
        
        if self.y<(y_start - self.size):
            self.y += y_range + self.size + space
        if self.y>(y_start+y_range):
            self.y -= y_range + self.size + space
            
    def draw(self,win):
        pygtxt.screen_text_initpos(self.id_n,int(self.x),int(self.y))
        
        
vel_group1 = [1, 2, 4, 5, 10, 20]

vel_group2 = [20, 10, 5, 4, 2]

vel_type1 = 0

vel_type2 = 0

clock = pygame.time.Clock()

clock_time = 60

run = True

rolletes = 3

chances = [0.5,1,2,5,10,20]
chances.append(100-sum(chances))

prizes = [250,50,25,15,10,2.5,0]

SSR = ["金"]

SR = ["銀"]

R = []

for i in slots_design[0]:
    if i in SSR+SR:
        continue
    R.append(i)

allowed_moves = []

for i in range(-len(slots_design[0])+1,len(slots_design[0])):
    if i%2 == 0:
        continue
    allowed_moves.append(i)

p_grand_group = []

x_location = []

x_start = 150

x_space = 100

for r in range(rolletes):
    p_grand_group.append([])
    x_location.append(x_start+r*x_space)

roll_start = 200

chosen_id = []

for r in range(rolletes):
    
    chosen_id.append(randint(0,n_blocks-1))

    for i in range(n_blocks):
    
        p_grand_group[r].append(player(slots_design[r][i], vel_group1[vel_type1], x_location[r], roll_start + i*(size+space), size))

now = time()

time_limit = 0.5

stage = 0

show_range = 150

c_roll = 3

init_stage = False

money = 500

excitement = 0

while run:
    
    clock.tick(clock_time)
    
    keys = pygame.key.get_pressed()
            
    mouse = pygame.mouse.get_pressed()
    
    mouse_pos = pygame.mouse.get_pos()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    # Quits
    if keys[pygame.K_ESCAPE]:
        run = False
        
    # Plays
    if keys[pygame.K_r] and c_roll == 3 and money-5>=0:
        pygame.time.delay(150)
        
        money -= 5
        
        your_luck = play_n_win(slots_design,SSR,SR,R,chances,prizes)
        
        chosen_id = your_luck[0]
        
        init_stage = True
        
        vel_type1 = 0
        now = time()
        
        c_roll = 0
        
    # Reset Money:
    
    if keys[pygame.K_e] and c_roll == 3:
        pygame.time.delay(150)
        
        money = 500
        
        excitement = 0
    
    win.fill((255,255,255))
    
    x_line_len = x_location[len(x_location)-1]-x_location[0]+int(1.5*size)
            
    pygame.draw.rect(win,(255,32,32),(x_location[0]-int(size/2),roll_start+size,x_line_len+int(size/2),int(1.5*size)))
    
    pygame.draw.rect(win,(32,255,32),(x_location[0]-int(size/2),roll_start+show_range/2-int(size/4),x_line_len+int(size/2),int(1.5*size)))
    
    pygame.draw.rect(win,(32,32,255),(x_location[0]-int(size/2),roll_start+show_range-1.5*size,x_line_len+int(size/2),int(1.5*size)))
    
    
    for r,p_group in zip(range(rolletes),p_grand_group):
    
        for p in p_group:

            p.action(roll_start, move_range, space)

            if roll_start-size < p.y < roll_start+show_range:

                p.draw(win)

            pygame.draw.rect(win,(255,255,255),(x_location[r],roll_start-size,size,size))
            pygame.draw.rect(win,(255,255,255),(x_location[r],roll_start+show_range,size,int(1.5*size)))
            
    countdown = round(time_limit - time() + now,1)

    if countdown < 0:
        countdown = 0
        
    if countdown == 0 and init_stage:

        vel_type1 += 1

        now = time()
    
        for p_group in p_grand_group:

            for p in p_group:

                p.y_vel = vel_group1[vel_type1]
                
        if vel_type1+1 == len(vel_group1):
            
            init_stage = False
            
    if c_roll<rolletes and not init_stage:
        
            if countdown == 0:

                if stage == 0:

                    vel_type2 += 1

                    for p in p_grand_group[c_roll]:

                        p.y_vel = vel_group2[vel_type2]

                    if vel_type2+1 == len(vel_group2):

                        stage = 1

                    now = time()

                elif stage == 1:

                    if roll_start-size-1 <= p_grand_group[c_roll][chosen_id[c_roll]].y <= roll_start-size+1:

                        for p in p_grand_group[c_roll]:

                            p.y_vel = 1

                        stage = 2

                        now = time()

                elif stage == 2:

                    if p_grand_group[c_roll][chosen_id[c_roll]].y == roll_start+show_range/2:

                        for p in p_grand_group[c_roll]:

                            p.y_vel = 0

                        c_roll += 1
                        stage = 0
                        vel_type2 = 0
                        now = time()
                        
                        if c_roll == 3:
                            
                            r_gang = [[chosen_id[0]-1,chosen_id[1]-1,chosen_id[2]-1],
                                      [chosen_id[0],chosen_id[1],chosen_id[2]],
                                      [chosen_id[0]+1,chosen_id[1]+1,chosen_id[2]+1]]
                            
                            for ri in range(len(r_gang)):
                                for rj in range(len(r_gang[ri])):
                                    while r_gang[ri][rj] >= len(slots_design[0]):
                                        r_gang[ri][rj] -= len(slots_design[0])
                                    while r_gang[ri][rj] <= -len(slots_design[0]):
                                        r_gang[ri][rj] += len(slots_design[0])
                            
                            prize_results =  [[slots_design[0][r_gang[0][0]],slots_design[1][r_gang[0][1]],slots_design[2][r_gang[0][2]]],
                                             [slots_design[0][r_gang[1][0]],slots_design[1][r_gang[1][1]],slots_design[2][r_gang[1][2]]],
                                             [slots_design[0][r_gang[2][0]],slots_design[1][r_gang[2][1]],slots_design[2][r_gang[2][2]]]]
                                           
                            excitement = your_luck[1]
                            
                            money += excitement
                            
                            #for i in prize_results:
                            #    print(i)
                            #
                            #print(excitement)
                            #
                            #print()                          
                        
    if c_roll<rolletes:
        
        action = "Rolling"
        
    #    pygtxt.screen_text_centerpos("c_roll: {0} stage: {1}  y: {2} y_vel: {3}".format(c_roll,stage,
    #                            p_grand_group[c_roll][chosen_id[c_roll]].y, 
    #                            p_grand_group[c_roll][chosen_id[c_roll]].y_vel), 250, 450)
        
    else:
        
        action = "Press R to roll and E to reset the moneis"
                        
    pygtxt.screen_text_centerpos(action, 250, 50)
    pygtxt.screen_text_centerpos("Moneis: {0}$ (Last roll money: +{1}$)".format(money,excitement), 250, 100)
                
    pygame.display.update()
        
pygame.quit()
