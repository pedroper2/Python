import os 
#função retorno.
def logoSenai ():
    os.system ("cls||clear")
    print ("==== ===== ====")
    print ("===== Senai ====")
    print("==== ===== =====")
def somar (n1,n2):
    resultado= n1 + n2
    return resultado
#solcitando dados para o usuário.
logoSenai ()
primeiroNumero= int (input ("Digite o primeiro número"))
logoSenai()
segundoNumero= int (input ("Digite o segundo número"))

soma=somar (primeiroNumero + segundoNumero)
print(f"Soma: {soma}")