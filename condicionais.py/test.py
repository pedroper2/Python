import os
os.system ("clear||cls")
nome = str (input (" Digite seu nome "))
notaUm= float (input ("Digite a primeira nota "))
notaDois= float (input ("Digite a segunda nota "))
notaTres= float (input ("Digite a terceira nota "))
soma = notaUm + notaDois + notaTres
media = soma /3
print (f"{nome}")
if media >= 7:
    print ("Aprovado")
else : 
    print ("Reprovado")
