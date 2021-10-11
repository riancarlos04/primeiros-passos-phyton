contador = 0
n = int(input('Digite um numero: '))
for c in range (1, 11):
    if n % c != 0:
        verificador = 1
    else:
        verificador = 2
if verificador == 1:
    print(f'O numero {n} é PRIMO')
elif verificador == 2:
    print(f'O numero {n} NÃO É PRIMO')

