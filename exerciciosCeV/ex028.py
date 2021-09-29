from random import randint
from time import sleep
num = randint(0, 5)
print('-=-'*20)
print('JOGO DA ADIVINHAÇÃO')
print('-=-'*20)
numU = int(input('Dgite um número entre 0 e 5: '))
print('PROCESSANDO...')
sleep(3)
if num == numU :
    print(f'PARABENS, voce acertou o numero escolhido pelo computador!')
    print(f'Seu número {numU} numero do computador {num}')
else:
    print('ERROU, tente novamente!')
    print(f'Seu numero {numU} numero do computador {num}')
