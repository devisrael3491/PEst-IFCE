lista_de_frutas = ['abacaxi', 'banana','caju','morango','manga']

fruta = str(input('insira o nome de uma fruta para ser removida: ')).lower()

if fruta in lista_de_frutas:
    lista_de_frutas.remove(fruta)
    print(f'{fruta} removida com sucesso!')
else:
    print(f'{fruta} não está na lista! ')

print(f'A lista com as frutas resultantes é {lista_de_frutas}')
