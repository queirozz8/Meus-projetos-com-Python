def voto(ano=0):
    from datetime import date
    atual = date.today().year
    idade = atual - ano
    if idade < 16:
        return f'Com {idade} anos, você tem menos de 16 anos e NÃO VOTA.'
    
    elif 16 <= idade < 18:
        return (f'Com {idade} anos, o voto é OPCIONAL, pois você ainda não fez 18 anos, mas tem 16 ou 17 anos.') 
    
    elif 18 <= idade:
        if idade > 65:
            return f'Com {idade} anos, o voto é OPCIONAL, pois você tem mais de 65 anos.'
        else:
            return f'Com {idade} anos, você é OBRIGADO À VOTAR, pois tem entre 18 à 65 anos.'
    
print(voto(int(input('Que ano você nasceu? (ANO DE NASCIMENTO, não sua idade): '))))