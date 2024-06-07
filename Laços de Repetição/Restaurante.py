import os 
os.system ("cls||clear")
soma= 0 
LISTA_PRATO= []
prato= ""

while True:
    
    print("1- maça")
    print("2- abacaxi")
    print("3- arroz")
    print("4- carne")
    print("5- feijão")
    print("6- picanha")
    print("7- peixe")
    print("0- encerra")
    
    opcao= int (input ("qual a opcão ? "))
    os.system ("cls || clear")
    if opcao > 7 or opcao < 0:
        os.system ("cls || clear")
        print( "opção invalida")
        break
    match (opcao):
        case 1:
            prato= 'maça'
            preco= 10
            soma+= preco
            LISTA_PRATO.append (prato)
            print ("Deseja adicona mais um prato?")
        case 2: 
            prato= 'abacaxi'
            preco= 9
            soma+= preco
            LISTA_PRATO.append (prato)
            print ("Deseja adicona mais um prato?")
        case 3:
            prato= 'arroz'
            preco= 8
            soma+= preco
            LISTA_PRATO.append (prato)
            print ("Deseja adicona mais um prato?")
        case 4:
            prato = 'carne'
            preco = 7
            soma+= preco
            LISTA_PRATO.append (prato)
            print ("Deseja adicona mais um prato?")
        case 5: 
            prato = 'feijão'
            preco= 6
            soma+= preco
            LISTA_PRATO.append (prato)
            print ("Deseja adicona mais um prato?")
        case 6: 
            prato= 'picanha'
            preco= 11
            soma+= preco
            LISTA_PRATO.append (prato)
            print ("Deseja adicona mais um prato?")
        
        case 7: 
            prato= 'lagosta'
            preco= 12
            soma+= preco
            LISTA_PRATO.append (prato)
            print ("Deseja adicona mais um prato?")
        
        case 0:
            if prato == "": 
                print ("Nenhum prato")
                break
            else :
                Pagamento= int (input ("1 -a vista? 2- cartao? "))
                if Pagamento == 1:
                    desconto= soma * 0.10
                    resultado= soma - desconto
                elif Pagamento == 2 :
                    desconto= soma * 0.10
                    resultado= soma + desconto
                for i, prato in enumerate (LISTA_PRATO):
                    print (f"{i+1}° escolha: {prato}")
                print (f"O valor do acréscimo ficou: {desconto:.2f}")
                print (f"O preço total ficou: {soma}")
                print (f"O total a pagar: {resultado}")
                break
            break
                    
            
       



