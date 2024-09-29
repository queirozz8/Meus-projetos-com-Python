# **TIPOS PRIMITIVOS DO PYTHON**
1) **str (String)** Palavras ou conjunto de caracteres
2) **Int (Inteiro)** Números inteiros
3) **Float (Flutuantes/Real/Decimais)** Números flutuantes/Reais/Decimais. Com ponto
4) **Bool (Lógico)** True ou False (Verdadeiro ou Falso)



# **ESTRUTURAS DE DADOS (VARIÁVEIS COMPOSTAS/COLEÇÕES)**

# **TUPLAS**
Tuplas são estruturas de dados que armazenam uma sequência de itens. Os itens podem ser de diferentes tipos e são acessados por índices, que começam em 0. Tuplas **NÃO SÃO MUTÁVEIS.**
Tuplas são mais eficientes e rápidas, essa é sua vantagem em comparação com as Listas.
Uma Tupla é categorizada pelo símbolo de Parênteses `()`. 
As funções Built-In do Python funcionam em Tuplas também. Algumas funções das listas (Tipo as de Consulta) funcionam nas Tuplas também. 


# **LISTAS**
Listas são estruturas de dados que armazenam uma sequência de itens. Os itens podem ser de diferentes tipos e são acessados por índices, que começam em 0. Listas **SÃO MUTÁVEIS.**
Listas são mutáveis e mais versáteis, com mais funções e opções de modificação. Essa é sua vantagem em comparação com as Tuplas.
Uma Lista é categorizada pelo símbolo de Colchetes `[]`.
### Criando e Acessando Listas
Para criar uma lista: `lista = [1, 2, 3, 4, 5]` Para acessar um item na posição 2: 
```python
print(lista[2]) # Saída: 3
```
### Modificando Itens de Listas
Para modificar o valor no índice 2: 
```python
lista[2] = 10` `print(lista) # Saída: [1, 2, 10, 4, 5]
```

#  **LISTAS ANINHADAS (SUB-LISTAS DENTRO DE OUTRAS LISTAS)**

Quando criamos uma lista dentro de outra lista, nós estamos criando Listas Aninhadas.
Como usar elas?
```python
lista_maior = []
lista_maior.append([1, 2, 3])
print(lista_maior)
# saída: [[1, 2, 3]]
```
Agora, `lista_maior` tem 2 colchetes, pois 1 par de colchetes é da lista maior, e o outro é da sub-lista que está dentro dela.
Se fizessemos assim:
```python
print('-'*80)
print(f'{'ANALISADOR DE PESSOAS E PESOS':^80}')
print(f'{'Digite o nome de uma pessoa, seu peso e eu farei as análises no final.':^80}')
print('-'*80)
# temp é uma lista temporária, ela existe para verificar os maiores e menores números que o usuário digitou. Depois de analisar, ela manda os dados para a lista principal (princ)
# e apaga todos os dados que existem nela (clear):
temp = []
# princ é a lista principal, é a que vamos manipular:
princ = []
mai = men = 0

while True:
    temp.append(input('Nome: ').lstrip())
    temp.append(float(input('Peso: ')))
    # Se o valor que o usuário digitou foi o primeiro de todos:
    if len(princ) == 0:
        # mai e men é esse valor:
        mai = men = temp[1]
    else:
        # Se o peso que o usuário digitou é maior do que o maior número anterior:
        if temp[1] > mai:
            # O maior número agora se torna o peso que o usuário colocou atualmente:
            mai = temp[1]
        # Se o peso que o usuário digitou é menor do que o menor número anterior:
        if temp[1] < men:
            # O menor número agora se torna o peso que o usuário colocou atualmente:
            men = temp[1]
    # Manda os dados (Nome da pessoa e o peso dela) para a lista principal (princ):
    princ.append(temp[:])
    # Apaga todos os dados da lista, para assim ela receber mais um nome e peso de outra pessoa e passar para a lista principal:
    temp.clear()
    resp = ''
    # Enquanto resposta for uma string vazia ou o primeiro caractere dela não estiver dentro das opções disponíveis ('SsNn'):
    while not resp or resp[0] not in 'SsNn':
        resp = input('Deseja continuar? [S/N]: ').strip()
    if resp[0] in 'Nn':
        break

print('-='*60)
# TODAS AS PESSOAS E SEUS PESOS
# len(princ) mostra quantos elementos aquela lista tem:
print(f'Você digitou {len(princ)} pessoas:')
for n, p in enumerate(princ):
    # n começa com 0, então somamos +1 para exibir corretamente. p[0] são os nomes de todas as sub-listas que estão dentro da princ. p[1] são todos os pesos de todas as pessoas.
    print(f'{n+1}° Pessoa: {p[0]} - Peso: {p[1]}.')

# MAIORES PESOS
print(f'O MAIOR peso digitado foi {mai}Kg. Peso de ', end='')
maiores = []
# Para cada pessoa dentro de princ:
for p in princ:
    # Se o peso for o maior peso:
    if p[1] == mai:
        # Adiciona o nome da pessoa dentro da lista maiores. No final, a lista maiores fica com todos os nomes das pessoas mais pesadas:
        maiores.append(p[0])
# Para cada nome das pessoas dentro da lista maiores:
for i, nome in enumerate(maiores):
    # Mostre o nome da pessoa (Não tem peso na lista maiores, só os nomes, a variável nome passa por todos os nomes dentro da lista maiores):
    print(nome, end='')
    # Se o índice de cada nome for menor do que o tamanho da lista maiores - 1 (- 1 pois queremos desconsiderar a última pessoa da lista, para mostrarmos um ponto final).
    """Basicamente, vamos supor que maiores/menores é uma lista com 5 pessoas. len(maiores/menores) - 1 = 4. O enumerate vai funcionar assim:
    0 < 4. Mostre ', '
    1 < 4. Mostre ', '
    2 < 4. Mostre ', '
    3 < 4. Mostre ', '
    4 = 4 (É o último número da lista). Mostre '.' """
    if i < len(maiores) - 1:
        print(', ', end='')
    else:
        print('.')

# MENORES PESOS
print(f'O MENOR peso digitado foi {men}Kg. Peso de ', end='')
menores = []
# Para cada pessoa dentro de princ:
for p in princ:
    # Se o peso for o maior peso:
    if p[1] == men:
        # Adiciona o nome da pessoa dentro da lista menores. No final, a lista menores fica com todos os nomes das pessoas mais leves:
        menores.append(p[0])
# Para cada nome das pessoas dentro da lista maiores:
for i, nome in enumerate(menores):
    # Mostre o nome da pessoa (Não tem peso na lista menores, só os nomes, a variável nome passa por todos os nomes dentro da lista maiores):
    print(nome, end='')
    # Se o índice de cada nome for menor do que o tamanho da lista menores - 1 (-1 pois queremos desconsiderar a última pessoa da lista, para mostrarmos um ponto final).
    # A explicação dessa linha de código eu expliquei na parte das pessoas com maiores pesos:
    if i < len(menores) - 1:
        print(', ', end='')
    else:
        print('.')

print('-'*80)
print('FIM DO SOFTWARE!')
```
Esse é um exemplo de software que criei. Na parte onde o software mostra só os nomes das pessoas mais pesadas e mais leves, `nome` passa por cada nome da lista `maiores/menores`.

Outros exemplos:
```python
pessoas = [['Pedro', 25], ['Maria', 19], ['João', 32]]
print(pessoas[0][0]) # Saída: Pedro
print(pessoas[1][1]) # Saída: 19 (Idade de Maria)
print(pessoas[2][0]) # Saída: João
print(pessoas[0][1]) # Saída: 25 (Idade de Pedro)
print(pessoas[1]) # Saída: ['Maria', 19]
print(pessoas[2]) # Saída: ['João', 32]
```
as sub-listas vão ser representadas por: `lista_maior[elemento_da_lista_maior (que é o índice_da_sub-lista)][Elemento_da_sub-lista]`. Então, por exemplo: `print(pessoas[2][0])` Imprime João na tela. Pois fomos no elemento 2 da lista maior, que é a sub-lista do João, e pedimos para o Python mostrar o elemento 0 da sub-lista do João, que é o nome dele, então por isso, o resultado que mostra na tela é João.


# PRINCIPAIS FUNÇÕES DAS LISTAS
### Adição e Inserção
- `append()`: Adiciona um valor ao final da lista. 
```python
lista.append(6)print(lista) # Saída: [1, 2, 10, 4, 5, 6]
```
- `insert()`: Adiciona um valor em qualquer posição especificada da lista. O número que vem primeiro indica o índice, o que vem depois indica o elemento que será adicionado
```python
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lista.insert(2, 3) 
print(lista) # Saída: [1, 2, 3, 3, 4, 5, 6, 7, 8, 9, 10]
```
### Remoção
- `lista.pop(indice)`: Remove e retorna o elemento removido à uma variável. Nós indicamos o elemento que queremos remover pelo índice dele. Podemos remover somente 1 elemento por linha de código
```python
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
item = lista.pop() 
print(item) # Saída: 10 
print(lista) # Saída: [1, 2, 3, 4, 5, 6, 7, 8, 9]
```
- `del lista[indice]`: Remove o valor como se fosse o `pop()`, porém ele não retorna o valor removido. O tornando assim, menos flexível como o `pop()`
```python
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
del lista[2]
print(lista)
# Saída: [1, 2, 4, 5, 6, 7, 8, 9, 10]
```
- `remove(valor)`: Remove a primeira ocorrência do elemento. A diferença dele para os outros é que ele remove algo pelo elemento indicado, não pelo índice.
```python
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lista.remove(3) 
print(lista) # Saída: [1, 2, 4, 5, 6, 7, 8, 9, 10]
```
- `clear()`: Remove todos os itens da lista.
```python
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lista.clear()
print(lista) # Saída: []
```
### Consulta
- `index(x[, start[, end]])`: Retorna o índice da primeira ocorrência do item 
```python
lista = [1, 2, 10, 4, 5]
print(lista.index(10)) # Saída: 2
```
Caso queira pegar alguma ocorrência que seja depois da primeira, nós cortamos os índices:
```python
lista = [1, 2, 10, 4, 5, 10]
print(lista.index(10, 5)) # Saída: 5
```
A saída seria 2, porém nós cortamos o range do `index`, assim, ele só pode buscar o elemento à partir do índice 3, o primeiro 10 estava no índice 2, então o Python busca o próximo elemento, que está no índice 5. Nós também podemos fazer isso para filtrar o final, desse jeito:
```python
lista = [1, 2, 10, 4, 10, 10]
print(lista.index(10, 3, 5)) # Saída: 4
```
A saída foi 4 pois filtramos os índices, o Python começa procurando do índice 3 (que corta o primeiro 10), e termina no índice 5 (O último é desconsiderado, ele não conta o último 10 pois o índice que representa o final é sempre desconsiderado), então o único 10 encontrado é na posição 4.
- `count(x)`: Retorna o número de vezes que o item `x` aparece na lista. 
```python
lista = [1, 2, 3, 4, 3] 
print(lista.count(3)) # Saída: 1
```
### Ordenação e Reversão
- `lista.sort()`: Ordena a lista em ordem crescente ou alfabética.
```python
lista = [8, 2, 5, 3, 6]
print(lista.sort())
# Saída: [2, 3, 5, 6, 8]
```
#### Curiosidades sobre o `sort()`
1. Se você ordena uma lista de elementos de tipo `bool`, como `True` = 1 e `False` = 0, a lista ordenada de forma crescente retorna primeiro os elementos `False`, depois os `True`
2. Você não consegue ordenar uma lista que tenha mais de 1 tipo, somente é possível ser feito isso se você ordena uma lista que tenha números `float` e `int` dentro dela, mas se for, por exemplo, uma lista com valores `bool`, `int` e `str` e tentar ordenar ela com o `sort()`, o Python retornará um erro (obviamente, pois um tipo não é maior do que o outro.)

- `lista.sort(key=None, reverse=True)`: Ordena a lista em ordem decrescente ou alfabética (porém começando da letra "z" indo até "a")
```python
lista = [3, 1, 4, 2]
lista.sort()
print(lista) # Saída: [1, 2, 3, 4]
```
- `reverse()`: Inverte os itens da lista no lugar. 
```python
lista = [1, 2, 3, 4]
lista.reverse()
print(lista) # Saída: [4, 3, 2, 1]
```
- `sorted(lista)`: Não modifica a lista original, em vez disso, cria uma nova lista e ordena a lista antiga (desordenada) na lista nova. Ele faz as mesmas coisas e tem os mesmos parâmetros opcionais que o `sort()`, só que agora, ele retorna o valor. Quando queremos usar o `sort()` em f-strings, usamos o `sorted()`, pois o `sort()` só pode ser utilizado de forma avulsa em uma linha exclusiva para ele, já o `sorted()`, não.
### Cópia e Extensão
- `copy()`: Retorna uma cópia RASA da lista. 
```python
lista = [1, 2, 3, 4]

nova_lista = lista.copy()
print(nova_lista) # Saída: [1, 2, 3, 4]
# nova_lista é uma lista conectada com lista. Se você modifica um elemento de uma, a outra também é modificada.
```
- `[:]` (Também chamado de `slice`): Cria uma cópia SUPERFICIAL da lista.
```python
a = [1, 2, 3, 4, 5]
b = a[:]
print(a)
print(b)
# b é uma cópia independente de a, se modificamos um elemento de uma, a outra não vai ser modificada junto.
```
A diferença do uso de `copy()` para o `[:]` é que o `copy()` cria uma cópia RASA da lista; enquanto o slice `[:]` faz uma cópia SUPERFICIAL. Basicamente no `copy()`, as duas listas estão conectadas, o que você modifica em uma lista, é modificada em outra também. Já no slice `[:]`, as listas não são conectadas, a lista original passa todos os elementos dela para outra lista, mas isso não remove os elementos da lista original, ou cria uma ligação de uma com a outra. Só pega os elementos e adiciona eles em outra lista. Outras coisas que diferem elas é que `copy()` é um pouco mais pesado, porém mais legível e explícito; o `[:]` é um pouco mais rápido.

