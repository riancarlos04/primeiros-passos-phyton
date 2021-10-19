print('='*20)
print('10 TERMOS DE UMA PA')
print('='*20)
t1 = int(input('Primeiro termo: '))
r = int(input('Razao: '))
decimo = t1 + (10-1) * r
for c in range (t1, decimo + r, r):
    print(c, end=' -> ')
print('FIM')