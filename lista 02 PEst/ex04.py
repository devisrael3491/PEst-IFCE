n1 = int(input('insira o primeiro número: '))
n2 = int(input('insira o segundo número: '))
n3 = int(input('insira o terceiro número: '))

if n1 == n2 or n2 == n3 or n1 == n3:
    soma = 0
else:
    soma = n1+n2+n3
print(f'a soma é {soma}.')