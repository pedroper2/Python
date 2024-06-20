import os 
os.system("cls||clear")
pendentes = 1
def calculo_Ins(salario):
    if salario <= 1100.00:
        desconto_Ins= (salario * 7.5) / 100 
    
        
    elif salario <= 2203.48:
        desconto_Ins = (salario * 9)/100 
    
    
    elif salario <=3305.22:
        desconto_Ins = (salario * 12)/100 
      
    
    elif salario <= 6433.57:
        desconto_Ins = (salario * 14)/100
        return desconto_Ins
    else:
        desconto_Ins=  854.36
        return desconto_Ins

def imposto_Renda (salario):
    if salario >= 2259.21 and salario <= 2826.65:
        desconto_Irr= salario * 0.075
        dedudacao= pendentes * 189.59
        desconto_imposto = desconto_Irr + dedudacao
    
    elif salario <= 3751.05:
        desconto_Irr= salario * 0.015
        dedudacao= pendentes * 189.59
        desconto_imposto = desconto_Irr + dedudacao
        return desconto_imposto
    
    elif salario <= 4664.68:
        desconto_Irr= salario * 0.0225
        dedudacao = pendentes * 189.59 
        desconto_imposto = desconto_Irr + dedudacao
    
    else:
        desconto_Irr= salario * 0.275 
        dedudacao = pendentes * 189.59
        desconto_imposto= desconto_Irr + dedudacao
        return desconto_imposto
def calculo_Refeicao (refeicao):
    desconto_refeicao= refeicao * 0.20
    return desconto_refeicao
def calculo_Transporte (salario):
    if opcao_transporte == "S":
        desconto_transporte = salario * 0.06
    else:
        desconto_transporte=0
    return desconto_transporte
def calculo_Saude (pendentes):
    Valor_plano= 150
    desconto_pendente= Valor_plano * pendentes
    desconto_saude= desconto_pendente + Valor_plano
    return desconto_saude
login= input ("Digite sua matricula: ")
senha= input ("Senha: ")
salario= float (input ("Digite seu salário base: "))
refeicao= float(input ("Digite o valor do vale refeicao: "))
opcao_transporte= input ("deseja receber vale Transporte? (s/n) ")
opcao_transporte= opcao_transporte.upper()
pendentes= int (input ("Existe pessoas pendentes? quantas? "))
 
if opcao_transporte == "S":
    desconto_total=  calculo_Ins (salario) + imposto_Renda (salario) + calculo_Refeicao (refeicao) + calculo_Transporte (salario) + calculo_Saude (pendentes)
    
else:
    desconto_total= calculo_Ins (salario) + imposto_Renda (salario) + calculo_Refeicao (refeicao) + calculo_Saude (pendentes)

salario_liquido= salario - desconto_total
print (f" Salario Bruto: {salario}")
print (f" Desconto da reifeião: {calculo_Refeicao(refeicao)}")
print (f" Desconto do transpote: {calculo_Transporte (salario)}")
print (f" Desconto do plano de saude: {calculo_Saude (pendentes)}")
print (f" Desconto do INSS: {calculo_Ins (salario)}")
print (f" Desconto do IRR: {imposto_Renda (salario)}")
print (f"Seu salário liquido: {salario_liquido}")



        
        
        