class Transicao:
    def __init__(self, estado, simbolo_fita, simbolos_pilha, novo_estado, novos_simbolos_pilha):
        self.estado = estado
        self.simbolo_fita = simbolo_fita
        self.simbolos_pilha = simbolos_pilha
        self.novo_estado = novo_estado
        self.novos_simbolos_pilha = novos_simbolos_pilha

    def set_estado(self, estado):
        self.estado = estado

    def get_estado(self):
        return self.estado

    def set_simbolo_fita(self, simbolo_fita):
        self.simbolo_fita = simbolo_fita

    def get_simbolo_fita(self):
        return self.simbolo_fita

    def set_simbolos_pilha(self, simbolos_pilha):
        self.simbolos_pilha = simbolos_pilha

    def get_simbolos_pilha(self):
        return self.simbolos_pilha

    def set_novo_estado(self, novo_estado):
        self.novo_estado = novo_estado

    def get_novo_estado(self):
        return self.novo_estado

    def set_novos_simbolos_pilha(self, novos_simbolos_pilha):
        self.novos_simbolos_pilha = novos_simbolos_pilha

    def get_novos_simbolos_pilha(self):
        return self.novos_simbolos_pilha

    def mostra(self):
        print(self.estado.get_nome(), self.simbolo_fita, self.simbolos_pilha, self.novo_estado.get_nome(), self.novos_simbolos_pilha)