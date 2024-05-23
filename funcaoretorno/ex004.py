#função par/impar 
numeros=[]

def pares (numeros):
    par= 0
    for numero in numeros:
        if numeros % 2 == 0:
            par+= 1
    return par
def impares (numeros):
    impar= 0 
    for numero in numeros:
        if numeros % 2!= 0:
            impar+= 1
    return impar

for i in range (6):
    numero= int (input (f"Digite o numero: "))
    numeros.append(numero)

QuantidadeImpar= impares (numeros)
QuantidadePar= pares (numeros)

print (f"Quantidade de numeros impar: {QuantidadeImpar}")
print (f"quantidade de numeros pares: {QuantidadePar}")
