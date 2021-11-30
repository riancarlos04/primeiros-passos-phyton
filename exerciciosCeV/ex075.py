valores = (int(input('Digite um número: ')),
           int(input('Digite outro número: ')),
           int(input('Digite mais um número: ')),
           int(input('Digite o ultimo número: ')))
print(f'O valor 9 apareceu {valores.count(9)} vezes')
if 3 in valores:
    print(f'O primeiro vaor 3 apareceu na {valores.index(3) + 1}º posição')
else:
    print('O valor 3 não foi digitado em nenhuma posição')
print(f'Os números pares foram: ', end='')
for c in valores:
    if c % 2 == 0:
        print(c)

