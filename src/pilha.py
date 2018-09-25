class Pilha:
    def __init__(self, inicial):
        self.topo = No(inicial)
        self.tamanho = 1

    def get_topo(self):
        return self.topo

    def get_tamanho(self):
        return self.tamanho

    def is_empty(self):
        if self.tamanho == 0:
            return 1

    def push(self, dado, n = 1):
        for i in range(n):
            no = No(dado[i], proximo = None)
            if self.is_empty():
                self.topo = no

            else:
                no.set_proximo(self.topo)
                self.topo = no

            self.tamanho += 1

    def pop(self, n):
        topos = []
        for i in range(n):
            if self.tamanho == 0:
                print("Impossivel remover")
                return 0

            aux = self.topo
            self.topo = aux.get_proximo()
            aux.set_proximo(None)
            topos.append(aux)

            self.tamanho -= 1

        return topos

    

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