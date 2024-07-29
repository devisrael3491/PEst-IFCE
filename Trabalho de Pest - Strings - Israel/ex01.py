def is_underscore(string : str): #essa função é uma função auxiliar, feita apenas para melhorar a forma como as verificações são feitas.
    if string == '_':
        return True
    return False

def validar_user(user : str): #função que realmente valida o user, a ideia dela é percorrer cada caractere do user e verificar se é um caractere alfanumérico ou um underline, pelo menos uma dessas condições deve ser verdadeira, por isso o uso do operador "or"
#para que o caractere seja uma das opções válidas, ao mesmo tempo é necessário que o tamanho do user possua entre 6 e 15 caracteres, por isso o uso do operador "and", se o resultado dessa grande expressão lógica for false, significa que o user é inválido, então a função retorna False, realizando essa verificação para todos os caracteres do texto, se um for inválido, imediatemente é retornado False. 
    for caractere in user:
        if ((caractere.isalnum() or is_underscore(caractere)) and 6 <= len(user) <= 15) == False:
            return False
    return True
        
user = str(input('insira o seu nome de usuário: '))

if validar_user(user): #apenas uma condicional pra verificar se o usuário é válido e então mandar uma mensagem personalizada para cada caso.
    print(f'O usuário é válido.')
else:
    print(f'O usuário é inválido.')
    