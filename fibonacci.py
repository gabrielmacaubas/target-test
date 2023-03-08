def fibonacci(num:int):
    if num == 0 or num == 1:
        return True
    
    x = 0
    y = 1

    while True:
        aux = y
        y = x + y
        x = aux

        if y == num:
            return True
        elif y > num:
            return False


# insira o numéro desejado
num = 5
print(fibonacci(num))
