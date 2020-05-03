from pygame import display
from abc import ABCMeta, abstractmethod


# Cores
AMARELO = (255, 255, 0)
AZUL = (0, 0, 255)
CIANO = (0, 255, 255)
BRANCO = (255, 255, 255)
LARANJA = (255, 140, 0)
PRETO = (0, 0, 0)
ROSA = (255, 15, 192)
VERDE = (0, 255, 0)
VERMELHO = (255, 0, 0)

# Métricas
LARGURA = 800
ALTURA = 600
VELOCIDADE = 1
TAMANHO_ATORES = ALTURA // 30

# Direções
ACIMA = 1
ABAIXO = 2
DIREITA = 3
ESQUERDA = 4
CENTRO = 5

# Estados
JOGANDO = 0
PAUSADO = 1
GAMEOVER = 2
VITORIA = 3


class Posicao:

    def __init__(self, linha=0, coluna=0):
        self.linha = linha
        self.coluna = coluna

    def __call__(self):
        return self.linha, self.coluna


class Eixo:

    def __init__(self, eixo_x=0, eixo_y=0):
        self.eixo_x = eixo_x
        self.eixo_y = eixo_y

    def __call__(self):
        return self.eixo_x, self.eixo_y


class Dimensao:

    def __init__(self, largura=0, altura=0):
        self.largura = largura
        self.altura = altura

    def __call__(self):
        return self.largura, self.altura


class ElementoJogo(metaclass=ABCMeta):

    @abstractmethod
    def calcular_regras(self, estado):
        pass

    @abstractmethod
    def pintar(self, tela):
        pass

    @abstractmethod
    def processar_eventos(self, eventos, estado):
        pass


class Ator(metaclass=ABCMeta):

    @abstractmethod
    def aceitar_movimento(self, direcoes_possiveis):
        pass

    @abstractmethod
    def esquina(self, direcoes_possiveis):
        pass

    @abstractmethod
    def recusar_movimento(self, direcoes_possiveis):
        pass


class ValidadorAtor(metaclass=ABCMeta):

    def __init__(self):
        self.atores = []

    def adicionar_ator(self, ator):
        self.atores.append(ator)


class Tela:

    def __init__(self, largura=LARGURA, altura=ALTURA, flags=0, depth=0):
        self.dimensao = Dimensao(largura=largura,
                                 altura=altura)
        self.flags = flags
        self.depth = depth
        self.__tela = self.__criar()

    def __call__(self):
        return self.__tela

    def __criar(self):
        return display.set_mode((self.dimensao.largura, self.dimensao.altura), self.flags, self.depth)