n = int(input('insira um número de até 3 algarismos: '))

if n > 999 or n < 0:
    print(f'O número {n} tem mais do que 3 algarismos ou é negativo.')
else:
    unidade = n % 10
    dezena = (n // 10)  % 10
    centena = (n // 100)


    if centena == 0 and dezena == 0:
        inverso = unidade
    elif centena == 0:
        inverso = unidade * 10 + dezena
    else:
        inverso = unidade * 100 + dezena * 10 + centena

    if inverso == n:
        print(f'{n} é um palíndromo.')
    else:
        print(f'{n} não é um palíndromo.')

