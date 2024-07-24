def remover_espacos_duplicados(string : str):
    tamanho = len(string)

    string_cortada = string.split()
    nova_string = ''

    for i in string_cortada:
        nova_string += f'{i.strip()} '

    nova_string = nova_string.strip()
    
    return nova_string



frase = 'python       é          o                 melhor'
print(remover_espacos_duplicados(frase))
