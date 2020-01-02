# Player V1 = Accurate sample freq, but no autoplay/playlist while on background
# Your songs need to be .mp3 and located on an file named 'input'

import pygame
from pygametexting import pyg_text
    
def time_conv(seconds,song=False):
    s = round(seconds)
    m=0
    h=0
    if s>=60:
        m = s//60
        s = s%60
    if m>=60:
        h = m//60
        m = m%60
        
    if song:
        c_time = "{:02d}:{:02d}".format(m,s)
    else: 
        c_time = "{:02d}:{:02d}:{:02d}".format(h,m,s)
    
    return c_time
    
def player(m_list, x):
    import mutagen.mp3
    
    global name, audio_length
    
    song = m_list[x]
    name = song[0:-4]
    
    pygame.mixer.quit()
    audio_freq = mutagen.mp3.MP3(r'input/{}'.format(song)).info.sample_rate
    pygame.mixer.init(frequency=audio_freq)
    
    audio_length = mutagen.mp3.MP3(r'input/{}'.format(song)).info.length
    
    pygame.mixer.music.load(r'input/{}'.format(song))
    pygame.mixer.music.play(0)
    
def ext_file_list(file_addr,ext):
    import os
    
    file_list=os.listdir(file_addr)

    ext_list=[]

    for i in file_list:
        if i[-4::1]==ext:
            ext_list+=[i]
    return ext_list


mp3=ext_file_list(r'Your input music directory on here',".mp3")

pygame.init()

win=pygame.display.set_mode((800,300))

pygame.display.set_caption("First Song")

txtng=pyg_text(20,(255,255,255),"comicsansms",win)

pygame.mixer.music.set_volume(0.7)

pause = "On"

new_volume = 0

name = "???"

audio_length = 0

music_n = 0

back_color = (0,0,0)

start = False


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
    
    # Starts the player
    if mouse[0] and not start:
        pygame.time.delay(150)
        if start == False:
            start = True
        music_n=0
        player(mp3,0)
        
    # After initiated, it pauses and unpauses
    if (mouse[0] or keys[pygame.K_r]) and start:
        pygame.time.delay(150)
        if pause=="Off":
            pygame.mixer.music.pause()
            pause="On"
        elif pause=="On":
            pygame.mixer.music.unpause()
            pause="Off"
            
    # Resets the playlist to the beginning
    if keys[pygame.K_w] and start:
        pygame.time.delay(100)
        pause="Off"
        music_n=0
        player(mp3,0)
        
    # Moves to the previous song, and to the end if at the beginning
    if keys[pygame.K_q] or keys[pygame.K_LEFT] and start:
        pygame.time.delay(200)
        pause="Off"
        music_n-=1
        if music_n==-1:
            music_n=len(mp3)-1 
        player(mp3,music_n)
        
    # Moves to the next song, and to the beginning if at the end    
    if keys[pygame.K_e] or keys[pygame.K_RIGHT] and start:
        pygame.time.delay(200)
        pause="Off"
        music_n+=1
        if music_n==len(mp3):
            music_n=0
        player(mp3,music_n)
        
    
    # Decreases Volume
    if keys[pygame.K_2] and start:
        pygame.time.delay(100)
        if pygame.mixer.music.get_volume()>0.0:
            new_volume=pygame.mixer.music.get_volume()-0.1
            pygame.mixer.music.set_volume(new_volume)
            
    # Increases Volume
    if keys[pygame.K_3] and start:
        pygame.time.delay(100)
        if pygame.mixer.music.get_volume()<1.0:
            new_volume=pygame.mixer.music.get_volume()+0.1
            pygame.mixer.music.set_volume(new_volume)

    win.fill(back_color)
    
    if not pygame.mixer.music.get_busy() and pause == "Off" and start:
        music_n+=1
        player(mp3,music_n)
    
    if not start:
        
        start_text="Click to start"
        txtng.screen_text_centerpos(start_text, 400, 150)
    
    if start:
    
        # Pause_Text
    
        pause_text = 'Pause : {}'.format(pause)
        txtng.screen_text_centerpos(pause_text,400,250)
    
        # Song
    
        song_name = 'Song {}: {}'.format(music_n+1,name)
        txtng.screen_text_centerpos(song_name,400,50)
    
        # Song_Time
    
        song_time = 'Music Time : {}/{}'.format(time_conv(pygame.mixer.music.get_pos()/1000,True), time_conv(audio_length,True))
        txtng.screen_text_initpos(song_time,285,100)
        
        title="First Song - {}".format(song_name)
        
        pygame.display.set_caption(title)
        
    
    pygame.display.update()
    

pygame.quit()
