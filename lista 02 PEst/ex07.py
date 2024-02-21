num = int(input('insira um número de 3 algarismos: '))

uni = num % 10
cen = num // 100
dez = (num - cen * 100 - uni) / 10
inv = (uni * 100) + (dez * 10) + cen

if num == inv:
    print('palíndromo.')
else:
    print('não palíndromo.')