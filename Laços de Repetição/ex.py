import os
import sys

os.system("cls || clear")

maiorIdade = 0
menorIdade = sys.maxsize
somaSalarios = 0
quantidadeSalarios = 0
mediaSalarios = 0
mulheres5k=0

while True:
    print("Código \t Descrição")
    print("1 \t Adicionar pessoa")
    print("2 \t Exibir resultados e sair")
    opcao = int(input("Digite a opção desejada: "))
   
    match(opcao):
        case 1:
            print("=== Solicitando dados ===")
            idade = int(input("Digite a idade: "))
            sexo= str (input("M/F"))  
            sexo = sexo.upper()
            while sexo != 'F' and sexo != 'M':
                print ("Digite novamente")
                sexo= str (input("M/F"))
            salario= float (input ("Digite o salario"))
            while salario < 0:
                print("Digite um salario valido")
                salario= float (input ("Digite o salario"))
            somaSalarios += salario
            if sexo == 'F' and salario > 5000:
                   mulheres5k += 1
            quantidadeSalarios+= 1
            maiorIdade = max(idade, maiorIdade)
            menorIdade = min(idade, menorIdade)

            if quantidadeSalarios != 0:
                mediaSalarios = somaSalarios / quantidadeSalarios
       
        case 2:
            print("=== Mostrando resultados ===")
            print(f"Média de salários do grupo: {mediaSalarios}")
            print(f"Maior idade do grupo: {maiorIdade}")
            print(f"Menor idade do grupo: {menorIdade}")
            print(f"Mulheres com salário a partir de 5 mil: {mulheres5k}")
            break
        case _:
            print("Opção inválida. \nTente novamente.")

      