import numpy as np


def DFT(x, N=0):
    '''
    Funcao que implementa a DFT pela definicao. Retorna os coeficientes em modulo
    Recebe como parametros:
        x -> Vetor a ser transformado
        N -> Numero de pontos que deseja-se obter na transformacao
        y -> Vetor com os coeficientes x[k] (Valores retornados em valor absoluto)

    '''

    # Condicoes para garantir o numero minimo de pontos, de maneira que y seja pelo menos do mesmo tamanho de x
    if (not N) or (N<len(x)):
        N = len(x)

    x = np.append(x, np.zeros(N - len(x)))  # Completa X com 0's
    y = np.array([])  # Cria o vetor de saida
    s = 0
    j = 1j

    for k in range(N):
        for n in range(len(x)):
            s += x[n] * np.exp(-j * 2 * np.pi / N * k * n)

        y = np.append(y, np.abs(s))
        s = 0
    return y
