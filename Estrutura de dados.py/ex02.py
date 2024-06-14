import os 
from dataclasses import dataclass
QUANTIDADE_DE_LIVROS= 2
os.system("cls||clear")
livros=[]
@dataclass
class Informacao:
    titulo:str
    autor:str
    pagina:int
    preco:float
for i in range (QUANTIDADE_DE_LIVROS):
    livro= Informacao (
    titulo= input ("Qual o titulo do livro? "),
    autor= input ("Qual o autor do livro? "),
    pagina= int (input("Quantas paginas tem o livro? ")),
    preco= int(input("Qual o valor do livro? "))
    )
    livros.append(livro)
for i in livros:
    print (f"{i.titulo}")
    print (f"{i.autor}")
    print (f"{i.pagina}")
    print (f"{i.preco}")
