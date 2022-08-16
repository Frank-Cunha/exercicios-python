'''
Faça um programa que mostre os n termos da Série a seguir:
  S = 1/1 + 2/3 + 3/5 + 4/7 + 5/9 + ... + n/m. 
Imprima no final a soma da série.
'''

n1 = 1
n2 = 1
soma = [n1/n2]
n = int(input("Digite o valor do n: "))

print("\nS = "+ str(n1) +"/"+str(n2), end="")
while n1 <= n - 1:
    n1 += 1
    n2 += 2
    soma.append(n1/n2)
    print(" + " +str(n1)+"/"+ str(n2), end="")

print(" = %.2f"% sum(soma))


