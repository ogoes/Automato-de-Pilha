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
				trasintions.append(i)
			
		simbolos = []
		for i in transitions: 
			if i.get_simbolo_fita() == self.epsilon:
				simbolos.append(i)
			
			if i.get_simbolo_fita() == execucao.get_entrada()
				simbolos.append(i)

		final = []
		for i in simbolos:
			if i.get_simbolos_fita()[0] == self.epsilon:
				final.append(i)
			
			if execucao.get_pilha().verifica_topo(i.get_simbolos_fita()) == 1:
				final.append(i)
				
		return final

	def run (self):

		while True:
			
			aux_execs = []
			aux_trans = []
			for i in self.execucoes:
				if i.is_finised():
					print("Entrada aceita")
					return 0
				else:
					trans = self.get_transicoes(i)

					if len(trans) == 1:
						aux_execs.append(i)
						aux_trans.append(trans[0])
					elif len(trans) > 1:
						aux_execs.append(i)
						aux_trans.append(trans[0])

						for t in trans[1:]:
							aux_execs.append(deepcopy(i))
							aux_trans.append(t)

			self.execucoes = aux_execs
			for (i, execs) in enumerate(self.execucoes):
				execs.execute(aux_trans[i])
		