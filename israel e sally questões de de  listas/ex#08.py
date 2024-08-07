numeros = []

def verificar_se_eh_maior(num : int, lista : list):
    for numero in lista:
        if numero > num:
            return False
    return True

def encontrar_pos_ideal(num : int, lista : list):

    tamanho = len(lista)

    for i in range(tamanho):
        numero_atual = lista[i]

        

        


while True:
    numero = int(input('insira um número: '))
    if len(numeros) == 0:
        numeros.append(numero)
    else:
        tamanho = len(numeros)
        for i in range(tamanho):
            if (numeros[i] > numero) and (i != tamanho -1):
                numeros.insert(i, numero)
                break
            elif (i != tamanho - 1):
                numeros.append(numero)

    cont = str(input('deseja continuar? [s/n] ')).lower()
    while cont != 's' and cont != 'n':
        print('E: resposta inválida! ')
        cont = str(input('deseja continuar? [s/n] ')).lower()
    if cont == 'n':
        break


    
    


print(numeros)
