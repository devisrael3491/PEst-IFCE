pontos = {'Marcella' : 89,
          'Hosana' : 45,
          'Maxwell' : 16,
          'abacaxi' : 121,
          'Israel' : 40}
soma = 0
for ponto in pontos.values():
    soma += ponto

med = soma / 5
print(pontos)
print(f'A média de pontos dos jogadores é {med:.2f}')

