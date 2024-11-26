pessoa = {
    'nome:': 'Pedro Artur',
    'sobrenome:': 'Lima',
    'idade:': 18,
    'altura:': 1.77,
    'endereços:': [
        {'rua': 'tal rua', 'numero': 123},
        {'rua': 'outra rua', 'numero': 321},
    ],
}

for chave in pessoa:
    print(chave, pessoa[chave])