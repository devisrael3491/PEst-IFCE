fim = int(input('insira um número: '))
count = 1
while count <= fim:
    if count % 3 != 0 and count % 5 != 0:
        print(count)
    elif count % 3 == 0 and count % 5 == 0:
        print('FizzBuzz')
    elif count % 3 == 0:
        print('Fizz')
    elif count % 5 == 0:
        print('Buzz')
    count += 1