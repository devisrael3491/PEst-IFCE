def pedir_notas():
    dados = {}
    notas = []
    disciplinas = ['Português', 'Matemática']
    for disciplina in disciplinas:
        for i in range(3):
            nota = float(input(f'insira a {i+1}ª nota de {disciplina}: '))
            notas.append(nota)
        dados[disciplina] = notas[:]
        notas.clear()
    return dados    
        
def adicionar_aluno(lista_de_alunos : list):
    disciplinas = {}
    nome = str(input('insira o nome do aluno: '))
    disciplinas = pedir_notas()
    lista_de_alunos[nome] = disciplinas

def escolher_opcao(inicio : int, limite : int, mensagem : str):
    op = int(input(mensagem))
    while op < inicio or op > limite:
        print(f'E: "{op}" não é uma opção válida.')
        op = int(input(mensagem))
    return op

def atualizar_notas(lista_de_alunos : dict):
    n = 1
    chaves = list(lista_de_alunos.keys())
    for k in chaves:
        print(f"({n}) - {k}")
        n+=1
    op = escolher_opcao(1, len(chaves), 'Escolha o ID do aluno: ')
    dados = {}
    notas = []
    disciplinas = ['Português', 'Matemática']
    for disciplina in disciplinas:
        for i in range(3):
            nota_atual = {lista_de_alunos[chaves[op]][disciplina]}
            print(f'{i+1}ª nota de {disciplina} -> {lista_de_alunos[chaves[op]][disciplina]}')
            nota = float(input(f'insira a nova {i+1}ª nota de {disciplina} (digite -1 para manter a atual) : '))
            if nota == -1:
                notas.append(nota_atual)
            else:
                notas.append(nota)
        lista_de_alunos[chaves[op-1]][disciplina] = notas[:]
        notas.clear()
    
    return lista_de_alunos
        
def remover_aluno(lista_de_alunos : dict):
    n = 1
    chaves = list(lista_de_alunos.keys())
    for k in chaves:
        print(f"({n}) - {k}")
        n+=1
    op = escolher_opcao(1, len(chaves), 'insira o ID do aluno: ')
    removido = lista_de_alunos.pop(chaves[op-1])
    
    return chaves[op]

def exibir_med(lista_de_alunos : dict):
    n = 1
    chaves = list(lista_de_alunos.keys())
    for k in chaves:
        print(f"({n}) - {k}")
        n+=1
    op = escolher_opcao(1, len(chaves), 'Escolha o ID do aluno: ')
    print(f'Dados de {chaves[op-1]}: ')
    med_geral = 0
    for k, v  in lista_de_alunos[chaves[op-1]].items():
        n = 1
        print(f'Disciplina: {k}')
        soma = 0
        for nota in v:
            print(f'   {n}ª nota: {nota}')
            n += 1
            soma += nota
        med = soma / len(v)
        med_geral += med
        print(f'Média {med}')
    print(f'Média geral: {med_geral/2}')



alunos = {
    'Artur': {'Matemática': [8.5, 7.2, 6.9], 'Português': [9.0, 8.5, 9.5]},
    'Julia': {'Matemática': [7.5, 6.0, 8.0], 'Português': [9.0, 9.0, 9.5]},
    'Pedro': {'Matemática': [8.0, 7.5, 9.0], 'Português': [9.0, 8.5, 9.5]}
}

while True:
    print(f'[1] adicionar aluno\n[2] atualizar notas\n[3] remover aluno\n[4] exibir médias\n[5] sair')
    op = escolher_opcao(1, 4, 'insira a opção correspondente: ')
    
    if op == 1:
        adicionar_aluno(alunos)
    elif op == 2:
        atualizar_notas(alunos)
    elif op == 3:
        removido = remover_aluno(alunos)
        print(f'Aluno {removido} com sucesso.')
    elif op == 4:
        exibir_med(alunos)
    else:
        print(f'Saindo...')
        break