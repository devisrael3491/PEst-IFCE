def converter_moeda(reais : float, para_dolar = True):
    if para_dolar:
        valor = reais / 2
    else:
        valor = reais
    return valor

reais = float(input('digite uma quantia em reais: '))

dolar = input('você quer converter esse valor? [s/n] ')

while dolar != 's' and dolar != 'n':
    dolar = input('você quer converter esse valor? [s/n] ')
if dolar == 's':
    dolar = True
else:
    dolar = False

valor = converter_moeda(reais, dolar)

print("o valor convertido é {valor}.")