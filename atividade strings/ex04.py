def salto(string : str, pulo : int):
    tamanho = len(string)
    new_string = ''
    for i in range(0, tamanho):
        if i % pulo == 0:
            new_string += string[i]
    return new_string

string = input('insira uma string: ')
pulo = int(input('insira o tamanho do salto: '))

new_string = salto(string,pulo)
print(f'a string com os pulos aplicados se torna: {new_string}')