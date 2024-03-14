def contador_de_digitos(n : int):
    count = 0
    while n > 0:
        resto = n % 10
        count += 1
        n = (n - resto) // 10
    return count

num = int(input('insira um número: '))

if num > 0: 
    digitos = contador_de_digitos(num)
elif num < 0:
    num *= -1
    digitos = contador_de_digitos(num)
else:
    digitos = 1

print(f'Esse número tem {digitos} algarismos.')
    