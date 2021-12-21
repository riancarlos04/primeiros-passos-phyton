#Minha resolução
"""valores = [0, 0, 0, 0, 0]
for c, v in enumerate(valores):
    valores[c] = int(input(f'Digite um Numero para a posição {c}: '))
print('-='*20)
print(f'Voce digitou os valores: {valores}')
print(f'O maior valor digitado foi {max(valores)}, na posição {valores.index(max(valores))}')
print(f'O menor valor digitado foi {min(valores)} na posição {valores.index(min(valores))}')"""

#resoluçãodoguanabara
valores = []
maior = menor = 0
for c in range(0, 5):
    valores.append(int(input(f'Digite um número na posição {c}: ')))
    if c == 0:
        menor = maior = valores[c]
    else:
        if valores[c] > maior:
            maior = valores[c]
        if valores [c] < menor:
            menor = valores[c]

print('=-'*30)
print(f'Voce digitou os valores: {valores}')
print(f'O maior valor digitado foi {maior} nas posiçoes ', end='')
for i, v in enumerate(valores):
    if v == maior:
        print(f'{i}...', end='')
print()
print(f'O menor valor digitado foi {menor} nas posições ', end='')
for i, v in enumerate(valores):
    if v == menor:
        print(f'{i}...', end='')
