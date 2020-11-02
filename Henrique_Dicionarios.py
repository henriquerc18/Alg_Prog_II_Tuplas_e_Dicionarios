# Autor: Henrique Rosa Carvalho
# Aula 06 - Tuplas e Dicionários
# Ex. 2 - Dicionários
'''
Construa um algoritmo que peça ao usuário para informar o nome, a
nota01 e a nota02 de um aluno. Guarde estas informações em um
dicionário. Após, calcule a nota final deste aluno [(nota01 + nota02)/2] 
e adicione ao dicionário. Ao final, imprima todos os dados do
dicionário.
'''


notas_alunos = {}

nome = input("Nome: ")

nota01 = int(input("Nota 1: "))
nota02 = int(input("Nota 2: "))

media = (nota01 + nota02)/2

notas_alunos[nome] = [nota01, nota02, media]

print(notas_alunos)
   

    
    
    
