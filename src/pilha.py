class Pilha:
    def __init__(self, inicial):
        self.pilha = [inicial]
        self.tamanho = 1

    def get_topo(self):
        return self.pilha[0]

    def get_tamanho(self):
        return self.tamanho

    def is_empty(self):
        if self.tamanho == 0:
            return 1

    def push(self, dado):
        # dado já é um vetor de simbolos

        self.pilha = dado + self.pilha
        self.tamanho += len(dado)

    def pop(self):
        aux = self.pilha[0]
        self.pilha = self.pilha[1:]

        return aux

    def verifica_topo(self, dados): ## verifica o top da pilha sem remover elementos
        # vetor de verificação
        tamanho = len(dados)
        verifica = self.pilha[:tamanho+1]
        
        if dados == verifica:
            return 1
        else:
            return 0;

    
