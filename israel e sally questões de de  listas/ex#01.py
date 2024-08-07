numeros = []

while True:
    numero = int(input('insira um número: (0 sai) '))
    if numero == 0:
        break
    else:
        numeros.append(numero)


print(f'A lista com os números digitados é {numeros}')