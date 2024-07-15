print(f'\n>>>Validando o teorema de fermat<<<\n')


a = int(input('insira o valor de a: '))
b = int(input('insira o valor de b: '))
c = int(input('insira o valor de c: '))
n = int(input('insira o valor de n: '))


if n > 2:
    if a > 0 and b>0 and c>0:
        if (a**n + b ** n == c ** n):
            print(f'O teorema de Fermat foi violado!')
        else:
            print(f'O teorema de Fermat permanece de pé!')
    else:
        print(f'Os valores de a,b e c devem ser maiores que 0.')
else:
    print(f'Para a validação ocorrer é necessário que n seja maior que 2.')
