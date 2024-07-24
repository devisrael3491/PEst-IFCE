def palavra_mais_longa(string : str):
    palavras = string.split(' ')
    for i in palavras:
        if i == palavras[0]:
            maior_palavra = i
        else:
            if len(i) > len(maior_palavra):
                maior_palavra = i
    return maior_palavra

string = str(input('insira uma string: '))
maior = palavra_mais_longa(string)
print(f'a maior palavra de "{string}" é {maior}')