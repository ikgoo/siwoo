import pygame 
from settings import *
from tile import Tile
from player import Player
from debug import debug
from support import import_csv_layout,import_folder
from random import choice
from weapon import Weapon
from ui import UI
from enemy import enemy
class Level:
    def __init__(self):

        # get the display surface 
        self.display_surface = pygame.display.get_surface()

        # sprite group setup
        self.visible_sprites = YSortCameraGroup()
        self.obstacle_sprites = pygame.sprite.Group()
        self.currunt_attack = None
        self.attack_sprites = pygame.sprite.Group()
        self.attackable_sprites = pygame.sprite.Group()
        # sprite setup
        self.create_map()
        self.ui = UI()
    
    def create_Attack(self):
        self.currunt_attack = Weapon(self.player,[self.visible_sprites,self.attack_sprites])
    def create_magic(self,style,strenght,cost):
        pass

    def create_map(self):
        layouts = {
            'boundary':import_csv_layout('..\\map\\map_FloorBlocks.csv'),
            'grass': import_csv_layout('..\\map\\map_Grass.csv'),
            'object': import_csv_layout('..\\map\\map_LargeObjects.csv'),
            'entites' : import_csv_layout('..\\map\\map_Entities.csv')
			
  
  
          }
        graphics =  {
            'grass':import_folder('..\\graphics\\grass'),
            'objects':import_folder('..\\graphics\\objects')
        }
        print(graphics)
        for style,layout in layouts.items():
            for row_index,row in enumerate(layout):
                for col_index, col in enumerate(row):
                    if col != '-1':
                        x = col_index * TILESIZE
                        y = row_index * TILESIZE
                        if style == 'boundary':
                            Tile((x,y),[self.obstacle_sprites],'invisible')
                        if style == 'grass':
                            random_grass_image=choice(graphics['grass'])
                            Tile((x,y),[self.visible_sprites,self.obstacle_sprites,self.attackable_sprites],'grass',random_grass_image)
                        if style == 'object':
                            surf = graphics['objects'][int(col)]
                            Tile((x,y),[self.visible_sprites,self.obstacle_sprites],'object',surf)
                        if style == 'entites':
                            if col == '394':
                                self.player = Player((x,y),
                                    [self.visible_sprites],
                                    self.obstacle_sprites,
                                    self.create_Attack,
                                    self.destory_weapon,
                                    self.create_magic)
                            else:
                                if col == '390': monster_name = 'bamboo'
                                if col == '391': monster_name = 'spirit'
                                if col == '392': monster_name = 'raccoon'
                                if col == '393': monster_name = 'squid'
                                enemy(monster_name,
                                      (x,y),
                                      [self.visible_sprites,
                                       self.attackable_sprites],
                                      self.obstacle_sprites)





	
    def create_attack(self):
        self.currunt_attack = Weapon(self.player,[self.visible_sprites,self.attack_sprites])
	
    def destory_weapon(self):
        if self.currunt_attack:
            self.currunt_attack.kill()
        self.currunt_attack = None
    
    def player_attack_logic(self):
        if self.attack_sprites:
            for attack_sprite in self.attack_sprites:
                collision_sprites = pygame.sprite.spritecollide(attack_sprite,self.attackable_sprites,False)
                if collision_sprites:
                    for target_sprite in collision_sprites:
                        if target_sprite.sprite_type == 'grass':
                            target_sprite.kill()
                        else:
                            target_sprite.get_damage(self.player,attack_sprite.sprite_type)


		
	
	
    def run(self):
        # update and draw the game
        self.visible_sprites.coustom_draw(self.player)
        self.visible_sprites.update()
        self.ui.display(self.player)
        self.visible_sprites.enemy_update(self.player)
        self.player_attack_logic()
  
class YSortCameraGroup(pygame.sprite.Group):
    def __init__(self):
        
        #setup
        super().__init__()
        self.display_surface = pygame.display.get_surface()
        self.half_width = self.display_surface.get_size()[0] // 2
        self.half_height = self.display_surface.get_size()[1] // 2
        self.offset = pygame.math.Vector2()
        self.floor_surf =pygame.image.load("..\\graphics\\tilemap\\ground.png").convert()
        self.floor_rect = self.floor_surf.get_rect(topleft = (0,0))
    
    def coustom_draw(self,player):
        
        # getting the offset
        self.offset.x = player.rect.centerx - self.half_width
        self.offset.y = player.rect.centery - self.half_height
        
        floor_offset_pos = self.floor_rect.topleft - self.offset
        self.display_surface.blit(self.floor_surf,floor_offset_pos)
        #for sprite in self.sprites():
        for sprite in sorted(self.sprites(),key = lambda sprite: sprite.rect.centery):
            offset_pos = sprite.rect.topleft - self.offset
            

            
            self.display_surface.blit(sprite.image,offset_pos)
    
    def enemy_update(self,player):
        enemy_sprites = [sprite for sprite in self.sprites() if hasattr(sprite,'sprite_type') and  sprite.sprite_type == 'enemy']
        for sprite in enemy_sprites:
            sprite.enemy_update(player)