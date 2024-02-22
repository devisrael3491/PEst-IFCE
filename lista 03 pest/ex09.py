num = n = int(input('insira um número: '))
soma = 0

while n > 0:
    resto = n % 10
    soma += resto ** len(str(num))
    n = (n - resto) // 10

if soma == num:
    print(f'número de armstrong.')
else:
    print(f'não é um número de armstrong.')