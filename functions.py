from config import *

from config import *

class Upgrade:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.cor = laranja
        self.duracao = 150
        self.contador_duracao = 0

    def definir_posicao(self):
        self.x = round(random.randrange(0, largura_tela - block_size) / 20.0) * 20.0
        self.y = round(random.randrange(0, altura_tela - block_size) / 20.0) * 20.0

    def desenhar(self):
        if self.x != -1 and self.y != -1:
            pygame.draw.rect(tela, self.cor, [self.x, self.y, block_size, block_size])
    
    def reiniciar(self):
        self.x = -1
        self.y = -1
        self.contador_duracao = 0
    
    def posicao_aleatoria(self):
        self.x = round(random.randrange(0, largura_tela - block_size) / 20.0) * 20.0
        self.y = round(random.randrange(0, altura_tela - block_size) / 20.0) * 20.0

    def aplicar_upgrade(self):
        self.contador_duracao = self.duracao
    
    def upgrade_ativo(self):
        return self.contador_duracao > 0
    
    def atualizar(self):
        if self.contador_duracao > 0:
            self.contador_duracao -= 1
            if self.contador_duracao == 0:
                self.reiniciar()


def mensagem(msg, branco, x=0, y=0):
    texto = fonte.render(msg, True, branco)
    tela.blit(texto, [x, y])

def desenha_cobrinha(block_size, cobra):
    for segmento in cobra:
        pygame.draw.rect(tela, (255, 255, 255), [segmento[0], segmento[1], block_size, block_size])
    
def desenha_comidinha(block_size, comida_x, comida_y):
    pygame.draw.rect(tela, (0, 255, 0), [comida_x, comida_y, block_size, block_size])