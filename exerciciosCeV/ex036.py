print('-='*20)
print('EMPRESTIMO BANCARIO')
print('-='*20)
Vcasa = float(input('Qual o valor da casa R$ '))
sal = float(input('Qual o seu salário R$ '))
anos = int(input('Gostaria de pagar em quantos anos: '))
prestM = Vcasa / (anos * 12)
print(f'Para pagar uma casa no valor de R$ {Vcasa:.2f} em {anos}:')
if prestM <= 30/100 * sal :
    print('SEU EMPRESTIMO FOI APROVADO!')
    print(f'O valor da prestação sera de R$ {prestM:.2f} por Mes')
else:
    print('INFELIZMENTE SEU EMPRESTIMO FOI NEGADO')
    print(f'O VALOR DA PRESTAÇÃO R$ {prestM} SUPEROU 30% DO SEU SALÁRIO')