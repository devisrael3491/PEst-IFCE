notas = {}

for i in range(5):
    disciplina = str(input('digite uma disciplina: '))
    nota = float(input(f'insira a nota em {disciplina}: '))
    notas[disciplina]=nota

for disciplina, nota in notas.items():
    print(f'{disciplina}: {nota}')