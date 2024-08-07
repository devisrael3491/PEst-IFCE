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

def atender_pessoa(pessoa : str, fila : list):

    if pessoa in fila:
        print(f'{pessoa} foi atendido(a) com sucesso!')
        fila.remove(pessoa)
    else:
        print(f'{pessoa} não está na fila!')




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
        pessoa = str(input('insira opessoa que deseja remover: '))
        atender_pessoa(pessoa, fila)
    else:
        print(f'Obrigado, volte sempre!!!')
        break