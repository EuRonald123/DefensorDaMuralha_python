import pygame

class BarraVida:
    def __init__(self, x, y, largura_max, altura, imagem_path):
        self.x = x
        self.y = y
        self.largura_max = largura_max
        self.altura = altura
        self.imagem_original = pygame.image.load('assets/vida/' + imagem_path).convert_alpha()
    
    def update(self, hp_atual, hp_max):
        if hp_atual <= 0:
            largura = 0
        else:
            largura = int((hp_atual / hp_max) * self.largura_max)
        self.imagem = pygame.transform.scale(self.imagem_original, (largura, self.altura))
    
    def drawin(self, tela):
        tela.blit(self.imagem, (self.x, self.y))