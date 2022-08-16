#Altere o programa anterior, intercalando 3 vetores de 10 elementos cada.

vetor_1 = []
vetor_2 = []
vetor_3 = []
vetor_4 = []

for i in range(10):
    print("Digite o "+ str(i +1) +"o. número: ", end="")
    vetor_1.append(int(input()))
print("")
for i in range(10):
    print("Digite o "+ str(i +1) +"o. número: ", end="")
    vetor_2.append(int(input()))
print("")
for i in range(10):
    print("Digite o "+ str(i +1) +"o. número: ", end="")
    vetor_3.append(int(input()))

for i in range(10):
    vetor_4.append(vetor_1[i])
    vetor_4.append(vetor_2[i])
    vetor_4.append(vetor_3[i])

print("\nQuarto vetor: "+ str(vetor_4[0]), end="")

for i in range (1, len(vetor_4)):
    print(", "+ str(vetor_4[i]), end="")