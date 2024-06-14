import os
from dataclasses import dataclass
os.system("cls||clear")
def cab ():
    os.system("cls||clear")
QUANTIDADE_ALUNO=2
@dataclass
class Aluno:
    nome: str
    idade: int
    peso: int 
#alunos= []
#for i in range(QUANTIDADE_ALUNO):
 #   nome_do_aluno= input ("Digite seu nome: ")
  #  idade_do_aluno= int (input ("Digite sua idade: "))
   # peso_do_aluno= int (input ("digite o peso"))
   #Aluno=(nome= nome_do_aluno,idade=idade_do_aluno,peso=peso_do_aluno)
   #alunos.append(aluno)

#ou

alunos= []
for i in range(QUANTIDADE_ALUNO):
    aluno = Aluno (

        nome= input ("Digite seu nome: "),
        idade= int (input ("Digite sua idade: ")),
        peso= int (input ("digite o peso"))
    )
    alunos.append(aluno)
cab()
for i in alunos:
    print(f"Nome: {i.nome}")
    print(f"Idade: {i.idade}")
    print(f"Peso: {i.peso}")

