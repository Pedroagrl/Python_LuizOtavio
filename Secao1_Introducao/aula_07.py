nome = input("Digite seu nome: ")
idade = input("Digite sua idade: ")
if idade and nome:
    print(f"Seu nome é {nome}")
    print(f"Seu nome invertido é {nome[::-1]}")
    if " " in nome:
        print("Seu nome tem espaço")
    else:
        print("Seu nome não tem espaço")
    print(f"Seu nome tem {len(nome)} letras")
    print(f"A primeira letra do seu nome é {nome[0]}")
    print(f"A ultima letra do seu nome é {nome[-1]}")
else:
    print("Desculpa, voce deixou campos vazios")