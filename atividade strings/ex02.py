def intervalo(string : str, ind1 : int, ind2 : int):
    return string[ind1:ind2]

string = input('insira uma string: ')
ind1 = int(input('insira o primeiro índice: '))
ind2 = int(input('insira o segundo índice: '))

new_string = intervalo(string, ind1, ind2)

print(f'a substring contida no intervalo é {new_string}')