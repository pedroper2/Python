contador=0 
soma=0
while True:
    numero= float (input ("Digite um numero "))
    if numero > 0:
        soma += numero
        contador+= 1
    else:
        if contador == 0:
            print ("numero não informado")
        else:
            break

media= soma / contador
print (f"A media: {media}")
