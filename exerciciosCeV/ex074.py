from random import randint
numeros = ((randint(1,10)), (randint(1,10)),
           (randint(1,10)), (randint(1,10)),
           (randint(1,10)), (randint(1,10)))
print('Os números sorteados foram: ', end='')
for c in numeros:
    print(c, end=' ')
print(f'\nO maior numero foi: {max(numeros)}')
print(f'O menor número foi: {min(numeros)}')
