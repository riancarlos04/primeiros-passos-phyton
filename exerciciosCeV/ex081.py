numeros = []
while True:
    numeros.append(int(input('Digite um número: ')))
    r = str(input('Deseja continuar? [S/N]')).upper().strip()[0]
    if r in 'Nn':
        break
print('-='*30)
print(f'Ao total foram digitados {len(numeros)} numeros: ')
numeros.sort(reverse=True)
print(f'Os valores em ordem decrescente são: {numeros}')
if 5 in numeros:
    print('O valor 5 está na lista')
else:
    print('O Valor 5 não está na lista')