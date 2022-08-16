'''
Nome na vertical em escada. Modifique o programa anterior de forma a mostrar o nome em formato de escada.

F
FU
FUL
FULA
FULAN
FULANO
'''

nome = input("Digite seu nome: ")
print()

cont = 1
for i in nome:
    print(nome[:cont])
    cont +=1