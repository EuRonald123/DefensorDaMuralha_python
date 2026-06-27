import pygame
from entities.Entity import Entity
from ammo.Ammo import Ammunition


class Player(Entity):
    def __init__(self):
        animation_frames = [
            'assets/soldados/player/1.png',
            'assets/soldados/player/2.png',
            'assets/soldados/player/3.png'
        ]
        super().__init__(None, 280, 270, 5, 40, 60, animation_frames=animation_frames, animation_speed=4)
        self.speed = 7
        self.vertical_speed = 6
        
    def movement(self, keys, screen_width, screen_height):
        self. is_moving = False #-> para movimentar apenas quando se mover
        
        if keys[pygame.K_a] and self.x >= 0:
            self.x -= self.speed
            self.is_moving = True
        if keys[pygame.K_d] and self.x <= screen_width - 40:
            self.x += self.speed
            self.is_moving = True
        if keys[pygame.K_w] and self.y >= 0:
            self.y -= self.vertical_speed
            self.is_moving = True
        if keys[pygame.K_s] and self.y <= screen_height - 60:
            self.y += self.vertical_speed
            self.is_moving = True
        
        
        if self.is_moving:
            self.update_animation() #-> para atualizar a animação do player hehe
        else:
            #fica no frame 0
            self.current_frame = 0
            self.animation_counter =0
            self.image = self.animation_frames[0]
            
        self.update_rect()
    
    def shoot(self, bullet_type=1):
        return Ammunition(self.x + 15, self.y + 15, bullet_type)