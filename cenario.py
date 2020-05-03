import pygame, model, pacman, fantasma


class Cenario(model.ElementoJogo, model.ValidadorAtor):

    def __init__(self, tela, pacman, tamanho):
        super().__init__()
        self.tela = tela
        self.pacman = pacman
        self.tamanho = tamanho
        self.vidas = 5
        self.pontos = 0
        self.estado = model.JOGANDO
        self.matriz = [
            [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
            [2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2],
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 1, 2],
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 1, 1, 1, 1, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 1, 2],
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 1, 2],
            [2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2],
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 1, 2],
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 1, 2],
            [2, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 2],
            [2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2],
            [2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2],
            [2, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 2],
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 0, 0, 0, 0, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 1, 2],
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 1, 2, 0, 0, 0, 0, 0, 0, 2, 1, 2, 2, 1, 2, 2, 2, 2, 1, 2],
            [2, 1, 1, 1, 1, 1, 1, 2, 2, 1, 2, 0, 0, 0, 0, 0, 0, 2, 1, 2, 2, 1, 1, 1, 1, 1, 1, 2],
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 0, 0, 0, 0, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 1, 2],
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 1, 2],
            [2, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 2],
            [2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2],
            [2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2],
            [2, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 2],
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 1, 2],
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 1, 2],
            [2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2],
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 1, 2],
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 1, 1, 1, 1, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 1, 2],
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 1, 2],
            [2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2],
            [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]
        ]

    def calcular_regras(self, _=None):
        if self.estado == model.JOGANDO:
            self.calcular_regras_jogando()
        elif self.estado == model.PAUSADO:
            self.calcular_regras_pausado()
        elif self.estado == model.GAMEOVER:
            self.calcular_regras_gameover()
        elif self.estado == model.VITORIA:
            self.calcular_regras_vitoria()

    def calcular_regras_gameover(self):
        pass

    def calcular_regras_jogando(self):
        for ator in self.atores:
            intencao_movimento = model.Posicao(linha=ator.intencao_movimento.linha,
                                               coluna=ator.intencao_movimento.coluna)

            direcoes_possiveis = self.obter_direcoes(linha=ator.posicao.linha,
                                                     coluna=ator.posicao.coluna)

            e_esquina = len(direcoes_possiveis) > 2
            e_fantama = isinstance(ator, fantasma.Fantasma)
            posicao_ator_igual_posicao_pacman = ator.posicao.linha == self.pacman.posicao.linha and \
                                                ator.posicao.coluna == self.pacman.posicao.coluna
            venceu = self.pontos == 306
            dentro_da_tela = 0 <= intencao_movimento.coluna < 28 and 0 <= intencao_movimento.linha < 29
            nao_e_parede = self.matriz[intencao_movimento.linha][intencao_movimento.coluna] != 2
            tem_pastilha = self.matriz[intencao_movimento.linha][intencao_movimento.coluna] == 1
            e_pacman = isinstance(ator, pacman.PacMan)

            if e_esquina:
                ator.esquina(direcoes_possiveis)
            if e_fantama and posicao_ator_igual_posicao_pacman:
                self.vidas -= 1
                if not self.vidas:
                    self.estado = model.GAMEOVER
                    self.pacman.movimento_boca(self.estado)
                else:
                    self.pacman.resetar()
            elif venceu:
                self.estado = model.VITORIA
                self.pacman.movimento_boca(self.estado)
            else:
                if dentro_da_tela and nao_e_parede:
                    ator.aceitar_movimento()
                    if tem_pastilha and e_pacman:
                        self.pontos += 1
                        self.matriz[intencao_movimento.linha][intencao_movimento.coluna] = 0
                else:
                    ator.recusar_movimento(direcoes_possiveis)

    def calcular_regras_pausado(self):
        pass

    def calcular_regras_vitoria(self):
        pass

    def escrever(self, texto, tamanho=24, cor=model.AMARELO, nome_fonte='arial', **kwargs):
        pygame.font.init()
        fonte = pygame.font.SysFont(nome_fonte, tamanho, True, False)
        imagem_texto = fonte.render(texto, True, cor)

        direcao = kwargs.get('posicao')
        if direcao is None:
            eixo_x = kwargs.get('eixo_x')
            eixo_y = kwargs.get('eixo_y')
            posicao = model.Eixo(eixo_x=eixo_x,
                                 eixo_y=eixo_y)
        else:
            if direcao == model.CENTRO:
                largura_central = (self.tela.get_width() - imagem_texto.get_width()) // 2
                altura_central = (self.tela.get_height() - imagem_texto.get_height()) // 2
                posicao = model.Eixo(eixo_x=largura_central,
                                     eixo_y=altura_central)

        self.tela.blit(imagem_texto, posicao())

    def obter_direcoes(self, linha, coluna):
        direcoes = []
        linha = int(linha)
        coluna = int(coluna)

        pode_acima = self.matriz[linha - 1][coluna] != 2
        pode_abaixo = self.matriz[linha + 1][coluna] != 2
        pode_direita = self.matriz[linha][coluna + 1] != 2
        pode_esquerda = self.matriz[linha][coluna - 1] != 2

        if pode_acima:
            direcoes.append(model.ACIMA)
        if pode_abaixo:
            direcoes.append(model.ABAIXO)
        if pode_direita:
            direcoes.append(model.DIREITA)
        if pode_esquerda:
            direcoes.append(model.ESQUERDA)

        return direcoes

    def pintar(self, _=None):
        if self.estado == model.JOGANDO:
            self.pintar_jogando()
        elif self.estado == model.PAUSADO:
            self.pintar_jogando()
            self.pintar_pausado()
        elif self.estado == model.GAMEOVER:
            self.pintar_jogando()
            self.pintar_gameover()
        elif self.estado == model.VITORIA:
            self.pintar_jogando()
            self.pintar_vitoria()

    def pintar_gameover(self):
        self.escrever(texto='G A M E  O V E R',
                      posicao=model.CENTRO,
                      cor=model.VERMELHO)

    def pintar_jogando(self):
        for indice_linha, linha in enumerate(self.matriz):
            self.pintar_linha(indice_linha, linha)
        self.pintar_pontos()

    def pintar_linha(self, indice_linha, linha):
        for indice_coluna, coluna in enumerate(linha):
            local = model.Eixo(eixo_x=indice_coluna * self.tamanho,
                               eixo_y=indice_linha * self.tamanho)
            pontos_retangulo = local.eixo_x, local.eixo_y, self.tamanho, self.tamanho
            metade_tamanho = self.tamanho // 2

            cor = model.PRETO
            if coluna == 2:
                cor = model.AZUL
            pygame.draw.rect(self.tela, cor, pontos_retangulo)
            if coluna == 1:
                pygame.draw.circle(self.tela, model.BRANCO,
                                   (local.eixo_x + metade_tamanho, local.eixo_y + metade_tamanho),
                                   self.tamanho // 10)

    def pintar_pausado(self):
        self.escrever(texto='P A U S A D O',
                      posicao=model.CENTRO)

    def pintar_pontos(self):
        self.escrever(texto=f'Score: {self.pontos}',
                      eixo_x=30 * self.tamanho,
                      eixo_y=50)
        self.escrever(texto=f'Vidas: {self.vidas}',
                      eixo_x=30 * self.tamanho,
                      eixo_y=80)

    def pintar_vitoria(self):
        self.escrever(texto='V I T Ó R I A ! ! !',
                      posicao=model.CENTRO,
                      cor=model.VERDE)

    def processar_eventos(self, eventos, _=None):
        for evento in eventos:
            if evento.type == pygame.QUIT:
                exit()
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_p:
                    if self.pacman.velocidade_abertura_boca:
                        self.pacman.velocidade_boca_antes_da_pausa = self.pacman.velocidade_abertura_boca
                    if self.estado == model.JOGANDO:
                        self.estado = model.PAUSADO
                    else:
                        self.estado = model.JOGANDO
                    self.pacman.velocidade_boca_na_pausa = self.pacman.movimento_boca(self.estado)
