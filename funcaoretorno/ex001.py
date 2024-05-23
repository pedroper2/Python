import os
os.system ("cls||clear")
#função de retorno
def somar (N1,N2):
    Resultado= N1 + N2
    return Resultado
def subtrair (N1,N2):
    Resultado= N1-N2
    return Resultado
def multiplicar (N1,N2):
    return N1 * N2
PrimeiroNumero= int (input ("Digite o primeiro numero "))
segundoNumero= int (input ("Digite o segundo numero "))
multiplicao= multiplicar (PrimeiroNumero,segundoNumero)
soma=somar (PrimeiroNumero,segundoNumero)
subtracao=subtrair(PrimeiroNumero,segundoNumero)
print (f"soma {soma}")
print (f"Multiplicação {multiplicao}")
print (f"Subtração {subtracao}")

