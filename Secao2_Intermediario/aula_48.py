pessoa = {}

chave = 'nome'

pessoa[chave] = 'Pedro'
pessoa['sobrenome'] = 'Artur'


print(pessoa[chave])

pessoa[chave] = 'Maria'

del pessoa['sobrenome']
print(pessoa)
print(pessoa['nome'])

if pessoa.get('sobrenome') is None:
    print('NÃO EXISTE')
else:
    print(pessoa['sobrenome'])