- `extend(iterable)`: Estende a lista adicionando todos os itens do `iterable`.
```python
lista = [1, 2, 3]` 
lista.extend([4, 5])
print(lista) # Saída: [1, 2, 3, 4, 5]
```


# **DICIONÁRIOS**
Os Dicionários são usados para armazenar dados em pares chave-valor, onde cada chave é única e está associada a um valor. Eles são úteis quando você precisa acessar dados rapidamente usando uma chave em vez de uma posição, como em listas. Um Dicionário é categorizado pelo símbolo de Chaves `{}`. Dicionários **SÃO MUTÁVEIS.** Eles se assemelham à objetos em Javascript. Vale lembrar que Objetos em Javascript podem ter funcionalidades extras que realmente se parecem com objetos de outras linguagens. E que objetos em Python não são objetos em Javascript.
- **Chaves** são as 'Categorias' de cada variável. Sintaxe: `dict.keys()`
- **Valor** são os valores que ficam dentro das suas respectivas chaves. Sintaxe: `dict.values()`
- **Itens** são o todo do dicionário, é o par Chave-Valor. Sintaxe: `dict.items()`
```python
meu_dicionario = {'nome': 'João', 'idade': 30, 'cidade': 'São Paulo'}
```
Neste exemplo, `nome`, `idade` e `cidade` são as chaves, e `'João'`, `30` e `'São Paulo'` são os valores associados a cada chave.


**Acessando Valores**

```python
meu_dicionario = {'nome': 'João', 'idade': 30, 'cidade': 'São Paulo'}
nome = meu_dicionario['nome']
print(nome)  # imprime 'João'
```
Para acessar um valor em um dicionário, você usa a chave correspondente entre colchetes (`[]`).


**Adicionando Pares Chave-Valor**
```python
meu_dicionario = {'nome': 'João', 'idade': 30, 'cidade': 'São Paulo'}
meu_dicionario['endereco'] = 'Rua ABC, 123'
print(meu_dicionario)  # {'nome': 'João', 'idade': 30, 'cidade': 'São Paulo', 'endereco': 'Rua ABC, 123'}
```
Você pode adicionar um par chave-valor a um dicionário usando a sintaxe de atribuição. Não utilizamos o `append()`, utilizamos o `=`.


**Atualizando Valores**
```python
meu_dicionario = {'nome': 'João', 'idade': 30, 'cidade': 'São Paulo'}
meu_dicionario['idade'] = 31
print(meu_dicionario)  # {'nome': 'João', 'idade': 31, 'cidade': 'São Paulo'}
```
Você pode atualizar um valor em um dicionário usando a sintaxe de atribuição também.


# PRINCIPAIS FUNÇÕES DOS DICIONÁRIOS

1. **`keys()`**: Retorna um objeto de visualização que exibe uma lista de todas as chaves no dicionário.
Sintaxe:
```python
meu_dicionario = {'nome': 'João', 'idade': 30, 'cidade': 'São Paulo'}
chaves = meu_dicionario.keys()
print(chaves)  # dict_keys(['nome', 'idade', 'cidade'])
```
2. **`values()`**: Retorna um objeto de visualização que exibe uma lista de todos os valores no dicionário.
Sintaxe:
```python
meu_dicionario = {'nome': 'João', 'idade': 30, 'cidade': 'São Paulo'}
valores = meu_dicionario.values()
print(valores)  # dict_values(['João', 30, 'São Paulo'])
```
3. **`items()`**: Retorna um objeto de visualização que exibe uma lista de todos os pares chave-valor no dicionário.
Sintaxe:
```python
meu_dicionario = {'nome': 'João', 'idade': 30, 'cidade': 'São Paulo'}
itens = meu_dicionario.items()
print(itens)  # dict_items([('nome', 'João'), ('idade', 30), ('cidade', 'São Paulo')])
```
Iterando sobre os `items()`:
```python
meu_dict = {'nome': 'Henrique', 'Sonho': 'Ser programador'}
for chaves, valores in meu_dict.items:
	print(f'{chaves} = {valores}.')
