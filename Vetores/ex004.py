import os
os.system ("cls||clear")
numeros=[]
pares=0
impar=0
QUANTIDADE_NUMEROS= 6
for i in range (QUANTIDADE_NUMEROS):
    numero = int (input ("Digite um numero: "))
    numeros.append (numero)
    if numero %2 == 0 :
        pares+= 1
    else: 
        impar+=1
for i, numero in enumerate(numeros):
     print(f"{i+1}º Numero {numero}")
print(f"Pares: {pares}")
print(f"Impar {impar}")