#Altere o programa de cálculo dos números primos, informando, caso o número não seja primo, por quais número ele é divisível.


num = int(input("Digite um número inteiro: "))
fatores = []

for i in range(1, num + 1):
    if num%i == 0:
        fatores.append(i)
if len(fatores) > 2:
    print("O número não é primo")
    print("Números que o", num, "É divisível: ", fatores)
else:
    print("O número é primo")