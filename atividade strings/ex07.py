def invertendo_substring(string1 : str, string2 : str):
    tamanho_string1 = len(string1)
    tamanho_string2 = len(string2)

    string1 = string1[::-1]
    string2 = string2[::-1]

    primeira_metade_string2 = string2[:tamanho_string2//2]
    segunda_metade_string1 = string1[tamanho_string1//2:]

    

    return  primeira_metade_string2 + segunda_metade_string1

string1 = input('insira a primeira string: ')
string2 = input('insira a segunda string: ')

new_string = invertendo_substring(string1, string2)

print(f'a nova string é {new_string}.')


