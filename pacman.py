import pygame, model


class PacMan(model.ElementoJogo, model.Ator):

    def __init__(self, tamanho,
                 coluna, linha,
                 eixo_x, eixo_y,
                 velocidade_eixo_x=0, velocidade_eixo_y=0):
        self.tamanho = tamanho
        self.raio = self.tamanho // 2
        self.posicao = model.Posicao(linha=linha,
                                     coluna=coluna)
        self.centro = model.Eixo(eixo_x=eixo_x,
                                 eixo_y=eixo_y)
        self.velocidade = model.Eixo(eixo_x=velocidade_eixo_x,
                                     eixo_y=velocidade_eixo_y)
        self.intencao_movimento = model.Posicao(linha=self.posicao.linha,
                                                coluna=self.posicao.coluna)
        self.abertura_boca = 0
        self.velocidade_abertura_boca = model.VELOCIDADE
        self.velocidade_boca_antes_da_pausa = self.velocidade_abertura_boca

    def aceitar_movimento(self, _=None):
        self.posicao.linha = self.intencao_movimento.linha
        self.posicao.coluna = self.intencao_movimento.coluna

    def calcular_regras(self, _=None):
        self.intencao_movimento.linha += self.velocidade.eixo_y
        self.intencao_movimento.coluna += self.velocidade.eixo_x
        self.centro.eixo_x = int(self.posicao.coluna * self.tamanho + self.raio)
        self.centro.eixo_y = int(self.posicao.linha * self.tamanho + self.raio)

    def esquina(self, _=None):
        pass

    def movimento_boca(self, estado):
        if estado == model.JOGANDO:
            self.velocidade_abertura_boca = self.velocidade_boca_antes_da_pausa
        else:
            self.velocidade_boca_antes_da_pausa = self.velocidade_abertura_boca
            self.velocidade_abertura_boca = 0

    def pintar(self, tela):
        # Desenhar corpo
        pygame.draw.circle(tela, model.AMARELO, (self.centro.eixo_x, self.centro.eixo_y), self.raio)

        # Desenhar boca
        self.abertura_boca += self.velocidade_abertura_boca
        if self.abertura_boca > self.raio:
            self.velocidade_abertura_boca = -model.VELOCIDADE
        elif self.abertura_boca < 0:
            self.velocidade_abertura_boca = model.VELOCIDADE

        canto_da_boca = model.Eixo(eixo_x=self.centro.eixo_x,
                                   eixo_y=self.centro.eixo_y)
        labio_superior = model.Eixo(eixo_x=self.centro.eixo_x + self.raio,
                                    eixo_y=self.centro.eixo_y - self.abertura_boca)
        labio_inferior = model.Eixo(eixo_x=self.centro.eixo_x + self.raio,
                                    eixo_y=self.centro.eixo_y + self.abertura_boca)
        pontos_boca = [canto_da_boca(), labio_superior(), labio_inferior()]
        pygame.draw.polygon(tela, model.PRETO, pontos_boca)

        # Desenhar olho
        raio_olho = self.raio // 10
        eixo_olho = model.Eixo(eixo_x=int(self.centro.eixo_x + self.raio * 0.33),
                               eixo_y=int(self.centro.eixo_y - self.raio * 0.70))
        pygame.draw.circle(tela, model.PRETO, eixo_olho(), raio_olho)

    def processar_eventos(self, eventos, estado):
        if estado == model.JOGANDO:
            for evento in eventos:
                if evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_RIGHT:
                        self.velocidade.eixo_x = model.VELOCIDADE
                    elif evento.key == pygame.K_LEFT:
                        self.velocidade.eixo_x = -model.VELOCIDADE
                    elif evento.key == pygame.K_DOWN:
                        self.velocidade.eixo_y = model.VELOCIDADE
                    elif evento.key == pygame.K_UP:
                        self.velocidade.eixo_y = -model.VELOCIDADE
                elif evento.type == pygame.KEYUP:
                    if (evento.key == pygame.K_RIGHT) or (evento.key == pygame.K_LEFT):
                        self.velocidade.eixo_x = 0
                    elif (evento.key == pygame.K_DOWN) or (evento.key == pygame.K_UP):
                        self.velocidade.eixo_y = 0

    def recusar_movimento(self, _=None):
        self.intencao_movimento.linha = self.posicao.linha
        self.intencao_movimento.coluna = self.posicao.coluna

    def resetar(self):
        self.posicao.linha = 1
        self.posicao.coluna = 1
        self.centro.eixo_x = model.LARGURA // 2
        self.centro.eixo_y = model.ALTURA // 2
        self.velocidade.eixo_x = 0
        self.velocidade.eixo_y = 0
        self.intencao_movimento.linha = self.posicao.linha
        self.intencao_movimento.coluna = self.posicao.coluna
        self.abertura_boca = 0
        self.velocidade_abertura_boca = model.VELOCIDADE
        self.velocidade_boca_antes_da_pausa = self.velocidade_abertura_boca
