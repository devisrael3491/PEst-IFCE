def intercalar_letras(string1 : str, string2 : str):
    tamanho1 = len(string1)
    tamanho2 = len(string2)
    nova_string = ''
    if tamanho1 >= tamanho2:
        for i in range(0, tamanho2):
            nova_string += string1[i] + string2[i]
        if tamanho1 > tamanho2:
            for j in range(-i-1, 0, 1):
                nova_string += string1[j]

    elif tamanho2 > tamanho1:
        for i in range(0, tamanho1):
            nova_string += string1[i] + string2[i]
        for j in range(-i-1, 0 , 1):
            nova_string += string2[j]

    return nova_string
string1 = input('insira a primeira string: ')
string2 = input('insira a segunda string: ')
new_string = intercalar_letras(string1, string2)
print(new_string)