def calculadora(n1 : float, n2 : float, op : str):
    
    if verifica(op) == False:
        print('erro: operação inválida.')
        return ''
    
    if op == "+":
        result = n1 + n2
    elif op == "-":
        result = n1 - n2
    elif op == "*":
        result = n1 * n2
    else:
        if n2 == 0:
            print("erro: não há divisão por zero.")
            return ''
        else:
            result = n1 / n2
    return result

def verifica(opera):
    if opera == "+" or opera == "-" or opera == "*" or opera == "/":
        return True
    return False

n1 = float(input('insira um número: '))
n2 = float(input('insira outro número: '))
print("\n[+] soma\n[-] subtração\n[*] multiplicação\n[/] divisão\n")
op = input('insira uma operação: ')

print(calculadora(n1,n2,op))