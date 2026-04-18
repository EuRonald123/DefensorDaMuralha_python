import pygame
#import os
import random
from pygame.locals import*
#from sys import exit
pygame.init()

#Tela
largura_x,altura_y = 600,600
tela = pygame.display.set_mode((largura_x,altura_y))
#Mudar nome da janela do game
pygame.display.set_caption('Defensores da Muralha')
relogio = pygame.time.Clock()
#Cenário
fundo=pygame.image.load('Background/Fundo1.jpg').convert_alpha()
fundo=pygame.transform.scale(fundo,(largura_x,altura_y))

menu=pygame.image.load('Background/menu5.1.jpg').convert_alpha()
menu=pygame.transform.scale(menu,(largura_x,altura_y))

tela_pause=pygame.image.load('Background/menu4.jpg').convert_alpha()
tela_pause=pygame.transform.scale(tela_pause,(largura_x,altura_y))

brasas=pygame.image.load('Background/efeitoFogo.png').convert_alpha()
brasas=pygame.transform.scale(brasas,(largura_x,altura_y))

#barra de vida
x_barra_vida=240
y_barra_vida=20
barra_vida=pygame.image.load('Vida/hp muralha.png').convert_alpha()
barra_vida=pygame.transform.scale(barra_vida,(x_barra_vida,y_barra_vida))

#barra de vida player
x_barra_vida_player=120
y_barra_vida_player=15
barra_vida_player=pygame.image.load('Vida/hp_player.png').convert_alpha()
barra_vida_player=pygame.transform.scale(barra_vida_player,(x_barra_vida_player,y_barra_vida_player))

#jogadores e inimigos
x_player=40  #tamanho do jogador
y_player=60
player=pygame.image.load('soldados/player/2.png').convert_alpha()
player=pygame.transform.scale(player,(x_player,y_player))

#municoes
x_municao1=8
y_municao1=20
municao1=pygame.image.load('municoes/bala1.png').convert_alpha()
municao1=pygame.transform.scale(municao1,(x_municao1,y_municao1))

x_municao2=15
y_municao2=29
municao2=pygame.image.load('municoes/bala2.png').convert_alpha()
municao2=pygame.transform.scale(municao2,(x_municao2,y_municao2))

#inimigos
x_inimigo1=40
y_inimigo1=60
inimigo1=pygame.image.load('soldados/inimigo1/1.png').convert_alpha()
inimigo1=pygame.transform.scale(inimigo1,(x_inimigo1,y_inimigo1))

x_inimigo2=80
y_inimigo2=100
inimigo2=pygame.image.load('soldados/inimigo2/3.png').convert_alpha()
inimigo2=pygame.transform.scale(inimigo2,(x_inimigo2,y_inimigo2))

x_inimigo3=65
y_inimigo3=80
inimigo3=pygame.image.load('soldados/inimigo3/2.png').convert_alpha()
inimigo3=pygame.transform.scale(inimigo3,(x_inimigo3,y_inimigo3))

#muralha
pos_x_barra_vida=350
pos_y_barra_vida=5
#player
pos_x_barra_vida_player=470
pos_y_barra_vida_player=38

#pos_x_player=(largura_x//2)-(x_player//2)
#pos_y_player=(altura_y//2)-(y_player//2)

#bool
tiro=False
tiro2=False
rodando = False
#rodando1 = True
game_menu = True
fim_jogo = False


#transformando imagens em objetos
player_rect=player.get_rect()
inimigo1_rect=inimigo1.get_rect()
inimigo2_rect=inimigo2.get_rect()
inimigo3_rect=inimigo3.get_rect()
municao1_rect=municao1.get_rect()
municao2_rect=municao2.get_rect()
barra_vida_rect=barra_vida.get_rect()
barra_vida_player_rect=barra_vida_player.get_rect()


#funções
#respawn
def respawn():
    x= random.randint(1,540)
    y= -160
    return [x,y]

def respawn_inimigo2():
    x= random.randint(1,540)
    y= -200
    return [x,y]

def respawn_inimigo3():
    x= random.randint(1,540)
    y= -360
    return [x,y]

def respawn_municao():
    tiro=False
    respawn_municao_x=pos_x_player+15
    respawn_municao_y=pos_y_player+15
    velocidade_mun1=0
    return[tiro,respawn_municao_x,respawn_municao_y,velocidade_mun1]

