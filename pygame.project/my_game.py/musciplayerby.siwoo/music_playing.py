import pygame
import os
from mutagen import File



class music:
    def __init__(self,music_name:str,sound_path,image_path,screen:pygame.Surface,box_x,box_y,music_stop,music_own_number,music_box):
        self.music_name = music_name
        self.sound_path = sound_path
        self.screen = screen
        self.image_path = image_path
        self.box_x = box_x
        self.box_y = box_y
        self.music_stop = music_stop
        self.music_own_number = music_own_number
        self.music_box = pygame.image.load((os.path.join(self.image_path,"music.png")))
    def sound_box(self):
        self.music_box = pygame.transform.scale(self.music_box,(500,100))
        return self.box_y
        

    def sound_play(self,event,music_arrow_number):
        if event.key == pygame.K_SPACE:
            if self.music_own_number == music_arrow_number:
                    pygame.mixer.music.load(self.music_name)
                    pygame.mixer.music.play()

    def update(self):
        self.screen.blit(self.music_box,(self.box_x,self.box_y))
        audio = File(self.music_name)
            
        try:

            for title in audio.tags:
                title = audio.tags[title][0]
                if title == int:
                    return 'there is no name'
                else:
                    return title
        except:
            return "there is no name"

        
 