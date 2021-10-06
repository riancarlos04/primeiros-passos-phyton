produto = float(input('Digite o valor do produto R$ '))
print('''Opçoes de pagamento:
[ 1 ] A vista (dinheiro ou cheque)
[ 2 ] A vista no cartao
[ 3 ] 2x no cartao
[ 4 ] 3x ou mais no cartao ''')
opcao = int(input('Digite a opção: '))
if opcao == 1:
    valorfinal = produto - (produto * 10 / 100)
    print(f'O valor final será de R$ {valorfinal:.2f}')
elif opcao == 2:
    valorfinal = produto - (produto * 5 / 100)
    print(f'O valor final sera de R$ {valorfinal:.2f}')
elif opcao == 3:
    parcela = produto / 2
    print(f'O valor da parcela é de R${parcela:.2f} e o valor final do produto é R$ {produto:.2f}')
elif opcao == 4:
    numparcela = int(input('Digite o número de parcelas: '))
    valorfinal = produto + (produto * 20 / 100)
    parcela = valorfinal / numparcela
    print(f'O valor da parcela sera de R$ {parcela:.2f} e o valor final sera de R$ {valorfinal:.2f}')
else:
    print('Opção invalida')