num = int(input('Digite um Numero: '))
cont = 0
for c in range(1, num + 1):
    if num % c == 0:
        print('\033[33m', end=' ')
        cont += 1
    else:
        print('\033[31m', end=' ')
    print(f'{c}', end=' ')
print(f'\n\033[mO numero {num} foi divisivel {cont} vezes!')
if cont == 2:
    print(f'Por isso o numero {num}, É PRIMO')
else:
    print(f'Por isso o numero {num}, NÃO É PRIMO')

