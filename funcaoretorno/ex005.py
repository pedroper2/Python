import os
os.system ("cls||clear")
def inflacionar (valor):
    if valor < 100:
        desconto= valor * 0.10
        resultado = valor - desconto
        return resultado
    else :
        desconto = valor * 0.20
        resultado = valor - desconto
    return resultado
produto= int (input ("Digite o valor do produto "))
real = inflacionar (produto)
print(f"Aplicado o desconto: {real} ")
