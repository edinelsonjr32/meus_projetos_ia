import numpy as np


class VetorOrdenado:
    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.ultima_posicao = -1
        self.valores = np.empty(self.capacidade, dtype=int)

    def imprime(self):
        if self.ultima_posicao == -1:
            print("Vetor vazio")
        else:
            for i in range(self.ultima_posicao + 1):
                print(i, '-', self.valores[i])

    def insere(self, valor):
        if self.ultima_posicao == self.capacidade - 1:
            print('capacidade máxima atingida')
            return
        posicao = 0
        for i in range(self.ultima_posicao + 1):
            posicao = i
            if self.valores[i] > valor:
                break
            if i == self.ultima_posicao:
                posicao = i + 1
        x = self.ultima_posicao

        while x >= posicao:
            self.valores[x+1] = self.valores[x]
            x -= 1
        self.valores[posicao] = valor
        self.ultima_posicao += 1


vetor = VetorOrdenado(10)
vetor.insere(4)
vetor.insere(3)
vetor.insere(10)
vetor.insere(1)
vetor.insere(7)
vetor.insere(5)
vetor.insere(8)

vetor.imprime()
