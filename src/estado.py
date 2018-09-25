class Estado:
    def __init__(self, nome):
        self.nome = nome 
        self.inicial = False
        self.final = False

    def get_nome(self):
        return self.nome

    def set_nome(self, nome):
        self.nome = nome
    
    def is_inicial(self):
        return self.inicial

    def set_inicial(self):
        self.inicial = True

    def is_final(self):
        return self.inicial

    def set_final(self):
        self.inicial = True