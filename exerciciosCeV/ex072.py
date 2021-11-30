extenso = ('Zero', 'Um', 'Dois', 'Tres', 'Quatro',
          'Cinco', 'Seis', 'Sete', 'Oito', 'Nove',
          'Dez', 'Onze', 'Doze', 'Treze', 'Quatoze',
          'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito',
          'Dezenove', 'Vinte')
while True:
    while True:
        num = int(input('Digite um numero entre 0 e 20 para ser escrito por extenso: '))
        if num >= 0 and num <= 20:
            break
        print('Tente novamente. ', end='')
    print(f'O numero {num} por extenso é: {extenso[num]}')
    opçao = str(input('Gostaria de continuar? [S/N]')).strip().upper()[0]
    while opçao not in 'SN':
        opçao = str(input('Opção inválida.Gostaria de continuar? [S/N]')).strip().upper()[0]
    if opçao == 'N':
        break