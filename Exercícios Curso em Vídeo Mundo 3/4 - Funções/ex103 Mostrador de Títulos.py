def escreva(palavra):
    # Modifique o número depois do "+" para adicionar mais linhas no começo e final do Título
    tam = len(palavra) + 4
    print('~'*tam)
    # Escreve a palavra centralizada no tamanho que foi anteriormente passado na função:
    print(f'{palavra:^{tam}}')
    print('~'*tam)


# Programa Principal
escreva('CRIADOR DE TÍTULOS. Exemplos abaixo...')
escreva('Gustavo Guanabara')
escreva('Curso de Python no YouTube')
escreva('CeV')
escreva(input('Que outro título você quer que eu mostre? '))