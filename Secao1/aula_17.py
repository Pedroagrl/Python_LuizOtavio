nota1 = -1
nota2 = -1

while True:
    nota = float(input("Numero: ")) 

    if 0 <= nota <= 10:  
        if nota1 == -1:  
            nota1 = nota
        elif nota2 == -1:  
            nota2 = nota
            break  
    else:
        print("Nota invalida")  
media = (nota1 + nota2) / 2  
print("Media = {:.2f}".format(media))  