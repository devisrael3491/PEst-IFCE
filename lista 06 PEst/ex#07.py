votos = [1, 2, 3, 1, 2, 1, 3, 3, 1, 2]

apurado_de_votos = {}

for voto in votos:
    if voto in apurado_de_votos:
        apurado_de_votos[voto] += 1
    else:
        apurado_de_votos[voto] = 1

print(apurado_de_votos)