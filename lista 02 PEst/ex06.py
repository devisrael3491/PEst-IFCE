n = int(input('digite um número de 5 dígitos: '))

uni = n % 10
dez = ((n - uni) / 10) % 10
dm = n // 10000
m = (n - dm) // 1000
cen = (n - m - dm) // 100

if (uni == dez or uni == cen or uni == m or uni == dm) or (dez == cen or dez == m or dez == dm) or (cen == m or cen == dm) or (m == dm):
    print('repete algum número')
else:
    print('não repete nenhum.')