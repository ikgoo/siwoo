import pygame
import os
import tkinter as tk
from tkinter import filedialog
class plusbutten:
    def __init__(self,screen:pygame.Surface,image_path,but_x,but_y,music_image:pygame.Surface,plus_music_rect:pygame.rect):
        self.music_image = music_image
        self.screen = screen
        self.image_path = image_path
        self.but_x = but_x
        self.but_y = but_y
        self.plus_music_rect = self.music_image.get_rect()
        self.plus_music_rect.left = self.but_x
        self.plus_music_rect.top = self.but_y

        
    def pressed(self,event,filetypes):
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            print(mouse_pos)
            if mouse_pos[0] >= self.plus_music_rect[0] and mouse_pos[0] <= self.plus_music_rect[0] + 100 and mouse_pos[1] >= self.plus_music_rect[1] and mouse_pos[1] <= self.plus_music_rect[1] + 200:
                file_path_surch = filedialog.askopenfilename(filetypes=filetypes)
                return file_path_surch
        return 1
            
    def update(self):
        self.screen.blit(self.music_image,(self.but_x,self.but_y))
                