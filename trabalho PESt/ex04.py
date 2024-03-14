def fatorial(n : int):
    fatorial = 1
    for f in range(1, n+1):
        fatorial *= f
    return fatorial

def comb(n : int, p : int):
    binominal = fatorial(n) / (fatorial(p) * fatorial(n-p))
    return binominal

n = int(input('insira um número: '))
p = int(input('insira outro número: '))

if n > 0 and p > 0:
    coeficiente_bin = comb(n, p)
    print(f'o coeficiente binominal é {coeficiente_bin}. ')
else:
    print('valor inválido para fatorial.')

