frase = 'O Python é uma linguagem de programção' \
    'multiparadigma' \
    'Python foi criado por Guido van Rossum'

i = 0
qtd_mais_vezes = 0
letra_mais_vezes = ''


while i < len(frase):
    letra_atual = frase[i]

    if letra_atual == ' ':
        i += 1
        continue

    vezes_letra_apareceu_atual = frase.count(letra_atual)

    if qtd_mais_vezes < vezes_letra_apareceu_atual:
        qtd_mais_vezes = vezes_letra_apareceu_atual
        letra_mais_vezes = letra_atual

    i += 1

print(
    'A letra que apareceu mais vezes foi '
    f'"{letra_mais_vezes}" que apareceu  '
    f'{qtd_mais_vezes}x'
)