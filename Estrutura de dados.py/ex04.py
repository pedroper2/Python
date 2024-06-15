import os 
import math
from dataclasses import dataclass
variaveis= []
@dataclass
class infomacao:
    nome:str
    peso:int
    altura:float 
    imc:int
    resultado:str
def cab():
    os.system("cls||clear")
    print ("===Senai===")
def Calculo_imc(peso,altura):
    calculo= peso /math.pow(altura,2)
    return calculo
def Resultado_imc(imc):
    if imc < 18.5:
        resultado= "muito magro"
    elif imc > 18.5:
        resultado= 'normal'
    return resultado
while True:
    nome= input ("digite o nome:  ou digite sair ").strip()
    if nome.upper() == "SAIR":
        break
    peso = int (input ("Digite o peso: "))
    altura= float(input ("Digite a altura: "))
    imc= Calculo_imc (peso,altura)
    resultado= Resultado_imc (imc)
    variavel= infomacao(
        nome= nome, 
        peso =peso ,
        altura= altura,
        imc= imc,
        resultado= resultado 
    )
    variaveis.append(variavel)
    cab()
    for i in variaveis:
        print(f"Usuario: {i+1}")
        print (f"nome: {i.nome}")
        print (f"peso: {i.peso}")
        print (f"altura: {i.altura}")
        print (f"imc: {i.imc}")
        print (f"Estado: {i.resultado}")






