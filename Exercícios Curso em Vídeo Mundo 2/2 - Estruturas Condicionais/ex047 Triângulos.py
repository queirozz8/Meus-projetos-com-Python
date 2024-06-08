l1 = float(input("Digite o primeiro segmento do triângulo: "))
l2 = float(input("digite o segundo segmento do triângulo: "))
l3 = float(input("Digite o terceiro segmento do triângulo: "))
print(f"SEGMENTOS: {l1}, {l2}, {l3}.")
if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l1 + l2:
    print("Os segmentos de reta que foram dados PODEM FORMAR um triângulo.")
    if l1 == l2 == l3:
        print("Os segmentos de reta que foram dados formam um triângulo EQUILÁTERO (Todos os lados iguais).")
    elif l1 != l2 and l1 != l3:
        print("Os segmentos de reta que foram dados formam um triângulo ESCALENO (Todos os lados diferentes).")
    else: 
        print("Os segmentos de reta que foram dados formam um triângulo ISÓSCELES (Dois lados diferentes).")
else:
    print("Os segmentos de reta que foram dados NÃO PODEM FORMAR um triângulo.")
