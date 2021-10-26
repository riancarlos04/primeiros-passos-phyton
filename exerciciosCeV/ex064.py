num = 0
cont = 0
soma = 0
while num != 999:
    num = int(input('Digite um número [999 para parar]: '))
    if num != 999:
        cont +=1
        soma += num
print(f'Ao todo foram digitados {cont} numeros e a soma entre eles é {soma}')