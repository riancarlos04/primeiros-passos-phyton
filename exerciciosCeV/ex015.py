dia = int(input('Quantidades de dias: '))
km = float(input('Quantos Km rodados: '))
vt = (60 * dia) + (0.15 * km)
print(f'O valor a se pagar devido à {dia} dias e {km}Km é de R$ {vt:.2f}')