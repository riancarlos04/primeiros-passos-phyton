medida = float(input('Uma distancia em metros: '))
cm = medida * 100
mm = medida * 1000
dm = medida * 10
dam = medida / 10
hm = medida / 100
km = medida / 1000
print(f'a media de {medida}m corresponde a {km}km , {hm}hm, {dam}dam, {dm}dm, {cm}cm e {mm}mm')