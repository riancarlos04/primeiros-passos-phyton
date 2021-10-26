t1 = 0
t2 = 1
proximo = 0
c = 1
print('-'*30)
print('SEQUENCIA DE FIBONACCI')
print('-'*30)
num = int(input('Digite quantos termos da sequencia de Fibonacci deseja ver: '))
print('~'*30)
print(t1, '->',t2, end='')
while c <= num - 2:
    proximo = t1 + t2
    print('->', proximo, end='')
    t1 = t2
    t2 = proximo
    c += 1
