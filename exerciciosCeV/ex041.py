from datetime import date
anoat = date.today().year
print('-='*20)
print('CLASSIFICAÇÃO DE ACORDO A IDADE')
print('-='*20)
anonasc = int(input('Digite seu ano de nascimento: '))
idade = anoat - anonasc
if idade <=9:
    print(f'De acordo sua idade de {idade} anos, voce é MIRIM')
elif idade <= 14 :
    print(f'De acordo sua idade de {idade} anos, voce é INFANTIL')
elif idade <= 19:
    print(f'De acordo sua idade de {idade} anos, voce é JUNIOR')
elif idade <= 25 :
    print(f'De acordo sua idade de {idade} anos, voce é SÊNIOR')
else:
    print(f'De acordo com sua idade de {idade} anos, voce é MASER')
