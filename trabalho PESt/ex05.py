def conversor_moeda(real : float, taxa : float):
    dolar = real * taxa
    return dolar

real = float(input('insira um valor em reais: '))
taxa = float(input('insira uma taxa de câmbio para dólar: '))

while real <= 0 or taxa <= 0:
    print('valores inválidos.')
    real = float(input('insira um valor em reais: '))
    taxa = float(input('insira uma taxa de câmbio para dólar: '))

dolar = conversor_moeda(real, taxa)

print(f'seu valor em dolar: U$ {dolar}.')



