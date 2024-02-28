n = int(input('insira um número: '))
soma = 0
if n < 0:
    n *= -1


for i in range(n,0, -1):
    if i % 3 == 0 or i % 5 == 0:
        soma += i

print(f'a soma é {soma}')

