import numpy as np


class FilaPrioridade:

    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.numero_elementos = 0
        self.valores = np.empty(self.capacidade, dtype=int)

    def __fila_vazia(self):
        return self.numero_elementos == 0

    def __fila_cheia(self):
        return self.numero_elementos == self.capacidade

    def enfileirar(self, valor):
        if self.__fila_cheia():
            print('A fila está cheia')
            return
        # se a fila estiver vazia adiciona o valor na primeira posicao do vetor,
        # e incrementamos o numero de elementos.
        if self.numero_elementos == 0:
            self.valores[self.numero_elementos] = valor
            self.numero_elementos += 1
        else:
            '''
            senão, enquanto x(que recebe a posicao[indice] que é igual ao numero de elementos -1,
            for maior ou igual que 0, e se o valor que eu recebi for maior que o primeiro valor do meu vetor
            na posicao [x - ou seja ultima posicao/primeira], nós remanejamos os valores do vetor usando o 
            self.valores[x + 1] = self.valores[x] --> Aqui passamos o valor para o lado direito para colocarmos
            o valor maior no indice correto na fila de prioridade.
            '''
            x: int = self.numero_elementos - 1
            while x >= 0:
                if valor > self.valores[x]:
                    self.valores[x + 1] = self.valores[x]
                else:
                    break
                # Decrementa o valor do x que é pra fazer o controle
                # de quantos remanjamentos que fazemos
                x -= 1
            # Fora do while quando o valor for menor que os numeros do nosso vetor
            # nós adicionamos ele na primeira posicao e aumentamos o contador
            # numero de elementos para sabermos a quantidade de elementos e controlarmos os indices.
            self.valores[x + 1] = valor
            self.numero_elementos += 1

    def desenfileirar(self):
        if self.__fila_vazia():
            print('A fila está vazia')
            return
        # Se não estiver vazia, vamos buscar o valor que vamos desenfileirar
        # que é o primeiro elemento/ultimo e decrementamos o numero de elementos
        valor = self.valores[self.numero_elementos - 1]
        self.numero_elementos -= 1
        return valor

    def primeiro(self):
        if self.__fila_vazia():
            return -1
        # Mostra o valor [indice igual ao numero de elementos -1],
        # ou seja o primeiro elemento
        return self.valores[self.numero_elementos - 1]


# Debug/teste

fila = FilaPrioridade(5)
print(fila.primeiro())
# 30
fila.enfileirar(30)
print(fila.primeiro())
# 50 30
fila.enfileirar(50)
print(fila.primeiro())
# Tradicional: 10 50 30
# Prioridade: 50 30 10
fila.enfileirar(10)
print(fila.primeiro())
print(fila.valores)
# Tradicional: 40 10 50 30
# Prioridade: 50 40 30 10
fila.enfileirar(40)
print(fila.primeiro())
print(fila.valores)
# Tradicional: 20 40 10 50 30
# Prioridade: 50 40 30 20 10
fila.enfileirar(20)
print(fila.primeiro())
print(fila.valores)
fila.enfileirar(2)
fila.desenfileirar()
print(fila.primeiro())
fila.desenfileirar()
print(fila.primeiro())
fila.desenfileirar()
print(fila.primeiro())
print(fila.valores)
fila.enfileirar(5)
print(fila.primeiro())
print(fila.valores)

