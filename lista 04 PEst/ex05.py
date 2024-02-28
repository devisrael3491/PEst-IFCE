divisores = 0

num = int(input('insira um número: '))

for n in range(num, 0, -1):
    if num % n == 0:
        divisores += 1
if divisores == 2:
    print('número primo')
else:
    print('número não primo')