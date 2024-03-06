def contagem_regressiva(n : int):
    if n < 0:
        n *= -1

    for i in range(n, -1, -1):
        print(i)

contagem_regressiva(59)