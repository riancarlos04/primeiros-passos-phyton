s1 = float(input('Digite o seguimento 1: '))
s2 = float(input('Digite o seguimento 2: '))
s3 = float(input('Digite o seguimento 3:'))
if s1 < (s2 + s3) and s2 < (s1 + s3) and s3 < (s1 + s2):
    print(f'Com os seguimentos acima pode se formar um triangulo ', end='')
    if s1 == s2 == s3:
        print('EQUILÁTERO!')
    elif s1 != s2 != s3 != s1:
        print('ESCALENO!')
    else:
        print('ISÓCELES')

else:
    print('Com os seguimentos acima NÃo se pode formar um triangulo')
