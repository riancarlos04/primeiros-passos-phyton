numeros = []
pares = []
impares = []
while True:
    n = int(input('Digite um número: '))
    numeros.append(n)
    if n % 2== 0:
        pares.append(n)
    else:
        impares.append(n)
    r = str(input('Deseja continuar?[S/N] '))
    if r in 'Nn':
        break
print('-='*30)
print(f'Voce digitou os números: {numeros}')
pares.sort()
print(f'Os números pares foram {pares}')
impares.sort()
print(f'Os números impares foram {impares}')