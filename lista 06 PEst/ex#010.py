def adicionar_produto(produtos : dict):
    dados = {}
    nome = str(input('insira o nome do produto: ')).capitalize()
    categoria = str(input('insira a categoria do produto: ')).capitalize()
    preco = float(input('insira o preco do produto: '))
    dados['categoria'] = categoria
    dados['preco'] = preco
    produtos[nome] = dados

def atualizar_preco(produtos : dict, nome : str):
    if nome.capitalize() in produtos:
        novo_preco = float(input(f'insira o novo preço de {nome}: '))
        produtos[nome]['preco'] = novo_preco
    else:
        print(f'o produto "{nome}" não está em nosso catálogo.')

def excluir_produto(produtos : dict, nome : str):
    if nome.capitalize() in produtos:
        print(f'o produto {produtos.pop(nome)} foi removido com sucesso.')
    else:
        print(f'o produto "{nome}" não está em nosso catálogo.')

produtos = {
    'Coca-Cola': {'categoria': 'Bebida', 'preco': 4.5},
    'Pizza': {'categoria': 'Comida', 'preco': 35},
    'Detergente': {'categoria': 'Limpeza', 'preco': 2},
    'Laranja': {'categoria': 'Frutas', 'preco': 5.2}
}


while True:
    print(f'[1] adicionar produto\n[2] atualizar preço\n[3] excluir produto\n[4] sair')
    op = int(input('insira a opção correspondente: '))
    while op < 1 or op > 4:
        print(f'E: {op} é uma opção inválida.')
    if op == 1:
        adicionar_produto(produtos)
    elif op == 2:
        produto = str(input('insira o nome do produto que quer atualizar o preço: '))
        atualizar_preco(produtos, produto)
    elif op == 3:
        produto = str(input('insira o nome do produto que quer deletar: '))
        excluir_produto(produtos, produto)
    elif op == 4:
        for k, v in produtos.items():
            print(f"{k} : R$ {v['preco']:.2f} ")
        break