```
Aqui, `chaves` são todas as chaves que o `items` vai passar com o `for loop`. A mesma coisa com `valores`, são todos os valores que `items` vai passar com o `for loop`.
4. **`get()`**: Retorna o valor para uma chave dada se ela existir no dicionário. Caso contrário, ele retorna um valor padrão.
Sintaxe:
```python
meu_dicionario = {'nome': 'João', 'idade': 30, 'cidade': 'São Paulo'}
nome = meu_dicionario.get('nome')
print(nome
```
5. **`setdefault()`**: Define um valor para uma chave se ela ainda não existir no dicionário. Se a chave já existir, o valor não é alterado.
Sintaxe:
```python
meu_dicionario = {'nome': 'João', 'idade': 30}
meu_dicionario.setdefault('cidade', 'São Paulo')
print(meu_dicionario)  # {'nome': 'João', 'idade': 30, 'cidade': 'São Paulo'}

meu_dicionario.setdefault('nome', 'Maria')
print(meu_dicionario)  # {'nome': 'João', 'idade': 30, 'cidade': 'São Paulo'}
```
6. **`update()`**: Atualiza o dicionário com novos pares chave-valor. Se uma chave já existir, o valor é atualizado.
Sintaxe:
```python
meu_dicionario = {'nome': 'João', 'idade': 30}
meu_dicionario.update({'cidade': 'São Paulo', 'pais': 'Brasil'})
print(meu_dicionario)  # {'nome': 'João', 'idade': 30, 'cidade': 'São Paulo', 'pais': 'Brasil'}

meu_dicionario.update({'nome': 'Maria'})
print(meu_dicionario)  # {'nome': 'Maria', 'idade': 30, 'cidade': 'São Paulo', 'pais': 'Brasil'}
```
Note que `update()` pode receber outro dicionário como parâmetro, ou uma lista de pares chave-valor separados por vírgulas.
7. **`pop()`**: Remove um par chave-valor do dicionário e retorna o valor.
Sintaxe: 
```python
meu_dicionario = {'nome': 'João', 'idade': 30, 'cidade': 'São Paulo'}
meu_dicionario.pop('idade')
print(meu_dicionario)  # {'nome': 'João', 'cidade': 'São Paulo'}
```
8. **`clear()`**: Remove todos os pares chave-valor do dicionário.
Sintaxe:
```python
meu_dicionario = {'nome': 'João', 'idade': 30, 'cidade': 'São Paulo'}
nome = meu_dicionario.get('nome')
print(nome
```


# ÍNDICES
Índice é o nome do número que determina aonde um elemento de uma variável composta está.
Os índices sempre começam com 0 até o infinito, então se quiser indicar o primeiro elemento de uma variável composta, esse elemento fica no índice 0.
Quando você faz um `for loop`, por exemplo, o último índice que o programador passou é onde o Python vai parar, isso é, ele não vai fazer nada com o último índice que o programador digitou, ele vai usar o último índice para parar o que ele estava fazendo.
Outro exemplo é com Tuplas:
```python
tupla = ("Elemento_1", "Elemento_2", "Elemento_3")
print(tupla[0:2])
# Saída:
['Elemento_1','Elemento_2']
```
Nesse exemplo, o Python não mostrou o Elemento_3 (Que é indicado pelo índice 2) pois o Python sempre PARA no último índice indicado pelo programador (Nesse caso, 2 foi o índice indicado, então o Python para nele).
Outro exemplo, uma Tupla:
```python
tupla = ("Elemento_1", "Elemento_2", "Elemento_3")
print(tupla[1])
# Saída: Elemento_2
```
Nesse exemplo, a saída é `Elemento_2` pois o índice que foi requisitado foi o 1.

Caso queira indicar o último elemento de uma tupla, lista ou dicionário, mas sem precisar ficar contando quantos elementos aquela variável composta tem, nós digitamos números negativos.
- Último elemento da variável composta: -1
- Penúltimo elemento: -2
- Antepenúltimo: -3
- E assim por diante.


# USANDO O `LEN`
O `len` retorna o tamanho de uma variável composta, por exemplo:
```python
lanche = ("Hambúrguer", "Pizza", "Suco", "Pudim")
for comida in range(len(lanche)): # Ou range(0, len(lanche))
	print(f"Vou comer {lanche[comida]} na posição {comida}")
'''
Saída:
Vou comer Hambúrguer na posição 0
Vou comer Pizza na posição 1
Vou comer Suco na posição 2
Vou comer Pudim na posição 3'''
```
É importante ver que na linha 3, se colocássemos só `print(f"Vou comer {comida} ..."`, não funcionaria como o esperado, ele mostraria "vou comer 0 na posição 0", quando queríamos que ele mostrasse "vou comer Hambúrguer na posição 0"; pois `comida` é só o índice de `lanche`, `lanche` é uma tupla, comida é só o índice que representa o elemento atual que o `for loop` está abordando naquele momento. Se quisermos que ele mostre o elemento que ele está no momento, devemos colocar `lanche[comida]`, dessa forma, estamos falando "quero que você mostre o `lanche`, mas na posição que o `comida` está agora"


# FUNÇÕES BUILT-IN DO PYTHON PARA ESTRUTURAS DE DADOS (FUNÇÕES QUE VOCÊ USAR EM QUALQUER ESTRUTURA DE DADOS)

**Funções de Manipulação de Listas**

1. `len()`: Retorna o comprimento de uma lista.
2. `sum()`: Retorna a soma de todos os elementos em uma lista. Se uma lista tiver números negativos, ele subtrai os números negativos:
```python
lista = [-5, -4, 3, -2, 6, 1, 2, -2]
print(lista.sort())
```
O que ele fez foi: Somou os números positivos: 12, e subtraiu pelos negativos: -1.
3. `max()`: Retorna o maior elemento em uma lista. Se 2 valores são iguais, ele retorna o valor que tem índice menor. Tipo 5.0 e 5, se 5.0 vier antes de 5, então `max()` retorna 5.0, se for ao contrário, `max()` retorna 5. Você consegue comparar o valor de múltiplas variáveis usando o `max`. Tipo assim:
```python
a = 10
b = 20
c = 15

maior = max(a, b, c)

print(maior)  # Isso vai imprimir 20, que é o maior valor entre a, b e c
```
4. `min()`: Retorna o menor elemento em uma lista. Se 2 valores são iguais, ele retorna o valor que tem índice menor. Tipo 5.0 e 5, se 5.0 vier antes de 5, então `min()` retorna 5.0, se for ao contrário, `min()` retorna 5. Você consegue comparar o valor de múltiplas variáveis usando o `min`. Tipo assim:
```python
a = 10
b = 20
c = 15

menor = min(a, b, c)

print(menor)  # Isso vai imprimir 15, que é o menor valor entre a, b e c
```
5. `map()`: Aplica uma função em todo elemento novo de uma lista que for adicionado.
Sintaxe:
```python
lista = [1, 2, 3, 4, 5]
while True:
	lista.append(int(input('Digite um número: '))
	map(str, lista)
	# Agora todos os valores da lista conforme eles vão sendo adicionados, vão todos virando strings.
```
Exemplo de uso do `map()` e do `join()`:
```python
lista_num = []

while True:
    n = int(input('Digite um valor: '))
    if n not in lista_num:
        lista_num.append(n)
    else:
        print(f'Este valor já está na sua lista! Não vou adicionar pois {n} é um valor duplicado, já está na lista.')


    print(f'Sua lista está assim: ', end='')

    print(', '.join(map(str, lista_num)) + '.')
    print()
    r = ''
    while not r or r[0] not in 'SsNn':
        r = str(input('Quer continuar? [S/N]: ')).strip()
    if r in 'Nn':
        break
```
`map(str, lista_num)`: à cada elemento novo da lista `lista_num`, transforme ele em uma string usando a função `str()`.
`', '.join(...)`: concatene cada elemento da lista de strings (menos o último, como você mencionou) com a string `', '`.
`+ '.'`: quando terminar tudo isso, mostre um ponto final (`.`) no fim da string.

6. `join()`: É um separador de strings (Só funciona em strings). No caso de cima (do `map()`), `join()` junta todos os valores da lista (Que viraram strings) e separa eles por ', '. A saída, caso eu colocasse, por exemplo:  1 2 3 4 5. Saída: 1, 2, 3, 4, 5. `join()` NÃO MOSTRA O SEPARADOR NO FINAL DA LISTA. Isso é, ele não mostrou a vírgula no final, como podemos ver. Então por isso que escrevi o `+ '.'`, para sair assim: 1, 2, 3, 4, 5. Caso eu queria administrar o número de novo, já que eu transformei eles em strings, eu poderia só transformar eles de volta em números inteiros, ou então fazer cópias das listas originais, para mostrar elas na tela, como queria. Tipo assim:
```python
num = [1, 2, 3, 4, 5]
num_str = [str(x) for x in num]
# Saída: ['1', '2', '3', '4', '5']
```
Vale lembrar que o `join()` espera um iterável, isso é, uma tupla, lista, dicionário, conjunto, strings ou geradores, como o `map()` e `filter()`. Nesse caso, por exemplo:
```python
num = [1, 2, 3, 4, 5]
print(f'Número(s) oganizado(s) em ordem decrescente: {', '.join(map(str, num))}.')
```
1) `num` é uma lista de números inteiros: `[1, 2, 3, 4, 5]`.
2) `map(str, num)` aplica a função `str` a cada elemento da lista `num`. Isso significa que cada número inteiro é convertido para uma string.
3) O resultado de `map(str, num)` é um iterável de strings: `['1', '2', '3', '4', '5']`.
4) O método `join` é chamado com a string `', '` como separador e o iterável de strings como argumento.
5) `join` concatena as strings do iterável com a string `', '` como separador, produzindo a string final: `'1, 2, 3, 4, 5'`.
6) A string final é impressa com a mensagem de saída.
O código funciona porque `map` é uma função que aplica uma função (neste caso, `str`) a cada elemento de um iterável (neste caso, `num`). O resultado é um iterável de strings, que pode ser passado para a função `join`.

Mas se digitarmos assim:
```python
num = [1, 2, 3, 4, 5]
print(f'Número(s) oganizado(s) em ordem decrescente: {', '.join(str(num))}.')
```
**O que acontece:**
1) **Erro**: `join` espera um iterável de strings como argumento, mas recebe uma string única `'5'`. Isso causa um erro, pois `join` não sabe como concatenar uma string única com vírgulas.
**Por que o código não funciona:**
O problema é que `str(num)` converte o número inteiro para uma string única, em vez de produzir um iterável de strings. Como resultado, o método `join` não pode concatenar as strings com vírgulas, pois não há strings para concatenar.

O segundo código não funciona porque `str(num)` tenta converter o objeto `num` inteiro para uma string, em vez de converter cada elemento do iterável `num` para uma string.
A função `join` espera um iterável de strings como argumento, e não uma string única. Quando você passa `str(num)` para `join`, você está passando uma string única, que não é o que `join` espera.
Por exemplo, se `num` é `[1, 2, 3, 4, 5]`, `map(str, num)` retorna um iterável que produz as strings `"1"`, `"2"`, `"3"`, `"4"` e `"5"`. Já `str(num)` retorna a string `"[1, 2, 3, 4, 5]"`.
Portanto, o primeiro código funciona porque `map` converte cada elemento do iterável `num` para uma string, e `join` pode concatenar essas strings com vírgulas. Já o segundo código não funciona porque `str(num)` não produz um iterável de strings, e `join` não pode concatenar uma string única com vírgulas.

Às vezes, precisamos transformar uma lista de números em uma lista de strings para o `join()` funcionar corretamente. Porém, quando você modifica a lista para uma lista de strings, talvez você precise fazer operações que só funcionam em tipos `int` no Python; e sua lista é uma lista de `str`.
Existem 3 formas de se resolver isso em Python:
1) Criando uma cópia da lista com o `copy()`:
```python
num = [[], []]
r = int(input('Quantos números deseja adicionar na sua lista? '))
for c in range(r):
    valor = int(input(f'Digite o {c+1}° número da sua lista: '))
    if valor % 2 == 0:
        num[0].append(valor)
    else:
        num[1].append(valor)
print('-='*30)
num_copia = num[0].copy(), num[1].copy()
print(f'Os números PARES e de forma ORDENADA digitados foram: {', '.join(map(str, sorted(num_copia[0]))) + '.'}')
print(f'Os números ÍMPARES e de forma ORDENADA digitados foram: {', '.join(map(str, sorted(num_copia[1]))) + '.'}')
```
Nesse código, nós temos que copiar cada sub-lista da lista maior, pois se digitarmos só `num_copia = num.copy()`,  `num_copia` não seria uma lista independente. Você mudaria os elementos dentro da lista `num_copia`, e os elementos da lista `num` também mudariam. Não queremos isso, então copiamos uma sub-lista por uma.
2) Criando uma cópia da lista com o slice `[:]`:
```python
num = [[], []]
r = int(input('Quantos números deseja adicionar na sua lista? '))
for c in range(r):
	valor = int(input(f'Digite o {c+1}° número da sua lista: '))
	if valor % 2 == 0:
		num[0].append(valor)
	else:
		num[1].append(valor)
print('-='*30)
num_copia = num[0][:], num[1][:]
print(f'Os números PARES e de forma ORDENADA digitados foram: {', '.join(map(str, sorted(num_copia[0]))) + '.'}')
```
A diferença do uso de `copy()` para o `[:]` é que o `copy()` cria uma cópia RASA da lista; enquanto o slice `[:]` faz uma cópia SUPERFICIAL. Basicamente no `copy()`, as duas listas estão conectadas, o que você modifica em uma lista, é modificada em outra também. Já no slice `[:]`, as listas não são conectadas, a lista original passa todos os elementos dela para outra lista, mas isso não remove os elementos da lista original, ou cria uma ligação de uma com a outra. Só pega os elementos e adiciona eles em outra lista. Outras coisas que diferem elas é que `copy()` é um pouco mais pesado, porém mais legível e explícito; o `[:]` é um pouco mais rápido.
3) Mudar o tipo da variável novamente para o tipo que deseja fazer as manipulações:
```python
num = [[], []]
r = int(input('Quantos números deseja adicionar na sua lista? '))
for c in range(r):
    valor = int(input(f'Digite o {c+1}° número da sua lista: '))
    if valor % 2 == 0:
        num[0].append(valor)
    else:
        num[1].append(valor)
print('-='*30)
print(f'Os números PARES e de forma ORDENADA digitados foram: {', '.join(map(str, num[0])) + '.'}')
print(f'Os números ÍMPARES e de forma ORDENADA digitados foram: {', '.join(map(str, num[1])) + '.'}')
map(int, num[0])
map(int, num[1])
```
Mas eu prefiro das outras formas. consome menos linhas, e não precisa ficar fazendo gambiarras com tipagem.
Caso uma lista tenha muitas sub-listas, você pode resolver esse problema de 2 formas:
1) Importando a bilbioteca copy e usando o `copy.deepcopy(variavel)`:
```python
import copy

num = [[1, 2], [3, 4], [5, 6], [7, 8]]
num_copia = copy.deepcopy(num)

# Agora, num_copia é uma cópia completamente independente de num
num_copia[0].append(9)
print(num) # [[1, 2], [3, 4], [5, 6], [7, 8]]
print(num_copy) # [[1, 2, 9], [3, 4], [5, 6], [7, 8]]
```
`deepcopy()` é uma função que recursivamente passa pela estrutura de dados inteira, criando novas cópias de cada sub-lista e seus elementos. Isso garante que a lista copiada seja completamente independente da lista original. Basicamente ele faz o que o `copy()` faria manualmente, porém de forma automatizada.

2) Usando `for loops`/Compreensões de Listas para copiar automaticamente todas as sub-listas
1° forma, com `for loops`, caso quisesse criar realmente uma cópia independente e profunda:
```python
num = [[1, 2], [3, 4], [5, 6], [7, 8]]
num_copia = []
for sublista in num:
	copia_sublista = []
	for elemento in sublista:
		copia_sublista.append(elemento)
	num_copia.append(copia_sublista)
```
Criamos `elemento` pois `sublista` só itera sobre as sublistas dentro da lista maior, então o `len` da `sublista` é 4, não 8. Um dos elementos da `sublista`, por exemplo, é `[3, 4]`. Caso quiséssemos modificar algum elemento específico dentro das sub-listas, precisaríamos de uma variável como a `elemento`.


2° forma, com os `for loops`
```python
num = [[1, 2], [3, 4], [5, 6], [7, 8]]
num_copia = []
for sublista in num:
    num_copia.append(sublista[:])
```
3° forma, com Compreensões de Listas em Python:
```python
num = [[1, 2], [3, 4], [5, 6], [7, 8]]
num_copia = [sublista.copy() for sublista in num]
```


4. `any()`: Retorna `True` se qualquer elemento em uma lista for verdadeiro.
5. `all()`: Retorna `True` se todos os elementos em uma lista forem verdadeiros.
6. `enumerate()`: Retorna um iterador que produz pares de valores, onde o primeiro elemento é o índice e o segundo elemento é o valor correspondente na lista.
7. `zip()`: Retorna um iterador que produz pares de valores, onde cada par é composto por um elemento de cada lista.


**Funções de Manipulação de Dicionários**

1. `len()`: Retorna o comprimento de um dicionário.
2. `sum()`: Retorna a soma de todos os valores em um dicionário.
3. `max()`: Retorna o maior valor em um dicionário.
4. `min()`: Retorna o menor valor em um dicionário.
5. `any()`: Retorna `True` se qualquer valor em um dicionário for verdadeiro.
6. `all()`: Retorna `True` se todos os valores em um dicionário forem verdadeiros.


# USANDO O `ENUMERATE`
O `enumerate` numera todos os elementos de uma variável composta, por exemplo:
```python
lanche = ("Hambúrguer", "Pizza", "Suco", "Pudim")
for pos, comida in enumerate(lanche):
	print(f"Vou comer {comida} na posição {pos}")
'''
Saída:
Vou comer Hambúrguer na posição 0
Vou comer Pizza na posição 1
Vou comer Suco na posição 2
Vou comer Pudim na posição 3'''
```
`pos` é a variável que o `enumerate` retorna, `comida` é o contador do `for loop`, o `enumerate` vai numerar todos os elementos da tupla/lista/dicionário e retornar eles em algum lugar, nesse caso, a variável `pos`.


# OPERADOR * EM LISTAS E TUPLAS
O operador `*` desempacota os elementos de uma sequência (lista, tupla, etc.) removendo os colchetes `[]` ou parênteses `()` que os envolvem.
Quando você tem uma lista ou tupla e deseja exibir ou utilizar seus elementos individualmente, em vez de exibi-la como uma sequência única envolvida por colchetes ou parênteses, você pode usar o * para desempacotar essa sequência. ESSE OPERADOR É INVÁLIDO EM F-STRINGS
```python
numeros = [1, 2, 3]
print(numeros)  # Saída: [1, 2, 3]
print(*numeros) # Saída: 1 2 3

letras = ('a', 'b', 'c')
print(letras)   # Saída: ('a', 'b', 'c')
print(*letras)  # Saída: a b c
```
No primeiro exemplo, `print(numeros)` exibe a lista `[1, 2, 3]` com os colchetes. Já `print(*numeros)` desempacota a lista, exibindo seus elementos 1, 2 e 3 separadamente, sem os colchetes.

No segundo exemplo, acontece o mesmo com a tupla `('a', 'b', 'c')`. `print(letras)` exibe a tupla com parênteses, enquanto `print(*letras)` exibe seus elementos `a`, `b` e `c` separadamente, sem os parênteses.

Outro exemplo, desta vez com uma tupla:
```python
pessoa = ('João', 25, 'Programador')
print(pessoa)  # Saída: ('João', 25, 'Programador')

print(*pessoa)  # Saída: João 25 Programador
```
Aqui, `pessoa` é uma tupla com três elementos. Usando `*pessoa`, desempacotamos a tupla, fazendo com que `print()` receba três argumentos separados: 'João', 25 e 'Programador'.

Então, em resumo, o operador `*` desempacota uma sequência (lista, tupla, etc.) em argumentos separados para uma função. Isso é útil quando você deseja passar os elementos de uma sequência individualmente para uma função, em vez de passá-los como uma única sequência.
O operador `*` "tira" os colchetes ou parênteses que envolvem a sequência, exibindo ou passando seus elementos de forma individual, o que geralmente é uma forma mais "polida" ou legível de trabalhar com esses elementos separadamente.

# TUPLAS
```python
# Descompactando uma tupla
tupla = (1, 2, 3, 4, 5)
primeiro, *meio, ultimo = tupla
print(primeiro)  # 1
print(meio)  # [2, 3, 4]
print(ultimo)  # 5
```
Nesse caso, `primeiro` vai receber o valor 1, que é o primeiro valor, `meio`, como tem um asterísco `*`, vai pegar todos os elementos do meio da estrutura de dados, criar o mesmo tipo de estrutura de dados (e colocar nessa variável) e adicionar os valores do meio da variável, e `ultimo` recebe o último elemento da estrutura de dados.
# LISTAS
```python
# Descompactando uma lista
lista = [1, 2, 3, 4, 5]
primeiro, *meio, ultimo = lista
print(primeiro)  # 1
print(meio)  # [2, 3, 4]
print(ultimo)  # 5
```
Nesse caso, `primeiro` vai receber o valor 1, que é o primeiro valor, `meio`, como tem um asterísco `*`, vai pegar todos os elementos do meio da estrutura de dados, criar o mesmo tipo de estrutura de dados (e colocar nessa variável) e adicionar os valores do meio da variável, e `ultimo` recebe o último elemento da estrutura de dados.

Observe que, **no caso de listas, o valor atribuído à variável `meio` é uma lista, enquanto que no caso de tuplas, o valor atribuído à variável `meio` é uma tupla. Isso acontece porque listas são mutáveis, enquanto tuplas são imutáveis.**
A descompactação também pode ser usada com outras estruturas de dados, como strings e conjuntos, desde que elas sejam iteráveis.
# LIST COMPREHENSIONS (COMPREENSÃO DE LISTAS)
É uma forma mais compacta de se escrever operações de `for loops` com Listas. Onde você escreve tudo numa linha só.
Por exemplo, com `for loops`:
```python
squares = []
for x in range(10):
    squares.append(x**2)
```
com List Comprehensions:
```python
squares = [x**2 for x in range(10)]
```
Para ler a sintaxe, temos que imaginar o seguinte: `for x in range(10)` "para cada x de 0 até 10" `x**2` "x vai ser elevado ao quadrado". Ou seja, 0², 1², 2², 3², etc.
```python
even_numbers = [x for x in range(20) if x % 2 == 0]
```
para x de 0 até 20, retorne x se x % 2 == 0 (se for par). Então basicamente, "de todos os números que estão entre 0 e 20, analise o número atual (x), se ele % 2 == 0, então retorne esse número.". 
```python
squares = [x ** 2 for x in range(10) if x % 2 == 0]
```
para x de 0 até 10, retorne x² se x % 2 == 0.
- Geralmente, Compreensões de Listas são mais rápidas em Python (porém com diferenças de tempo BEM pequenas, tipo:
Teste 1
`for loop`: 0.11 segundos 
List comprehension: 0.07 segundos
Teste 2
Média do `for loop`: 0.079 segundos 
Média da list comprehension: 0.071 segundos
Teste 3
Média do `for loop`: 0.11 segundos 
Média da list comprehension: 0.10 segundos
Como dá para ver, nem 1 segundo de diferença)
- Outra coisa, ela é mais complicada do que a versão padrão das Listas e dos `for loops`, alguns programadores indicam você só aprender a entender o código de outros programadores que usam isso, mas que você usar não é algo tão importante assim. 
- Eu, por enquanto, prefiro os `for loops`, pois não acredito que você complicar seu código atoa por uns segundinhos e umas linhas de código à menos vá te fazer programar melhor. No máximo, eu faço algumas coisas que são bem simples com as Compreensões de Listas; se for algo mais complexo, a forma padrão se sai melhor.
ChatGPT disse: 
- **Clareza e Manutenção**: Use loops for quando precisar de clareza e facilidade de manutenção.
- **Complexidade**: Evite usar list comprehensions para operações complexas que podem comprometer a legibilidade do código.
- **Desempenho**: Considere usar list comprehensions para operações simples onde a sintaxe é clara e direta.




# ITERABILIDADE, O QUE É ISSO?
```python
# Lista
data_list = [1, 2, 3]
a, b, c = data_list
print(a, b, c)  # Output: 1 2 3

# Tupla
data_tuple = (4, 5, 6)
x, y, z = data_tuple
print(x, y, z)  # Output: 4 5 6

```
### Objetos Comuns Iteráveis
Os objetos mais comuns que são iteráveis em Python incluem:
- Listas (`list`)
- Tuplas (`tuple`)
- Dicionários (`dict`)
- Conjuntos (`set`)
- Strings (`str`)
- Faixas (`range`)
Cada um desses objetos pode ser iterado em um loop `for` e pode ser descompactado porque eles fornecem um iterador que permite percorrer seus elementos.

## Exemplo de Descompactação com Função
Você também pode usar a descompactação em funções:
```python
def my_function(a, b, c):
    print(a, b, c)

# Lista
args_list = [1, 2, 3]
my_function(*args_list)  # Output: 1 2 3

# Tupla
args_tuple = (4, 5, 6)
my_function(*args_tuple)  # Output: 4 5 6
```
Neste exemplo, o operador `*` é usado para descompactar a lista ou tupla ao passar os argumentos para a função.
Em resumo, **ser iterável significa que um objeto pode ser percorrido elemento por elemento**, o que é fundamental para operações como descompactação.


# **MANIPULANDO STRINGS:**

# Funções de Manipulação de Strings
1. `len()`: Retorna o comprimento de uma string.
2. `ord()`: Retorna o código ASCII de um caractere.
3. `chr()`: Retorna o caractere correspondente a um código ASCII.
4. `join()`: Junta strings em uma única string.
5. `split()`: Divide uma string em uma lista de substrings.
6. `lower()`: Converte uma string para minúsculas.
7. `upper()`: Converte uma string para maiúsculas.
8. `strip()`: Remove espaços em branco do início e do fim de uma string.
9. `replace()`: Substitui uma substring em uma string. Exemplo: `return f'{moeda}{preco:<.2f}'.replace('.', ',')`, isso retorna um número, só que o que seria retornado com ponto final, agora é retornado com uma vírgula.
10. `center(x)`: Centraliza uma string em x caracteres.


# CONCATENANDO STRINGS
Para concatenar 2 ou mais strings, usamos o sinal de `+` entre as strings:
```python
primeiro_nome = "Henrique"
sobrenome = "Jorge"
print(f"{primeiro_nome} " + sobrenome)
# Saída: Henrique Jorge
```


# SEPARANDO STRINGS COM `.split()`
1) Você cria sua variável, com o nome que você quiser, ex:
`nome_completo = str(input('Qual é o seu nome completo?'))`
2) Você cria uma outra variável, essa variável vai armazenar cada nome como uma str diferente, começando do 0 e indo até o infinito.
obs: Os parênteses vazios do .split signficam que cada string vai ser separada pelo espaço entre elas, por exemplo: 
Henrique Jorge de Queiroz. 
Str 0: Henrique 
Str 1: Jorge 
Str 2: de 
Str 3: Queiroz
Entããão...
`partes_do_nome = nome_completo.split()`

3) Você cria ou outra variável, essa vai ser do primeiro nome (é o nome que você quer exibir, se fosse algum outro nome, você mudaria o nome da variável e o número da lista split que ela está).
`primeiro_nome = partes_do_nome[0]`

4) Faça o programa falar o primeiro nome do usuário, o `.Title` serve para o nome sair em letras maiúsculas
`print('Olá, {}'.format (primeiro_nome.Title))`

Entrada: henrique jorge de queiroz
Saída: `Olá, Henrique`


5) Você também pode dizer o que vai determinar cada espaçamento de strings, tipo:
`partes_do_nome = nome_completo.split('o')`
nesse caso, a letra (o) vai ser o separador das strings, se eu falasse Henrique Jorge de Queiroz, ficaria assim:

Saída: `['henrique j', 'rge de queir', 'z']`


# ESCREVENDO PRINT COM VÁRIAS LINHAS

1) Se você quer escrever um texto grande, mas quer pular linhas enquanto esse texto é exibido, mas não quer ter que ficar escrevendo cada print toda linha, faça isso:

```python
print('''Alguma coisa, alguma coisa,
alguma coisa, alguma coisa, alguma coisa, alguma coisa''')
```
saída: 
```
Alguma coisa, alguma coisa,
alguma coisa, alguma coisa, alguma coisa, alguma coisa
```

# `"\N"`
`'\n'` é uma sequência de escape que representa uma nova linha. Essas sequências de escape são códigos começando com uma barra invertida `\` que têm um significado especial na linguagem.
No caso de '\n' especificamente, ela é interpretada como um caractere que insere uma nova linha, ou seja, move o cursor para a próxima linha. Isso é útil quando você deseja imprimir ou manipular strings em linhas separadas.



# PROCURANDO ALGO EM UMA STRING

1) Vamos usar este exemplo: Eu quero que o usuário digite o nome dele, eu falarei se o nome/sobrenome dele possui o nome 'Silva'. Pra isso, vamos fazer o seguinte:

Pergunta o nome do usuário:
`nome = str(input('Qual é o seu nome? '))`

Adiciona a variável bool (verdadeiro ou falso) de se tem a palavra Silva ou não. E coloca o nome completo em letras minúsculas pra realizar a verificação, ele deve procurar se em algum lugar do nome possui o nome 'silva', não 'Silva'. Ele também usa o comando 'in' (Tradução para ptbr: em) pra verificar se possui Silva EM nome
`temsilva = bool('silva' in nome.lower())`

Fala se seu nome possui o nome Silva ou não no seu nome completo
`print(f"Seu nome/sobrenome possui Silva? {temsilva}")`
Se o nome for "Henrique Jorge de Queiroz":
Saída: `False`
Se o nome for alguma coisa que tenha "Silva":
Saída: `True`


# USANDO `F-STRING`
f-string é tipo um `.format` só que melhor, pra usar ele você coloca a letra f antes de abrir as aspas da sua `string`, quando for colocar alguma variável no `print`, abre as chaves e coloca o nome da variável. Esse é o `f-string.`
**Sintaxe:** `print(f"A soma total foi {soma})"`
**Jeito antigo com o .format:** `print("A soma total foi {}".format(soma))`




# USANDO `RAW-STRING`
`Raw-String` é um tipo de `string` que você cria caso queira escrever coisas que tenham `\`. O Python indentifica os `\` como caracteres de escape, caso queira desconsiderar isso do Python, criamos as `Raw-Strings`.
Sintaxe:
```python
caminho: str = r"\Users\Rick\Downloads\Pasta"
print(caminho)
# Saída: \Users\Rick\Downloads\Pasta
```
Caso queira utilizar as `raw-strings` com as `f-strings`, só colocar o `rf` ou `fr` na frente (Como você colocaria normalmente utilizando `f-strings` ou `raw-strings` avulsas.




# COMO SABER SE UMA STRING COMEÇA COM ALGUMA PALAVRA ESPECÍFICA

1) O exemplo que eu usei foi de um programa que eu criei. O usuário fala um nome de uma cidade e o programa fala se essa cidade começa com a palavra 'Santo'.
2) Pergunta o nome da cidade e apaga algum espaço extra que acabe tendo na string
`cidade = str(input('Digite o nome de uma cidade: ')).strip()`
Fala na tela se a cidade começa com a palavra santo, pra isso ele coloca o nome inteiro da cidade tudo em maiúsculo e procura pela palavra SANTO, isso evita bugs.
`print(cidade[:5].upper() == 'SANTO')`


# FATIANDO STRINGS
**Sintaxe: `[<número>:]`
Exemplo de uso:
```python
a = "Olá, Mundo!"
print(a [2:])
# Saída: á, Mundo!
```
Aqui, "2" é o índice da string, então em Olá, Mundo!, a letra que representa o índice 2 é o "á", então estamos pedindo para que o Python mostre na tela a variável "a" à partir do índice 2 (`[2]`) e termine no final da string (`:`)

**Exemplo de uso mais avançado:**
```python
escolha_usuario = input("Par ou Ímpar? (P/I): ").strip().lower()
while not escolha_usuario or escolha_usuario[0] not in "pi":
	print("Opção inválida, por favor, digite novamente")
	escolha_usuário = input("Par ou Ímpar? (P/I): ")

```
Na linha 2, `escolha_usuario[0] not in "pi":`, `[0]` faz com que a verificação seja na primeira letra que o usuário digitar, independente se ele digitar "Par", ou "impar", vai funcionar do mesmo jeito pois a primeira letra da palavra que ele digitou é a que vai ser abordada, por causa do `[0]`.


# FORMATANDO STRINGS (COM F-STRING)
**Sintaxe:** `print(f"{"STRING QUE QUER FORMATAR":<opção>}")`
Após os `:`, existem diversas opções de formatação que podemos colocar em nossas strings:
- `<`: Alinha à esquerda
- `>`: Alinha à direita
- `^`: Centraliza. Sintaxe: 
```python
print("-"*30)
print(f"{'LISTAGEM DE PREÇOS':^30}")
print("-"*30)
''' Saída: 
------------------------------
      LISTAGEM DE PREÇOS      
------------------------------
'''
```
Vale lembrar que todos esses sinais tem o `:` no início, mas vou adicionar para reforçar
- `:=`: Força a exibição do sinal de número (por exemplo, `-` para números negativos)
- `:+`: Força a exibição do sinal de número (por exemplo, `+` para números positivos)
- (espaço): Força a exibição do sinal de número (por exemplo, `-` para números negativos) e adiciona um espaço para números positivos
- `:#`: Força a exibição do prefixo para números (por exemplo, `0b` para binário, `0o` para octal, etc.)
- `:,` ou `:_`: Adiciona separadores de milhar (por exemplo, `1,000,000` em vez de `1000000`. Ou `1_000_000` em vez de `1000000`. Existe a biblioteca `humanize` para isso também, ela retorna os números com `,`.
- `b`, `c`, `d`, `o`, `x`, `X`, `e`, `E`, `f`, `F`, `g`, `G`, `n`, `s`: Especificam o tipo de formatação para números (por exemplo, `b` para binário, `f` para ponto flutuante, etc.)
```python
print(f"{'Hello':<10}")  # Alinha à esquerda com largura de 10 caracteres
print(f"{'Hello':>10}")  # Alinha à direita com largura de 10 caracteres
print(f"{'3.14159':.2f}")  # Formata como um número de ponto flutuante com 2 casas decimais
```
- Caso queira mostrar um número em notação científica, digitamos `e`:
```python
numero_grande = 1_620_000_000
print(f'{numero_grande}:.2e')
# Saída:
1.62e+09
```
Você também pode escrever o seu número grande em notação científica, só que a variável precisa ser do tipo `float`:
```python
numero_grande: float = 1.62e9
print(f'{numero_grande}:.2e')
# Saída:
1.62e+09
```


# `=` EM F-STRINGS
**Sintaxe:**
```python
nome = 'Henrique'
idade = 14
print(f'{nome =}, {idade =}')  # Saída: nome = 'Henrique', idade = 14
```
A sintaxe `f'{idade =}'` é equivalente a `f'idade = {idade}'`. Ela imprimirá a string `'idade = 14'`.
É importante notar que isso não vai fazer tudo que as `f-strings` fazem naturalmente, só use isso se for para simplificar algo que já é simples, tipo no exemplo mostrado (não precisa ser tão simples assim, né).


# `NOT <VARIÁVEL DE TIPO STR>`
Quando fazemos a verificação em uma variável de tipo `str`, muitas vezes codamos algo tipo assim:
```python
escolha_usuario = input("Par ou Ímpar? (P/I): ").strip().lower()
while not escolha_usuario or escolha_usuario[0] not in "pi":
	print("Opção inválida, por favor, digite novamente")
	escolha_usuário = input("Par ou Ímpar? (P/I): ")
```
Na linha 2, `while not escolha_usuario` verifica se aquela variável está vazia, se esse fosse o caso, o usuário não teria digitado nada, só apertado `enter`, e se ele fizer isso, o software pede para ele digitar novamente, dessa vez, com uma opção válida, se ele não digitar, fica infinitamente nisso.

# USANDO AS FUNCIONALIDADES `FIND`, `RFIND`, `STRIP`, `RTRIP`, `LSTRIP` E `COUNT`
Lembre-se sempre de usar os parênteses depois de escrever o nome da funcionalidade

1- `.Count()`
Count é usado para contar caracteres dentro de strings, o ex que eu usei foi esse:

Quero achar quantas letras "E" tem na palavra Henrique Jorge de Queiroz, pra isso, utilizamos o `count()`
`nome = str(input('Qual é o seu nome? ')).strip .lower`
`print(f"Quantas letras 'E' possui o seu nome? {nome.count('e')}"`
Executando o programa...
```
Qual é o seu nome? Henrique Jorge de Queiroz
Quantas letras E possui o seu nome? 5
```

2- `.Find()`
Find é utilizado para achar alguma coisa dentro de uma string, o ex que eu usei pra mostrar isso foi esse:

Quero saber em qual posição o primeiro E fica no meu nome, pra isso, utilizamos o find
O +1 é utlizado porque em Python, o primeiro elemento de uma lista é 0, não 1. Mas nós humanos usamos 1, então pra não ficar confuso eu "altero" para o padrão dos humanos
`print('Em qual posição a primeira letra E fica? {}'.format(nome.find('e')+1))` 

3- `.RFind()`
RFind e utilizado para achar alguma coisa dentro de uma string, porém da direita para a esquerda, e não da esquerda para a direita. O ex que eu usei foi esse:
Quero saber em qual posição o último E fica no meu nome, pra isso, utilizamos o RFind
`print('Em qual posição a última letra E fica? {}'.format(nome.rfind('e')+1))`

4- `.Strip()`

Strip é utilizado para remover os espaços adicionais que os usuários podem colocar quando forem digitar alguma coisa no seu programa. O ex que eu usei foi esse:
Quero apagar os espaços adicionais que o usuário pode colocar quando ele for digitar algo no meu programa, pra isso, utilizamos o strip
`nome = str(input('Qual é o seu nome? ')).strip()`

Isso apaga os espaços adicionais da resposta do usuário

5- `.LStrip()`
LStrip é a mesma coisa do strip, só que ao invés de apagar todos os espaços da resposta do usuário, ele vai apagar só os primeiros, os da esquerda

6- `.RStrip()`
RStrip é a mesma coisa do strip, só que ao invés de apagar todos os espaços da resposta do usuário, ele vai apagar só os últimos, os da direita



# **ESTRUTURAS CONDICIONAIS:**
# `if` (se)
**Exemplo:**
```python
n1 = 5
n2 = 3
if n1 > n2:
	print("O primeiro número é maior que o segundo número")
```
# `elif` (se não, se)
Exemplo:
```python
n1 = 5
n2 = 3
if n1 > n2:
	print("O primeiro número é maior que o segundo número")
elif n1 < n2:
	print("O segundo número é maior que o primeiro número")
```
# `else` (Caso contrário)
Exemplo:
```python
n1 = 5
n2 = n3
if n1 > n2:
	print("O primeiro número é maior que o segundo número")
elif n1 < n2:
	print("O segundo número é maior que o primeiro número")
else:
	print("Tanto o primeiro quanto o segundo número são iguais")
```


# `match/case`
É uma forma diferente de se usar estruturas condicionais.
**Sintaxe:**
```python
match x:
    case 1:
        print("x é 1")
    case 2:
        print("x é 2")
    case _:
        print("x é outro valor")
```
`match` sempre está associado com uma variável. `case` é tipo um `if/elif`. `case _` é tipo um `else`.
**Exemplo de uso:**
```python
# Exemplo 1: Correspondência de valor
x = 1
match x:
    case 1:
        print("x é 1")
    case 2:
        print("x é 2")
    case _:
        print("x é outro valor")

# Exemplo 2: Correspondência de padrão de lista
my_list = [1, 2, 3]
match my_list:
    case [1, 2, 3]:
        print("A lista é [1, 2, 3]")
    case [4, 5, 6]:
        print("A lista é [4, 5, 6]")
    case _:
        print("A lista é outra coisa")

# Exemplo 3: Correspondência de padrão de dicionário
my_dict = {"name": "John", "age": 30}
match my_dict:
    case {"name": "John", "age": 30}:
        print("O dicionário é {'name': 'John', 'age': 30}")
    case {"name": "Jane", "age": 25}:
        print("O dicionário é {'name': 'Jane', 'age': 25}")
    case _:
        print("O dicionário é outro coisa")

# Exemplo 4: Correspondência de padrão de classe
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

person = Person("John", 30)
match person:
    case Person("John", 30):
        print("A pessoa é John com 30 anos")
    case Person("Jane", 25):
        print("A pessoa é Jane com 25 anos")
    case _:
        print("A pessoa é outra coisa")
```
**Quando usar `if`/`elif`/`else`**:
- Quando você precisa de uma lógica de controle de fluxo mais complexa, com várias condições e ações diferentes.
- Quando você precisa de uma condição que não é uma simples igualdade ou correspondência de padrão.
- Quando você precisa de uma lógica de controle de fluxo que envolva variáveis ou expressões mais complexas.
**Quando usar `match`/`case`**:
- Quando você precisa de uma correspondência de padrão simples e eficiente, especialmente com estruturas de dados como listas, tuplas, dicionários, etc.
- Quando você precisa de uma forma concisa e expressiva de lidar com diferentes casos para um determinado tipo de dados.
- Quando você precisa de uma forma de garantir que todos os casos possíveis sejam cobertos para um determinado tipo de dados.
Em resumo, `if`/`elif`/`else` é mais flexível e pode lidar com uma ampla variedade de situações, enquanto `match`/`case` é mais conciso e eficiente para lidar com correspondências de padrão simples e estruturas de dados.

**Exemplos de quando usar cada um**:
- Use `if`/`elif`/`else` quando você precisa de uma lógica de controle de fluxo mais complexa, como:
```python
if x > 5:
    print("x é maior que 5")
elif x == 5:
    print("x é igual a 5")
else:
    print("x é menor que 5")
```

- Use `match`/`case` quando você precisa de uma correspondência de padrão simples e eficiente, como:
```python
match x:
    case 1:
        print("x é 1")
    case 2:
        print("x é 2")
    case _:
        print("x é outro valor")
```
Em resumo, ambos têm seus próprios casos de uso e devem ser escolhidos com base nas necessidades específicas do seu código.


# OPERADOR TERNÁRIO
O operador ternário em Python é uma forma concisa de fazer atribuições condicionais. Ele é usado para executar uma expressão baseada em uma condição em uma única linha de código. A sintaxe do operador ternário em Python é:
`valor = expressão_verdadeira if condição else expressão_falsa`
### Exemplo:
Vamos supor que você queira atribuir um valor baseado em uma condição. Usando um operador ternário, você pode fazer isso em uma linha:
```python
idade = 18
status = "Maior de idade" if idade >= 18 else "Menor de idade"
print(status)
```
Nesse exemplo, `status` será `"Maior de idade"` se `idade` for maior ou igual a 18. Caso contrário, `status` será `"Menor de idade"`.
```python
idade = 18
status = "Maior de idade" if idade >= 18 else "Menor de idade"
print(status)
```

```python
squares = [x**2 for x in range(10) if x % 2 == 0]
print(squares)
```
### Operador ternário em funções
O operador ternário também pode ser usado em funções para retornar valores com base em uma condição:
```
def verificar_idade(idade):
    return "Maior de idade" if idade >= 18 else "Menor de idade"

print(verificar_idade(20))  # Output: Maior de idade
print(verificar_idade(15))  # Output: Menor de idade
```
O operador ternário é uma maneira concisa de expressar uma lógica condicional que, de outra forma, exigiria uma estrutura `if-else` mais longa. Ele é semelhante a uma list comprehension.
O Gustavo Guanabara, por exemplo, não gosta do Operador Ternário. Eu acho que é meio estranho sim. Prefiro usar da forma original.


# **ESTRUTURAS DE REPETIÇÃO:**
# `for loop` (Para)
**Sintaxe:** 
```python
for i in range(inicio, fim, passos):
	faça alguma coisa
```
ou:
```python
lista = [Henrique, Angélica, Alvin]
for nomes in lista:
	faça alguma coisa
```
Podemos usar o `for` não só com listas, mas com strings também, tuplas, etc.
ou:
```python
for i in range(3):
	print("Teste")
'''Saída:
Teste
Teste
Teste'''
```
O `3` digitado no `range` significa o `stop` do `for loop`, então ele vai parar no número que foi colocado. Geralmente escrevemos assim quando queremos fazer um `for loop` que começa com 0, assim, você não precisa colocar o `start`, o Python já indentifica o `start` como 0. Vale lembrar que o `for loop` vai pular o último número do loop, o último número só significa que ele parou.


**Papel de cada palavra-chave do Python no `for loop`:**
Em um exemplo de `for i in range(1, 11):`, significa "para cada número dentro de 1 até 10":
Em um exemplo de:
```python
lista = [1, 2, 3, 4, 5]
for valor in lista:
```
Significa: "para cada valor dentro da lista que eu criei:"

**Outros exemplos:**
Exemplo 1: 
`for i in range(1, 11)`
`for` = para
`i` = cada coisa
`in` = dentro de
`range` = números de
`(1, 11)` = 1 até 10, pois paramos no 11 e não o mostramos
Então basicamente fica: "Para cada coisa (número) dentro de (números de 1 até 10) faça tal coisa"

Exemplo 2:
```python
notas_estudantes = ["A", "B", "F", "A-"]
for notas in notas_estudantes:
	print(notas)
```
`for` = para
`notas` = cada coisa
`in` = dentro de
`notas_estudantes` = coisa que eu quero que ele conte, nesse caso, eu quero que ele conte a lista que eu criei, com todas as notas dos estudantes
Então basicamente fica: "Para cada coisa (`notas`) dentro de `notas_estudantes`, mostre a nota atual que você está (que seria a `notas`)."


O `range` é opcional, eu posso usar sem o `range`.
Um exemplo sem o `range` seria:
```python
notas_estudantes = ["F", "A+", "A-", "C"]
for notas in notas_estudantes:
	print(notas)
'''Saída: 
F
A+
A-
C'''
```
Nesse exemplo, o Python não mostra 1, 2, 3 porque não tem range, no caso, `notas` significa "para cada nota dentro de todas as notas dos estudantes", então `notas` vai receber à cada loop, o próximo valor da lista. E o Python também não pula o último valor, ele mostra o último valor pois não tem o `range` dentro do `for`.

Quando você está usando um o `for` junto com o `range`, o Python ignora o número que você disse para acabar, então por exemplo:
```python
for i in range(1, 11):
	print("Oi")
# A saída vai ser 10 "oi"s, porque o Python ignora o último número.
```
Vale dizer também que o laço for pode ser dividido em passos, então por exemplo:
```python
for i in range (0, 11, 2):
	print(i)
''' A saída vai ser:
2
4
6
8
10, pois pedimos para o que o for pule de 2 em 2.'''
```


# `while loop` (Enquanto)
Sintaxe:
```python
exemplo = 1
while exemplo <= 10:
	print(exemplo)
'''A saída vai ser:
1
2
3
4
5
6
7
8
9
10'''
```
# Como separar de x em x no `while loop`, como se fosse um `for`
Se quiser fazer loops que pulem de tanto em tanto, igual um `for i in range(1, 10, 2)`, esse "2", para fazer em uma estrutura while, precisamos criar uma variável para indicar esse último número, pode ser "contador", ou algo do tipo; e dentro do while loop, incrementar o quanto você quer que ele pule, se for igual ao que eu escrevi no for, ficaria assim no while:
```python
numero = int(input("Digite um número: "))
contador = 2

while contador <= numero:
	print(contador)
	contador += 2
'''Se o número digitado pelo usuário for 10, a saída é essa:
2
4
6
8
10'''
```
Como foi dito, eu criei uma variável que representa o contador, no `for` não precisamos disso, mas no `while`, sim.
Dentro da estrutura, incrementei o quanto eu queria que pulasse, quis que fosse 2, então coloquei 2.
Se eu quisesse que fosse de 0 de 2 em 2 até 10, ao invés de começar por 2, que foi o que eu fiz, eu poderia mudar o valor da variável `contador` para 0
# Como fazer contagens regressivas no `while loop`, como se fosse um `for`
Se quiser fazer loops que tenham contagens regressivas, a mesma ideia, você cria uma variável representando a terceira configuração que fazemos no for loop, podemos chamar ela de `contador` ou algo do tipo.
```python
numero = 0
contador = 10
while contador >= numero:
	print(contador)
	contador -= 1
'''Saída:
10
9
8
7
6
5
4
3
2
1
0'''
```
Percebe-se que o contador vai receber o início de trás para frente da nossa contagem, isso é, do maior número para o menor, não igual antes, que a variável contador receberia o menor número e ia até o maior número (que era a variável numero).  
Um exemplo de código que podemos usar para demonstrar a utilização dessa técnica é um Software que faz o cálculo de fatorial de um número, suponhamos que esse número seja 5, para fazermos 5!, segue o Software:
```python
numero_atual = 5
fatorial = 1
while numero_atual >= 1:
    if numero_atual > 1:
        print(f"{numero_atual}", end=" x ")
    else:
        print(f"{numero_atual} = ", end="")
    fatorial *= numero_atual
    numero_atual -= 1
print(fatorial)
```
Fatorial recebe 1, é o neutro.
Enquanto o numero_atual (contador) for menor do que 1 (queremos parar no 1, se nós multiplicase-mos por 0, daria 0 no final).
se o numero_atual for maior do que 0:
mostra na tela o número atual com o final " x "
se o numero_atual for menor ou igual à 0:
mostra na tela o número atual com o final " = "
fatorial vai receber todos os números atuais multiplicados
e o numero_atual vai descendo conforme o while loop vai passando por essa linha de código, é crucial para conseguirmos escrever do maior para o menor número
"print("1 = ", end="")" corrige o final quando todos os números foram escritos, no caso, a saída iria ser `5 x 4 x 3 x 2 x 120`, é aí que o "1 =" vem, ele corrige isso, então a saída fica `5 x 4 x 3 x 2 x 1 = 120`.


# **FUNÇÕES**
Funções são uma forma de automatizar rotinas em seu código, é muito útil.
**Sintaxe:**
```python
def soma_numeros(*num):
    print(num)
    while True:
        num.append(int(input('Digite o número: ')))
        resp = input('Deseja continuar? [S/N]: ').strip().upper()
        if resp == 'N':
            break
    print(f'A soma de todos os números digitados é {sum(num)}.')

# Programa Principal
soma_numeros()
```
O que fica dentro dos parênteses da função são os parâmetros (Variáveis que ela vai usar) dela. Quando à chamamos, nós passamos o valor que esse parâmetro vai ter. No início do código, o Python pula a função e executa o programa principal, quando chamarmos a função, devemos passar o valor do parâmetro (Nesse código, foi nenhum, pois o parâmetro vai receber o seu valor dentro da própria função). Quando passamos os valores dos parâmetros, o primeiro valor representa o valor do primeiro parâmetro da função que foi criado quando ela foi criada também, o segundo valor é do segundo parâmetro, e assim por diante; a menos que você expecifique a ordem de cada valor em cada parâmetro, por exemplo:

# FUNÇÕES COM VALORES DE PARÂMETROS ESPECIFICADOS
```python
def div(a, b):
	d = a / b
	print(f'A divisão vale {d}.')

div(b=3, a=5)
```
Nesse exemplo, eu especifiquei o valor que cada parâmetro vai receber, eu coloquei que `b=3` antes de a, que é o primeiro parâmetro, eu consegui fazer isso pois eu especifiquei o valor e a ordem de cada valor em cada parâmetro. Vale lembrar que se você especificou o valor de um parâmetro, precisa especificar de todos os outros.

# FUNÇÕES COM PARÂMETROS OPCIONAIS
```python
def somar(a=0, b=0, c=0):
    s = a + b + c
    print(f'A soma vale {s}.')

somar(1, 2)
```
Aqui, eu não especifiquei o terceiro valor, porém não deu erro, pois o Python utilizou o valor padrão de c, que é 0, então o output é "A soma vale 3."

# FUNÇÕES COM MÚLTIPLOS PARÂMETROS (EMPACOTAMENTO DE PARÂMETROS)
Caso for ter uma função com parâmetros indefinidos, você precisa fazer o empacotamento de parâmetros, se não, sua função não irá funcionar. Exemplos:
```python
def contador(*num):
	print(f'Recebi os valores {num}, e são ao todo {len(num)} números.')

contador(2, 1, 7)
contador(8, 0)
contador(4, 4, 7, 6, 2)
```
O desempacotamento que o Python faz nada mais é do que adicionar todos os valores passados na chamada da função em uma tupla. Caso quiser usar listas, é assim:
```python
def dobra(lst):
	pos = 0
	while pos < len(lst):
	lst[pos] *=2
	pos += 1

valores = [7, 2, 5, 0, 4]
dobra(valores)
print(valores)
```
O que você faz é: não desempacotar. Você pega os valores passados e adiciona eles numa lista no programa principal, e depois você passa ele como parâmetro na sua função.

# ESCOPO DE VARIÁVEIS
```python
def teste():
	x = 8 
	print(f'Na função teste, n vale {n}')
	print(f'Na função teste, x vale {x}')

# Programa Principal
n = 2
print(f'No programa principal, n vale {n}')
teste()
print('No programa principal, x vale {x}')
```
Nesse exemplo, n é uma variável de ESCOPO GLOBAL, ela tem o mesmo valor em ambas as áreas, pois ela foi declarada no programa principal, não dentro de uma função. Porém x foi declarado dentro de uma função, então, esse software dará um erro, pois ele não reconhece o valor x, pois é uma variável de ESCOPO LOCAL, que só é identificada e só pode ser utilizada dentro da função onde ela foi criada.
```python
def teste(b):
	b += 4
	c = 2
	print(f'A dentro vale {a}')
	print(f'B dentro vale {b}')
	print(f'C dentro vale {c}')

a = 5
teste(a)
print(f'A fora vale {a}')
print(f'B fora vale {b}')
print(f'C fora vale {c}')
```
Nesse exemplo, a vai ter o mesmo valor (5) tanto localmente quanto globalmente; b e c não irão ser mostrados no programa principal pois são variáveis locais, e esse software dará um erro, ele conseguirá mostrar o valor de dentro, que será b = 9 e c = 2, porém fora, não.
```python
def teste(b):
	a = 8
	b += 4
	c = 2
	print(f'A dentro vale {a}')
	print(f'B dentro vale {b}')
	print(f'C dentro vale {c}')

a = 5
teste(a)
print(f'A fora vale {a}')
```
Nesse exemplo (Adicionei uma linha após a criação da função), eu estou criando uma outra variável a (Não é a mesma variável, uma tem o valor de 8, a outra tem o valor de 5), e são variáveis diferentes, o "a" criado dentro da função é o "a" local, que vai ser mostrado no "A dentro vale {a}", mas não será mostrado no "A fora vale {a}", pois em um, está se referindo ao "a" local, que vale 8, e o "a" global, que vale 5. As mudanças que acontecem em uma variável não modificam a outra.
```python
def funcao():
	n1 = 4
	print(f'N1 dentro vale {n1}')

n1 = 2
funcao()
print(f'N1 fora vale {n1}')
```
Nesse caso, n1 dentro é o n1 local, e n1 fora é o n1 global; consequentemente, uma vale 4, e a outra vale 2. Output: "N1 dentro vale 4", e "N1 fora vale 2".

## `global <variavel>`
Caso estiver em uma função e quiser modificar o valor de uma variável global dentro da função, você deve usar o `global`, que vai indicar para o Python de que aquela variável se trata de uma variável global. Exemplo:
```python
def teste(b):
	global a
	a = 8
	b += 4
	c = 2
	print(f'A dentro vale {a}')
	print(f'B dentro vale {b}')
	print(f'C dentro vale {c}')

a = 5
teste(a)
print(f'A fora vale {a}')
```
Nesse exemplo, uma variável local "a" não existe mais, e sim, modificamos o valor de "a" (Que antes era 5), e agora tem o valor de "8". Depois que chamamos a função, "a" não volta à ser 5, agora ele é 8. "b" também não é somado com o novo valor de "a", ele é somado com o antigo, pois o valor antigo foi o valor passado para o parâmetro b, não o novo, então ele usa o antigo mesmo que o valor de "a" seja modificado depois. Output: "A dentro vale 8", "B dentro vale 9" (Foi somado com o valor antigo, 5 + 4), "C dentro vale 2".

# ESCOPO EM IMPORTAÇÕES DE BIBLIOTECAS
Quando queremos importar uma função de uma biblioteca, as vezes ela não precisa ser importada no programa inteiro, as vezes ela vai ser utilizada só dentro de uma função, então fazemos a importação local, que economiza memória e processamento do computador:
```python
def fatorial(n=1, show=False):
    from time import sleep
    """
    -> Calcula o fatorial de um número
    :param n: (Opcional, por padrão é 1) O número à ser calculado.
    :param show: (opcional, por padrão é False) Mostrar ou não a conta feita.
    """
    print('O fatorial é: ')
    f = 1
    for i in range(n, 0, -1):
        f *= i
        # Se show estiver como True, mostre a conta feita, então mostre o número atual (i), se o i for igual à 1 (Último número), você mostra "=", se não, mostre "x" mesmo:
        if show:
            print(f'{i}', end=' ', flush=True)
            sleep(0.3)
            if i == 1:
                print(f'=', end=' ', flush=True)
                sleep(0.3)
            else:
                print('x', end=' ', flush=True)
                sleep(0.3)
    # Independente se show estiver como True ou False, a função vai retornar o valor de f:
    return f

# Programa Principal
print(fatorial(5, True), end='.')
```
Nesse exemplo, o `sleep()` foi importado para ser usado só dentro da função, não no programa todo, pois não há necessidade, então fazer dessa maneira economiza memória.

# RETORNANDO VALORES EM FUNÇÕES
As funções podem não ter valor de retorno, ou podem ter, ou seja, vai retornar para uma outra função ou variável, mas se você chamar ela sozinha, ela não vai mostrar nada, caso quisesse que ela mostrasse alguma coisa, você usaria o `print()` dentro da função, ao invés do `return`, ou você chamaria a função dentro do `print()`, por exemplo: `print(funcao(a, b, c))`, aí sim ela mostraria os dados. Ou, por exemplo: 
```python
def somar(a, b, c):
    return a + b + c

soma = somar(1, 2, 3)
```
Aqui, a função `somar()` retorna a soma, porém não faz nada com ela, só retorna ela; cabe à nós decidir o que vamos fazer com esse retorno.
```
def somar(a=0, b=0, c=0):
	return a + b + c

r1 = somar(3, 2, 5)
r2 = somar(1, 7)
r3 = somar(4)
print(f'Meus cálculos deram {r1}, {r2} e {r3}.')
```
Exemplo mais completo:
```python
def notas(*n, sit=False):
    """
    -> Função que informa o total de notas de um aluno, a maior e menor nota, a média, e se o usuário quiser, a situação também.
        n (tuple): Tupla que vai receber as notas dos alunos, é ela quem vai dar todas as informações que precisamos para mostrar a saída de volta ao usuário.
        sit (bool, optional): Padrão False, se for True, vai retornar a situação do aluno junto do dicionário também.

    Returns:
        Um dicionário contendo as informações do aluno
    """
    aluno = {}
    print(f'Notas recebidas: {n}.')
    aluno['Total'] = len(n)
    aluno['Maior'] = max(n)
    aluno['Menor'] = min(n)
    media = sum(n) / len(n)
    aluno['Média'] = media
    if sit:
        if media > 7:
            aluno['Situação'] = 'BOA'
        elif media > 5:
            aluno['Situação'] = 'RAZOÁVEL'
        else:
            aluno['Situação'] = 'RUIM'
    # Se sit for False, o dicionário aluno não vai ter o item de situação, e assim que retornamos o dicionário, não terá a situação do aluno, como o usuário pediu. O item
    # Situação só vai ser criado se sit for igual à True:
    return aluno

# Programa Principal
# Mude o sit para "False" caso não queria que o software mostre a situação do aluno:
resp = notas(5.5, 7.5, 6.3, 7.5, 2.3, 1.7, 7.4, sit=True)
print(resp)
help(notas)
```

# INTERACTIVE HELP IN PYTHON
A função built-in do Python chamada `help()` te dá a documentação de quase todas as funções e bibliotecas existentes, caso tenha dúvidas, use o `help()` tanto no terminal quanto em códigos mesmo.
## Docstrings em funções próprias
Quando você mesmo cria uma função no seu código, você pode deixar essa mesma documentação que as outras funções tem, isso se chama docstring.
**Sintaxe:**
```python
def fatorial(n=1, show=False):
    from time import sleep
    """
    -> Calcula o fatorial de um número
    :param n: (Opcional, por padrão é 1) O número à ser calculado.
    :param show: (opcional, por padrão é False) Mostrar ou não a conta feita.
    """
    print('O fatorial é: ')
    f = 1
    for i in range(n, 0, -1):
        f *= i
        # Se show estiver como True, mostre a conta feita, então mostre o número atual (i), se o i for igual à 1 (Último número), você mostra "=", se não, mostre "x" mesmo:
        if show:
            print(f'{i}', end=' ', flush=True)
            sleep(0.3)
            if i == 1:
                print(f'=', end=' ', flush=True)
                sleep(0.3)
            else:
                print('x', end=' ', flush=True)
                sleep(0.3)
    # Independente se show estiver como True ou False, a função vai retornar o valor de f:
    return f
  
# Programa Principal
print(fatorial(5, True), end='.')
```

# FUNÇÕES GERAIS NO PYTHON
1. `abs()`: Retorna o valor absoluto de um número. Se for um número negativo, por exemplo, se o número é -4, o número absoluto dele é 4. Se o número é 7.3, o número absoluto é o mesmo. Basicamente, ele ignora o sinal de números positivos e negativos.
2. `round()`: Retorna o valor arredondado de um número.
3. `pow()`: Retorna o resultado de uma potência.
4. `divmod()`: Retorna o quociente e o resto de uma divisão.
5. `bin()`: Converte um número para uma string binária.
6. `oct()`: Converte um número para uma string octal.
7. `hex()`: Converte um número para uma string hexadecimal.
8. `id()`: Retorna o identificador único de um objeto.
9. `type()`: Retorna o tipo de um objeto.
10. `print()`: Imprime um valor na saída padrão.


# FUNÇÕES DE CONVERSÃO NO PYTHON

1. `int()`: Converte um valor para um inteiro.
2. `float()`: Converte um valor para um número de ponto flutuante.
3. `complex()`: Converte um valor para um número complexo.
4. `str()`: Converte um valor para uma string.
5. `list()`: Converte um valor para uma lista.
6. `tuple()`: Converte um valor para uma tupla.
7. `dict()`: Converte um valor para um dicionário.
8. `set()`: Converte um valor para um conjunto.
9. `frozenset()`: Converte um valor para um conjunto imutável.


# **MODULARIZAÇÃO E PACOTES**
Modularização é o processo de dividir um programa em partes menores e independentes, chamadas módulos, que podem ser desenvolvidos, testados e mantidos separadamente. Isso facilita a organização e a reutilização do código.
## Módulos 
Um módulo em Python é simplesmente um arquivo contendo código Python. Para criar um módulo, basta criar um arquivo com extensão `.py`, quando criar um arquivo com a intenção de ser um módulo, você precisa criar funções dentro dele, para que ele possa ser importado e que essas funções possam ser utilizadas em outros arquivos.
**Exemplo de módulo:**
```python
def leia_dinheiro(msg):
    valido = False
    while not valido:
        entrada = input(msg).strip().replace(',', '.')
        if entrada.isalpha() or entrada == '':
            print(f'\033[031mERRO: "{entrada}" é um preço inválido!\033[m')
        else:
            valido = True
            return float(entrada)
```
Quando quiser utilizar esse módulo em algum arquivo, nós o importamos para o código do arquivo que vai utilizar o módulo.
##  Estrutura:
```
diretorio_pai/
│
├── Programa Principal.py
└── Moeda.py
```
Aqui, "Moeda.py" é o módulo que vamos importar em "Programa Principal.py", geralmente dessa forma: `import moeda`, ou `from moeda import funcao_especifica`.

## Pacotes
Pacotes são uma forma de estruturar módulos Python em diretórios, facilitando a organização de projetos maiores. Um pacote é um diretório que contém um arquivo especial `__init__.py` (pode estar vazio), além de outros módulos e subpacotes. São mais utilizados em projetos grandes.
## Estrutura:
```
diretorio_pai/
│
├── Programa Principal.py
│
├── pacote_1/
	└── __init__.py
│
└── pacote_2/
	└── __init__.py
```

## Exemplo completo com Modularização e Pacotes:
Essa é a estrutura desse exemplo:
```
diretorio_pai/
│
├── Programa Principal.py
│
├── dado/
	└── __init__.py
│
└── moeda/
	└── __init__.py
```
Aqui, `Programa Principal.py` vai importar os módulos `__init__.py` (Arquivos onde ficam as funções) dos pacotes `dado/` e `moeda/`.

`__init__.py` de `dado/` possui esse código:
```python
def leia_dinheiro(msg):
    valido = False
    while not valido:
        # A entrada do usuário é primeiramente lida como uma string, para que possamos substituir todas as ',' que o usuário digitar, por '.', para que o Python entenda:
        entrada = input(msg).strip().replace(',', '.')
        # Se a entrada do usuário for alfanumérica (Ou seja, tem alguma letra) ou for uma string vazia, exiba uma mensagem de erro na cor vermelha:
        if entrada.isalpha() or entrada == '':
            print(f'\033[031mERRO: "{entrada}" é um preço inválido!\033[m')
        # Caso contrário, se for realmente um número, então valido recebe True, e a função retorna a entrada, só que do tipo float agora:
        else:
            valido = True
            return float(entrada)
```
Aqui, a função `leia_dinheiro(msg)` é como se fosse um `input`, só que o que ela tem de especial é que ela tem um certo nível de tratamento de erros.

`__init__.py` de `moeda/` possui esse código:
```python
def metade(preco=0, formato=False):
    """
    -> Retorna a metade do preço fornecido.
    preco é o preço que o usuário fornecer, se ele não fornecer nenhum preço, então o padrão é 0.
    formato é o formato que o preço vai ser mostrado. Por padrão ele é False, mas se for True, ele vai ser exibido de forma formatada, com a moeda e com vígulas ao invés de
    pontos finais.
    Retorna res de forma não formatada se formato não for True, mas caso for, retorna com a formatação."""

    res = preco / 2
    return res if not formato else moeda(res)


def dobro(preco=0, formato=False):
    """
    -> Retorna o dobro do preço fornecido.
    preco é o preço que o usuário fornecer, se ele não fornecer nenhum preço, então o padrão é 0.
    formato é o formato que o preço vai ser mostrado. Por padrão ele é False, mas se for True, ele vai ser exibido de forma formatada, com a moeda e com vígulas ao invés de
    pontos finais.
    Retorna res de forma não formatada se formato não for True, mas caso for, retorna com a formatação."""
    
    res = preco * 2
    return res if not formato else moeda(res)


def aumentar(preco=0, taxa=0, formato=False):
    """
    -> Retorna o preço fornecido, só que com um aumento de taxa%.
    preco é o preço que o usuário fornecer, se ele não fornecer nenhum preço, então o padrão é 0.
    taxa é a porcentagem de aumento/desconto no preço.
    formato é o formato que o preço vai ser mostrado. Por padrão ele é False, mas se for True, ele vai ser exibido de forma formatada, com a moeda e com vígulas ao invés de
    pontos finais.
    Retorna res de forma não formatada se formato não for True, mas caso for, retorna com a formatação."""
    
    res = preco + (preco * taxa / 100)
    return res if not formato else moeda(res)


def diminuir(preco=0, taxa=0, formato=False):
    """
    -> Retorna o preço fornecido, só que com um desconto de taxa%.
    preco é o preço que o usuário fornecer, se ele não fornecer nenhum preço, então o padrão é 0.
    taxa é a porcentagem de aumento/desconto no preço.
    formato é o formato que o preço vai ser mostrado. Por padrão ele é False, mas se for True, ele vai ser exibido de forma formatada, com a moeda e com vígulas ao invés de
    pontos finais.
    Retorna res de forma não formatada se formato não for True, mas caso for, retorna com a formatação."""

    res = preco - (preco * taxa / 100)
    return res if not formato else moeda(res)


def moeda(preco=0, moeda='R$'):
    """
    -> Mostra o preço de forma formatada, bonita.
    preco é o preço que o usuário fornecer, se ele não fornecer nenhum preço, então o padrão é 0.
    moeda é a moeda que vai ser mostrada antes do preço, você pode modificar ela se quiser, o padrão é R$, mas pode colocar USD$, etc."""
    
    return f'{moeda}{preco:<.2f}'.replace('.', ',')


def resumo(preco=0, taxa_a=10, taxa_r=5):
    """
    -> Retorna a saída de todas as outras funções numa tabelinha.
    preco é o preço fornecido pelo usuário. Por padrão, é 0.
    taxa_a é a taxa de aumento fornecida pelo usuário. Por padrão, é 10.
    taxa_r é a taxa de redução fornecida pelo usuário. Por padrão, é 5."""
    
    print('-'*40)
    print('RESUMO DO VALOR'.center(40))
    print('-'*40)
    print(f'Preço analisado: \t{moeda(preco)}.')
    print(f'DOBRO do preço: \t{dobro(preco, True)}.')
    print(f'METADE do preço: \t{metade(preco, True)}.')
    print(f'{taxa_a}% de AUMENTO: \t{aumentar(preco, taxa_a, True)}.')
    print(f'{taxa_r}% de DESCONTO: \t{diminuir(preco, taxa_r, True)}.')
    print('-'*40)
```
Esse módulo é onde as principais funções do código vão ser armazenadas, cada uma faz uma coisa com o preço, e no final é mostrada no `resumo()`.

`Programa Principal.py`:
```python
from utilidadesCeV import moeda, dado

p = dado.leia_dinheiro('Digite o preço: R$')
taxa_au = float(input('Quantos % de aumento? '))
taxa_di = float(input('Quantos % de desconto? '))
moeda.resumo(p, taxa_au, taxa_di)
```
`utilidadesCeV` é o diretório pai desse exemplo, eu importei as coisas dentro dos diretórios `moeda/` e `dado/`. p recebe a função `leia_dinheiro` de `dado/`, que vai verificar se a entrada do usuário é realmente correta; `taxa_au` é a taxa de aumento que vamos passar para a função `resumo()` dentro de `moeda/` no futuro, ela vai armazenar o `input()` de quanto o usuário quer aumentar o preço; e a mesma coisa para `taxa_di`, que é a taxa de diminuição do preço, que vai ser passada também para a função `resumo()`. Por fim, chamamos a função que está dentro de `moeda/`, que é a função `resumo()`, com os parâmetros: primeiro, o número que o usuário quer que aumente, e segundo, o número que o usuário quer que ele desconte.

## Vantagens da modularização e pacotes
- **Reutilização de código**: Módulos e pacotes podem ser reutilizados em diferentes partes do projeto ou em projetos diferentes.
- **Organização**: Facilita a organização do código em partes menores e mais gerenciáveis.
- **Manutenção**: Torna a manutenção do código mais fácil, pois cada módulo/pacote pode ser atualizado independentemente.
- **Colaboração**: Permite que diferentes desenvolvedores trabalhem em diferentes módulos/pacotes simultaneamente.
## Boas práticas
- Dê nomes significativos aos módulos e pacotes.
- Mantenha cada módulo focado em uma única responsabilidade.
- Documente seus módulos e pacotes para facilitar o uso e manutenção.


# **TRATAMENTO DE ERROS**
# `try`, `except`, `else` e `finally`:
`try` significa "Tente", é para o computador tentar fazer alguma coisa. Caso não funcione, então temos o `except`, que é: "caso isso que o computador fez não deu certo, faça isso:". Se o `try` der certo e você quiser que ele faça algo caso dê certo, porém isso depois do `except`, você usa o `else`. Quando quiser que ele faça algo independente do que aconteça, use o `finally`.

**Exemplos de uso:**
```python
try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b
except:
    print('Infelizmente, tivemos um problema...')
else:
    print(f'O resultado é {r:.1f}')
finally:
    print('Volte sempre! Muito obrigado!')
```

Exemplo um pouco mais específico, nós podemos criar vários excepts. Agora, para quase todos os erros que o usuário poderia fazer, o software tem uma resposta:
```python
try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b
except (ValueError, TypeError):
    print('Tivemos um problema com os tipos de dados que você digitou.')
except (ZeroDivisionError):
    print('Não é possível dividir um número por zero!')
except KeyboardInterrupt:
    print('O usuário preferiu não informar os dados!')
except Exception as erro:
    print(f'O erro encontrado foi {erro.__cause__}')
else:
    print(f'O resultado é {r:.1f}')
finally:
    print('Volte sempre! Muito obrigado!')
```
Você também pode descrever para o usuário/desenvolvedor o tipo de erro que está ocorrendo. Mas sem estar naquele texto clássico de erro que o Python dá. Como por exemplo:
```python
try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b
except Exception as erro:
    print(f'Infelizmente, tivemos um problema... o erro é {erro.__class__s}')
else:
    print(f'O resultado é {r:.1f}')
finally:
    print('Volte sempre! Muito obrigado!')
```


# **MANIPULAÇÃO DE ARQUIVOS EM PYTHON**
## Funções e Métodos
1. **`open(file, mode)`**
    - Abre um arquivo e retorna um objeto de arquivo.
    - `file`: Nome do arquivo a ser aberto.
    - `mode`: Modo em que o arquivo será aberto (detalhes abaixo).
2. **`file.close()`**
    - Fecha o arquivo. É importante fechar o arquivo após terminar de usá-lo para liberar os recursos do sistema.
3. **`file.read(size=-1)`**
    - Lê o conteúdo do arquivo. Se `size` for passado, lê até `size` bytes/caracteres.
4. **`file.readline(size=-1)`**
    - Lê uma linha do arquivo. Se `size` for passado, lê até `size` bytes/caracteres.
5. **`file.readlines()`**
    - Lê todas as linhas do arquivo e retorna uma lista de strings, cada uma representando uma linha.
6. **`file.write(string)`**
    - Escreve a string fornecida no arquivo.
7. **`file.writelines(lines)`**
    - Escreve uma lista de strings no arquivo. Não adiciona quebras de linha automaticamente.
8. **`file.seek(offset, whence=0)`**
    - Move o ponteiro de leitura/escrita para uma posição específica no arquivo.
    - `offset`: Número de bytes a mover.
    - `whence`: Ponto de referência (`0` para início, `1` para posição atual, `2` para fim do arquivo).
9. **`file.tell()`**
    - Retorna a posição atual do ponteiro de leitura/escrita no arquivo.
10. **`file.flush()`**
    - Esvazia o buffer de escrita, garantindo que todos os dados sejam gravados no arquivo.
11. **`file.truncate(size=None)`**
    - Reduz o tamanho do arquivo para o valor especificado por `size`. Se `size` não for especificado, o arquivo é truncado na posição atual do ponteiro.

### Modos de Abertura (`mode`)
1. **`'r'`**
    - Abre o arquivo para leitura. O arquivo deve existir.
2. **`'w'`**
    - Abre o arquivo para escrita. Cria um novo arquivo se ele não existir ou trunca o arquivo se ele já existir.
3. **`'x'`**
    - Abre o arquivo para escrita exclusivamente. Cria um novo arquivo, mas falha se o arquivo já existir.
4. **`'a'`**
    - Abre o arquivo para adição (append). Os dados são adicionados ao fim do arquivo. Cria o arquivo se ele não existir.
5. **`'b'`**
    - Abre o arquivo em modo binário (por exemplo, `'rb'`, `'wb'`).
6. **`'t'`**
    - Abre o arquivo em modo texto (por exemplo, `'rt'`, `'wt'`). Este é o padrão se nenhum modo for especificado.
7. **`'+'`**
    - Abre o arquivo para atualização (leitura e escrita) (por exemplo, `'r+'`, `'w+'`).




# **OUTRAS COISAS**


# WALRUS OPERATOR
**Sintaxe:** `:=`
A principal vantagem do Walrus Operator é que ele permite escrever código mais conciso e legível, evitando a necessidade de linhas adicionais apenas para atribuição de valores.
**Exemplo sem o Walrus Operator:**
```python
# Calculando o comprimento de uma lista
lista = [1, 2, 3, 4, 5]
comprimento = len(lista)
if comprimento > 3:
    print("A lista é grande")
else:
    print("A lista é pequena")
# Saída: A lista é grande
```

**Com o Walrus Operator:**
```python
# Calculando o comprimento de uma lista
lista = [1, 2, 3, 4, 5]
if (comprimento := len(lista)) > 3:
    print("A lista é grande")
else:
    print("A lista é pequena")
```
Neste exemplo, `comprimento := len(lista)` atribui o valor de `len(lista)` à variável `comprimento` e, em seguida, avalia o valor atribuído na expressão condicional.
O Walrus Operator pode ser usado em uma ampla variedade de situações, como loops, compreensões de listas, expressões condicionais e mais. No entanto, é importante usá-lo com moderação e apenas quando ele realmente torna o código mais claro e legível, pois um uso excessivo pode dificultar a compreensão do código.


# ANOTAÇÕES DE TIPO (TYPE HINTS)

# Variáveis simples:
```python
nome: str = "Alice"
idade: int = 30
altura: float = 1.75
is_estudante: bool = True
```

# Listas:
```python
numeros: list[int] = [1, 2, 3, 4, 5]
nomes: list[str] = ["Alice", "Bob", "Charlie"]
```

# Dicionários:
```python
pessoa: dict[str, str] = {"nome": "Alice", "cidade": "São Paulo"}
contagem: dict[str, int] = {"maçãs": 3, "bananas": 2}
```

# Tuplas:
```python
coordenadas: tuple[float, float] = (10.5, 20.3) 
info_pessoa: tuple[str, int, bool] = ("Alice", 30, True)
```

# Conjuntos:
`frutas: set[str] = {"maçã", "banana", "laranja"}`

# Funções:
```python
def saudacao(nome: str) -> str:
    return f"Olá, {nome}!"

def soma(a: int, b: int) -> int:
    return a + b
```

# Classes:
```python
class Pessoa:
    def __init__(self, nome: str, idade: int):
        self.nome: str = nome
        self.idade: int = idade

    def apresentar(self) -> str:
        return f"Meu nome é {self.nome} e tenho {self.idade} anos."
```

# Union types (quando uma variável pode ter mais de um tipo):
```python
from typing import Union

resultado: Union[int, str] = 42  # pode ser int ou str
```

# Optional (para variáveis que podem ser None):
```python
from typing import Optional

valor: Optional[int] = None  # pode ser int ou None
```

# Any (para tipos dinâmicos):
```python
from typing import Any

valor_dinamico: Any = "qualquer coisa"
```

# Callable (para funções):
```python
from typing import Callable

def executar_operacao(func: Callable[[int, int], int], a: int, b: int) -> int:
    return func(a, b)
```

# TypedDict (para dicionários com chaves específicas):
```python
from typing import TypedDict

class PessoaDict(TypedDict):
    nome: str
    idade: int

pessoa: PessoaDict = {"nome": "Alice", "idade": 30}
```




**Exemplos de uso:** 
```
variavel: tipo = valor
```
**Outro exemplo:** 
```python
def soma(a: int, b: int) -> int:
    return a + b
```
Neste exemplo, `a: int` e `b: int` são anotações de tipo para os parâmetros `a` e `b`, indicando que eles devem ser inteiros. A anotação `-> int` depois da definição da função indica que a função deve retornar um inteiro.
No entanto, é importante notar que as anotações de tipo em Python são apenas para fins de documentação e não são verificadas em tempo de execução pelo interpretador Python.
**Outro exemplo:**
```python
nome: str = "João"
idade: int = 25
preço: float = 19.99
ativos: bool = True
```
## Anotações de Tipo em Funções

Adicionar anotações de tipo a funções envolve especificar os tipos dos parâmetros e do valor de retorno. A sintaxe é:
```python
def nome_da_função(parametro1: tipo1, parametro2: tipo2) -> tipo_de_retorno:
    ...
```
**Exemplos de anotações de tipo em Funções:**
```python
def soma(a: int, b: int) -> int:
    return a + b

def cumprimentar(nome: str) -> str:
    return f"Olá, {nome}!"

def calcular_area(raio: float) -> float:
    return 3.14 * raio * raio
```
## Anotações de Tipo em Classes
Você também pode usar anotações de tipo dentro de classes. Por exemplo:
```python
from typing import List, Optional

class Pessoa:
    def __init__(self, nome: str, idade: int, amigos: Optional[List[str]] = None):
        self.nome: str = nome
        self.idade: int = idade
        self.amigos: Optional[List[str]] = amigos if amigos is not None else []

    def adicionar_amigo(self, amigo: str) -> None:
        self.amigos.append(amigo)
```


# FORMATANDO NÚMEROS FLOAT
`{}` É o marcador de espaço reservado na string onde o valor formatado será inserido.
`:` Indica que a formatação seguirá algumas instruções adicionais.
`{.2f}` Especifica a precisão da formatação para números de ponto flutuante. Neste caso, o `2` indica que você quer duas casas decimais após o ponto decimal, e o `f` indica que é um número de ponto flutuante (float).
a expressão `{:.2f}` está formatando o valor da variável 'raiz' com duas casas decimais após o ponto decimal. Em `.format` fica mais fácil, mas em `f-string` pode parecer mais difícil, aqui está um exemplo:
```python
n1 = float(input("Digite um número: "))
n2 = float(input("Digite outro número: "))
print(f"A soma desses 2 números é {n1 + n2:.2f})

'''se os números forem 5.111 + 5.111, o resultado seria 10.222, mas como estamos formatando, a saída é:
10.22'''
```


# ORDEM DE PRECEDÊNCIA DE CONTAS ARITMÉTICAS
1) (Parênteses)
2) ** (Potenciação)
3) `*`, /, //, % (Multiplicação, divisão, divisão exata (quando algum resultado seria em float e você quer que mostre só o resultado sem a vírgula, tipo 5/2= 2.5, você pediria pra mostrar só "2" ao invés de '2.5'), resto da divisão)
4) +, - (Adição, subtração)
5) ! (Fatorial)



# **FÓRMULAS DE MATEMÁTICA**

# COMO CALCULAR RAÍZ QUADRADA EM PYTHON
1) Você importa a biblioteca math, ou só a funcionalidade de raiz quadrada da biblioteca math, desse jeito:

