entrada = input('[E]Entrar [S]Sair: ').upper()
senha_digitada = input('Senha: ')

senha_permitida = '123456'

if entrada == 'E' and senha_digitada == senha_permitida:
    print('Senha correta!')
    print('Entrar')
elif entrada == 'E' and senha_digitada != senha_permitida:
    print('Senha incorreta!')
    print('Sair')
elif 'S':
    print('Sair')
else:
    print('Valor não encontrado!')