menorpeso = 1000
maiorpeso = 0
for c in range (1, 6):
    peso = float(input(f'Peso da pessoa {c} (Kg) : '))
    if peso < menorpeso:
        menorpeso = peso
    elif peso > maiorpeso:
        maiorpeso = peso
print(f'''O maior peso digitado foi {maiorpeso:.2f} Kg
O menor peso digitado foi {menorpeso:.2f} Kg''')