sal = float(input('Qual p valor do salário R$ '))
if sal >= 1250:
    aum = ((10/100) * sal) + sal
    print(f'Seu novo salário sera de R$ {aum:.2f}')
else:
    aum = ((15/100) * sal) + sal
    print(f'Seu novo salário sera de R$ {aum:.2f}')