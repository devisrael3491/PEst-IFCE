cidades = ['maranguape','fortaleza', 'são paulo', 'rio de janeiro', 'brasilia', 'porto alegre']

cidade = str(input('insira o nome de uma cidade: '))

if cidade in cidades:
    print(f'{cidade} existe na lista de cidades!')
else:
    print(f'{cidade} não existe na lista de cidades.')
    
