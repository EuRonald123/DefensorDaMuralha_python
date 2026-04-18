import pygame

class AudioManager:
    def __init__(self):
        pygame.mixer.music.set_volume(0.4)
        pygame.mixer.music.load('assets/audios/musicas/Twisted Metal_ Black _ Music- Main Menu.mp3')

        self.morte1 = pygame.mixer.Sound('assets/audios/hit, morte, etc/morte1.wav')
        self.morte1.set_volume(0.6)

        self.morte2 = pygame.mixer.Sound('assets/audios/hit, morte, etc/morte2.wav')
        self.morte2.set_volume(0.3)

        self.morte3 = pygame.mixer.Sound('assets/audios/hit, morte, etc/morte3.1.wav')
        self.morte3.set_volume(0.3)

        self.tiro = pygame.mixer.Sound('assets/audios/hit, morte, etc/tiro1.wav')
        self.tiro.set_volume(0.3)

        self.colisao_player = pygame.mixer.Sound('assets/audios/hit, morte, etc/dano_personagem.wav')
        self.colisao_player.set_volume(0.3)
    
    def tocar_musica_menu(self):
        pygame.mixer.music.play(-1)
    
    def tocar_musica_pause(self):
        pygame.mixer.music.play(start=8.4)
    
    def parar_musica(self):
        pygame.mixer.music.stop()
    
    def tocar_som_morte(self, tipo_inimigo):
        if tipo_inimigo == 1:
            self.morte1.play()
        elif tipo_inimigo == 2:
            self.morte2.play()
        else:
            self.morte3.play()