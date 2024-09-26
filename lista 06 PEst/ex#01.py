lista_de_compras = {'arroz' : 3,
                    'feijão' : 5,
                    'batata' : 10,
                    'cenoura' : 2
}

for i in range(5):
    produto = str(input('digite um produto: '))
    qtd = int(input(f'insira a quantidade de {produto}: '))
    lista_de_compras[produto]=qtd

print(lista_de_compras)