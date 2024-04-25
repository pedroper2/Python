#produto= str= (input ("Digite o produto "))
quantidade= int (input ("Quantidade: "))
valor = float (input ("Valor: "))
total = quantidade * valor
if quantidade <= 5:
    desconto = total * 0.02
    resultado = total - desconto
elif quantidade > 5 or quantidade <= 10:
    desconto = total * 0.03
    resultado = total - desconto
else:
    desconto= total * 0.05
print (f"O valor total foi de {total}")
print (f"O valor total com um desconto adquirido é {resultado}")