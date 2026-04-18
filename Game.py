import pygame
import json
import os
from cryptography.fernet import Fernet
from entities.Player import Player
from entities.Enemies import Enemy
from ammo.Ammo import Ammunition
from lifebar.Life_bar import BarraVida
from audiomanager.Audio_manager import AudioManager

class Game:
    RECORDS_FILE = 'records.enc'
    ENCRYPTION_KEY = b'aeZWx_AV89LkB7mJ3xP5nQ2cH6rT4wY8uK0sD1eF2gI='  # Chave Fernet válida em base64

    def __init__(self):
        pygame.init()
        self.screen_width = 600
        self.screen_height = 600
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption('Defensor da Muralha')
        #icone 
        icon = pygame.image.load('assets/icons/icone.ico')
        pygame.display.set_icon(icon)
        
        
        #clock
        self.clock = pygame.time.Clock()

        self._load_assets()
        self.audio = AudioManager()

        self.font_ui = pygame.font.SysFont('arial', 25, True, True)
        self.font_title = pygame.font.SysFont('arial', 30, True, False)
        self.font_small = pygame.font.SysFont('Wide Latin', 15)
        self.font_game_over = pygame.font.SysFont('Jokerman', 70, True, False)
        self.font_info = pygame.font.SysFont('arial', 25, True, False)
        self.font_info_small = pygame.font.SysFont('arial', 20, True, True)

        self.tempo_record = 0
        self.max_inimigos_mortos = 0
        self.menu_brasas_y = self.screen_height
        
        self._load_records()
        

    def _load_assets(self):
        self.background = pygame.image.load('assets/backgrounds/Fundo1.jpg').convert_alpha()
        self.background = pygame.transform.scale(self.background, (self.screen_width, self.screen_height))

        self.menu = pygame.image.load('assets/backgrounds/menu5.1.jpg').convert_alpha()
        self.menu = pygame.transform.scale(self.menu, (self.screen_width, self.screen_height))

        self.pause_screen = pygame.image.load('assets/backgrounds/menu4.jpg').convert_alpha()
        self.pause_screen = pygame.transform.scale(self.pause_screen, (self.screen_width, self.screen_height))

        self.brasas = pygame.image.load('assets/backgrounds/efeitoFogo.png').convert_alpha()
        self.brasas = pygame.transform.scale(self.brasas, (self.screen_width, self.screen_height))
        
        self.icone_mao = pygame.image.load('assets/icons/mao seta.png').convert_alpha()
        self.icone_mao = pygame.transform.scale(self.icone_mao, (60, 60))
        
        self.menu_credits = pygame.image.load('assets/backgrounds/menu.jpg').convert_alpha()
        self.menu_credits = pygame.transform.scale(self.menu_credits, (self.screen_width, self.screen_height))

    def _load_records(self):
        if os.path.exists(self.RECORDS_FILE):
            try:
                cipher = Fernet(self.ENCRYPTION_KEY)
                with open(self.RECORDS_FILE, 'rb') as f:
                    encrypted_data = f.read()
                    decrypted_data = cipher.decrypt(encrypted_data)
                    data = json.loads(decrypted_data.decode())
                    self.tempo_record = data.get('tempo_record', 0)
                    self.max_inimigos_mortos = data.get('max_inimigos_mortos', 0)
            except:
                self.tempo_record = 0
                self.max_inimigos_mortos = 0
        else:
            self.tempo_record = 0
            self.max_inimigos_mortos = 0

    def _save_records(self):
        data = {
            'tempo_record': self.tempo_record,
            'max_inimigos_mortos': self.max_inimigos_mortos
        }
        cipher = Fernet(self.ENCRYPTION_KEY)
        json_data = json.dumps(data).encode()
        encrypted_data = cipher.encrypt(json_data)
        
        with open(self.RECORDS_FILE, 'wb') as f:
            f.write(encrypted_data)

    def _reset_round(self):
        self.player = Player()
        self.enemies = [Enemy(1, 0), Enemy(2, 0), Enemy(3, 0)]

        self.bullet1 = Ammunition(self.player.x + 15, self.player.y + 15, 1)
        self.bullet2 = Ammunition(self.player.x + 15, self.player.y + 15, 2)
        self.bullet1.active = False
        self.bullet2.active = False

        self.hp_player = 5
        self.hp_player_max = 5
        self.hp_muralha = 10
        self.hp_muralha_max = 10

        self.player_bar = BarraVida(470, 38, 120, 15, 'hp_player.png')
        self.wall_bar = BarraVida(350, 5, 240, 20, 'hp muralha.png')

        self.inimigos_mortos = 0
        self.inimigos_mortos_ganho_hp = 0

        self.timer = 0
        self.tempo_segundos = 0

    def _draw_menu_option(self, text, x, y, is_selected, font_medieval):
        """Desenha uma opção do menu com ícone de mão seta"""
        texto_render = font_medieval.render(text, True, (255, 255, 255))
        self.screen.blit(texto_render, (x, y))
        
        if is_selected:
            #desenha do lado
            self.screen.blit(self.icone_mao, (x+180, y - 16))

    def _sync_bullets_with_player(self):
        if not self.bullet1.active:
            self.bullet1.x = self.player.x + 15
            self.bullet1.y = self.player.y + 15
            self.bullet1.update_rect()
        if not self.bullet2.active:
            self.bullet2.x = self.player.x + 15
            self.bullet2.y = self.player.y + 15
            self.bullet2.update_rect()

    def _gain_hp(self):
        if self.inimigos_mortos_ganho_hp == 15:
            if self.hp_player < 4:
                self.hp_player += 1
            self.inimigos_mortos_ganho_hp = 0

    def _pause(self):
        pause = True
        self.audio.tocar_musica_pause()
        while pause:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    raise SystemExit
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        pause = False
                        self.audio.parar_musica()
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        raise SystemExit

            fonte2_pause = pygame.font.SysFont('Jokerman', 70, True, False)
            fonte_pause = pygame.font.SysFont('Jokerman', 30, True, False)
            texto_pause = fonte2_pause.render('Pause', 2, (255, 255, 255))
            texto1_pause = fonte_pause.render('ESC: sair', 2, (255, 255, 255))
            texto2_pause = fonte_pause.render('ESPAÇO: continuar', 2, (255, 255, 255))

            self.screen.blit(self.pause_screen, (0, 0))
            self.screen.blit(texto2_pause, (20, 490))
            self.screen.blit(texto1_pause, (20, 530))
            self.screen.blit(texto_pause, (190, 50))

            pygame.display.flip()
            self.clock.tick(10)

    def _handle_game_over(self):
        if self.tempo_segundos > self.tempo_record:
            self.tempo_record = int(self.tempo_segundos)
        if self.inimigos_mortos > self.max_inimigos_mortos:
            self.max_inimigos_mortos = int(self.inimigos_mortos)
        
        self._save_records()

        while True:
            self.screen.fill((0, 0, 0))

            texto_atual_recorde = self.font_info.render('Atual         |         Recorde', 2, (255, 255, 255))
            texto_ini_mt = self.font_info.render(str(self.inimigos_mortos), 2, (255, 255, 255))
            texto_kills = self.font_info.render('Kills:', 2, (255, 255, 255))
            texto_max_ini_mt = self.font_info.render(str(self.max_inimigos_mortos), 2, (255, 255, 255))
            texto_max_tempo = self.font_info.render(str(self.tempo_record) + ' s', 2, (255, 255, 255))
            texto_tempo = self.font_info.render('Tempo:', 2, (255, 255, 255))
            texto_temp_atual = self.font_info.render(str(self.tempo_segundos) + ' s', 2, (255, 255, 255))
            texto_game_over = self.font_game_over.render('Fim de Jogo', 2, (255, 255, 255))
            texto_fim1 = self.font_info_small.render('ESC: Desistir', 2, (255, 255, 255))
            texto_fim2 = self.font_info_small.render('M: Nova chance', 2, (255, 255, 255))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    raise SystemExit
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_m:
                        return
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        raise SystemExit

            self.screen.blit(texto_atual_recorde, (220, 260))
            self.screen.blit(texto_kills, (50, 300))
            self.screen.blit(texto_max_ini_mt, (460, 300))
            self.screen.blit(texto_ini_mt, (250, 300))
            self.screen.blit(texto_tempo, (50, 350))
            self.screen.blit(texto_max_tempo, (460, 350))
            self.screen.blit(texto_temp_atual, (250, 350))
            self.screen.blit(texto_game_over, (100, 70))
            self.screen.blit(texto_fim1, (20, 520))
            self.screen.blit(texto_fim2, (20, 550))
            pygame.display.flip()

    def _menu_loop(self):
        self.audio.tocar_musica_menu()
        menu_options = ['Iniciar', 'Pontuações', 'Controles', 'Créditos', 'Sair']
        selected_option = 0
        font_medieval = pygame.font.SysFont('Jokerman', 40, True, False)
        
        while True:
            self.screen.blit(self.menu, (0, 0))
            
            # Animação do fogo
            rel_y = self.menu_brasas_y % self.brasas.get_rect().height
            self.screen.blit(self.brasas, (0, rel_y - self.brasas.get_rect().height))
            if rel_y < self.screen_height:
                self.screen.blit(self.brasas, (0, rel_y))
            self.menu_brasas_y -= 5
            
            # Desenha título
            texto_nome_jogo = self.font_title.render('DEFENSOR DA MURALHA', 2, (255, 255, 255))
            self.screen.blit(texto_nome_jogo, (100, 25))
            
            # Desenha opções do menu 
            start_y = 220
            spacing = 60
            for idx, option in enumerate(menu_options):
                is_selected = (idx == selected_option)
                self._draw_menu_option(option, 15, start_y + (idx * spacing), is_selected, font_medieval)
            
            # Desenha instruções
            texto_instrucao = self.font_small.render('Setas: Navegar | Enter: Confirmar', True, (200, 200, 200))
            self.screen.blit(texto_instrucao, (30, 580))
            
            pygame.display.flip()
            
            # Eventos do menu
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    raise SystemExit
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        selected_option = (selected_option - 1) % len(menu_options)
                    if event.key == pygame.K_DOWN:
                        selected_option = (selected_option + 1) % len(menu_options)
                    if event.key == pygame.K_RETURN:
                        if selected_option == 0:  # Iniciar
                            return
                        elif selected_option == 1:  # Pontuações
                            self._show_pontuacoes()
                        elif selected_option == 2:  # Controles
                            self._show_controles()
                        elif selected_option == 3:  # Créditos
                            self._show_creditos()
                        elif selected_option == 4:  # Sair
                            pygame.quit()
                            raise SystemExit

            self.clock.tick(60)

    def _show_pontuacoes(self):
        """Mostra a tela de pontuações"""
        while True:
            self.screen.fill((0, 0, 0))
            
            texto_titulo = self.font_title.render('PONTUAÇÕES', 2, (255, 255, 255))
            self.screen.blit(texto_titulo, (180, 50))
            
            #Para mostrar os records do arquivo criptografado
            texto_record_tempo = self.font_ui.render(f'Melhor Tempo: {self.tempo_record}s', 2, (144, 238, 144))
            texto_record_kills = self.font_ui.render(f'Máximo de Kills: {self.max_inimigos_mortos}', 2, (144, 238, 144))
            
            self.screen.blit(texto_record_tempo, (30, 200))
            self.screen.blit(texto_record_kills, (30, 240))
            
            texto_esc = self.font_small.render('ESC: Voltar', True, (200, 200, 200))
            self.screen.blit(texto_esc, (30, 580))
            
            pygame.display.flip()
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    raise SystemExit
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        return
            
            self.clock.tick(60)
    
    def _show_controles(self):
        """Mostrar aa tela de controles"""
        while True:
            self.screen.fill((0, 0, 0))
            
            texto_titulo = self.font_title.render('CONTROLES', 2, (255, 255, 255))
            self.screen.blit(texto_titulo, (190, 30))
            
            # Textos dos controles
            controles = [
                'W - Mover para cima',
                'A - Mover para esquerda',
                'S - Mover para baixo',
                'D - Mover para direita',
                '',
                'K - Tiro rápido (fraco)',
                'L - Tiro lento (forte)',
                '',
                'P - Pausar',
            ]
            
            y_pos = 120
            for controle in controles:
                if controle == '':
                    y_pos += 20
                else:
                    texto = self.font_ui.render(controle, True, (255, 200, 100))
                    self.screen.blit(texto, (30, y_pos))
                    y_pos += 40
            
            texto_esc = self.font_small.render('ESC: Voltar', True, (200, 200, 200))
            self.screen.blit(texto_esc, (30, 580))
            
            pygame.display.flip()
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    raise SystemExit
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        return
            
            self.clock.tick(60)
    
    def _show_creditos(self):
        """Mostra a tela de créditos"""
        while True:
            self.screen.blit(self.menu_credits, (0, 0))
            
            texto_producao = self.font_game_over.render('EM PRODUÇÃO', 2, (255, 100, 100))
            self.screen.blit(texto_producao, (100, 220))
            
            texto_esc = self.font_small.render('ESC: Voltar', True, (200, 200, 200))
            self.screen.blit(texto_esc, (30, 580))
            
            pygame.display.flip()
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    raise SystemExit
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        return
            
            self.clock.tick(60)

    def _handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                raise SystemExit
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    raise SystemExit
                if event.key == pygame.K_k:
                    if not self.bullet1.active:
                        self.bullet1.active = True
                        self.audio.tiro.play()
                if event.key == pygame.K_l:
                    if not self.bullet2.active:
                        self.bullet2.active = True
                if event.key == pygame.K_p:
                    self._pause()

    def _update_time(self):
        if self.timer < 60:
            self.timer += 1
        else:
            self.tempo_segundos += 1
            self.timer = 0

    def _update_player(self):
        keys = pygame.key.get_pressed()
        self.player.movement(keys, self.screen_width, self.screen_height)
        self._sync_bullets_with_player()

    def _update_bullets(self):
        if self.bullet1.active:
            self.bullet1.bullet_movement(self.tempo_segundos)
            if self.bullet1.off_screen():
                self.bullet1.active = False
        if self.bullet2.active:
            self.bullet2.bullet_movement(self.tempo_segundos)
            if self.bullet2.off_screen():
                self.bullet2.active = False

    def _update_enemies(self):
        for enemy in self.enemies:
            enemy.update(self.tempo_segundos)
            if enemy.wall_arrived():
                self.hp_muralha -= enemy.wall_damage
                enemy.respawn()

    def _handle_collisions(self):
        damage_to_player = {1: 1, 2: 3, 3: 999}
        for enemy in self.enemies:
            if self.player.rect.colliderect(enemy.rect):
                self.audio.colisao_player.play()
                self.hp_player -= damage_to_player[enemy.enemy_type]
                enemy.respawn()
                self.inimigos_mortos += 1
                self.inimigos_mortos_ganho_hp += 1

        if self.bullet1.active:
            for enemy in self.enemies:
                if self.bullet1.rect.colliderect(enemy.rect):
                    if enemy.receive_damage(self.bullet1.damage):
                        self.audio.tocar_som_morte(enemy.enemy_type)
                        enemy.respawn()
                        self.inimigos_mortos += 1
                        self.inimigos_mortos_ganho_hp += 1
                    self.bullet1.active = False
                    break

        if self.bullet2.active:
            for enemy in self.enemies:
                if self.bullet2.rect.colliderect(enemy.rect):
                    if enemy.receive_damage(self.bullet2.damage):
                        self.audio.tocar_som_morte(enemy.enemy_type)
                        enemy.respawn()
                        self.inimigos_mortos += 1
                        self.inimigos_mortos_ganho_hp += 1
                    self.bullet2.active = False
                    break

    def _update_bars(self):
        self.wall_bar.update(self.hp_muralha, self.hp_muralha_max)
        self.player_bar.update(self.hp_player, self.hp_player_max)

    def _draw(self):
        self.screen.blit(self.background, (0, 0))

        texto_tempo = self.font_small.render('Tempo: ' + str(self.tempo_segundos), 2, (255, 222, 173))
        texto_kills = self.font_small.render('Inimigos mt: ' + str(self.inimigos_mortos), 2, (255, 222, 173))

        if self.bullet1.active:
            self.bullet1.drawin(self.screen)
        if self.bullet2.active:
            self.bullet2.drawin(self.screen)

        for enemy in self.enemies:
            enemy.drawin(self.screen)

        self.player.drawin(self.screen)
        self.wall_bar.drawin(self.screen)
        self.player_bar.drawin(self.screen)
        self.screen.blit(texto_tempo, (5, 10))
        self.screen.blit(texto_kills, (5, 30))
        pygame.display.flip()

    def _game_loop(self):
        self._reset_round()
        self.audio.parar_musica()

        while True:
            self.clock.tick(60)
            self._handle_events()
            self._update_time()
            self._update_player()
            self._update_bullets()
            self._update_enemies()
            self._handle_collisions()
            self._gain_hp()
            self._update_bars()

            if self.hp_player <= 0 or self.hp_muralha <= 0:
                self._handle_game_over()
                return

            self._draw()

    def run(self):
        while True:
            self._menu_loop()
            self._game_loop()
            


if __name__ == '__main__':
    Game().run()
