s = 0
cont = 0
for c in range(0, 6):
    n = int(input('Digite um numero: '))
    if n % 2 == 0:
        s += n
        cont += 1
print(f'A somatoria dos números {cont} pares foi {s}')