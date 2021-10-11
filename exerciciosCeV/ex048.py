s = 0
for c in range (1, 501):
    if c % 2 == 1 and c % 3 == 0:
        print(c)
        s = s + c
print(f'O somatorio dos numeros é igual a {s}')
