#lista de compras
def mostrar_lista(lista_de_compras : list):
    if len(lista_de_compras) == 0:
        print(f'Sua lista de compras está vazia!')
    else:
        print(f'>>> Lista de compras atual: ')
        
        for item in lista_de_compras:
            print(f'  > {item}')

def adicionar_produto(produto : str, lista_de_compras : list):

    if produto in lista_de_compras:
        print(f'Você já comprou esse produto.')
    else:
        print(f'{produto} foi adicionado à lista!')
        lista_de_compras.append(produto)

def remover_produto(produto : str, lista_de_compras : list):

    if produto in lista_de_compras:
        print(f'{produto} foi removido com sucesso!')
        lista_de_compras.remove(produto)
    else:
        print(f'{produto} não está na lista!')



lista_de_compras = []

while True:
    print(f'[1] verificar lista de compras\n[2] adicionar produto\n[3] remover produto\n[4] sair')
    opera = int(input('insira uma operação: '))

    while opera < 1 or opera > 4:
        print('E: operação inválida.')
        opera = int(input('insira uma operação: '))

    if opera == 1:
       mostrar_lista(lista_de_compras)

    elif opera == 2:
        produto = str(input('insira um produto: '))
        adicionar_produto(produto, lista_de_compras)

    elif opera == 3:
        produto = str(input('insira o produto que deseja remover: '))
        remover_produto(produto, lista_de_compras)
    else:
        print(f'Obrigado, volte sempre!!!')
        mostrar_lista(lista_de_compras)
        break
