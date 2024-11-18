def multiplicacao(*args):
    total = 1
    for numeros in args:
        total = total * numeros
    return total

multiplicacao_total = multiplicacao(1, 2, 3, 4, 5, 6)

print(f'O total foi {multiplicacao_total}')

def par_impar(numero):
    multiplo_de_dois = numero % 2 == 0

    if multiplo_de_dois:
        return f'{numero} é par'
    return f'{numero} é impar'
    
print(par_impar(multiplicacao_total))