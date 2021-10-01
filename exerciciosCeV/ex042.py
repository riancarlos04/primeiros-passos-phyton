s1 = float(input('Digite o seguimento 1: '))
s2 = float(input('Digite o seguimento 2: '))
s3 = float(input('Digite o seguimento 3:'))
if s1 < (s2 + s3) and s2 < (s1 + s3) and s3 < (s1 + s2) and s1 == s2 and s2 == s3:
    print(f'Com os seguimentos acima pode se formar um triangulo EQUILÁTERO ')
elif 1 < (s2 + s3) and s2 < (s1 + s3) and s3 < (s1 + s2) and s1 == s2 and s3 != s1 or s2 == s3 and s1 != s3 or s3 == s1 and s2 != s1:
    print(f'Com os seguimentos acima pode se formar um triangulo ISOCELES ')
elif s1 < (s2 + s3) and s2 < (s1 + s3) and s3 < (s1 + s2) and s1 != s2 and s2 != s3 and s3 != s1:
    print(f'Com os seguimentos acima pode se formar um triangulo ESCALENO ')
else:
    print('Com os seguimentos acima NÃo se pode formar um triangulo')
