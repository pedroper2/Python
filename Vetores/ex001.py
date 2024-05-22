import os
os.system ("clear || cls")
QUANTIDADE_NOTAS = 3
notas = []
soma=0;media=0

for i in range (QUANTIDADE_NOTAS):
    nota = int (input (f"Digite a nota: "))
    soma+= nota 
    notas.append(nota)

for i in range (QUANTIDADE_NOTAS):
    print (f"Nota: { notas [i]}")

#exibindo Resultados
media = sum (notas) / QUANTIDADE_NOTAS
print (f"A média é {media}")

#ForEach / outro modo
for nota in notas:
    print(f"Nota:{notas}")


    