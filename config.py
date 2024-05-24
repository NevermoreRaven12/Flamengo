import pygame
import time
import random   

pygame.init()

# Fonte do Jogo

fonte = pygame.font.SysFont("Arial", 35)

# Pontuação

pontuacao = 0

# Cores

branco = (255, 255, 255)
preto = (0, 0, 0)
vermelho = (213, 50, 80)
verde = (0, 255, 0)
laranja = (255, 165, 0)

#Configurações da tela

largura_tela = 800
altura_tela = 600
tela = pygame.display.set_mode((largura_tela, altura_tela))
pygame.display.set_caption('Snake Game')

#FPS
clock = pygame.time.Clock()
fps = 15

#Tamanho dos Blocos

block_size = 20



