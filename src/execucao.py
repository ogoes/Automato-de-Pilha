class Algoz:

    def __init__(self, entrada, pilha, estado_inicial):

        self.entrada = entrada
        self.pilha = pilha
        self.estado_inicial = estado_inicial
        self.estado_atual = estado_inicial

    def get_estado(self):
        return self.estado_atual

    def get_topo_pilha(self, n):
        aux = []
        for i in range(n):
            aux.append(self.pilha.pop())
        
    def is_finished(self): 
        if self.estado_atual.is_final():
            print("Entrada aceita")
            return 0
    
        if self.pilha.is_empty():
            return 0
    
    def execute(self):
        pass