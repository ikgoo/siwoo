import pygame 
from settings import *
from support import import_folder
from entity import Entity
class Player(Entity):
    def __init__(self,pos,groups,obstacle_spr,create_attack,destroy_weapon,create_magic):
        super().__init__(groups)
        self.image = pygame.image.load('..\\graphics\\test\\player.png').convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)
        self.hitbox = self.rect.inflate(0,-26)
        self.import_player_assets()
        self.status = 'down'


        

        self.speed = 5
        self.attacking = False
        self.attack_cooldown = 400
        self.attack_time = 0
        self.obs_spr = obstacle_spr
        self.create_attack = create_attack
        self.weapon_index = 0
        self.destroy_attack = destroy_weapon
        self.weapon = list(weapon_data.keys())[self.weapon_index]
        self.can_switch = True
        self.weapon_switch_time = None
        self.switch_duration_cooldown = 200

        self.create_magic = create_magic
        self.magic_index = 0
        self.magic = list(magic_data.keys())[self.magic_index]
        self.can_swicth_magic = True
        self.magic_swicth_time = None
        #states
        self.states = {'health':100,'energy' : 60,'attack' : 10, 'magic' : 4 , 'speed' : 5}
        self.health = self.states['health']  * 0.5
        self.energy = self.states['energy'] * 0.8
        self.exp = 123
        self.speed = self.states['speed']
    
    def import_player_assets(self):
        character_path = '..\\graphics\\player\\'
        self.animations = {'up': [],'down': [],'right': [],'left': [],
			'left_idle':[],'right_idle':[],'up_idle':[],'down_idle':[],
			'left_attack':[],'right_attack':[],'up_attack':[],'down_attack':[]}
    
        for animation in self.animations.keys():
            full_path = character_path + animation
            self.animations[animation] = import_folder(full_path)
    
    def input(self):
        keys = pygame.key.get_pressed()

        if not self.attacking:
            
            if keys[pygame.K_w]:
                self.dir.y = -1
                self.status = 'up'
            elif keys[pygame.K_s]:
                self.dir.y = 1
                self.status = 'down'
            else:
                self.dir.y = 0
    
            if keys[pygame.K_d]:
                self.dir.x = 1
                self.status = 'right'
            elif keys[pygame.K_a]:
                self.dir.x = -1
                self.status = 'left'
            else:
                self.dir.x = 0
            
            if keys[pygame.K_SPACE]:
                self.attacking = True
                self.attack_time = pygame.time.get_ticks()
                self.create_attack()
            
            if keys[pygame.K_LCTRL]:
                self.attacking = True
                self.attack_time = pygame.time.get_ticks()
                style = list(magic_data.keys())[self.magic_index]
                strenght = list(magic_data.values())[self.magic_index]['strength'] + self.states['magic']
                cost = list(magic_data.values())[self.magic_index]['cost']
                self.create_magic(style,strenght,cost)

            if keys[pygame.K_q] and self.can_switch:
                self.can_switch = False
                self.weapon_switch_time = pygame.time.get_ticks()
                if self.weapon_index < len(list(weapon_data.keys())) - 1:
                    self.weapon_index += 1
                else:
                    self.weapon_index = 0
                self.weapon = list(weapon_data.keys())[self.weapon_index]
            
            if keys[pygame.K_e] and self.can_swicth_magic:
                self.can_swicth_magic = False
                self.magic_switch_time = pygame.time.get_ticks()
                if self.magic_index < len(list(magic_data.keys())) - 1:
                    self.magic_index += 1
                else:
                    self.magic_index = 0
                self.magic = list(magic_data.keys())[self.magic_index]
                
    def get_status(self):
        # print(self.dir.x)
        # print(self.dir.y)


        if round(self.dir.x,1) == 0.0 and round(self.dir.y,1) == 0.0:
            if not 'idle' in self.status and not 'attack' in self.status:
                self.status = self.status + '_idle'
        if self.attacking:
            self.dir.x = 0
            self.dir.y = 0
            if not 'attack' in self.status:
                if 'idle' in self.status:
                    self.status = self.status.replace('_idle','_attack')
                else:
                    self.status = self.status + '_attack'
        else:
            if 'attack' in self.status:
                self.status = self.status.replace('_attack','')

    def cooldowns(self):
        current_time = pygame.time.get_ticks()
        
        if current_time - self.attack_time >= self.attack_cooldown + weapon_data[self.weapon]['cooldown']:
            self.attacking = False
            self.destroy_attack()
        if not self.can_switch:
            if current_time - self.weapon_switch_time >= self.switch_duration_cooldown:
                self.can_switch = True

        if not self.can_swicth_magic:
            if current_time - self.magic_switch_time >= self.switch_duration_cooldown:
                self.can_swicth_magic = True
    
    def animate(self):
        animation = self.animations[self.status]
        
        self.frame_index += self.animation_speed
        if self.frame_index >= len(animation):
            self.frame_index = 0
            
        self.image = animation[int(self.frame_index)]
        self.rect = self.image.get_rect(center = self.hitbox.center)
    
    def get_full_weapon_damage(self):
        base_damage = self.states['attack']
        weapon_damage = weapon_data[self.weapon]['damage']
        return base_damage + weapon_damage
    
    def update(self):
        self.input()
        self.cooldowns()
        self.get_status()
        self.animate()
        self.move(self.speed)
        
    
            
    
        
      
            
  