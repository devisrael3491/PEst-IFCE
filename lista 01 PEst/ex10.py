num = int(input('insira um número de 4 algarismos: '))

unidade = num % 10

milhar = num // 1000

dezena = ((num - unidade) / 10) % 10

centena = (num - unidade - milhar * 1000 - dezena * 10) / 100

soma = unidade + dezena + centena + milhar

print(f'a soma dos algarismos de {num} é {int(soma)}.')


