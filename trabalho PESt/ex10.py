def caminhada_aleatoria(passos : int):
    from random import randint
    
    pos_x = 0
    pos_y = 0

    for i in range(1, passos + 1):
        
        direcao = randint(1,4)

        #1 - esquerda
        #2 - direita
        #3 - baixo
        #4 - cima
        
        if direcao == 1:
            pos_x -= 1
            print('player andou para esquerda.')
        elif direcao == 2:
            pos_x += 1
            print('player andou para a direita.')
        elif direcao == 3:
            pos_y -= 1
            print('player andou para baixo')
        else:
            pos_y += 1
            print('player andou para cima')

    pos_f = f'({pos_x},{pos_y})'

    print(f'player parou em {pos_f}')


caminhada_aleatoria(10)


        

        




