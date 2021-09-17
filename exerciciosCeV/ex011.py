lar = float(input('Qual a largura da parede em M : '))
alt = float(input('Qual a altura da parede em M : '))
area = lar * alt
tinta = area / 2
print(f'Sua parede têm {area:.2f}m², sendo assim são necessarias {tinta:.1f} litros de tinta')