```python
from math import sqrt
n = float(input('Digite um número: ')) 
raiz = sqrt[ou qualquer outra funcionalidade que eu quiser de uma biblioteca] (n)
print ('A raiz quadrada desse número é: {:.2f}'.format(raiz)

```
OU
```python
import math
num = int(input('Digite um número: '))
raiz = math.sqrt(num)
print ('A raiz de {} é igual a {:.2f}'.format(num, raiz))
```
2) Ou você pega o seu número e faz a exponenciação dele por 0.5, ou seja. Ex:
```python
n = float(input('Digite um número: '))
print('A raiz quadrada desse número é {:.2f}'.format (n **(1/2)
```




# COMO PEGAR A UNIDADE, DEZENA, CENTENA, MILHAR, ETC DE FORMA MATEMÁTICA
1) Vamos pegar o exemplo de um programa que eu criei, ele pede um número de 0 ate 9999, quando o usuário diz o número, ele diz a unidade, dezena, centena e unidade de milhar do número, e mostra '0' quando o número não possui alguma categoria
Pergunta o número do usuário
`num = int(input('Digite seu número de 0 até 9999: '))`
Faz a conta pra cada categoria. A fórmula é: 
Se é unidade, pega esse número e faz a divisão inteira dele por 1 (unidade), depois você faz o módulo (%) do resultado por 10
`u = num // 1 % 10`
Se é dezena, pega esse número e faz a divisão inteira dele por 10 (dezena), depois você faz o módulo (%) do resultado por 10
`d = num // 10 % 10`
Se é centena, pega esse número e faz a divisão inteira dele por 100 (centena), depois você faz o módulo (%) do resultado por 10
`c = num // 100 % 10`
Se é unidade de milhar, pega esse número e faz a divisão inteira dele por 1000 (unidade de milhar), depois você faz o módulo (%) do resultado por 10
`m = num // 1000 % 10`
e assim por diante...
Escreve na tela cada resultado da fórmula
```python
print('Unidade: {}'.format(u))
print('Dezena: {}'.format(d))
print('Centena: {}'.format(c))
print('Unidade de milhar: {}'.format(m))
```


