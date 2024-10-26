primeiro_valor = input('Digite um valor: ')
segundo_valor = input('Digite outro valor: ')

primeiro_valor_int = int(primeiro_valor)
segundo_valor_int = int(segundo_valor)

if primeiro_valor_int > segundo_valor_int:
    print(f'O primeiro valor "{primeiro_valor_int}" é maior que o segundo valor "{segundo_valor_int}"')
elif segundo_valor_int > primeiro_valor_int:
    print(f'O segundo valor "{segundo_valor_int}" é maior que o primeiro valor "{primeiro_valor_int}"')
else: 
    print(f'Os valores {primeiro_valor_int} e {segundo_valor_int} são iguais.')