from datetime import date
contMaior = 0
contMenor = 0
anoatual = date.today().year
for c in range (0, 7):
    anonasc = int(input('Digite seu ano de nascimento: '))
    if anoatual - anonasc >= 18:
        contMaior = contMaior + 1
    else:
        contMenor = contMenor + 1
print(f'''Ao total temos: 
{contMenor} pessoas que nao atingiram a maioridade
{contMaior} pessoas que ja antingiram a maioridade''')