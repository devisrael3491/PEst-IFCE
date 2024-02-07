num = int(input('insira a quantidade de horas: '))

hora = int(input('insira o horário atual: '))

tempo = num % 24

hora += tempo

if hora > 24:
    hora -= 24
    
print(f'o alarme tocará {hora}:00')
