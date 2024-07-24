def conta_vogal(string : str):
    qtd_vogais = 0
    vogais = 'aeiouáéíóúàèìòùãõ'
    for i in string:
        if i.lower() in vogais:
            qtd_vogais += 1
    return qtd_vogais

string = str(input('insira uma string: '))
vogais = conta_vogal(string)
print(f'A string {string} tem {vogais} vogais.')