# Autor: Henrique Rosa Carvalho
# Aula 06 - Tuplas e Dicionários
# Ex. 1 - Tuplas
'''
Construa um algoritmo que possua uma tupla com os números escritos por extenso de “zero” a “nove”.
Peça ao usuário para digitar um nome de 0 a 9 e retorne a ele o número por extenso,
sem usar estruturas condicionais (if e switch).
'''

num_extenso = "Zero", "Um", "Dois", "Três", "Quatro", "Cinco", "Seis", "Sete", "Oito", "Nove", "Dez"
num = int(input("Número de 0 à 9: "))
print(num_extenso[num])
