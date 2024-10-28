entrada = input("Digite um numero: ")

if entrada.isdigit():
    entrada_int = int(entrada)
    par_impar = entrada_int % 2 == 0
    par_impar_texto = 'Impar'

    if par_impar:
        par_impar_texto = 'Par'
    
    print(f'O numero {entrada_int} é {par_impar_texto}')
else:
    print('Você não digitou um numero inteiro ')