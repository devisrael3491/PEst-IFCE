n = int(input('insira um número de 5 algarismos: '))

if n >=  10000 and n <= 99999:

    unidade = n % 10
    dezena_de_milhar = n // 10000
    unidade_de_milhar = (n - dezena_de_milhar * 10000) // 1000
    dezena = ((n - unidade) / 10) % 10
    centena = (n - (dezena_de_milhar * 10000) - (unidade_de_milhar * 1000) - (dezena * 10) - (unidade)) // 100

    if (unidade == dezena or unidade == centena or unidade == unidade_de_milhar or unidade == dezena_de_milhar) or \
    (dezena == centena or dezena == unidade_de_milhar or dezena == dezena_de_milhar) or \
    (centena == unidade_de_milhar or centena == dezena_de_milhar) or (unidade_de_milhar == dezena_de_milhar):
        print(f'Há pelo menos dois algarismos iguais no número {n}')
    else:
        print(f'Nenhum dígito se repete no número {n}.')

else:
    print(f'o número {n} não possui 5 algarismos.')

