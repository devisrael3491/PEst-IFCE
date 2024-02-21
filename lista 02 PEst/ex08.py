a = int(input('insira um número a: '))
b = int(input('insira um número b: '))
c = int(input('insira um número c: '))
n = int(input('insira um número n: '))

if n > 2 and ((a ** n + b ** n) == c ** n):
    print('teorema violado.')
else:
    print('teorema não violado.')
