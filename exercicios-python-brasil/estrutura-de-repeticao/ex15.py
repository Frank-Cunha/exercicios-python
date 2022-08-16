#A série de Fibonacci é formada pela seqüência 1,1,2,3,5,8,13,21,34,55,... Faça um programa capaz de gerar a série até o n−ésimo termo.

import time

n1 = 1
n2 = 1

while True:
    print(n1)
    print(n2)
    n1 += n2
    n2 += n1
    time.sleep(1)
