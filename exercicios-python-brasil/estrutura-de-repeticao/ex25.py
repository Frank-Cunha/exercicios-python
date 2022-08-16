#Faça um programa que peça para n pessoas a sua idade, ao final o programa devera verificar se a média de idade da turma varia entre 0 e 25,26 e 60 e maior que 60; e então, dizer se a turma é jovem, adulta ou idosa, conforme a média calculada.
resposta = "S"
idades = []
soma_idades = 0

while resposta == "S":
    idades.append(int(input("Digite a idade da pessoa: ")))
    resposta = input("Adicionar mais idades? S/N ")

for i in idades:
    soma_idades += i

media_idade = soma_idades/len(idades)

if media_idade <= 25:
    print("Média de idade da turma: ", media_idade, "\nTurma jovem")
elif media_idade <= 60:
    print("Média de idade da turma: ", media_idade, "\nTurma adulta")
elif media_idade > 60:
    print("Média de idade da turma: ", media_idade, "\nTurma idosa")
else:
    print("Erro")






