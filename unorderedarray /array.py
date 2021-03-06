import numpy as np

class VetorNaoOrdenado:
    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.ultima_posicao = -1
        self.valores = np.empty(self.capacidade, dtype=int)

    # O (n)
    def prints(self):
        if self.ultima_posicao == -1:
            print('O vetor está vazio')
        else:
            for i in range(self.ultima_posicao +1):
                print(f'Posicão: {i} - valor: {self.valores[i]}')

    # O(1) - O (2)
    def insert(self, valor):
        if self.ultima_posicao == self.capacidade -1:
            print('Capacidade maxima atingida')
        else:
            self.ultima_posicao += 1
            self.valores[self.ultima_posicao] = valor

    # O(n)
    def search(self, valor):
        for i in range(self.ultima_posicao + 1):
            if valor == self.valores[i]:
                return i
        return -1


    def delete(self,valor):
        position = self.search(valor)
        if position == -1:
            return -1
        else:
            for i in range(position, self.ultima_posicao):
                self.valores[i] = self.valores[i + 1]

            self.ultima_posicao -= 1


vetor = VetorNaoOrdenado(5)
vetor.prints()
vetor.insert()
vetor.search()
vetor.delete()