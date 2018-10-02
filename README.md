# Autômato de Pilha

Projeto para a matéria de Linguagens Formais, Autômatos e Computabilidade
Desenvolvido por Dennis Urtubia, Jorge Rossi e Otávio Goes.

Dado uma descrição de funcionamento de um Autômato de Pilha e uma entrada para verficação, o programa escrito em Python 3 efetua as possíveis transições entre os estados e retorna rejeição ou aceitação por estado final ou pilha vazia.

# Funcionamento do código fonte

A estrutura do programa foi definida em 5 classes e a main.
As classes mais importantes do código são a de controle de execuções (maquina.py) e as execuções em si (execucoes.py)

- ##### execucao.py
  Nesse arquivo se encontra a classe `Algoz`, a qual representa um fluxo de execução da máquina. A mesma recebe como argumentos do método construtor a entrada da fita, a pilha e o estado atual. O método mais importante é o `execute()`, onde de fato a transição é executada. Primeiramente, o símbolo da fita da transição é lido e removido da fita (shift), a menos que seja um _epsilon_. Após isso, os simbolos são removidos da pilha (se for _epsilon_, não remove). Então, o estado atual da execução é definido para o novo estado da transição e os novos símbolos são adicionados no topo da pilha (se for _epsilon_, não adiciona).
- ##### maquina.py
  No início desta classe, temos o método `init()` que é responsável por fazer a atribuição dos dados na máquina, cria estados e os define como inicial ou um dos finais, cria transições adicionando-as a uma lista e cria a primeira execução do programa.
  Esta classe também possui o método `get_transicoes()` para coletar as transições com base em uma execução. A coleta das transições é feita em 3 partes, primeiramente é verificado as transições disponíveis para o estado atual da execução, a partir disso, é coletado as transições com o mesmo símbolo de entrada ou que tenha _epislon_. Doravante e por último, é coletada as transições com o mesmo símbolo da pilha.
  Por fim temos o método `run()`, onde verifica a aceitação ou rejeição das execuções. Para isso, foi adicionado dois vetores auxiliares para execuções e transições onde são designadas e executadas as transições correspondentes para cada execução (caso haja não determinísmo).

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

## License

MIT
