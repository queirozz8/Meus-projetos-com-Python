print("-=" * 20)
print("        ANALISADOR DE TRIÂNGULOS")
print("-=" * 20)

r1 = float(input("Digite o primeiro segmento de reta do triângulo: "))
r2 = float(input("Digite o segundo segmento de reta do triângulo: "))
r3 = float(input("Digite o terceiro segmento de reta do triângulo: "))

print(f"SEGMENTOS: {r1}, {r2}, {r3}")

# If the straight segment of the triangle it's lower than the sum of the other 2 segments:
# Se um segmento de reta do triângulo é menor do que a soma dos outros 2 segmentos:
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print("Os segmentos acima PODEM FORMAR um triângulo.")
else:
    # If it's not lower than the sum of the other 2 segments:
    # Se não for menor do que a soma dos outros 2 segmentos:
    print("Os segmentos acima NÃO PODEM FORMAR um triângulo.")
