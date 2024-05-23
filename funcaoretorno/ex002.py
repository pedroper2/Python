import os

def logoSenai ():
    os.system ("cls||clear")
    print ("==== ==== ==== ")
    print ("==== SENAI ==== ")
    print ("==== ==== ==== ")
#Função media
def media (n1,n2):
    soma= n1 + n2
    resultado= soma / 2
    return resultado
logoSenai ()
primeiroNumero= int (input ("Digite o primeiro numero "))
logoSenai ()
segundoNumero= int (input ("Digite o segundo numero "))
Media= media (primeiroNumero,segundoNumero)
print (f"A Media dos numeros é: {Media}")
