import os
os.system ("cls||clear")
resultado= False
a=int (input ("Digite o primeiro numero: "))
operador= input ("Digite a operação + * / -")
b= int (input ("Digite o segundo numero: "))
match (operador):
    case '+':
        resultado = a + b
    case '-':
        resultado = a - b
    case '*':
        resultado = a * b 
    case '/':
        resultado = a / b 
    case '_':
        print ("Operador invalido")
         

print (f"RESULTADO: {resultado}")