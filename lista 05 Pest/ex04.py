def eh_primo(n : int):
    
    divisores = 0
    count = 1
    while count <= n:
        if n % count == 0:
            divisores += 1
        count += 1
    if divisores == 2:
        return True
    return False

print(eh_primo(8))

