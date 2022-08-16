#Faça um Programa que leia dois vetores com 10 elementos cada. Gere um terceiro vetor de 20 elementos, cujos valores deverão ser compostos pelos elementos intercalados dos dois outros vetores.

vetor_1 = []
vetor_2 = []
vetor_3 = []

for i in range(10):
    print("Digite o "+ str(i +1) +"o. número: ", end="")
    vetor_1.append(int(input()))
print("")
for i in range(10):
    print("Digite o "+ str(i +1) +"o. número: ", end="")
    vetor_2.append(int(input()))

for i in range(10):
    vetor_3.append(vetor_1[i])
    vetor_3.append(vetor_2[i])

print("\nTerceiro vetor: "+ str(vetor_3[0]), end="")

for i in range (1, len(vetor_3)):
    print(", "+ str(vetor_3[i]), end="")


    
