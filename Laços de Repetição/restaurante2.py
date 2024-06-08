import os 
os.system("cls||clear")
LISTA_PRATOS= []
soma= 0
prato= ""
while True :
    print ("1- feijão")
    print ("2- arroz")
    print ("3- carne")
    print ("4- abacaxi")
    print ("5- ovos")
    print ("6- laranja")
    print ("0-encerra")
    cardapio= int (input ("Deseja qual prato??"))
    os.system ("cls||clear")
    if cardapio > 6 or cardapio < 0:
        print ("Digite uma opção valida.")
        break
    match (cardapio):
        case 1:
            prato= "feijao"
            valor= 5
            soma+= valor
            LISTA_PRATOS.append(prato)
            print ("Deseja mais um prato?")
        case 2: 
            prato= "arroz"
            valor= 10
            soma+= valor
            LISTA_PRATOS.append(prato)
            print ("Deseja mais um prato?")
        case 0:
            if prato== "":
                print ("nenhum prato adicionado")
                break
            else:
                Pagamento= int (input ("Qual a forma de pagamento? 1-Á vista 2- cartão"))
                match (Pagamento):
                    case 1:
                        variavel= "desconto"
                        Pagamento= "Á vista"
                        desconto= soma *0.10
                        resultado= soma- desconto
                    case 2:
                        variavel = "acrescimo"
                        Pagamento = "Cartão"
                        desconto= soma * 0.10
                        resultado= soma + desconto
                for i, prato in enumerate (LISTA_PRATOS):
                    print (f"O {i+1}° pedido foi: {prato}")
                print (f"forma de pagamento: {Pagamento}")
                print (f"Com o {variavel} ficou: {desconto}")
                print (f"Total: {soma}")
                print (f"Subtotal a pagar: {resultado}")
                
                


    