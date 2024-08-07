numeros = [2, 3, 0, -7, 15, 25, 8, 1]

numero = int(input('insira um número para ser inserido na lista: '))
pos = int(input('insira uma posição em que deseja inserir o elemento: '))
while pos >= len(numeros):
    print(f'E: a posição é inválida.')
    pos = int(input('insira uma posição em que deseja inserir o elemento: '))

numeros.insert(pos, numero)

print(f'A lista resultante é {numeros}')