def substituir_vogais(texto : str): #uma função auxiliar criada para fazer a função que vai criptografar.
    

    a = 'aAáÁàÀâÂãÃ' #minha ideia foi armazenar as versões das vogais em uma string com o nome delas.
    e = 'eEéÉèÈêÊẽẼ'
    i = 'iIíÍìÌîÎĩĨ'
    o = 'oOóÓòÒôÔõÕ' 
    u = 'uUúÚùÙûÛũŨ'

    nova_string = '' #criei uma variável para  armazenar a string com as modificações feitas

    for caractere in texto: #utilizo um loop para  percorrer todos os caracteres e verificar se o mesmo é uma vogal.

        if caractere in a: #verificando se o caractere é uma das versões da letra "a"
            indice = a.find(caractere) #caso ele seja uma versão de "a", o método find vai encontrar o índice do caractere na string que armazena as versões de "a"
            nova_string += e[indice] #todas as varíaveis que armazenam versões de vogais possuem exatamente o mesmo tamanho, a ideia é utilizar o índice encontrado para substituir a vogal pela sua versão equivalente entre as versões da próxima vogal, graças a organização das strings, isso mantém os devidos acentos, inclusive funciona para letras maiúsculas.
        elif caractere in e: #o raciocínio é o mesmo em todas as vogais.
            indice = e.find(caractere)
            nova_string += i[indice]
        elif caractere in i:
            indice = i.find(caractere)
            nova_string += o[indice]
        elif caractere in o:
            indice = o.find(caractere)
            nova_string += u[indice]
        elif caractere in u:
            indice = u.find(caractere)
            nova_string += a[indice]
        else: #caso o caractere não esteja em nenhuma variável que armazena vogais, ele permanece inalterado.
            nova_string += caractere

    return nova_string #a função retorna a string com as alterações realizadas

def tenis_polar(string : str): #função que faz a troca dos caracteres usando o código tenis-polar.

    tenis = 'tTeEéÉèÈêÊẽẼnNiIíÍìÌîÎĩĨsS' #a ideia é a mesma da função anterior, criar strings que armazenam os caracteres das palavras 'tenis' e 'polar com o mesmo tamanho.
    polar = 'pPoOóÓòÒôÔõÕlLaAáÁàÀâÂãÃrR' #tomei todos os cuidados para garantir que a substituição seja correta mesmo em casos em que há vogais acentuadas

    nova_string = '' #uma string vazia para armazenar a string com alterações.
    for caractere in string: #utilizo um loop for para percorrer o texto original e fazer as verificações.
        if caractere in tenis: #se o caractere está na string tenis então a ideia é trocar ele pelo caractere de mesmo índice da string 'polar', assim a regra da substituição será seguida.
            indice = tenis.find(caractere)
            nova_string += polar[indice]
        elif caractere in polar: #a lógica aplicada é a mesma, mas dessa vez os caracteres que estão presentes na string polar são trocados pelo caractere da string tenis de mesmo índice.
            indice = polar.find(caractere)
            nova_string += tenis[indice]
        else: #se o caractere não está presente em nenhuma das duas strings, ele não será alterado.
            nova_string += caractere
        
    return nova_string #a string com as devidas alterações é retornada

def criptografar(string : str): #a função que irá criptografar segundo a ordem perdida na questão, usando as funções de substituição.
    string = tenis_polar(string) #primeiro é aplicado o código tenis-polar
    string = substituir_vogais(string) #por último todas as vogais são substituídas pela próxima vogal.
    return string #a string criptografada é retornada.

print(criptografar('Ataque ao amanhecer')) #a saída é exatamente "Opoqau oi omolhucus" conforme o exemplo da questão.