def respawn_municao2():
    tiro2=False
    respawn_municao_x=pos_x_player+15
    respawn_municao_y=pos_y_player+15
    velocidade_mun2=0
    return[tiro2,respawn_municao_x,respawn_municao_y,velocidade_mun2]

#records
tempo_record=0
max_inimigos_mortos=0


#colisões
def colisao_inimigo1():
    global hp_player
    if player_rect.colliderect(inimigo1_rect):
        hp_player-=1
        return True
    else:
        return False

def colisao_inimigo2():
    global hp_player
    if player_rect.colliderect(inimigo2_rect):
        hp_player-=3
        return True
    else:
        return False
    
def colisao_inimigo3():
    global hp_player
    if player_rect.colliderect(inimigo3_rect):
        hp_player-=hp_player
        return True
    else:
        return False

#colisao municao1 inimigos 1,2 e 3
def colisao_municao_inimigo():
    global hp_inimigo1
    if municao1_rect.colliderect(inimigo1_rect):
        hp_inimigo1-=1
        return True
    else:
        return False

def colisao_municao_inimigo2():
    global hp_inimigo2
    if municao1_rect.colliderect(inimigo2_rect):
        hp_inimigo2-=1
        return True
    else:
        return False
    
    
def colisao_municao_inimigo3():
    global hp_inimigo3
    if municao1_rect.colliderect(inimigo3_rect):
        hp_inimigo3-=1
        return True
    else:
        return False
    

#colisao municao2 inimigos 1,2 e 3    
def colisao_municao2_inimigo():
    global hp_inimigo1
    if municao2_rect.colliderect(inimigo1_rect):
        hp_inimigo1-=3
        return True
    else:
        return False


def atualizar_barra_vida_player():
    #global hp_player
    global barra_vida_player
    #global y_barra_vida_player
    if hp_player <= 0:
        barra_vida_player=pygame.image.load('Vida/hp_player.png').convert_alpha()
        barra_vida_player=pygame.transform.scale(barra_vida_player,(0,y_barra_vida_player))
    else:
        if hp_player >= 1 and hp_player <= 5:
            barra_vida_player=pygame.image.load('Vida/hp_player.png').convert_alpha()
            barra_vida_player=pygame.transform.scale(barra_vida_player,(24 * hp_player,y_barra_vida_player))


def atualizar_barra_vida_muralha():
    #global hp_player
    global barra_vida
    #global y_barra_vida_player
    if hp_muralha <= 0:
        barra_vida=pygame.image.load('Vida/hp muralha.png').convert_alpha()
        barra_vida=pygame.transform.scale(barra_vida,(0,y_barra_vida))
    else:
        if hp_muralha >= 1 and hp_muralha <= 10:
            barra_vida=pygame.image.load('Vida/hp muralha.png').convert_alpha()
            barra_vida=pygame.transform.scale(barra_vida,(24 * hp_muralha,y_barra_vida))
    


def colisao_municao2_inimigo2():
    global hp_inimigo2
    if municao2_rect.colliderect(inimigo2_rect):
        hp_inimigo2-=3
        return True
    else:
        return False

def colisao_municao2_inimigo3():
    global hp_inimigo3
    if municao2_rect.colliderect(inimigo3_rect):
        hp_inimigo3-=3
        return True
    else:
        return False
    

def ganho_hp():

    global inimigos_mortos_ganho_hp
    global hp_player
    if inimigos_mortos_ganho_hp==30:
        if hp_player<4:
            hp_player+=1
            inimigos_mortos_ganho_hp=0
            return True
    else:
        return False

def j_pause():
    pause=True
    #musica_fundo_menu.play(start=8.3)
    #pygame.mixer_music.unpause()
    pygame.mixer_music.play(start=8.4)
    while pause:
        for event in pygame.event.get():
            if event.type == QUIT:  
                pygame.quit()
                quit()
            if event.type == KEYDOWN:
                if event.key == K_SPACE:
                    pygame.time.wait(500)
                    pause=False
                if event.key == K_ESCAPE:
                    pygame.time.wait(1000)
                    pygame.quit()
                    quit()
                    
        fonte2_pause=pygame.font.SysFont('Jokerman', 70, True, False)        
        fonte_pause=pygame.font.SysFont('Jokerman', 30, True, False)
        texto_pause = fonte2_pause.render('Pause', 2, (255,255,255))
        texto1_pause = fonte_pause.render('ESC: sair', 2,(255,255,255))
        texto2_pause = fonte_pause.render('ESPAÇO: continuar', 2,(255,255,255))

        tela.blit(tela_pause,(0,0))
        tela.blit(texto2_pause,(20,490))
        tela.blit(texto1_pause,(20,530))
        tela.blit(texto_pause,(190,50))

        pygame.display.flip()
        relogio.tick(10)


