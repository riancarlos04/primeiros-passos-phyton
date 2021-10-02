from math import pow
print('-='*20)
print('CALCULADORA DE IMC')
print('-='*20)
altura = float(input('Digite a sua altura (M) : '))
peso = float(input('Digite o seu peso (Kg): '))
IMC = peso / (pow(altura, 2))
if IMC < 18.5:
    print(f'Seu IMC é de {IMC:.2f}, VOCE ESTA ABAIXO DO PESO')
elif IMC >= 18.5 and IMC < 25:
    print(f'Seu IMC é de {IMC:.2f}, VOCE ESTA NO PESO IDEAL')
elif IMC >= 25 and IMC < 30:
    print(f'Seu IMC é de {IMC:.2f}, VOCE ESTA COM SOBREPESO')
elif IMC >= 30 and IMC < 40:
    print(f'Seu IMC é de {IMC:.2f}, VOCE COM OBESIDADE')
else:
    print(f'Seu IMC é de {IMC:.2f}, VOCE ESTA COM OBESIDADE MORBIDA')
