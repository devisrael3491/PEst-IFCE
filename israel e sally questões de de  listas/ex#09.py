from random import randint

numeros = []
numeros.append(randint(1,100))

while True:
    palpite = int(input('insira um palpite: '))
    if palpite > numeros[0]:
        print('Seu palpite é maior que o número...')
    elif palpite < numeros[0]:
        print('Seu palpite é menor que o número...')
    else:
        print('PARABÉNS, VOCÊ GANHOU!!!')

        resp = str(input('deseja continuar? [s/n]')).lower()
        while resp != 's' and resp != 'n':
            print("E: resposta inválida. ")
            resp = str(input('deseja continuar? [s/n]')).lower()
        if resp == 'n':
            break
        else:
            del numeros[0]
            numeros.append(randint(1,100))
