from math import sin, cos, tan, radians
ang = float(input('Digite o angulo: '))
sen = sin(radians(ang))
cos = cos(radians(ang))
tg = tan(radians(ang))
print(f'O angulo de {ang}º tem o SENO de {sen:.2f}')
print(f'O angulo de {ang}º tem o COSSENO de {cos:.2f}')
print(f'O angulo de {ang}º tem a TANGENTE de {tg:.2f}')
