fat = 1
num = int(input('insira um número: '))
for f in range(num,0,-1):
    fat*=f

print(f'o fatorial é {fat}')