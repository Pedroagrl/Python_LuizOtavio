# x, y, *resto = 1, 2, 3, 4
# print(x, y, resto)

def soma(*args):
    total = 0
    for numero in args:
        total += numero
    return total

soma_total = soma(1, 2, 3, 4, 5, 6)
print(soma_total)