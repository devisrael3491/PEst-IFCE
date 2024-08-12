def encontra_pos_ideal(numero, numeros : list):
    tamanho = len(numeros)
    for i in range(tamanho):
        if numeros[i] >= numero:
            return i
    return tamanho

numeros = []

while True:
    numero = int(input('insira um número: '))
    pos = encontra_pos_ideal(numero, numeros)
    numeros.insert(pos, numero)

    cont = str(input('deseja continuar? [s/n] ')).lower()
    while cont != 's' and cont != 'n':
        print('E: resposta inválida! ')
        cont = str(input('deseja continuar? [s/n] ')).lower()
    if cont == 'n':
        break

print(numeros)

