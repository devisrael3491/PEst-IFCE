def primeiro_e_ultimo(string : str):
    return string[0] + string[-1]

string = input('insira uma string: ')
new_string = primeiro_e_ultimo(string)
print(f'a string que contém o primeiro e último caractere a string original é {new_string}')