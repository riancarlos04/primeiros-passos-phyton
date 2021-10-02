from random import choice
print('-='*20)
print('PEDRA , PAPEL OU TESOURA')
print('-='*20)
lista = ['PEDRA', 'PAPEL', 'TESOURA']
jogador = str(input('Faca uma jogada (PEDRA, PAPEL OU TESOURA): ')).strip().upper()
computador = choice(lista)
if jogador == 'PEDRA' and computador == 'TESOURA':
    print('Voce ganhou!, computador jogou TESOURA')
elif jogador == 'TESOURA' and computador == 'PEDRA':
    print('Voce Perdeu!, computador jogou PEDRA')
elif jogador == 'PAPEL' and computador == 'PEDRA':
    print('Voce ganhou!, computador jogou PEDRA')
elif jogador == 'PEDRA' and computador == 'PAPEL':
    print('Voce Perdeu!, computador jogou PAPEL')
elif jogador == 'TESOURA' and computador == 'PAPEL':
    print('Voce ganhou, computador jogou PAPEL')
elif jogador == 'PAPEL' and computador == 'TESOURA':
    print('Voce perdeu!, computador jogou TESOURA')
elif jogador == computador:
    print(f'EMPATE, computador jogou {computador}')

