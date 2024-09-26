frase = str(input('insira uma frase: '))
palavras = frase.split()
ocorrencia = {}
for palavra in palavras:
    if palavra in ocorrencia:
        ocorrencia[palavra] += 1
    else:
        ocorrencia[palavra] = 1

for palavra, qtd in ocorrencia.items():
    print(f'{palavra} - {qtd}')

