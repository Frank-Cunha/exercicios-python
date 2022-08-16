#Sendo H= 1 + 1/2 + 1/3 + 1/4 + ... + 1/N, Faça um programa que calcule o valor de H com N termos.

n1 = 1
n2 = 1
soma = [n1/n2]
n = int(input("Digite o valor do n: "))

print("\nH = "+ str(n1) +"/"+str(n2), end="")
while n2 <= n - 1:
    n2 += 1
    soma.append(n1/n2)
    print(" + " +str(n1)+"/"+ str(n2), end="")

print(" = %.2f"% sum(soma))
