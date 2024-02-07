capa = 24.95
unidades = 60

prec = (capa * unidades) * 0.6
frete = (unidades - 1) * 0.75 + 3

total = frete + prec

print(f'os livros custaram R$ {total:.2f}.')

