'''
Em uma eleição presidencial existem quatro candidatos. Os votos são informados por meio de código. Os códigos utilizados são:
1 , 2, 3, 4  - Votos para os respectivos candidatos 
(você deve montar a tabela ex: 1 - Jose/ 2- João/etc)
5 - Voto Nulo
6 - Voto em Branco
Faça um programa que calcule e mostre:
O total de votos para cada candidato;
O total de votos nulos;
O total de votos em branco;
A percentagem de votos nulos sobre o total de votos;
A percentagem de votos em branco sobre o total de votos. Para finalizar o conjunto de votos tem-se o valor zero.
'''

numeros_candidatos = [1, 2, 3, 4, 5, 6]
candidatos = ["Jose", "João", "Arnaldo", "Maria", "Voto Nulo", "Voto Branco"]
votos = []
cont = 0

while True:
    votos.append(int(input("Digite o número do candidato (digite 5 para Voto Nulo ou 6 para voto branco): ")))
    if votos[cont] == 0:
        votos.pop()
        break
    cont += 1
    
print("")
for i in range(len(numeros_candidatos)):
    print(candidatos[i] +":", votos.count(numeros_candidatos[candidatos.index(candidatos[i])]),"Votos")

nulos_percentagem = (votos.count(5)/len(votos))*100
brancos_percentagem = (votos.count(6)/len(votos))*100

print("\nPercentagem de votos nulos sobre o total de votos: ", int(nulos_percentagem),"%")
print("Percentagem de votos brancos sobre o total de votos: ", int(brancos_percentagem),"%")




