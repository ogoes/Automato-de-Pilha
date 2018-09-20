#!/usr/bin/python3
import sys
from pprint import pprint
from maquina import Maquina


def readlines(filename):
	file = open(filename)

	lines = [line.strip() for line in file.readlines()]
	dados = {   'alfabeto_entrada': lines[0].split(' '),
				'alfabeto_pilha': lines[1].split(' '),
				'epsilon': lines[2].replace(' ', ''),
				'inicial_pilha': lines[3].split(' '),
				'estados': lines[4].split(' '),
				'estado_inicial': lines[5],
				'estados_finais': lines[6].split(' '),
				'transicoes': []
			}


	dados['transicoes'] = []
	for line in lines[ 7: ]:
		spliteds = line.split(' ')

		transitions = {
						'estado_atual': spliteds[0],
						'simbolo_corrente': spliteds[1],
						'pop_pilha': [],
						'estado_destino': spliteds[3],
						'push_pilha': []
		}
		if spliteds[2] != dados['epsilon']:
			aux = spliteds[2][0:7]
			if aux == dados['epsilon']:
				transitions['pop_pilha'].append(aux)
				transitions['pop_pilha'] += [sin for sin in spliteds[2][7:]]
			else:
				transitions['pop_pilha'] += [sin for sin in spliteds[2]]
		else:
			transitions['pop_pilha'] = [dados['epsilon']]


		if spliteds[4] != dados['epsilon']:
			aux = spliteds[4][0:7]
			if aux == dados['epsilon']:
				transitions['push_pilha'] = [sin for sin in spliteds[4][:6:-1]]
				transitions['push_pilha'].append(aux)
			else:
				transitions['push_pilha'] += [sin for sin in spliteds[4][::-1]]
		else:
			transitions['push_pilha'] = [dados['epsilon']]


		dados['transicoes'].append(transitions)

	return dados

if __name__ == "__main__":

	if len(sys.argv) < 3:
		print("Chamada de execução:\n\t\t\t$ ./main.py config.txt \"entrada\"\n")
		exit(1)

	configuracoes = readlines(sys.argv[1])
	machine = Maquina(configuracoes, sys.argv[2].strip('"'))
