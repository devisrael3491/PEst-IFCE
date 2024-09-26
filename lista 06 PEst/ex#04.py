idades = {}

for i in range(3):
    nome = str(input('nome: '))
    idade = int(input(f'idade de {nome}: '))
    idades[nome] = idade

soma = 0
for nome, idade in idades.items():
    print(f'{nome} tem {idade} anos.')
    soma += idade

med = soma / 3

print(f'A média de idades do grupo é {med:.2f} anos.')