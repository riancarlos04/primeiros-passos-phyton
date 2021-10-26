print(' '*7, 'GERADOR DE PA')
print('-='*20)
t1 = int(input('Primeiro termo: '))
razao =  int(input('Razão: '))
termo = t1
cont = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while cont <= total :
        print(f'{termo} -> ', end='')
        termo += razao
        cont += 1
    print('PAUSA')
    mais = int(input('Quantos termos voce quer mostrar a mais? '))
print('FIM')
print(f'Ao todo foram mostrados {total} termos mostrados')
