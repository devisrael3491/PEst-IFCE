def concatenar_fatiar(string1 : str, string2 : str):
    return string1[0:3] + string2[-3:]

string1 = input('insira a primeira string: ')
string2 = input('insira a segunda string: ')

new_string = concatenar_fatiar(string1, string2)
print(f'a string formada pelos caracteres é {new_string}')