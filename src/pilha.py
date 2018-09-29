class Pilha:
    def __init__(self, inicial):
        self.pilha = [inicial[0]] ## inicia pilha com simbolo
        self.tamanho = 1

    def get_topo(self):
        return self.pilha[0]

    def get_tamanho(self):
        return self.tamanho

    def is_empty(self): ## verifica pilha vazia
        if self.tamanho == 0:
            return 1

    def push(self, dado): ## adiciona um vetor de simbolor na pilha
        # dado já é um vetor de simbolos

        self.pilha = dado + self.pilha
        self.tamanho += len(dado)

    def pop(self): ## remove um elemento da pilha
        aux = self.pilha[0]
        self.pilha = self.pilha[1:]
        self.tamanho -= 1

        return aux

    def verifica_topo(self, dados): ## verifica o topo da pilha sem remover elementos
        # vetor de verificação
        tamanho = len(dados)
        verifica = self.pilha[:tamanho]
        
        if dados == verifica:
            return 1
        else:
            return 0;

    def get_pilha(self):
        return self.pilha
