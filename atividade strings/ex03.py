def reverter(string : str):
    return string[::-1]

string = input('insira uma string: ')
inversa = reverter(string)
print(f'{string} invertida é {inversa}.')