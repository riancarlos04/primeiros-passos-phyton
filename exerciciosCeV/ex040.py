n1 = float(input('NOTA 1: '))
n2 = float(input('NOTA 2: '))
m = (n1 + n2)/2
if m <= 5:
    print(f'Com sua média {m:.2f} infelizmente voce foi REPROVADO')
elif m > 5 and m <= 6.9:
    print(f'Com sua media {m:.2f} voce ficou em RECUPERAÇÃO')
elif m >= 7:
    print(f'PARABENS, com sua media {m:.2f} voce foi APROVADO')
