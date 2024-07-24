def remover_espaco(string : str):
    string_nova = ''
    for i in string:
        if i.isspace() == False:
            string_nova += i
    return string_nova


def palindromo(string : str):
    if remover_espaco(string) == remover_espaco(string[::-1]):
        return True
    return False

string = str(input('insira uma string: '))

if palindromo(string):
    print(f'{string} é palíndromo.')
else:
    print(f'{string} não é palíndromo.')
