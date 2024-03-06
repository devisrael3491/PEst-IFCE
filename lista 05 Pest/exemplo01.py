def area(largura : float = 1, comprimento : float = 1):
    a = largura * comprimento
    print(f'a área do retângulo é {a}m²')

compri = float(input('insira o comprimento: '))
larg = float(input('insira a largura: '))

area(compri, larg)