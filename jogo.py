import pygame, model
from cenario import Cenario
from pacman import PacMan
from fantasma import Fantasma


class Jogo:

    def __init__(self):
        pygame.init()
        self.tela = model.Tela()
        self.pacman = PacMan(tamanho=model.TAMANHO_ATORES,
                             linha=1, coluna=1,
                             eixo_x=model.LARGURA // 2, eixo_y=model.ALTURA // 2,
                             velocidade_eixo_x=0, velocidade_eixo_y=0)
        qtd_linhas = 600 // 30
        self.cenario = Cenario(tela=self.tela(),
                               pacman=self.pacman,
                               tamanho=qtd_linhas)

    def game_loop(self):
        blinky = Fantasma(cor=model.VERMELHO,
                          tamanho=model.TAMANHO_ATORES)
        inky = Fantasma(cor=model.CIANO,
                        tamanho=model.TAMANHO_ATORES)
        clyde = Fantasma(cor=model.LARANJA,
                         tamanho=model.TAMANHO_ATORES)
        pinky = Fantasma(cor=model.ROSA,
                         tamanho=model.TAMANHO_ATORES)

        self.cenario.adicionar_ator(self.pacman)
        self.cenario.adicionar_ator(blinky)
        self.cenario.adicionar_ator(inky)
        self.cenario.adicionar_ator(clyde)
        self.cenario.adicionar_ator(pinky)
        while True:
            # Calcular regras
            self.cenario.calcular_regras()
            blinky.calcular_regras(self.cenario.estado)
            inky.calcular_regras(self.cenario.estado)
            clyde.calcular_regras(self.cenario.estado)
            pinky.calcular_regras(self.cenario.estado)
            self.pacman.calcular_regras()

            # Pinta
            self.tela().fill(model.PRETO)
            self.cenario.pintar(self.tela())
            self.pacman.pintar(self.tela())
            blinky.pintar(self.tela())
            inky.pintar(self.tela())
            clyde.pintar(self.tela())
            pinky.pintar(self.tela())
            pygame.display.update()
            pygame.time.delay(100)

            # Eventos
            eventos = pygame.event.get()
            self.cenario.processar_eventos(eventos)
            self.pacman.processar_eventos(eventos, self.cenario.estado)


if __name__ == '__main__':

    jogo = Jogo()
    jogo.game_loop()
