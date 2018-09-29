# Autômato de Pilha
Projeto para a matéria de Linguagens Formais, Autômatos e Computabilidade
Desenvolvido por Dennis Urtubia, Jorge Rossi e Otávio Goes.

Dado uma descrição de funcionamento de um Autômato de Pilha e uma entrada para verficação, o programa escrito em Python efetua as possíveis transições entre os estados e retorna rejeição ou aceitação por estado final ou pilha vazia.

# Funcionamento do código fonte
A estrutura do programa foi definida em 5 classes e a main.
As classes mais importantes do código são a de controle de execuções (maquina.py) e as execuções em si (execucoes.py)

- ##### maquina.py
    No início desta classe, temos o método construtor da classe que é responsável por fazer a atribuição dos dados na máquina, define os estados iniciais e finais

- ##### execucao.py
    Nesse arquivo se encontra a classe ```Algoz```, a qual representa um fluxo de execução da máquina. A mesma recebe como argumentos do método construtor a entrada da fita, a pilha e o estado atual. O método mais importante é o ```execute```, onde de fato a transição é executada. Primeiramente, o símbolo da fita da transição é lido e removido da fita (shift), a menos que seja um epsilon. Após isso, os simbolos são removidos da pilha (se for epsilon, não remove). Então, o estado atual da execução é definido para o novo estado da transição e os novos símbolos são adicionados no topo da pilha (se for epsilon, não adiciona).


# Execução do programa
#### Modo de execução do programa:
Primeiro passo:
```sh
$ cd pasta-do-projeto
```
Segundo passo:
```sh
$ cd src
```
Terceiro passo:
```sh
$ ./main.py descricaomaquina.txt "entrada"
```

License
-

MIT
