#nota= float = -1
#while nota > 10 or nota < 0:
 #   nota= int (input ("Qual a nota do aluno?"))

#print(f"A nota do aluno é {nota}")
while True:
    nota= float (input ("A nota do aluno "))

    if nota < 0 or nota > 10 :
        print ("nota invalida digite novamente")
    else:
        print ("nota valida nota:",nota)
        break
    