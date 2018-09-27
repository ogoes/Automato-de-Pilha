from estado import Estado
from execucao import Algoz
from pilha import Pilha
from transicao import Transicao
from copy import deepcopy

class Maquina:

	def __init__(self, dados, entrada):
		self.entrada = [entry for entry in entrada]
		self.alfabeto_entrada = dados['alfabeto_entrada']
		self.alfabeto_pilha = dados['alfabeto_pilha']
		self.epsilon = dados['epsilon']
		self.inicial_pilha = dados['inicial_pilha']
		self.estados_tmp = dados['estados']
		self.estado_inicial = dados['estado_inicial']
		self.estados_finais = dados['estados_finais']
		self.transicoes_tmp = dados['transicoes']


		self.estados = []
		for state in self.estados_tmp:
			estado = Estado(state)
			if state == self.estado_inicial:
				self.estado_atual = estado
				estado.set_inicial()
			if state in self.estados_finais:
				estado.set_final()

			self.estados.append(estado)

		self.transicoes = []
		for transition in self.transicoes_tmp:
			for i in self.estados:
				if i.get_nome() == transition['estado_atual']:
					cur_state = i
				if i.get_nome() == transition['estado_destino']:
					new_state = i
								
			simbol_ent = transition['simbolo_corrente']
			simbols_stack = transition['pop_pilha']
			new_simbols_stack = transition['push_pilha']

			self.transicoes.append(Transicao(cur_state, simbol_ent, simbols_stack, new_state, new_simbols_stack))

		self.execucoes = [Algoz(self.entrada, Pilha(self.inicial_pilha), self.estado_atual, self.epsilon)]


	def get_transicoes(self, execucao):
		transitions = []
		for i in self.transicoes:
			if i.get_estado().get_nome() == execucao.get_estado().get_nome():
				transitions.append(i)
		
		simbolos = []
		for i in transitions: 
			if i.get_simbolo_fita() == self.epsilon:
				simbolos.append(i)
			
			if i.get_simbolo_fita() == execucao.get_entrada():
				simbolos.append(i)

		final = []
		for i in simbolos:
			if self.epsilon in i.get_simbolos_pilha():
				final.append(i)
			
			elif execucao.verifica_pilha(i.get_simbolos_pilha()) == 1:
				final.append(i)
		
		return final

	def run (self):

		while True:

			aux_execs = []
			aux_trans = []

			for x in self.execucoes:
				if x.is_finished() == 1:
					print("Entrada aceita", end=' - ')
					x.descricao()
					return 0
			
			rejeitadas = []
			for i in self.execucoes:
				trans = self.get_transicoes(i)

				if len(trans) >= 1:
					aux_execs.append(i)
					aux_trans.append(trans[0])

					for t in trans[1:]:
						aux_execs.append(i.get_copia())
						aux_trans.append(t)
				else:
					rejeitadas.append(i)


			for i in range( len(aux_execs) ):
				aux_execs[i].execute(aux_trans[i])

			self.execucoes = aux_execs
		
			for r in rejeitadas:
				print("Execução Recusada", end=' - ')
				r.descricao()

			if len(aux_trans) == 0:
				print("Entrada Recusada")
				return 1
