import pygame
import random
from config import *
from functions import mensagem, desenha_cobrinha, desenha_comidinha, Upgrade

def snake_game():
    fim_jogo = False
    fim_de_jogo = False

    x1 = largura_tela / 2
    y1 = altura_tela / 2
    x1_mudanca = 0
    y1_mudanca = 0

    cobra = []
    comprimento_cobra = 1

    pontuacao = 0

    comida_x = round(random.randrange(0, largura_tela - block_size) / 20.0) * 20.0
    comida_y = round(random.randrange(0, altura_tela - block_size) / 20.0) * 20.0

    upgrade = Upgrade()
    upgrade.reiniciar()

    contador_frames = 0
    intervalo_aparicao = random.randint(200, 600)





    while not fim_jogo:
        while fim_de_jogo:
            tela.fill(branco)
            mensagem("Você perdeu! Pontuação: " + str(pontuacao) +  "Pressione Q - Quit ou C - Play Again", vermelho)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        fim_jogo = True
                        fim_de_jogo = False
                    if event.key == pygame.K_c:
                        snake_game()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fim_jogo = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and x1_mudanca == 0:
                    x1_mudanca = -block_size
                    y1_mudanca = 0
                elif event.key == pygame.K_RIGHT and x1_mudanca == 0:
                    x1_mudanca = block_size
                    y1_mudanca = 0
                elif event.key == pygame.K_UP and y1_mudanca == 0:
                    y1_mudanca = -block_size
                    x1_mudanca = 0
                elif event.key == pygame.K_DOWN and y1_mudanca == 0:
                    y1_mudanca = block_size
                    x1_mudanca = 0

        if x1 >= largura_tela or x1 < 0 or y1 >= altura_tela or y1 < 0:
            fim_de_jogo = True

        x1 += x1_mudanca
        y1 += y1_mudanca

        tela.fill(preto)
        
        # Verificar se é hora de mostrar o upgrade
        contador_frames += 1
        if contador_frames >= intervalo_aparicao:
            if upgrade.x == -1 and upgrade.y == -1:
                upgrade.posicao_aleatoria()
            contador_frames = 0
            intervalo_aparicao = random.randint(200, 600)

        # Desenhar o upgrade
        if upgrade.upgrade_ativo():
            upgrade.desenhar()

        desenha_comidinha(block_size, comida_x, comida_y)
        cabeca_cobra = []
        cabeca_cobra.append(x1)
        cabeca_cobra.append(y1)
        cobra.append(cabeca_cobra)

        if len(cobra) > comprimento_cobra:
            del cobra[0]

        for segmento in cobra[:-1]:
            if segmento == cabeca_cobra:
                fim_de_jogo = True

        desenha_cobrinha(block_size, cobra)
        mensagem("Pontuação: " + str(pontuacao), vermelho, 10, 10)
        pygame.display.update()

        # Verificar colisão com upgrade
        if x1 == upgrade.x and y1 == upgrade.y:
            
            pontuacao += 50
            upgrade.aplicar_upgrade()
            upgrade.reiniciar()

        upgrade.atualizar()
        
        if x1 == comida_x and y1 == comida_y:
            pontuacao += 10
            comida_x = round(random.randrange(0, largura_tela - block_size) / 20.0) * 20.0
            comida_y = round(random.randrange(0, altura_tela - block_size) / 20.0) * 20.0
            comprimento_cobra += 1

        clock.tick(fps)

    pygame.quit()
    quit()

snake_game()
