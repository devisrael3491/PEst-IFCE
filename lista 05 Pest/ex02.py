def cumprimentar(nome : str = "anônimo", saudacao : str = 'OLÁ'):
    print(f'{saudacao}, {nome}!')

nome = input('insira um nome: ')
sauda = input('digite uma saudacao: ')

cumprimentar(nome, sauda)

