num = divi =  int(input('insira um número: '))
bin_inv = 0
count = 0
while divi > 0:
    resto = divi % 2

    if resto != 0:
        bin_inv = bin_inv * 10 + resto
    else:
        if bin_inv == 0 and resto == 0:
            count += 1
        else:
           bin_inv = bin_inv * 10

    divi = divi // 2

print(bin_inv)

bina = 0

while bin_inv > 0:
    resto = bin_inv % 10
    bina = bina * 10 + resto
    bin_inv = (bin_inv - resto) // 10

print(f'seu número {num} em binário: {bina*10**(count)}.')