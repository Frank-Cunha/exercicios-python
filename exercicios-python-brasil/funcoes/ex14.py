'''
Quadrado mágico. Um quadrado mágico é aquele dividido em linhas e colunas, com um número em cada posição e no qual a soma das linhas, colunas e diagonais é a mesma. Por exemplo, veja um quadrado mágico de lado 3, com números de 1 a 9:

8  3  4 
1  5  9
6  7  2
Elabore uma função que identifica e mostra na tela todos os quadrados mágicos com as características acima. Dica: produza todas as combinações possíveis e verifique a soma quando completar cada quadrado. Usar um vetor de 1 a 9 parece ser mais simples que usar uma matriz 3x3.
'''
import random

def quadrado_magico(numeros):
    n = []
    conjuntos_possiveis = []
    for i in range(1, len(numeros)+1):
        n.append(i)
        for i2 in range(1, len(numeros)+1):
            while i2 in n:
                i2 = random.randint(1,len(numeros)+1)
            n.append(i2)
            for i3 in range(1, len(numeros)+1):
                while i3 in n:
                    i3 = random.randint(1,len(numeros)+1)
                n.append(i3)
                for i4 in range(1, len(numeros)+1):
                    while i4 in n:
                        i4 = random.randint(1,len(numeros)+1)
                    n.append(i4)
                    for i5 in range(1, len(numeros)+1):
                        while i5 in n:
                            i5 = random.randint(1,len(numeros)+1)
                        n.append(i5)
                        for i6 in range(1, len(numeros)+1):
                            while i6 in n:
                                i6 = random.randint(1,len(numeros)+1)
                            n.append(i6)
                            for i7 in range(1, len(numeros)+1):
                                while i7 in n:
                                    i7 = random.randint(1,len(numeros)+1)
                                n.append(i7)
                                for i8 in range(1, len(numeros)+1):
                                    while i8 in n:
                                        i8 = random.randint(1,len(numeros)+1)
                                    n.append(i8)
                                    for i9 in range(1, len(numeros)+1):
                                        while i9 in n:
                                            i9 = random.randint(1,len(numeros)+1)
                                        n.append(i9)
        conjuntos_possiveis.append(n)
        n = []
    print(len(conjuntos_possiveis))       
            
            
num = "834159672"

quadrado_magico(num)
