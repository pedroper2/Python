soma= 0
for c in range (3):

    while True:
        nota= float (input (f"Digite a º{c +1} nota "))
        if nota < 0 or nota > 10:
            print ("Nota invalida")
        else:
            soma+= nota
            media= soma / 3
            break
print (f"Media: {media}")
if media >= 7 :
    print ("Aprovado")
elif media >=5 or media ==6.9:
    print ("Recuperação")
elif media < 5:
    print ("Reprovado")

    
    