def eh_par(num : int):
    if num % 2 == 0:
        return True
    return False

n = int(input('insira um número: '))

if eh_par(n):
    print('número é par.')
else:
    print('número é ímpar.')
