frase = str(input('insira uma frase: ')).split()
frase = ''.join(frase).lower()

ocorrencia = {}
for caractere in frase:
    if caractere in ocorrencia:
        ocorrencia[caractere] += 1
    else:
        ocorrencia[caractere] = 1

for k, v in ocorrencia.items():
    print(f'{k} - {v}')