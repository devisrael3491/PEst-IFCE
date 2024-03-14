def mensagem_personalizada(nome : str = "anônimo"):
    return f"Olá, {nome}! como você está? "

nome = input('insira seu nome: ')

if nome == '':
    mensagem = mensagem_personalizada()
    print(mensagem)
else:
    mensagem = mensagem_personalizada(nome)
    print(mensagem)
    