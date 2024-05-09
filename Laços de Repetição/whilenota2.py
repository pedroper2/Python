import os

os.system ("clear || cls ")
soma= 0
contador = 0
while True:
    print ("MENU:")
    nota= float (input ("Digite uma nota"))
    print ("S-Adiciona mais uma nota")
    print ("P- Quantas notas inseridas")
    print ("N- calcula a media aritimetica")
    contador+=1
    soma+= nota
    opcao= str (input ("?"))
    os.system ("clear || cls")
    opcao = opcao.upper ()
    if opcao == "S":
        print("Novamente:")
    if  opcao == "P":
        print (f"Inseridas {contador} notas")
        break
    elif opcao == "N":
        media = soma / contador
        print (f"Media: {media}")
        break
