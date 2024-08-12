def mostrar_fila(fila : list):
    if len(fila) == 0:
        print(f'A fila está vazia...')
    else:
        print(f'Fila atual:: ')
        
        for pessoa in fila:
            print(f'  > {pessoa}')

def adicionar_pessoa(pessoa : str, fila : list):

    if pessoa in fila:
        print(f'{pessoa} já está esperando na lista.')
    else:
        print(f'{pessoa} foi adicionado à fila!')
        fila.append(pessoa)

def atender_pessoa(fila : list):
    tamanho = len(fila)
    if tamanho != 0:
        print(f'{fila[0]} foi atendido com sucesso!')
        del fila[0]
    else:
        print(f'a fila está vazia, ninguém para atender aqui...')



fila = []

while True:
    print(f'[1] verificar fila do consultório\n[2] adicionar pessoa\n[3] atender pessoa\n[4] sair')
    opera = int(input('insira uma operação: '))

    while opera < 1 or opera > 4:
        print('E: operação inválida.')
        opera = int(input('insira uma operação: '))

    if opera == 1:
       mostrar_fila(fila)

    elif opera == 2:
        pessoa = str(input('insira o nome da pessoa: '))
        adicionar_pessoa(pessoa , fila)

    elif opera == 3:
        atender_pessoa(fila)
    else:
        print(f'Obrigado, volte sempre!!!')
        break
