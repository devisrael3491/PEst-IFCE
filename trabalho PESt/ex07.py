def jogo_advinhacao():
    from random import randint
    sorteio = randint(0,100)
    tentativas = 0
    
    while True:
        palpite = int(input('Adivinhe um número entre 0 e 100: '))
        while palpite > 100 or palpite < 0:
            palpite = int(input('Erro.. Adivinhe um número entre 0 e 100: '))
        tentativas += 1
        if palpite > sorteio:
            print('muito alto, tente de novo!')
        elif palpite < sorteio:
            print('muito baixo, tente de novo!')
        else:
            print('você acertou!!!')
            break

    print(f'foram necessárias {tentativas} para você acertar!')


while True:
    jogo_advinhacao()
    continua = input('você quer continuar? [s/n] ')
    while continua != 's' and continua != 'n':
        continua = input('erro... você quer continuar? [s/n] ')
    if continua == "n":
        print('finalizando...')
        break

