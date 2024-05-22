import os
os.system ("cls || clear")
#criando um vetore
notas = []
for i in range (3):
    nota = int (input ("Digite uma nota: "))
    notas.append (nota)

for i in range(3):
    print(f"Nota: {notas [i]}")
