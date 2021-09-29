s1 = float(input('Digite o seguimento 1: '))
s2 = float(input('Digite o seguimento 2: '))
s3 = float(input('Digite o segumento 3: '))
if s1 < (s2 + s3) and s2 < (s1 + s3) and s3 < (s1 + s2):
    print('Os seguimentos acima PODEM formar um triangulo')
else:
    print('Os seguimentos acima NAO PODEM formar um triangulo')