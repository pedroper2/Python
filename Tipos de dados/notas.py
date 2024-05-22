import os
os.system ("cls||clear")
nome=str(input ("Digite o nome do aluno "))
idade=int(input ("Digite a idade "))
nota=int(input ("Digite a primeira nota "))
nota2=int(input ("Digite a segunda nota "))
soma= nota+nota2
media = soma / 2
os.system ("cls||clear")
print (f"{nome}")
print (f"{idade} anos")
print (f"A primeira nota: {nota}")
print (f"A segunda nota: {nota2}")
print(f"A media:{media}")