pesoMorango= float (input ("Digite o peso de morango que deseja leva"))
pesoMaca= float (input ("Digite o peso da maça que deseja leva"))
if pesoMorango > 5:
    precoMorango = 1.20
else:
    precoMorango = 1.80
if pesoMaca > 5:
    precomaca= 1.80
else:
    precomaca = 2.00
pesototal = pesoMorango + pesoMaca
subtotal = (pesoMaca + pesoMorango) * (precomaca + precoMorango)
if pesototal > 8 or subtotal > 25:
    desconto= (subtotal / 100) *10
    valototal= subtotal - desconto
print(f"O valor total a ser pago é R$ {valototal}")




