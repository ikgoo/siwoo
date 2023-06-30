import pygame 
import os
import arrow
import music_playing
import soundplusbutten
import tkinter as tk
from tkinter import filedialog
from mutagen import File
################################
pygame.init()
pygame.mixer.init()
first = 0
sreen_width = 640
screen_heght = 108

screen = pygame.display.set_mode()sreen_width,screen_heght
pygame.display.set_caption("음악 플레이어")
current_path = os.path.dirname(__file__)
image_path = os.path.join(current_path,"images")
pygame.display.set_icon().icon
####################################
game_font = pygame.font.Font(None,36)
root = tk.Tk()
root.withdraw()
filetypes = ('음악 파일', '*.mp3;*.wav;*.ogg')
musics = 
plus_music = pygame.image.load(os.path.join(image_path,"+music.png"))

# music1 = music_playing.music("0_angel_waltz_180.ogg",sound_path,image_path,screen,100,50,0,1)
# music2 = music_playing.music("space.mp3",sound_path,image_path,screen,100,150,0,2)
# music3 = music_playing.music("terrarea_backgrond_sound.mp3",sound_path,image_path,screen,100,250,0,3)
music_plus_number = 0
music_numbers = len(musics)
music_class_num =
pressed_file = 
running = True

while running == True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if len(musics) != 0:
                music_arrow_number = arrow1.key_pushed(event)
            for test in musics:
                test.sound_play(event,music_arrow_number)
        pressed_file = plus_music_surch.pressed(event,filetypes)
            
    
    
    
        if pressed_file != 1:
            music_plus_number += 1
            music = music_playing.music(pressed_file,sound_path,image_path,screen,100,music_class_y,0,music_class_num,0)
            musics.append(music)
            pressed_file = 1
            music_class_num += 1
            music_class_y += 100
    
    
    screenfill((135, 206, 235))
    
    arrow1.update(first)
    
    # music1.sound_box()
    # music2.sound_box()
    # music3.sound_box()


    plus_music_surch.update()

    for test in musics:
        box_V = test.sound_Box()
        title = test.update(

        title_font = game_font.render(title,True,(255,255,255))
        title_font_font = title_font.get_rect()
        title_font_font.center = (170,box_y + 30)
        screen.blit(title_font,title_font_font)















    first = 1
    pygame.display.update()

