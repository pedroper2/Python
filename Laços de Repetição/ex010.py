import os
os.system ("clear||cls")
salarioGeral=0
maiorIdade=0
menorIdade=99999
contadorM=0
while True:
    print ("Menu")
    print ("1- Adicionar pessoa")
    print ("2- Exibir resultado e sair.")
    opcao= int (input ("?"))
    if opcao ==1:
        idade= int (input ("Digite a sua idade "))
        sexo =str (input ("M/F? "))
        salario= float (input ("Salario? "))
        sexo= sexo.upper ()
        salarioGeral+= salario
        if sexo == "F" and salario > 5000:
            contadorM+= 1
        maiorIdade = max(idade, maiorIdade)
        menorIdade = min(idade, menorIdade)

    else:
        print("Exibindo resultados...")
        print (f"A Maior idade do grupo {maiorIdade}")
        print (f"A menor idade {menorIdade}")
        print (f"mulheres que ganhas mais de 5k.. {contadorM}")
    
   

    
        
    
    