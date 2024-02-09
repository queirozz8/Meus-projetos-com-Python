print ('Eu sou um programa criado para fornecer quantos litros de tinta você precisa para pintar uma parede, contando que: 1 L de tinta pinta 2 metros')
larg = float(input('Digite a largura da sua parede em metros: '))
alt = float(input('Digite a altura da sua parede em metros: '))
area = larg * alt
print ('Sua parede tem a dimensão de {}x{} e sua área é de {}m².'.format (larg, alt, area))
tinta = area / 2
print ('Você precisará de {}l de tinta para pintar essa parede'.format (tinta))
