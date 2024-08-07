numeros = [1,2,5,7,13, 16, 24, 8, 42, 1989]

for numero in numeros:
    if numero % 2 == 0:
        numeros.remove(numero)

print(f'A lista com os números resultantes é {numeros}')