# COMO SABER SE UM NÚMERO É PAR OU ÍMPAR
**PAR:** Você pega o seu número e faz a divisão dele por 2, se o resto da divisão for 0 quer dizer que esse número é PAR. Ex: se `<numero> % 2 = 0` então esse número é **PAR**
**ÍMPAR:** Você pega o seu número e faz a divisão dele por 2, se o resto da divisão for 1 quer dizer que esse número é ÍMPAR. Ex: se `<numero> % 2 = 1` então esse número é **ÍMPAR**


# COMO CALCULAR DESCONTAGEM
**Fórmula: Preço final = Preço inicial * (1 - porcentagem de desconto / 100)
Para calcular um preço com desconto, você subtrai a porcentagem de desconto do preço inicial:

**Exemplo: 
Preço inicial = 100
Porcentagem de desconto = 10%
Preço final = 100 * (1 - 10 / 100)
Preço final = 100 * 0,90
Preço final = 90

**Exemplo mais detalhado:
Preço inicial = 100
Porcentagem de desconto = 10%
Preço final = preço inicial * (1 - 10 / 100)
O que o computador vai fazer:
Dentro dos parênteses:
10 / 100 = 0.1
1 - 0.1 = 0.9
Fora dos parênteses:
preço inicial * 0.9 = 90
preço final = 90


