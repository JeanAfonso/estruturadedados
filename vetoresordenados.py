import numpy as np


class VetorOrdenado:

    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.ultima_posicao = -1
        self.valores = np.empty(self.capacidade, dtype=int)

    def imprime(self):
        if self.ultima_posicao == -1:
            print("O vetor está vazio")
        else:
            for i in range(self.ultima_posicao + 1):
                print(i, " _ ", self.valores[i])

    # O(n)
    def insere(self, valor):
        if self.ultima_posicao == self.capacidade -1:
            print('Capacidade maxima atingida')
            return

        posicao = 0
        for i in range(self.ultima_posicao + 1): # Para percorrer cada elemento.
            posicao = i
            if self.valores[i] > valor:
                break
            if i == self.ultima_posicao:
               posicao = i + 1

        x = self.ultima_posicao
        while x >= posicao:
            self.valores[x + 1] = self.valores[x]
            x -= 1

        self.valores[posicao] = valor
        self.ultima_posicao += 1

    # O(n)
    def pesquisar(self, valor):
        for i in range(self.ultima_posicao + 1):
            if self.valores[i] > valor or i == self.ultima_posicao:
                return -1
            if self.valores[i] == valor:
                return i

    # O(n)
    def excluir(self, valor):
        posicao = self.pesquisar(valor)
        if posicao == -1:
            return -1  # elemento nao existe entao não é possivel apagar
        else:
            for i in range(posicao, self.ultima_posicao):
                self.valores[i] = self.valores[i + 1]

            self.ultima_posicao -= 1

# teste do vetor

vetor = VetorOrdenado(10)

vetor.insere(6)
vetor.insere(4)
vetor.insere(3)
vetor.insere(5)
vetor.insere(1)
vetor.insere(8)

vetor.pesquisar(3)
vetor.pesquisar(2)
vetor.pesquisar(9)

vetor.excluir(5)
vetor.excluir(9)