contador=0;mediaPar=0;pares=0;impar=0;somaGeral=0;mediaPar= 0;somapar=0
import os
os.system ("clear||cls")
while True:
    numero= float (input ("Digite um numero"))
    if numero != 0:
        if numero > 0:
            contador+=1
            somaGeral+= numero
            if numero % 2 == 0:
                pares+=1
                somapar+= numero
                mediaPar= somapar/pares
            elif numero %2 != 0:
                impar+=1
    else:
         break
mediaGeral= somaGeral / contador 
print (f"Foram digitados {pares} pares e {impar} impares")
print(f"A media dos numeros pares é {mediaPar}")
print(f"A media geral dos numeros é {mediaGeral}")
