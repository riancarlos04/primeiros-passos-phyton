import math
co = float(input('Cateto oposto: '))
ca = float(input('Cateto adjacente: '))
hip = math.sqrt((math.pow(co, 2) + math.pow(ca, 2)))
print(f'Se como cateto oposto temos {co} e cateto adjacente temos {ca}, entao a hipotenusa é {hip:.2f}')