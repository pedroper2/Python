import os
from dataclasses import dataclass 
def cab ():
    os.system ("cls||clear")
    print("====SENAI====")
pets=[]
QUANTIDADE_DE_PETS=2
@dataclass
class Pet:
    nome:str 
    idade:int
    raca:str
    port:str
    alimentacao:str
for i in range (QUANTIDADE_DE_PETS):
    pet= Pet (
    nome= str (input ("Digite o nome do pet: ")),
    idade= int (input ("Digite a idade do pet: ")),
    raca= str (input ("Digite a raça do pet: ")),
    port= str (input ("Digite o port do pet: ")),
    alimentacao= str (input ("Qual a ração do pet? "))
    )
    pets.append(pet)
cab()
for i in pets:
    print (f"Nome: {i.nome}")
    print (f"Idade: {i.idade}")
    print (f"Raça: {i.raca}")
    print (f"Port: {i.port}")
    print (f"Alimentação: {i.alimentacao}")


        