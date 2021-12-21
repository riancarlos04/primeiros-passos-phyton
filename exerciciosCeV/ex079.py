valores = []
while True:
   numero = int(input('Digite um número: '))
   if numero not in valores:
       valores.append(numero)
       print('Valor adicionado com sucesso!')
   else:
       print('Valor já digitado! Não será adicionado...')

   r = str(input('Deseja adicionar mais números? [S/N]')).strip().upper()[0]
   if r in 'Nn':
       break
valores.sort()
print(f'Voce adicionou os valores: {valores}')