from math import hypot
co = float(input('Cateto oposto: '))
ca = float(input('Cateto adjacente: '))
hip = hypot(co, ca)
print(f'Se como cateto oposto temos {co} e cateto adjacente temos {ca}, entao a hipotenusa é {hip:.2f}')