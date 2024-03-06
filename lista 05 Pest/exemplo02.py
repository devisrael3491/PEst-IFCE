def ver(nome1 : str = "fulano", nome2 : str = "cicrano", idade1 : int = 0, idade2 : int = 0):
    if idade1 == idade2:
        print('os dois tem a mesma idade.')
    elif idade1 > idade2:
        velho = nome1
        vd = idade1
    else:   
        velho = nome2
        vd = idade2
    print(f'o mais velho é {velho} com {vd} anos.')

a = input('insira um nome: ')
b = input('insira outro nome: ')
c = int(input('insira uma idade: '))
d = int(input('insira uma idade: '))

ver(a,b,c,d)