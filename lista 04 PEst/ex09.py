fim = int(input('insira um número: '))

for num in range(1,fim+1):
    num2 = num    
    


    #contar os algarismos
    count = 0
    while num2 > 0:
        resto = num2 % 10
        count+=1
        num2 = (num2 - resto) / 10

    num2 = num

    arm = 0

    #criar o arm
    for n in range(1, count+1):
        rest = num2 % 10
        arm += rest ** count
        num2 = (num2 - rest) / 10

    if arm == num:
        print(num)