# COMO CALCULAR PORCENTAGEM ADICIONAL SOBRE ALGUM VALOR
**Fórmula: Valor Final = Valor Inicial * (1 + porcentagem de acréscimo / 100)
Se você quer adicionar 20% ao preço inicial, a porcentagem é 0,20, então a fórmula fica:
Preço Final = Preço Inicial * 1,20

Exemplo: Eu comprei um produto de 100R$, mas como ele foi importado tem um imposto de 17% sobre aquele valor. Qual vai ser o valor final adicionando esse imposto sobre o valor?
Valor Inicial = 100
Porcentagem = 17% (ou 0,17 em decimal)
Valor Final = 100 * (1 + 0,17)
Valor Final = 100 * 1,17
Valor Final = 117



# COMO CALCULAR CELSIUS PARA FAHRENHEIT
**Fórmula:** F = 9 * C (qtde Ceusius) / 5 + 32
# COMO CALCULAR FAHRENHEIT PARA CELSIUS
**Fórmula:** C = (F - 32) / 1,8




# O QUE SIGNIFICA CADA SÍMBOLO DE IGUAL
**Operadores de Comparação:**
1) `==` (é igual à). Ou seja, ex: `3 * 5 == 15`
2) `>=` (maior ou igual à)
3) `<=` (menor ou igual à)
4) `!=` (Diferente, não é)
**Operadores de Atribuição:**
1) `=` (recebe). Ou seja, ex: `teste = (recebe) input ("Digite um valor: ")`
2) `variável +=` (Adicionar alguma coisa à variável)
3) `variável -=` (Remover alguma coisa da variável)
4) `variável *=` (Multiplicar a variável com alguma coisa)
5) `variável **=` (Eleva a variável à potencia de alguma coisa)
6) `variável /=` (Dividir alguma coisa com a variável)
7) `variavel //=` (Divide a variável por alguma coisa e retorna a divisão exata dela)
8) `variável %=`  (Atribui o resto da divisão de uma variável por alguma coisa)
9) `!=` (Diferente, não é)
**Outros:**
1) `:=` (Walrus Operator)