#sons
pygame.mixer.music.set_volume(0.4)
pygame.mixer.music.load('audios/musicas/Twisted Metal_ Black _ Music- Main Menu.mp3')
pygame.mixer.music.play(-1)

#musica_fundo_menu = pygame.mixer.Sound('audios/musicas/Twisted Metal_ Black _ Music- Main Menu.mp3')
#musica_fundo_menu.set_volume(0.05)

audio_morte2 = pygame.mixer.Sound('audios/hit, morte, etc/morte2.wav')
audio_morte2.set_volume(0.3)

audio_morte1 = pygame.mixer.Sound('audios/hit, morte, etc/morte1.wav')
audio_morte1.set_volume(0.6)

audio_morte3 = pygame.mixer.Sound('audios/hit, morte, etc/morte3.1.wav')
audio_morte3.set_volume(0.3)

audio_tiro1 = pygame.mixer.Sound('audios/hit, morte, etc/tiro1.wav')
audio_tiro1.set_volume(0.3)

audio_colisao_player = pygame.mixer.Sound('audios/hit, morte, etc/dano_personagem.wav')
audio_colisao_player.set_volume(0.3)


#fontes
fonte=pygame.font.SysFont('arial', 25, True, True)
fonte_nm_jg=pygame.font.SysFont('arial', 30, True, False)
fonte_tp_kills=pygame.font.SysFont('Wide Latin',15)
fonte_game_over=pygame.font.SysFont('Jokerman', 70, True, False)
fonte2=pygame.font.SysFont('arial', 25, True, False)
fonte3=pygame.font.SysFont('arial', 20, True, True)

