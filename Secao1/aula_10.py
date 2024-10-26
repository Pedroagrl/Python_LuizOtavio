entrada = input('Que horas são ? (Em numeros inteiros): ')

try:
    horas = int(entrada)

    if 0 <= horas <= 11:
        print('Bom dia!')
    elif 12 <= horas <= 17:
        print('Boa tarde!')
    elif 18 <= horas <= 23:
        print('Boa noite!')
    else:
        print('Nao conheço essa hora!')
except:
    print('Porfavor, digite apenas numeros inteiros!')