# **IMPORTANDO FRAMEWORKS/BIBLIOTECAS**

Pra importar uma biblioteca do que for, escreva: `import [nome da bilioteca]`, desse jeito você importa todos as funcionalidades que aquela biblioteca tem.
Se você quer importar uma ou mais funcionalidades de uma biblioteca, mas não todas, escreva: `from [nome da biblioteca] import [funcionalidade que você quer importar, se for mais de 1 você coloca a vírgula e espaço e digita a funcionalidade]`


# BIBLIOTECA RANDOM (ALEATÓRIO)
`choice`: Escolhe UM elemento da lista de forma aleatória: 
```python
import random
options = ['pedra', 'papel', 'tesoura']
print(choice(options))
# A saída pode ser, por exemplo: pedra
```
`choices`: Pode escolher MÚLTIPLOS elementos da lista de forma aleatória:
```python
from random import choices
options = ['pedra', 'papel', 'tesoura']
print(choices(options, k = 2))
# A saída pode ser, por exemplo: ['papel', 'tesoura'], ou ['pedra', 'tesoura']
```
O `k=valor` define quantos elementos da lista o `choices()` vai retornar. Se não houver esse `k=valor`, o `choices()` retorna 1 valor só, dentro de uma lista. Caso eu não quisesse ter que ficar contando todos os elementos da estrutura de dados, ou eu talvez modifique a estrutura de dados no futuro, eu posso colocar `k=len(people)`, é uma forma mais inteligente de se fazer isso.

Existe o `weight=valor` também, que define a probabilidade do `choices()` escolher aquele elemento na estrutura de dados.
```python
from random import choice, choices
people = ['Bob', 'Tom', 'James', 'Sandra']
print(f'choice() = {choice (people)}')
weights = (15, 20, 35, 30)
print(f'choices() = {choices(people, k=5, weights=weights)}')
```
Nesse exemplo, Bob tem a probabilidade de 15%, Tom tem 20%, James tem 35% e Sandra tem 30%.
Eu poderia fazer desse jeito aqui, também:
```python
from random import choice, choices
people = ['Bob', 'Tom', 'James', 'Sandra']
print(f'choice() = {choice (people)}')
print(f'choices() = {choices(people, k=5, weights=[15, 20, 35, 30])}')
```
O resultado é o mesmo, só que no primeiro exemplo eu estou atribuindo essa lista de probabilidades em uma variável, aqui eu estou falando diretamente a lista para o `weight`.
`weight` só pode receber números positivos, pode receber números `float`, e a soma de todos os números digitados tem que ser igual à 1 (ou à 100), pois estamos trabalhando com porcentagem, por CENTO (100/1)

