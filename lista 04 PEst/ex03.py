
num = int(input('insira um número: '))

soma = 0

for n in range(0, num + 1, 2):
    soma += n
    
print(f'a soma é {soma}.')
