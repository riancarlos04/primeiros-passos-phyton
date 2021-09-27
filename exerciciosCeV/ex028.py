from random import randint
num = randint(0, 5)
numU = int(input('digite um número entre 0 e 5: '))
if num == numU :
    print(f'PARABENS, voce acertou o numero escolhido pelo computador!')
    print(f'Seu número {numU} numero do computador {num}')
else:
    print('ERROU, tente novamente!')
    print(f'Seu numero {numU} numero do computador {num}')