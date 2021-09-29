dist = float(input('Digite a distância da viagem (km): '))
print(f'Voce está prestes de começar uma viagem de {dist} Km')
if dist <= 200 :
    pas = dist * 0.50
    print(f'O valor da passagem será R$ {pas:.2f}')
else:
    pas = dist * 0.45
    print(f'O valor da passagem sera R$ {pas:.2f}')