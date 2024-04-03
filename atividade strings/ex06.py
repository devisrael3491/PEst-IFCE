def letras_alternadas(string : str):
    return string[::2]

string = input('insira uma string: ')
new_string = letras_alternadas(string)
print(f'{string} com letras alternadas é {new_string}.')