nome = str(input('Digite seu nome completo: ')).strip()
divisao = nome.split()
print(f'Primeiro nome {divisao[0]}')
print(f"seu ultimo nome {divisao[len(divisao) - 1]}")
