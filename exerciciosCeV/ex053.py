frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = junto[::-1]
'''for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]'''
print(f'O inverso de {junto} é {inverso}')
if junto == inverso:
    print('Temos um PALINDROMO')
else:
    print('A frase digitada NAO É UM PALINDROMO')