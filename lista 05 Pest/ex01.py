def calculadora(n1 : float, n2 : float, opera : str):
    if opera == 'soma':
        result = n1 + n2
    elif opera == 'subtracao':
        result = n1 - n2
    elif opera == 'multiplicacao':
        result = n1 * n2
    elif opera == 'divisao':
        result = n1 / n2
    else:
        result = "Você digitou uma operação inválida."
    return result

n1 = float(input('digite um número: '))
n2 = float(input('digite outro número: '))
opera = input('escolha uma operação: [soma, subtracao, multiplicacao, divisao] ')

resultado = calculadora(n1,n2,opera)

print(resultado)