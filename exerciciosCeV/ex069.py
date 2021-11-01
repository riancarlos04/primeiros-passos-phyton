contadoridade = homens = mulheres20 = 0
while True:
    idade = int(input('Digite a idade: '))
    if idade >= 18:
        contadoridade += 1
    sexo = ' '
    while sexo not in 'FM':
        sexo = str(input('Sexo [F/M]: ')).strip().upper()[0]
    if sexo == 'M':
        homens += 1
    if sexo == 'F' and idade <= 20:
        mulheres20 += 1
    opcao = ' '
    while opcao not in 'SN':
        opcao = str(input('Deseja continuar? [S/N]')).strip().upper()[0]
    if opcao == 'N':
        break
print(f'''AO TOTAL:
{contadoridade} pessoas tem mais de 18 anos
{homens} homens foram cadastrados
{mulheres20} mulheres tem menos de 20 anos''')