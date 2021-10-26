r = 'S'
cont = 0
somatorio = 0
maior = 0
menor = 0
while r in 'Ss':
    num = int(input('Digite um número: '))
    somatorio += num
    cont += 1
    if cont == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    r = str(input('Deseja continuar? [S/N]')).strip().upper()[0]
media = somatorio / cont
print(f'Ao todo foram mostrados {cont} numeros e a media entre eles é {media:.2f}')
print(f'O maior número digitado foi {maior}')
print(f'O menor número digitado foi {menor}')