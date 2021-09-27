vel = float(input('Qual a velocidade do carro (km/h): '))
if vel > 80 :
    print('Voce foi MULTADO!')
    mul = (vel - 80 ) * 7
    print(f'Sua multa foi de R$ {mul:.2f}')
else:
    print('PARABENS você nao ultrapassou o limite!')
