import sys
import os
os.system ("cls||clear")

soma= 0
quantidade=0
Maior=0
Menor= sys.maxsize
numeros= []
while True:
    numero= int (input ("Numero: "))
    if numero == 0:
        break
    quantidade+=1
    numeros.append(numero)
    soma+= numero
    Maior= max (numero,Maior)
    Menor= min (numero,Menor)

media= soma / quantidade
print(f"Menor numero: {Menor}")
print(f"Maior numero: {Maior}")
print(f"Média: {media}")




