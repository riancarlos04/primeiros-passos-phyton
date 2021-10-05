valor1 = int(input('Digite o valor 1: '))
valor2 = int(input('Digite o valor 2: '))
if valor1 > valor2 :
    print(f'O valor 1 [{valor1}] é o maior ')
elif valor2 > valor1 :
    print(f'O valor 2 [{valor2}] é o maior')
elif valor1 == valor2 :
    print('Nao existe valor maior, ambos são iguais')
