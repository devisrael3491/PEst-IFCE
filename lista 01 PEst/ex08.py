x1 = int(input('insira o ponto x da coordenada 1: '))
y1 = int(input('insira o ponto y da coordenada 1: '))
x2 = int(input('insira o ponto x da coordenada 2: '))
y2 = int(input('insira o ponto y da coordenada 2: '))

dist = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** (1/2)

print(f'a distância dos pontos é cerca de {dist:.2f}m.')