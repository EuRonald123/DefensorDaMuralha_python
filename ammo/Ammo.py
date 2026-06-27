import pygame

class Ammunition:
    def __init__(self, x, y, bullet_type):
        self.bullet_type = bullet_type
        self.x = x
        self.y = y
        self.active = True
        
        if bullet_type == 1:
            self.image = pygame.image.load('assets/munitions/bala1.png').convert_alpha()
            self.image = pygame.transform.scale(self.image, (8, 20))
            self.damage = 1
            self.base_speed = -13
        else:
            self.image = pygame.image.load('assets/munitions/bala2.png').convert_alpha()
            self.image = pygame.transform.scale(self.image, (15, 29))
            self.damage = 3
            self.base_speed = -3
        
        self.rect = self.image.get_rect()
        self.update_rect()
    
    def update_rect(self):
        self.rect.x = self.x
        self.rect.y = self.y
    
    def bullet_movement(self, time_seconds):
        if self.bullet_type == 1:
            self.y += self.base_speed - (time_seconds / 4)
        else:
            self.y += self.base_speed - (time_seconds / 14)
        self.update_rect()
    
    def off_screen(self):
        #retorna true se a muni saiu da tela
        return self.y <= -30
    
    def drawin(self, screen):
        screen.blit(self.image, (self.x, self.y))