`randint()`: Escolhe um número aleatório entre 2 polos. Por exemplo:
```python
import random
print(random.randint(1, 10))
# A saída pode ser um número de 1 até 10
```
`random()`: Retorna um número ponto flutuante aleatório no intervalo `[0.0, 1.0]`.
```python
import random
print(random.random())
# A saída pode ser, por exemplo: 0.5930548549876546, 1.0, 0.1231231231238564, etc.
```
`randrange()`: Retorna um elemento selecionado aleatoriamente a partir de um intervalo. Se parece com o `for loop` com o `range()`
```python
import random
print(random.randrange(1, 10, 2))
# A saída pode ser, por exemplo: 3
```
No `randrange()`, o último valor passado é desconsiderado, diferente do `randint()`, onde o último valor é incluído no intervalo de números que ele pode retornar. Além disso, podemos dizer de quanto em quanto nós queremos esse intervalo, se for algo como `print(random.randrange(0, 10, 2))`, o `randrange()` pode retornar um número que seja entre 0 e 9 (Pois o último valor é desconsiderado), só que no intervalo de 2 em 2, ou seja, ele pode retornar 0, 2, 4, 6, 8.
Nós também podemos, igual faríamos num `for loop`, dizer só o último número do intervalo, por exemplo:
```python
from random import randrange
print(randrange(5))
# A saída pode ser um número de 0 até 4
```
Nesse caso, o `randrange()` considera o 5 como o último valor do intervalo, então ele vai desconsiderar ele e contabilizar todos os números antecessores à ele, isso é, 0, 1, 2, 3 e por fim, 4.

Você não pode dar 2 números iguais para o intervalo do `randrange()`. Por motivos óbvios.
Você não pode colocar um número menor em seguida de um número maior, pois isso não faz sentido:
```
from random import randrange
print(randrange(2, 5))
# Tipo assim, vai retornar o erro "empty range in randrange(2, 5)"
```

`shuffle()`: Embaralha uma estrutura de dados.
```python
import random
deck = ['A', 'K', 'Q', 'J', '10']
random.shuffle(deck)
print(deck)
```
Outro exemplo:
```python
from random import shuffle
lista = ['Alvin', 'Luna', 'Rick']
print(shuffle(lista))
# A saída pode ser por exemplo: ['Luna', 'Rick', 'Alvin'], ['Rick', 'Luna', 'Alvin'], ['Luna', 'Alvin', 'Rick'], etc.
```

`sample`: Escolhe x elementos de uma população (Lista, tupla, etc), exibe eles na tela sem os outros elementos que não foram selecionados. Os elementos nunca são repetidos
```python
import random

# Definindo uma lista de números
numbers = [1, 2, 3, 4, 5]

# Usando sample para escolher aleatoriamente 3 elementos da lista
random_selection = random.sample(numbers, 3)

print("Seleção aleatória:", random_selection)
print("Lista original:", numbers)

```
`uniform()`: Mostra um número float entre 2 números
```python
import random

# Gerando um número float aleatório entre 1.0 e 10.0
random_number = random.uniform(1.0, 10.0)
print(random_number)
```



# BIBLIOTECA DATETIME
Para exibir a data/hora atual, usamos o `%`:
```python
from datetime import datetime
now: datetime = datetime.now()
print(f"{now:%d.%m.%y}")
# Vamos supor que hoje seja 29/06/2024:
# Saída:
29.06.2024
```


# BIBLIOTECA PYAUTOGUI (AUTOMAÇÕES)

`pyautogui.click(x=742, y=345)` -> clicar em algum lugar da tela | (CLICKS=2) significa o tanto de clicks que ele vai dar na tela | (BUTTON='right') aperta um botão específico do mouse, meio, direito, esquerdo, etc)
`pyautogui.write('alguma coisa')` -> escrever um texto
`pyautogui.press('enter')` -> pressionar 1 tecla do teclado
`pyautogui.hotkey('ctrl', 'c')` -> pressionar teclas especiais do teclado ao mesmo tempo
`pyautogui.PAUSE = 0.5` -> sempre que você rodar um novo comando do pyautogui vai ter a pausa de x segundos
`pyautogui.position()` -> posição do mouse na tela
`pyautogui.scroll()` -> Rolar o scroll do mouse




# BIBLIOTECA PANDAS (DADOS)
Usando um projeto como exemplo

`pandas.read_csv(produtos.csv)` -> lê um arquivo, pode ser csv, html, excel, word, sql, json, pdf, tudo
`for linha in tabela.index:` -> .index é de linha, para cada linha da minha tabela. Se fosse .columns seria para coluna, etc. For é estrutura de loop. 'Linha' é o nome do contador do loop
`codigo = tabela.loc` -> loc é pra localizar alguma coisa de uma tabela
`tabela.loc[linha, 'codigo']` -> Linha é o contador do loop, é cada linha mesmo. Codigo é a coluna de cada produto, ela precisa ser escrita da exata mesma forma que foi escrito na tabela
`tabela = tabela.drop(columns='CustomerID')` -> .drop é para jogar fora, tipo 
`tabela = tabela.dropna()` -> Tira os valores vazios da tabela
`display(tabela['cancelou'].value_counts(normalize=True))` -> Pega os valores da coluna 'cancelou', pega quem cancelou e quem não cancelou e faz a porcentagem deles por meio do 'normalize=True'




# BIBLIOTECA PLOTLY


`grafico = px.histogram(tabela, x='idade', color='cancelou')` -> px é a abreviação à ploty.express, histogram é o tipo do gráfico, como se fosse um de barra. O eixo y o plotly já sabe, mas você precisa falar o eixo x, o eixo x é a idade de cada cliente, e o color ali é pra comparar os que não cancelaram com os que cancelaram



# BIBLIOTECA PYGAME (PARA TOCAR MÚSICA)
1) Site para baixar vídeos do YouTube e converter eles para mp3: https://y2meta.app/pt15
2) Site para baixar vídeos do TikTok e converter eles para mp3: https://ssstik.io/en
3) importando a biblioteca pygame, que é voltada para jogos mas você consegue usar ela para tocar músicas também
```python
# Iniciando:
import pygame
pygame.init()
# Importando a música:
pygame.mixer.music.load("nome da sua musica".mp3)
# Iniciando a música:
pygame.mixer.music.play()
# Colocando por quanto tempo essa música vai ser tocada (em milisegundos, que são 50 segundos de música):
pygame.time.wait(50000)
```




# BIBLIOTECA JSON
A biblioteca JSON (JavaScript Object Notation) do Python é uma biblioteca padrão que permite trabalhar com dados no formato JSON. Aqui está uma explicação detalhada das funções e recursos disponíveis na biblioteca JSON do Python:


**Funções de codificação**
- `json.dumps()`: converte um objeto Python em uma string JSON.
```python
import json

data = {'nome': 'João', 'idade': 30}
json_data = json.dumps(data)
print(json_data)  # saída: '{"nome": "Jo\u00e3o", "idade": 30}'
```

- `json.dump()`: converte um objeto Python em uma string JSON e escreve em um arquivo.
```python
import json

data = {'nome': 'João', 'idade': 30}
with open('data.json', 'w') as f:
    json.dump(data, f)
```


**Funções de decodificação**
- `json.loads()`: converte uma string JSON em um objeto Python.
```python
import json

json_data = '{"nome": "Jo\u00e3o", "idade": 30}'
data = json.loads(json_data)
print(data)  # saída: {'nome': 'João', 'idade': 30}
```

- `json.load()`: lê um arquivo JSON e converte em um objeto Python.
```python
import json

with open('data.json', 'r') as f:
    data = json.load(f)
print(data)  # saída: {'nome': 'João', 'idade': 30}
```


**Outras funções**
- `json.JSONEncoder`: uma classe que pode ser usada para personalizar a codificação de objetos Python em JSON.
```python
import json

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

class PessoaEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Pessoa):
            return {'nome': obj.nome, 'idade': obj.idade}
        return super().default(obj)

pessoa = Pessoa('João', 30)
json_data = json.dumps(pessoa, cls=PessoaEncoder)
print(json_data)  # saída: '{"nome": "Jo\u00e3o", "idade": 30}'
```

- `json.JSONDecoder`: uma classe que pode ser usada para personalizar a decodificação de JSON em objetos Python.
```python
import json

class PessoaDecoder(json.JSONDecoder):
    def __init__(self, *args, **kwargs):
        super().__init__(object_hook=self.dict_to_pessoa, *args, **kwargs)

    def dict_to_pessoa(self, d):
        if 'nome' in d and 'idade' in d:
            return Pessoa(d['nome'], d['idade'])
        return d

json_data = '{"nome": "Jo\u00e3o", "idade": 30}'
pessoa = json.loads(json_data, cls=PessoaDecoder)
print(pessoa.nome)  # saída: João
print(pessoa.idade)  # saída: 30
```


**Constantes**

- `json.JSONDecodeError`: uma exceção que é lançada quando ocorre um erro durante a decodificação de JSON.
- `json.JSONEncodeError`: uma exceção que é lançada quando ocorre um erro durante a codificação de objetos Python em JSON.




# BIBLIOTECA EMOJI
Site dos emojis: https://www.webfx.com/tools/emoji-cheat-sheet/
1) 
`import emoji`

`print(emoji.emojize("aqui você escreve caracteres ascii, letras, essas coisas. emoji que você quiser, pode ser a imagem mesmo, ou pode ser o código dele"))`



# BIBLIOTECA TIME
`time.sleep(3)` 
Faz uma pausa só naquela hora que você falar para pausar no seu código



# ESCREVENDO COMENTÁRIOS:
1) Você pode usar o caractere `#` seguido do que você quiser escrever. O computador vai ignorar tudo escrito após o sinal de `#`
2) Você também pode usar os caracteres `'''comentário aleatório exemplo'''` para escrever seus comentários, porém, dessa forma você pode escrever comentários de várias linhas, o computador vai ignorar tudo até o final do comentário `'''`. Você pode usar aspas duplas também, `"""dessa forma"""`




# **OUTRAS COISAS**

# `itemgetter()`
`itemgetter()` é uma função da biblioteca `operator` do Python. Ela pega um ou mais itens numa estrutura de dados. O número inteiro que é passado dentro dos parênteses indica o índice do elemento que você quiser pegar.
**Exemplos de uso e sintaxe:**
```python
from operator import itemgetter

# Cria uma função que pega o item no índice 1
pegar_segundo = itemgetter(1)

# Usa a função criada
lista = [10, 20, 30]
resultado = pegar_segundo(lista)  # resultado será 20
```

```python
from operator import itemgetter

pessoas = [('João', 25), ('Maria', 30), ('Pedro', 20)]
pessoas_ordenadas = sorted(pessoas, key=itemgetter(1))
print(pessoas_ordenadas)
# Resultado: [('Pedro', 20), ('João', 25), ('Maria', 30)]
```
`key=itemgetter(1)` basicamente é: `sorted()` está perguntando "Você quer que eu ordene o quê?" e `key` fala que quer ordenar os itens baseado no `itemgetter(1)`, então `sorted()` entende que ele deve ordenar os itens baseado no segundo elemento da tupla, que é sua idade.
Outro exemplo com o `sorted()` e `itemgetter()`:
```python
from random import randint
from time import sleep
from operator import itemgetter

jogo = {'jogador_1': randint(1, 6),
        'jogador_2': randint(1, 6),
        'jogador_3': randint(1, 6),
        'jogador_4': randint(1, 6)}

ranking = []


print('Valores sorteados: ')
for k, v in jogo.items():
    print(f'{k} tirou {v} no dado.')
    sleep(1)
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
print('== RANKING DOS JOGADORES ==')
for i, v in enumerate(ranking):
    print(f' {i+1}° lugar: {v[0]} com {v[1]} pontos.')
    sleep(1)
```
Aqui é a mesma coisa, `sorted()` pergunta "Quer que eu ordene esse dicionário de que forma?" `key=itemgetter(1)` mostra que ele quer que os pares Chave-Valor sejam ordenados pelo valor (Se fosse 0, seria ordenado pelas chaves), isso é, pelo número que cada jogador tirou, do maior para o menor, por conta do `reverse=True`
 ```python
pegar_primeiro_e_terceiro = itemgetter(0, 2)
lista = [10, 20, 30, 40]
resultado = pegar_primeiro_e_terceiro(lista)  # resultado será (10, 30)
```

```python
pessoa = {'nome': 'Ana', 'idade': 28, 'cidade': 'São Paulo'}
pegar_nome_e_idade = itemgetter('nome', 'idade')
resultado = pegar_nome_e_idade(pessoa)  # resultado será ('Ana', 28)
```

## `getitem()` com outras funções:

1) Com `map()`:
```python
lista_de_tuplas = [(1, 'a'), (2, 'b'), (3, 'c')]
apenas_numeros = list(map(itemgetter(0), lista_de_tuplas))
# Resultado: [1, 2, 3]
```
2) Com `max()` e `min()`:
```python
from operator import itemgetter

pessoas = [{'nome': 'ChatGPT', 'idade': 2}, {'nome': 'Claude', 'idade': 1}]
# Pegando a pessoa mais velha e mais nova
pessoa_mais_velha = max(pessoas, key=itemgetter('idade'))
pessoa_mais_nova = min(pessoas, key=itemgetter('idade'))

# Pegando a idade da pessoa mais velha e mais nova
idade_mais_velha = pessoa_mais_velha['idade']
idade_mais_nova = pessoa_mais_nova['idade']

# Pegando o nome da pessoa mais velha e mais nova
nome_mais_velha = pessoa_mais_velha['nome']
nome_mais_nova = pessoa_mais_nova['nome']

print(f'Pessoa mais velha: {pessoa_mais_velha["nome"]}, {pessoa_mais_velha["idade"]}.')
print(f'Pessoa mais nova: {pessoa_mais_nova["nome"]}, {pessoa_mais_nova["idade"]}.')
```
aqui, `pessoa_mais_velha` e `pessoa_mais_nova` são duas variáveis que vão receber o item do dicionário `pessoas`, quem vai atribuir o item vai ser `max` e `min`, quem vai decidir quem vai ir pra cada variável vai ser o `key=itemgetter('idade')`, basicamente o que isso faz no `max()` é:  "pegue o maior elemento, baseado na chave 'idade'. Quem tiver a maior idade, atribua à essa variável". E a mesma coisa para `min()`, só que para a pessoa que tiver a menor idade.

3) Com Strings:
```python
pegar_primeira_letra = itemgetter(0)
palavra = "Python"
primeira_letra = pegar_primeira_letra(palavra)  # Retorna 'P'
```
5. Casos de uso comuns:
    - Ordenação de listas de objetos complexos
    - Extração de dados específicos de estruturas aninhadas
    - Mapeamento de dados em operações de processamento de dados
6. Vantagens:
    - Mais eficiente que usar lambdas para a mesma tarefa
    - Código mais limpo e legível em certas situações

O `itemgetter` é particularmente útil quando você precisa extrair repetidamente o mesmo item de múltiplos objetos, como em operações de ordenação ou mapeamento de dados.
