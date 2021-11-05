extenso = 'Zero', 'Um', 'Dois', 'Tres', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze', 'Quatoze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte'
while True:
    num = int(input('Digite um numero entre 0 e 20 para ser escrito por extenso: '))
    while num < 0 and num > 20:
        num = int(input('Opção Inválida. Digite um numero entre 0 e 20 para ser escrito por extenso: '))
    if num >= 0 and num <= 20:
        break
print(f'O numero {num} por extenso é: {extenso[num]}')