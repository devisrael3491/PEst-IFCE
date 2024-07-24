def inverter(string : str):
    return string[::-1]

string = str(input('insira uma string: '))
inversa = inverter(string)

print(f'minha string original: {string}')
print(f'minha string invertida: {inversa}')