divisores = 0
soma = 0
for num in range(1,100):
    divisores = 0
    for n in range(num, 0, -1):
        if num % n == 0:
            divisores += 1
    if divisores == 2:
        soma += num
        
print(f'a soma é {soma}')