#tela_menu
while game_menu:

    texto = fonte.render('Pressione ESPAÇO para iniciar', True, (255,255,255))
    texto_nome_jogo=fonte_nm_jg.render('DEFENSOR DA MURALHA',2,(255,255,255))
    

    tela.blit(menu,(0,0))
    tela.blit(texto,(100,420))
    tela.blit(texto_nome_jogo,(100,25))

    rel_y = altura_y % brasas.get_rect().height
    tela.blit(brasas,(0, rel_y-brasas.get_rect().height))
    if rel_y<600:
        tela.blit(brasas, (0, rel_y))
    altura_y-=0.08
    
    
    #tela.blit(brasas,(0,0))

    pygame.display.flip()
    

    
    for event in pygame.event.get():
        if event.type == QUIT:
            #game_menu=False
            pygame.quit()
            quit()
        if event.type == KEYDOWN:
            if event.key == K_SPACE:
                #game_menu=False
                rodando=True

    #Loop principal
    while rodando:
        pos_x_player,pos_y_player=280,270

        pos_x_inimigo1=(200)
        pos_y_inimigo1=(-160)

        pos_x_inimigo2=(200)
        pos_y_inimigo2=(-400)

        pos_x_inimigo3=(200)
        pos_y_inimigo3=(-650)

        velocidade_mun1=0
        pos_x_municao1=pos_x_player+15
        pos_y_municao1=pos_y_player+15

        velocidade_mun2=0
        pos_x_municao2=pos_x_player+15
        pos_y_municao2=pos_y_player+15

        #Vidas
        hp_inimigo1=2
        hp_player=5
        hp_muralha=10
        hp_inimigo2=5
        hp_inimigo3=8

        #inimigos mortos
        inimigos_mortos=0
        inimigos_mortos_ganho_hp=0

        #tempo
        timer=0
        tempo_segundos=0
        
        while rodando:
            #musica_fundo_menu.stop()
            pygame.mixer_music.stop()
            tela.blit(fundo, (0,0))
            relogio.tick(60)
            


            #textos
            texto=fonte_tp_kills.render('Tempo: '+str(tempo_segundos),2,(255,222,173))

            texto_ini_mt=fonte_tp_kills.render('Inimigos mt: '+str(inimigos_mortos),2,(255,222,173))

            

            
            for event in pygame.event.get():
                #teclas pressionar uma vez
                if event.type == QUIT:
                    #rodando=False
                    #game_menu=False
                    pygame.quit()
                    quit()
                
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        #rodando=False
                        #game_menu=False
                        pygame.quit()
                        quit()
                        
                    
                    #tiro
                    if event.key == K_k:
                        tiro=True
                        velocidade_mun1=-13-(tempo_segundos/4) #mudar a velocidade da munição aquiii!!!
                        if pos_y_municao1==pos_y_player+15 and pos_x_municao1==pos_x_player+15:
                            audio_tiro1.play()
                    if event.key == K_l:
                        tiro2=True
                        velocidade_mun2=-3-(tempo_segundos/14)  #mudar a velocidade da munição aquiii!!!

                    if event.key == K_p:
                        j_pause()


            #tempo
            if timer<60:
                timer+=1
            else:
                tempo_segundos+=1
                timer=0



            #teclas manter pressionado
            tecla=pygame.key.get_pressed()
            
            #movimento do player+colisão limite mapa
            if tecla[K_a]:
                if pos_x_player>=0:
                    pos_x_player-=7   #velocidade player
                    if not tiro:
                        pos_x_municao1-=7
                    if not tiro2:
                        pos_x_municao2-=7

            if tecla[K_d]:
                if pos_x_player<=600-x_player:
                    pos_x_player+=7#velocidade player
                    if not tiro:
                        pos_x_municao1+=7
                    if not tiro2:
                        pos_x_municao2+=7

            if tecla[K_w]:
                if pos_y_player>=0:
                    pos_y_player-=6 #velocidade player
                    if not tiro:
                        pos_y_municao1-=6
                    if not tiro2:
                        pos_y_municao2-=6
                    
            if tecla[K_s]:
                if pos_y_player<=600-y_player:
                    pos_y_player+=6#velocidade player
                    if not tiro:
                        pos_y_municao1+=6
                    if not tiro2:
                        pos_y_municao2+=6
                
            #retangulo dos personagens seguindo
            player_rect.x=pos_x_player
            player_rect.y=pos_y_player

            inimigo1_rect.x=pos_x_inimigo1
            inimigo1_rect.y=pos_y_inimigo1

            municao1_rect.x=pos_x_municao1
            municao1_rect.y=pos_y_municao1

            municao2_rect.x=pos_x_municao2
            municao2_rect.y=pos_y_municao2

            inimigo2_rect.x=pos_x_inimigo2
            inimigo2_rect.y=pos_y_inimigo2

            inimigo3_rect.x=pos_x_inimigo3
            inimigo3_rect.y=pos_y_inimigo3



            if hp_player<=0 or hp_muralha<=0:
                fim_jogo=True
                if tempo_segundos > tempo_record:
                    tempo_record = int(tempo_segundos)
                if inimigos_mortos > max_inimigos_mortos:
                    max_inimigos_mortos = int(inimigos_mortos)


            while fim_jogo:
                tela.fill((0,0,0))


                texto_atual_recorde=fonte2.render('Atual         |         Recorde', 2, (255,255,255))
                texto_ini_mt=fonte2.render(str(inimigos_mortos),2,(255,255,255))
                texto_kills=fonte2.render('Kills:',2,(255,255,255))
                texto_max_ini_mt=fonte2.render(str(max_inimigos_mortos),2,(255,255,255))
                texto_max_tempo=fonte2.render(str(tempo_record)+' s',2,(255,255,255))
                texto_tempo=fonte2.render('Tempo:',2,(255,255,255))
                texto_temp_atual=fonte2.render(str(tempo_segundos)+' s',2,(255,255,255))
                texto_gameOver=fonte_game_over.render('Fim de Jogo',2,(255,255,255))
                texto_fim1=fonte3.render('ESC: Desistir',2,(255,255,255))
                texto_fim2=fonte3.render('M: Nova chance',2,(255,255,255))

                for event in pygame.event.get():
                    if event.type == QUIT:
                        pygame.quit()
                        quit()
                    if event.type == KEYDOWN:
                        if event.key == K_m:
                            rodando=False
                            fim_jogo=False
                            pygame.mixer_music.play()
                        if event.key == K_ESCAPE:
                            pygame.quit()
                            quit()

                tela.blit(texto_atual_recorde,(220,260))
                tela.blit(texto_kills,(50,300))
                tela.blit(texto_max_ini_mt,(460,300))
                tela.blit(texto_ini_mt,(250,300))
                tela.blit(texto_tempo,(50,350))
                tela.blit(texto_max_tempo,(460,350))
                tela.blit(texto_temp_atual,(250,350))
                tela.blit(texto_gameOver,(100,70))
                tela.blit(texto_fim1,(20,520))
                tela.blit(texto_fim2,(20,550))
                pygame.display.flip()
                #pygame.time.wait(5000)

                
       
            #respawn inimigo colisão player
            if colisao_inimigo1()==True:
                audio_colisao_player.play()
                pos_x_inimigo1 = respawn()[0]
                pos_y_inimigo1 = respawn()[1]
                hp_inimigo1=2
                inimigos_mortos+=1
                inimigos_mortos_ganho_hp+=1
                


            if colisao_inimigo2()==True:
                audio_colisao_player.play()
                pos_x_inimigo2 = respawn_inimigo2()[0]
                pos_y_inimigo2 = respawn_inimigo2()[1]
                hp_inimigo2=5
                inimigos_mortos+=1
                inimigos_mortos_ganho_hp+=1

            if colisao_inimigo3()==True:
                audio_colisao_player.play()
                pos_x_inimigo3 = respawn_inimigo3()[0]
                pos_y_inimigo3 = respawn_inimigo3()[1]
                hp_inimigo3=8
                inimigos_mortos+=1
                inimigos_mortos_ganho_hp+=1

            #respawn inimigo colisão municao + sistema de vida
            #colisao municao inimigo
            if hp_inimigo1>0:
                if colisao_municao_inimigo()==True:
                    tiro,pos_x_municao1,pos_y_municao1,velocidade_mun1=respawn_municao()
            if hp_inimigo1<=0:
                audio_morte1.play()
                pos_x_inimigo1 = respawn()[0]
                pos_y_inimigo1 = respawn()[1]
                inimigos_mortos+=1
                inimigos_mortos_ganho_hp+=1
                hp_inimigo1=2
                tiro,pos_x_municao1,pos_y_municao1,velocidade_mun1=respawn_municao()

            #colisao inimigo2
            if hp_inimigo2>0:
                if colisao_municao_inimigo2()==True:
                    tiro,pos_x_municao1,pos_y_municao1,velocidade_mun1=respawn_municao()
            if hp_inimigo2<=0:
                audio_morte2.play()
                pos_x_inimigo2 = respawn_inimigo2()[0]
                pos_y_inimigo2 = respawn_inimigo2()[1]
                inimigos_mortos+=1
                inimigos_mortos_ganho_hp+=1
                hp_inimigo2=5
                tiro,pos_x_municao1,pos_y_municao1,velocidade_mun1=respawn_municao()

            #colisao inimigo3
            if hp_inimigo3>0:
                if colisao_municao_inimigo3()==True:
                    tiro,pos_x_municao1,pos_y_municao1,velocidade_mun1=respawn_municao()
            if hp_inimigo3<=0:
                audio_morte3.play()
                pos_x_inimigo3 = respawn_inimigo3()[0]
                pos_y_inimigo3 = respawn_inimigo3()[1]
                inimigos_mortos+=1
                inimigos_mortos_ganho_hp+=1
                hp_inimigo3=8
                tiro,pos_x_municao1,pos_y_municao1,velocidade_mun1=respawn_municao()

            #colisao municao2 inimigo1
            if hp_inimigo1>0:
                if colisao_municao2_inimigo()==True:
                    tiro2,pos_x_municao2,pos_y_municao2,velocidade_mun2=respawn_municao2()
            if hp_inimigo1<=0:
                audio_morte1.play()
                pos_x_inimigo1 = respawn()[0]
                pos_y_inimigo1 = respawn()[1]
                inimigos_mortos+=1
                inimigos_mortos_ganho_hp+=1
                hp_inimigo1=2
                tiro2,pos_x_municao2,pos_y_municao2,velocidade_mun2=respawn_municao2()

            #colisao municao2 inimigo2
            if hp_inimigo2>0:
                if colisao_municao2_inimigo2()==True:
                    tiro2,pos_x_municao2,pos_y_municao2,velocidade_mun2=respawn_municao2()
            if hp_inimigo2<=0:
                audio_morte2.play()
                pos_x_inimigo2 = respawn_inimigo2()[0]
                pos_y_inimigo2 = respawn_inimigo2()[1]
                inimigos_mortos+=1
                inimigos_mortos_ganho_hp+=1
                hp_inimigo2=5
                tiro2,pos_x_municao2,pos_y_municao2,velocidade_mun2=respawn_municao2()

            #colisao municao2 inimigo3
            if hp_inimigo3>0:
                if colisao_municao2_inimigo3()==True:
                    tiro2,pos_x_municao2,pos_y_municao2,velocidade_mun2=respawn_municao2()
            if hp_inimigo3<=0:
                audio_morte3.play()
                pos_x_inimigo3 = respawn_inimigo3()[0]
                pos_y_inimigo3 = respawn_inimigo3()[1]
                inimigos_mortos+=1
                inimigos_mortos_ganho_hp+=1
                hp_inimigo3=8
                tiro2,pos_x_municao2,pos_y_municao2,velocidade_mun2=respawn_municao2()


            if pos_y_inimigo1 >= 540:
                pos_x_inimigo1,pos_y_inimigo1 = respawn()[0],respawn()[1]
                hp_inimigo1=2
                hp_muralha-=1
            
            if pos_y_inimigo2 >= 500:
                pos_x_inimigo2,pos_y_inimigo2 = respawn()[0],respawn()[1]
                hp_inimigo2=5
                hp_muralha-=3

            if pos_y_inimigo3 >= 480:
                pos_x_inimigo3,pos_y_inimigo3 = respawn_inimigo3()[0],respawn_inimigo3()[1]
                hp_inimigo3=8
                hp_muralha-=7

            if pos_y_municao1<=-20:
                tiro,pos_x_municao1,pos_y_municao1,velocidade_mun1=respawn_municao()
            
            if pos_y_municao2<=-25:
                tiro2,pos_x_municao2,pos_y_municao2,velocidade_mun2=respawn_municao2()

            ganho_hp()

            
            
            #condição barra de vida da muralha diminuir
            atualizar_barra_vida_muralha()

            #condição barra de vida do player diminuir
            atualizar_barra_vida_player()
            
                
            
                
            #velocidade de movimento inimigos e restos
            pos_y_municao1+=velocidade_mun1#não mude a velocidade aqui!
            pos_y_municao2+=velocidade_mun2#não mude a velocidade aqui!


            pos_y_inimigo1+=(tempo_segundos/19)
            pos_y_inimigo2+=(tempo_segundos/28)
            pos_y_inimigo3+=(tempo_segundos/60)

            #pygame.draw.rect(tela,(255,0,127),(inimigo3_rect),2)
            #pygame.draw.rect(tela,(255,0,255),(inimigo2_rect),2)
            #pygame.draw.rect(tela,(255,0,0),(player_rect),2)
            #pygame.draw.rect(tela,(255,0,255),(inimigo1_rect),2)
            #pygame.draw.rect(tela,(100,255,255),(municao1_rect),2)
            #pygame.draw.rect(tela,(100,255,255),(municao2_rect),2)
            

            #verificadores

            #print(f'{pos_y_inimigo1:.6f}')
            #print(relogio)
            #print(tempo_segundos)
            #print(inimigos_mortos)
            #print(inimigos_mortos_ganho_hp)
            #print(hp_inimigo2)
            #print(hp_muralha)
            #print(hp_inimigo1)
            #print(hp_player)
            #print(tempo_record)
            #print(pos_y_player)



            tela.blit(municao1,(pos_x_municao1,pos_y_municao1))
            tela.blit(municao2,(pos_x_municao2,pos_y_municao2))
            tela.blit(inimigo1,(pos_x_inimigo1,pos_y_inimigo1))
            tela.blit(inimigo2,(pos_x_inimigo2,pos_y_inimigo2))
            tela.blit(inimigo3,(pos_x_inimigo3,pos_y_inimigo3))
            tela.blit(player,(pos_x_player,pos_y_player))
            tela.blit(barra_vida,(pos_x_barra_vida,pos_y_barra_vida))
            tela.blit(barra_vida_player,(pos_x_barra_vida_player,pos_y_barra_vida_player))
            tela.blit(texto,(5,10))
            tela.blit(texto_ini_mt,(5,30))
            #tela.blit(texto_max_ini_mt,(5,55))




            pygame.display.flip()




