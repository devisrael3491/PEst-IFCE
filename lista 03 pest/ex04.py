num = int(input('insira um número: '))

count = 1
print(f'os divisores de {num} são: ')
while count <= num:
    if num % count == 0:
        print(count)
    count += 1