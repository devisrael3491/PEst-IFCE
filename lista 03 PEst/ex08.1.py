bina = bina2 = int(input('insira um número binário: '))
deci = 0
pos = 0
while bina > 0:
    resto = bina % 10
    deci = deci +  resto * 2 ** (pos) 
    bina = (bina - resto) // 10
    pos += 1
print(f'seu binário {bina2} em decimal é {deci}.')

