nome= str (input ("qual o seu nome ?"))
sexo= str (input ("qual o seu sexo ??"))
estadoCivil= str (input ("qual o seu estado civil ??"))
sexo = sexo.upper
estadoCivil = estadoCivil.upper
if sexo == 'F' and estadoCivil == 'CASADA':
    tempo= float (input ("quanto tempo de casada?"))
print  (f"nome: {nome}")
print  (f"estado civil: {estadoCivil}")
print  (f"sexo: {sexo}")
print (f"tempo de casada: {tempo} anos")

