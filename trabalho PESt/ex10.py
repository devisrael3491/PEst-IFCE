def caminhada_aleatoria(passos : int):
    from random import randint
    
    x = 0
    y = 0
    for i in range(1, passos+1):
        direcao = randint(1,4)
    
        if direcao == 1:
            x -= 1
            print(f"player deu um passo para a esquerda\n")
        elif direcao == 2:
            x += 1
            print(f"player deu um passo para a direita\n")
        elif direcao == 3:
            y -= 1
            print(f"player deu um passo para  baixo\n")
        else:
            y += 1
            print(f"player deu um passo para cima\n")
    
    posicao_final = f'({x},{y})'
    
    print(f"player parou na posição {posicao_final}\n")
    
    distancia_total = (y**2 + x ** 2) ** (1/2)
    
    print(f"o jogador andou um total de {distancia_total:.2f}m de distância.\n")
    
passos = int(input('insira a quantidade de passos: '))

caminhada_aleatoria(passos)
