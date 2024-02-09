frase = str(input('Digite uma frase: ')).lower() .strip()
#EN: It counts how many letters "A" the phrase have using the functionality find
#BR: Conta quantas vezes a letra "A" aparece na frase usando a funcionalidade count
print('A letra A aparece {} vezes na frase'.format(frase.count('a')))

#EN: Find where the first letter "A" is using the find + 1 functionality, to put it in the human counting pattern
#BR: Acha onde a primeira letra "A" fica usando a funcionalidade find + 1, para colocar no padrão de contagem dos humanos
print('A primeira posição onde um A foi encontrado foi na posição {}'.format(frase.find('a')+1))

#EN: Find where the last letter "A" is using the rfind + 1 functionality, to put it in the human counting pattern
#BR: Acha onde a última letra "A" fica usando a funcionalidade rfind + 1, para colocar no padrão de contagem dos humanos
print('A útlima letra A foi encontrada na posição {}'.format(frase.rfind('a')+1))
