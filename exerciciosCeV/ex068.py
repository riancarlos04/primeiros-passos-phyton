from random import randint
cont = 0
print('-='*20)
print('VAMOS JOGAR PAR OU IMPAR')
print('-='*20)
while True:
    jogador = int(input('Digite um valor: '))
    ParImp = ' '
    while ParImp not in 'PI':
        ParImp = str(input('Par ou Impar? [P/I]')).strip().upper()[0]
    computador = randint(0, 10)
    soma = jogador + computador
    print('-'*20)
    if soma % 2 == 0:
        print(f'Voce jogou {jogador} e computador jogou {computador}. total de {soma} DEU PAR')
    else:
        print(f'Voce jogou {jogador} e computador jogou {computador}. total de {soma} DEU IMPAR')
    if ParImp == 'P' and soma % 2 == 0 or ParImp == 'I' and soma % 2 != 0 :
        print('VOCE VENCEU!')
        print('VAMOS JOGAR NOVAMENTE')
        print('-='*20)
        cont += 1
    else:
        print('VOCE PERDEU')
        print('-='*20)
        break

print(f'GAME OVER! Voce venceu {cont} vezes')