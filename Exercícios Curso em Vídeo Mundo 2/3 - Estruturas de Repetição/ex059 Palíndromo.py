print("   DETECTOR DE PALÍNDROMOS")
print("-"*30)
# I prefer to do like this:
# Eu prefiro fazer assim:
# But we are practicing "for", so I'm going to use "for" for this software
# Mas nós estamos praticando o "for", então eu vou fazer esse software com o "for"
'''frase = str(input("Digite uma frase: ")).strip().upper()
palavras = frase.split()
junto = "".join(palavras)
# The inverse = the sentence joins starting from the beginning (:) and going to the end (:) but going backwards (-1):
# O inverso = a frase junta começando do início (:) e indo até o final (:) só que indo de trás para frente (-1):
inverso = junto[::-1]
print(f"O inverso de {junto} é {inverso}")
if inverso == junto:
    print("Temos um palíndromo!")
else:
    print("A frase digitada não é um palíndromo!")'''
    

print("Um palíndromo é quando uma palavra na ordem original dela escrita inversamente é lida da mesma forma. Então 'ana' lido de trás para frente é igual, então é um palíndromo.")
frase = str(input("Digite uma frase (Palíndromos não são contados com pontuação e acentos, então escreva sem acentos, pontuação, etc. Só espaços): ")).strip().upper()
# Each word is separated with the .split():
# Cada palavra é separada com o .split():
palavras = frase.split()
# "junto" Removes the [] that would be in the sentence and remove the spaces:
#"junto" Remove os [] que ficariam na frase e deixa ela sem espaços:
junto = "".join(palavras)
inverso = ""
# It goes at the last letter (- 1) to the first (it wouldn't show the first letter, so we put -1) and goes backwards:
# Vai da última letra (- 1) até a primeira (A primeira seria 0, ele não mostraria a primeira letra, por isso colocamos -1) e vai de trás para frente (-1):
for letra in range(len(junto) - 1, -1, -1):
    # The 'inverso' (inverse word) will receive the word from the variable "junto", but inversely ([letter]). Because 'for' is going through all the letters of the word together, 
    # but in a  inverted, so "junto[letra]" means (All the letters of the word 'junto', but as 'letra' is inverted, the letter that the 'for' is traversing in this
    # moment is the letter of 'junto' but the position backwards), SO MEANS: "The 'inverso' (inverted word) receives all the letters in the reverse positions of 'junto'"
    
    # A palavra inversa vai receber a palavra da variável "junto", só que inversamente ([letra]). Pois o 'for' está percorrendo todas as letras da palavra junto, só que de forma 
    # invertida, então "junto[letra]" significa (Todas as letras da palavra junto, só que como 'letra' está de forma invertida, a letra que o 'for' está percorrendo nesse
    # momento é a letra de 'junto' só que a posição de trás para frente), ENTÃO SIGNIFICA: "A palavra invertida recebe todas as letras nas posições inversas de 'junto'"
    inverso += junto[letra]
print(f"O inverso de {junto} é {inverso}.")
if inverso == junto:
    print("Temos um palíndromo!")
else:
    print("A frase digitada não é um palíndromo!")
