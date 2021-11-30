brasileirao21 = ('Atlético-MG', 'Palmeiras', 'Flamengo', 'Bragantino',
                 'Fortaleza', 'Corinthians', 'Internacional', 'Fluminense',
                 'Cuiabá', 'América-MG', 'Atlético-GO', 'São Paulo',
                 'Ceará', 'Athlético-PR', 'Santos', 'Bahia', 'Sport Recife',
                 'Juventude', 'Grêmio', 'Chapecoense')
print('-='*30)
print(f"{'TABELA DO BRASILEIRAO 21': ^50}")
print('-='*30)
for c in range(0,20):
    print(f'{c+1: >10}º {brasileirao21[c]:>30}')


print('-'*45)
print(f"{'5 PRIMEIROS COLOCADOS': ^40}")
print('-'*45)
for c in range(0, 5):
    print(f'{c+1: >10}º {brasileirao21[c]:>30}')


print('-='*30)
print(f"{'TIMES EM ORDEM ALFABETICA': ^50}")
print('-='*30)
print(sorted(brasileirao21))

print('-='*30)
print(f'A Chapecoense está na {brasileirao21.index("Chapecoense") + 1}º Posição')
