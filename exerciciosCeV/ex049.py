n = int(input('Gostaria de ver a tabuada de qual numero: '))
print('-=' * 10)
for c in range (1, 11):
    print(f'[{n}] X [{c:2}] = {n*c:2} ')
print('-=' * 10)