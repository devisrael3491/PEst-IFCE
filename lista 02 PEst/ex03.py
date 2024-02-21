n = int(input('insira um inteiro: '))
if n > 10 and n < 20:
    print('maior que 10 e menor que 20.')
elif n > 30 or n < 5:
    print('menor que 5 ou maior que 30.')
else:
    print('não é maior que 10 e menor que 20 nem menor que 5 ou maior que 30.')