num = n = int(input('insira um número: '))
inverso = 0
while n > 0:
    resto = n % 10
    inverso = inverso * 10 + resto
    n = (n-resto) // 10

print(f'seu número {num} invertido é {inverso}.')

