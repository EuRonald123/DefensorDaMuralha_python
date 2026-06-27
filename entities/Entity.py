import pygame

class Entity:
    def __init__(self, image_path, x, y, hp, width, height, animation_frames=None, animation_speed=5):
        #pega imagem por imagem e adiciona na lista de animação. Bem mais legível
        if animation_frames:
            self.animation_frames = []
            for frame in animation_frames:
                img = pygame.image.load(frame).convert_alpha() 
                img = pygame.transform.scale(img, (width, height))
                self.animation_frames.append(img)
                
            self.image = self.animation_frames[0]
            self.current_frame = 0
            self.animation_counter = 0
            self.animation_speed = animation_speed
            self.is_animated = True
        else:
            self.image = pygame.image.load(image_path).convert_alpha()
            self.image = pygame.transform.scale(self.image, (width, height))
            self.is_animated = False
            

        self.x = x
        self.y = y
        self.hp = hp
        self.rect = self.image.get_rect()
        self.update_rect()
        
        
    def update_animation(self):
        #Atualizar frame da animaçaoo
        if self.is_animated:
            self.animation_counter += 1
            if self.animation_counter >= self.animation_speed:
                self.animation_counter = 0
                self.current_frame = (self.current_frame + 1) % len(self.animation_frames)
                self.image = self.animation_frames[self.current_frame]
            
    def update_rect(self):
        self.rect.x = self.x
        self.rect.y = self.y
        
    def drawin(self, tela):
        tela.blit(self.image, (self.x, self.y))
        
    def receive_damage(self, dano):
        self.hp -= dano
        if self.hp <= 0:
            return True
        else:
            return False
          
