from estado import Estado
from execucao import Algoz
from pilha import Pilha
from transicao import Transicao

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
			state = transition['estado_atual']
			simbol_ent = transition['simbolo_corrente']
			simbols_stack = transition['pop_pilha']
			new_state = transition['estado_destino']
			new_simbols_stack = transition['push_pilha']

			self.transicoes.append(Transicao(state, simbol_ent, simbols_stack, new_state, new_simbols_stack))

		self.execucoes = [Algoz(self.entrada, Pilha(self.inicial_pilha), self.estado_atual)]


	pass