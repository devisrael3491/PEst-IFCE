from random import randint
num = randint(1,9)
while True:
    
    palpite = int(input('insira um inteiro: '))
    if palpite > num:
        print('o número é menor.')
    elif palpite < num:
        print('o número é maior.')
    else:
        print('acertou.')
        resp = input('deseja continuar? [s/n] ')
        if resp == 'n' or resp == 'N':
            break
        else:
            num = randint(1,9)