#função tabuada
def tabuada ( n1,n2):
    resultado= n1*n2
    return resultado

numero=int(input ("Digite um numero para a tabuada "))
for i in range (1,11):
    multiplicacao= tabuada (numero,i)
    print (f"{numero} X {i}= {multiplicacao}")
