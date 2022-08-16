'''
Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
"Telefonou para a vítima?"
"Esteve no local do crime?"
"Mora perto da vítima?"
"Devia para a vítima?"
"Já trabalhou com a vítima?" O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".
'''
perguntas = ["Telefonou para a vítima? S/N ", "Esteve no local do crime? S/N ", "Mora perto da vítima? S/N ", "Devia para vítima? S/N ", "Já trabalhou com a vítima? S/N "]
respostas = []
suspeitas = 0
classificacao = ["Inocente", "Suspeita", "Cúmplice", "Assassino"]

for i in range(len(perguntas)):
    print(perguntas[i], end="")
    respostas.append(input())
    if respostas[i] == "S":
        suspeitas += 1
print("")
if suspeitas > 4:
    print(classificacao[3])
elif suspeitas > 2:
    print(classificacao[2])
elif suspeitas > 1:
    print(classificacao[1])
else:
    print(classificacao[0])
