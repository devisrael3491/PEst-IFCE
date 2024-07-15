nota = float(input('insira uma nota: '))

if nota >= 0 and nota <= 10:
    if nota >= 9:
        print('A')
    elif nota >= 7:
        print('B')
    elif nota >= 5:
        print('C')
    else:
        print('D')
else:
    print(f'{nota} não é uma nota válida.')
