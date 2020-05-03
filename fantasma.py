import model
from pygame import draw
from random import choice


class Fantasma(model.ElementoJogo, model.Ator):

    def __init__(self, cor, tamanho):
        self.cor = cor
        self.tamanho = tamanho
        self.posicao = model.Posicao(linha=13,
                                     coluna=15)
        self.intencao_movimento = model.Posicao(linha=self.posicao.linha,
                                          coluna=self.posicao.coluna)
        self.direcao = model.ACIMA
        self.velocidade = model.VELOCIDADE

    def aceitar_movimento(self, _=None):
        self.posicao.linha = self.intencao_movimento.linha
        self.posicao.coluna = self.intencao_movimento.coluna

    def calcular_regras(self, estado):
        if estado == model.JOGANDO:
            vai_acima = self.direcao == model.ACIMA
            vai_abaixo = self.direcao == model.ABAIXO
            vai_direita = self.direcao == model.DIREITA
            vai_esquerda = self.direcao == model.ESQUERDA

            if vai_acima:
                self.intencao_movimento.linha -= self.velocidade
            elif vai_abaixo:
                self.intencao_movimento.linha += self.velocidade
            elif vai_direita:
                self.intencao_movimento.coluna += self.velocidade
            elif vai_esquerda:
                self.intencao_movimento.coluna -= self.velocidade

    def esquina(self, direcoes_possiveis):
        self.mudar_direcao(direcoes_possiveis)

    def mudar_direcao(self, direcoes_possiveis):
        self.direcao = choice(direcoes_possiveis)

    def pintar(self, tela):
        fatia = self.tamanho // 8
        pixel = model.Eixo(eixo_x=int(self.posicao.coluna * self.tamanho),
                           eixo_y=int(self.posicao.linha * self.tamanho))

        # Desenhar corpo
        contorno = [
            (pixel.eixo_x, pixel.eixo_y + self.tamanho),
            (pixel.eixo_x + fatia, pixel.eixo_y + fatia * 2),
            (pixel.eixo_x + fatia * 3, pixel.eixo_y + fatia // 2),
            (pixel.eixo_x + fatia * 4, pixel.eixo_y),
            (pixel.eixo_x + fatia * 5, pixel.eixo_y),
            (pixel.eixo_x + fatia * 6, pixel.eixo_y + fatia // 2),
            (pixel.eixo_x + fatia * 7, pixel.eixo_y + fatia * 2),
            (pixel.eixo_x + self.tamanho, pixel.eixo_y + self.tamanho),
            (pixel.eixo_x + fatia * 8, pixel.eixo_y + fatia * 7),
            (pixel.eixo_x + fatia * 7, pixel.eixo_y + self.tamanho),
            (pixel.eixo_x + fatia * 6, pixel.eixo_y + fatia * 7),
            (pixel.eixo_x + fatia * 5, pixel.eixo_y + self.tamanho),
            (pixel.eixo_x + fatia * 4, pixel.eixo_y + fatia * 7),
            (pixel.eixo_x + fatia * 3, pixel.eixo_y + self.tamanho),
            (pixel.eixo_x + fatia * 2, pixel.eixo_y + fatia * 7),
            (pixel.eixo_x + fatia, pixel.eixo_y + self.tamanho)
        ]
        draw.polygon(tela, self.cor, contorno)

        # Desenhar olhos
        olho_raio_externo = fatia
        olho_raio_interno = fatia // 2
        olho_esquerdo_centro = model.Eixo(eixo_x=int(pixel.eixo_x + fatia * 2.5),
                                          eixo_y=int(pixel.eixo_y + fatia * 3))
        olho_direito_centro = model.Eixo(eixo_x=int(pixel.eixo_x + fatia * 5.5),
                                         eixo_y=int(pixel.eixo_y + fatia * 3))
        draw.circle(tela, model.BRANCO, olho_esquerdo_centro(), olho_raio_externo)
        draw.circle(tela, model.PRETO, olho_esquerdo_centro(), olho_raio_interno)
        draw.circle(tela, model.BRANCO, olho_direito_centro(), olho_raio_externo)
        draw.circle(tela, model.PRETO, olho_direito_centro(), olho_raio_interno)

    def processar_eventos(self, eventos, _=None):
        pass

    def recusar_movimento(self, direcoes_possiveis):
        self.intencao_movimento.linha = self.posicao.linha
        self.intencao_movimento.coluna = self.posicao.coluna
        self.mudar_direcao(direcoes_possiveis)
