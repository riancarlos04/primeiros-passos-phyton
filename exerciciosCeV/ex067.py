cont = 1
while True:
    num = int(input('Quer ver a tabuada de que valor: '))
    if num < 0 :
        break
    print('-'*20)
    cont = 1
    while cont <= 10:
        print(f'{num:2} X {cont:2} = {num * cont:2}')
        cont += 1
print('O PROGRAMA ACABOU! VOLTE SEMPRE')

