print(' '*7, 'GERADOR DE PA')
print('-='*20)
t1 = int(input('Primeiro termo: '))
razao =  int(input('Razão: '))
termo = t1
cont = 1
while cont <= 10:
    print(f'{termo} -> ', end='')
    termo += razao
    cont += 1
print('FIM')

