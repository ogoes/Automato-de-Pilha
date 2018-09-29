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
		self.estados_tmp = dados['estados'] ## nomes dos estados 
		self.estado_inicial = dados['estado_inicial']
		self.estados_finais = dados['estados_finais']
		self.transicoes_tmp = dados['transicoes'] ## dicts temporarios das transicoes
		#### Atribuicao dos dados simples ####

		self.estados = []
		for state in self.estados_tmp: ## criar objetos de estado
			estado = Estado(state)
			if state == self.estado_inicial: ## setar estado inicial
				self.estado_atual = estado
				estado.set_inicial()
			if state in self.estados_finais: ## setar estado(s) final(is)
				estado.set_final()

			self.estados.append(estado)

		self.transicoes = []
		for transition in self.transicoes_tmp: ## criar objetos de transicao
			for i in self.estados:
				if i.get_nome() == transition['estado_atual']: ## atribuir estado a transicao
					cur_state = i
				if i.get_nome() == transition['estado_destino']: ## atribuir estado a transicao
					new_state = i
								
			simbol_ent = transition['simbolo_corrente']
			simbols_stack = transition['pop_pilha']
			new_simbols_stack = transition['push_pilha']

			## adicionar uma transicao a lista de transicoes
			self.transicoes.append(Transicao(cur_state, simbol_ent, simbols_stack, new_state, new_simbols_stack))

		## cria a primeira execucao
		self.execucoes = [Algoz(self.entrada, Pilha(self.inicial_pilha), self.estado_atual, self.epsilon)]
		## execucoes sao objetos que possuem pilha, estado e entrada propria
		## caso não haja não determinismo, somente uma execucao sera mantida

	def get_transicoes(self, execucao):
		## coletas as transicoes a partir de uma execucao
		## a coleta esta "dividida" em tres partes: 
					#	coleta das transicoes disponiveis para o estado atual da execucao
					#	coleta das transicoes com o mesmo simbolo de entrada
					#	e no final, coleta das transicoes com os mesmos dados no top da pilha

		estados = []
		for i in self.transicoes: ## coleta das transicoes com base no estado que a execucao esta
			if i.get_estado().get_nome() == execucao.get_estado().get_nome():
				estados.append(i)
		

		# a partir das transicoes disponiveis para o estado atual da execucao
		# a(s) transicao(coes) com o mesmo simbolo de entrada eh(sao) coletada(s)
		simbolos = []
		for i in estados: 
			if i.get_simbolo_fita() == self.epsilon: ## transicoes com "epsilon" sao coletas
				simbolos.append(i)
			
			if i.get_simbolo_fita() == execucao.get_entrada():
				simbolos.append(i)

		# no final as transicoes que tiverem o topo da pilha compativel com o da execucao sao coletadas
		# a partir das transicoes coletadas enteriormente
		pilha = []
		for i in simbolos:
			if self.epsilon in i.get_simbolos_pilha(): ## transicoes com "epsilon" sao coletas
				pilha.append(i)
			
			elif execucao.verifica_pilha(i.get_simbolos_pilha()) == 1: ## verifica topo da pilha
				pilha.append(i)
		
		return pilha

	def run (self):

		while True:

			aux_execs = [] ## vetor auxiliar de execucao
			aux_trans = [] ## vetor auxiliar de transicao

				##	 execucoes[ exec1,  exec2, ...,  execn ]
				##				  ↓		  ↓			   ↓
				##	transicoes[ trans1, trans2, ..., transn ]
				##	
				## 	execucao aplica transicao correspondente no outro vetor


			for x in self.execucoes: ## verificacao de aceitacao das execucoes
				if x.is_finished() == 1:
					print("Entrada aceita", end=' - ')
					x.descricao()
					return 0
			
			rejeitadas = [] ## vetor de execucoes que terminarao (nao havera transicoes disponiveis)
			for i in self.execucoes:

				#### IMPORTANT ####
				## transicoes nao sao compiadas, sao apenas passadas como referencia
				## existe apenas um vetor (que nao eh alterado) com as "verdadeiras" transicoes _> self.transicoes

				trans = self.get_transicoes(i) ## coleta as transicoes a partir de uma execucao

				if len(trans) >= 1: ## caso haja transicoes
					## mantem a execucao, guardando-a no auxiliar de execucoes
					aux_execs.append(i)
					## assim como, definindo qual transicao ira executar
					aux_trans.append(trans[0])

					for t in trans[1:]: ## caso haja mais que uma transicao para aquela execucao
						aux_execs.append(i.get_copia()) ## faz a copia desta
						aux_trans.append(t) ## determina transicao que sera executada por esta copia
				else:
					rejeitadas.append(i) ## caso nao haja transicoes disponiveis a execucao sera rejeitada


			for r in rejeitadas: ## para cada execucao regeitada, e mostrado sua descricao instantanea
				if len(aux_trans) != 0:
					print("Execução Recusada", end=' - ')
					r.descricao()

			if len(aux_trans) == 0: ## caso não haja nenhuma transicao disponivel, nao havera mais execucoes. a entrada foi recusada
				print("Entrada Recusada", end=' - ')
				rejeitadas[0].descricao()
				return 1

			for i in range( len(aux_execs) ): ## loop de execucao
				aux_execs[i].execute(aux_trans[i])

			self.execucoes = aux_execs ## vetor principal de execucoes tem as execucoes que ainda estao "ativas"
		
