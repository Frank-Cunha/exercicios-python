'''
Nome na vertical em escada invertida. Altere o programa anterior de modo que a escada seja invertida.

FULANO
FULAN
FULA
FUL
FU
F
'''

nome = input("Digite seu nome: ")
print()

cont = 0
for i in nome:
    print(nome[:len(nome)-cont])
    cont +=1