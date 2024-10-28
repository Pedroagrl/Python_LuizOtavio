nome = 'Luiz Otavio '
indice = 0
novo_nome = ''


while indice < len(nome):
    letra = nome[indice]
    novo_nome += f'x{letra}'
    indice += 1

print(novo_nome)