from copy import deepcopy
class Algoz:

    def __init__(self, entrada, pilha, estado_inicial, epsilon):

        self.epsilon = epsilon
        self.entrada = entrada # entrada já é um vetor
        self.pilha = pilha
        self.estado_atual = estado_inicial


    def verifica_pilha(self, dados): ## verifica topo da pilha
        return self.pilha.verifica_topo(dados)

    def get_copia(self): ## funcao que faz a copia de uma execucao, com base nos dados atuais dela
        return Algoz(self.entrada, deepcopy(self.pilha), self.estado_atual, self.epsilon)

    def get_pilha(self):
        return self.pilha

    def get_entrada(self): ## retorn elemento na entrada
        if len(self.entrada) >= 1:
            return self.entrada[0]

    def shift(self): ## "consome" simbolo da entrada
        self.entrada = self.entrada[1:]

    def get_estado(self):
        return self.estado_atual

    def is_finished(self): ## verificacao de aceitacao da entrada pela execucao
        if  len(self.entrada) == 0:
            if self.estado_atual.is_final():
                return 1
    
            if self.pilha.is_empty():
                return 1
    
    def descricao(self): ## mostra descricao instantanea da execucao
        print("<", end=' ')
        print(self.estado_atual.get_nome(), end=', ')
        for i in self.entrada:
            print(i, end='')
        print(', ', end='')
        for x in self.pilha.get_pilha():
            print(x, end='')
        print(" >")

    def execute(self, transicao): ## metodo responsavel por executar uma transicao

        simbolo = transicao.get_simbolo_fita() ## simbolo entrada (transicao)
        if simbolo != self.epsilon:
            self.shift() ## consome entrada

        pilha_pop = transicao.get_simbolos_pilha() ## topo da pilha (transicao)
        if self.epsilon in pilha_pop:
            pilha_pop.remove(self.epsilon)
                
        for i in pilha_pop: ## pop para cada simbolo
            self.pilha.pop()

        self.estado_atual = transicao.get_novo_estado() ## novo estado

        pilha_push = transicao.get_novos_simbolos_pilha() ## colocar na pilha
        if self.epsilon in pilha_push:
            pilha_push.remove(self.epsilon)

        self.pilha.push(pilha_push) ## inserir na pilha
