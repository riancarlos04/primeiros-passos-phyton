valor1 = int(input('Digite o valor 1: '))
valor2 = int(input('Digite o valor 2: '))
r = 0
while r != 5:
    print('''
    -----------------------------
               MENU
    -----------------------------
    [ 1 ] Somar
    [ 2 ] Multiplicar
    [ 3 ] Maior
    [ 4 ] Novos numeros
    [ 5 ] Sair do programa
    ------------------------------
    ''')
    r = int(input('Digite a opção: '))
    if r == 1:
        soma = valor1 + valor2
        print(f'A soma entre {valor1} e {valor2} é {soma}')
    elif r == 2:
        produto = valor1 * valor2
        print(f'Multiplicando {valor1} por {valor2} temos o resultado {produto}')
    elif r == 3:
        maior = valor1
        if valor2 > valor1:
            maior = valor2
        print(f'O maior valor foi: {maior}')
    elif r == 4:
        valor1 = int(input('Digite o valor 1: '))
        valor2 = int(input('Digite o valor 2: '))
    elif r == 5:
        print('FECHANDO PROGRAMA')
    else:
        print('OPÇÃO INVALIDA')
print(('Fim do programa! Volte sempre'))

