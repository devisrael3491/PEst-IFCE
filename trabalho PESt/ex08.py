def fibonacci(termos : int):
    a1 = 0
    a2 = 1
    for i in range(1, termos):
        print(a1)
        a3 = a1 + a2
        a1 = a2
        a2 = a3
    
num = int(input('insira a quantidade de termos: '))

while num <= 0:
    num = int(input('erro... insira a quantidade de termos: '))

fibonacci(num)
