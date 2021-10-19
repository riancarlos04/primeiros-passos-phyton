somaidade = 0 #variavel para somar a idade
homemvelho = '' # variavel para o homem mais velho
idadehomevelho = 0 # variavel paraca idade do homem mais velho
contmulher = 0 # contador de mulher com menos de 20 anos
for c in range(1, 5):
    print(f'-'*5,f'PESSOA {c}', '-'*5)
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade (anos): '))
    somaidade += idade
    sexo = str(input('Sexo (M/F): ')).strip()
    if sexo in 'Mm' and idade > idadehomevelho:
        idadehomevelho = idade
        homemvelho = nome
    if sexo in 'Ff' and idade < 20:
        contmulher += 1
mediaidade = somaidade / 4
print(f'A media de idade é {mediaidade:.1f} anos')
print(f'O homem mais velho é {homemvelho} com {idadehomevelho} anos')
print(f'Ao total {contmulher} mulheres tem menos de 20 anos')