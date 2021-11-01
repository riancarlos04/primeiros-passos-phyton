print('-'*30)
print(f"{'LOJA ENCANTADA':-^30}")
print('-'*30)
soma = total1000 = menor = cont = 0
barato = ''
while True:
    produto = str(input('Nome do produto: ')).strip()
    preço = float(input('Preço: R$ '))
    cont += 1
    soma += preço
    if preço >= 1000:
        total1000 += 1
    if cont == 1 or preço < menor:
        menor = preço
        barato = produto
    opcao = ' '
    while opcao not in 'SN':
        opcao = str(input('Deseja continuar? [S/N]')).strip().upper()[0]
    if opcao == 'N':
        break
print(f'Total da compra: R$ {soma:.2f}')
print(f'AO total {total1000} produtos custaram mais de R$ 1000.00')
print(f'O produto mais barato foi {barato} que custa custa R$ {menor:.2f}')