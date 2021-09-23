frase = str(input('Digite uma frase: ')).strip()
print(f"A letra A apareceu {frase.upper().count('A')} vezes")
print(f"A primeira letra A apareceu na posição {frase.upper().find('A') + 1}")
print(f"A ultima letra A apareceu na posição {frase.upper().rfind('A') + 1}")