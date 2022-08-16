#Faça um programa que peça um número inteiro e determine se ele é ou não um número primo. Um número primo é aquele que é divisível somente por ele mesmo e por 1.

#Minha solução:

num = int(input("Digite um número inteiro: "))

if num%2 == 0 or num%3 == 0 or num%5 == 0 or num%7 == 0: 
    print("Não é número primo")
else:
    print("Número primo!") #Site de onde eu tirei a lógica da questão: https://www.todamateria.com.br/numeros-primos/

#Solução corrigida:

num = int(input("Digite um número inteiro: "))
fatores = []

for i in range(1, num + 1):
    if num%i == 0:
        fatores.append(i)
if len(fatores) > 2:
    print("O número não é primo")
else:
    print("O número é primo")
    
        
