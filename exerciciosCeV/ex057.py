s = ''
while s != 'M' and s != 'F':
    s = str(input('Digite o sexo [M/F]: ')).upper().strip()[0 ]
    if s != 'M' and s != 'F':
        print('Voce digitou errado, preste atenção e faça novamente!')
print(f'Sexo {s} registrado!')