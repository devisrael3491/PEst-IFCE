count = 0
soma = 0
num = int(input('insira um número: '))

for n in range(1, num+1):
    soma += n
    count += 1
    
med = soma / count

print(f'a média é {med}.')