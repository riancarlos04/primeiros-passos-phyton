n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2) / 2
print(f'A sua média foi {m:.2f}')
if m >= 6.0:
    print('A sua méddia foi boa, PARABENS!')
else:
    print('A sua média foi ruim, ESTUDE MAIS!')

