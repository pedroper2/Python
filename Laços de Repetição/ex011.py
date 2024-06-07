import os 
os.system ("clear||cls")
def cab ():
    os.system ("cls|| clear")
    print ("=====SENAI====")
opcao= int (input ("1- Pagamento a vista? 2- prazo? "))
valor= float (input ("valor do produto: "))
cab ()
match (opcao):
    case 1:
        desconto= valor * 0.10
        resultado= valor - desconto
        print (f"Valor do produto R$: {valor}")
        print ("forma de pagamento- á vista")
        print (f"Valor do desconto R$: {desconto}")
        print (f"Total a pagar: R$: {resultado}")
    case 2:
        parcela= int (input ("quantidade de parcela? ")) 
        valorParcela= valor / parcela
        print ("Forma de pagamento- á prazo")
        print (f"Quantidade de parcela: {parcela}x")
        print (f"Valor da parcela R$: {valorParcela}")
        print (f"Valor total R$: {valor}")

        