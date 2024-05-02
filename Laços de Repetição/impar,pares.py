impar=0 
par=0
for i in range (1,6):
    numero= int (input ("Digite um numero: "))
    if numero % 2== 0:
        par+= 1
    else:
        impar+= 1 
print (f"numeros par: {par}")
print (f"numeros impar: {impar} ")
