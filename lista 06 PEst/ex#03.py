idades = {}

for i in range(3):
    nome = str(input('nome: '))
    idade = int(input(f'idade de {nome}: '))
    idades[nome] = idade

for nome, idade in idades.items():
    print(f'{nome} tem {idade} anos.')