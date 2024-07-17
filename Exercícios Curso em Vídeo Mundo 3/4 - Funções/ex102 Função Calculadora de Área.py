def area():
    lar = float(input('LARGURA (m): '))
    com = float(input('COMPRIMENTO (m): '))
    print(f'A área de um terreno {lar}x{com} é de {lar*com}m².')
    
    
# Programa Principal
print('  Controle de Terrenos')
print('-'*20)
# Chamamos a função area(), que vai perguntar a largura e o comprimento do terreno, depois vai calcular e mostrar na tela:
area()
