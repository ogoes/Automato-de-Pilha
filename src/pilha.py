class Pilha:
    def __init__(self, topo = None):
        if topo != None:
            self.topo = topo
            self.tamanho = 1

    def get_topo(self):
        return self.topo

    def get_tamanho(self):
        return self.tamanho

    def eh_empty(self):
        if self.tamanho == 0:
            return 1

    def push(self, dado):
        no = No(dado, proximo=None)
        if self.eh_empty():
            self.topo = no

        else:
            no.set_proximo(self.topo)
            self.topo = no

        self.tamanho += 1

    def pop(self):
        if self.tamanho == 0:
            print("Impossivel remover")
            return 0

        aux = self.topo
        self.topo = aux.get_proximo()
        aux.set_proximo(None)

        self.tamanho -= 1

        return aux

class No:
    def __init__(self, dado, proximo = None):

        self.dado = dado
        self.proximo = proximo

    def set_proximo(self, proximo):
        self.proximo = proximo

    def get_proximo(self):
        return self.proximo
    
    def set_dado(self, dado):
        self.dado = dado

    def get_dado(self):
        return self.dado