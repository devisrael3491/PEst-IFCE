fim = int(input('insira um número: '))
soma = 0
count = 1

while count <= fim:
    soma = 0
    count2 = count
    while count2 > 0:
        resto = count2 % 10
        soma += resto ** len(str(count))
        count2 = (count2 - resto) // 10
    if soma == count:
        print(count)
    count += 1
   