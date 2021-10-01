from datetime import date
anoat = date.today().year
print('-='*20)
print('OLÁ JOVEM !')
print('-='*20)
ano = int(input('Digite o ano de nascimento: '))
print(f'Voce tem {anoat - ano} anos entao:')
if anoat - ano < 18 :
    print('VOCE AINDA IRA SE ALISTAR')
    print(f'FALTAM {18 - (anoat -ano)} ANOS PARA VOCE SE ALISTAR')
elif anoat - ano == 18:
    print('JÁ ESTÁ NA HORA DE VOCE SE ALISTAR')
elif anoat - ano > 18:
    print('JA PASSOU DA HORA DE VOCE SE ALISTAR')
    tempexc = (anoat - ano) - 18
    print(f'VOCE DEVIA TER SE ALISTADO HÁ {tempexc} ANOS ATRAS')