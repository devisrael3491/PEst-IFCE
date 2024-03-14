def simulador_jogo_dados(rodadas : int):
    from random import randint
    pontos_jogador1 = 0
    pontos_jogador2 = 0
    for i in range(1, rodadas + 1):
        dado1_jogador1 = 0
        dado2_jogador1 = 0
        dado1_jogador2 = 0
        dado2_jogador2 = 0

        print('>>> Turno do jogador 1 <<<')
        dado1_jogador1 = randint(1,6)
        print(f'jogador1 jogou seu primeiro dado -> {dado1_jogador1}.')
        dado2_jogador1 = randint(1,6)
        print(f'jogador1 jogou  seu segundo dado -> {dado1_jogador1}.')
        soma1 = dado1_jogador1 + dado2_jogador1

        print('>>> Turno do jogador 2 <<<')
        dado1_jogador2 = randint(1,6)
        print(f'jogador2 jogou seu primeiro dado -> {dado1_jogador2}.')
        dado2_jogador2 = randint(1,6)
        print(f'jogador2 jogou  seu segundo dado -> {dado2_jogador2}.')
        soma2 = dado2_jogador1 + dado2_jogador2

        if soma1 > soma2:
            print(f'jogador2 venceu a rodada {i}!!!')
            pontos_jogador1 += 1
        elif soma2 < soma1:
            print(f'jogador2 venceu a rodada {i}!!!')
            pontos_jogador2 += 1
        else:
            print(f'deu empate!!!')

    if pontos_jogador1 > pontos_jogador2:
        print('Parabéns ao vencedor: jogador1.')
    elif pontos_jogador2 > pontos_jogador1:
        print('Parabéns ao vencedor: jogador2')
    else:
        print('Parabéns ao ambos: empate!')


rodadas = int(input('insira o número de rodadas: '))
while rodadas <= 0:
    rodadas = int(input('Erro... insira o número de rodadas: '))

simulador_jogo_dados(rodadas)

        


