# Lista de palavras que vamos analisar:
palavras = ("aprender", "programar", "linguagem", "python",
            "curso", "grátis", "estudar", "praticar", 
            "trabalhar", "mercado", "programador", "futuro")
# Para cada palavra na tupla palavras:
for p in palavras:
    # upper deixa a palavra atual em maiúsculo:
    print(f"\nNa palavra {p.upper()} temos: ", end="")
    # Para cada letra na palavra atual:
    for letras in p:
        # Se a letra estiver dentro da tupla de vogais:
        if letras in "aáâãeéêiíoóôõuúû":
            # Mostre a letra (que é uma vogal):
            print(letras, end=" ")
