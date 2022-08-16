'''
Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
"Telefonou para a vítima?"
"Esteve no local do crime?"
"Mora perto da vítima?"
"Devia para a vítima?"
"Já trabalhou com a vítima?" O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".
'''
suspeita = 0

telefonou = input("Você telefonou para a vítima? (S/N) ") 
if telefonou == "S":
    suspeita = suspeita + 1

local_crime = input("Você esteve no local do crime? (S/N) ")
if local_crime == "S":
    suspeita = suspeita + 1

perto = input("Você mora perto da vítima? (S/N) ")
if perto == "S":
    suspeita = suspeita + 1

devia = input("Você devia para a vítima? (S/N) ")
if devia == "S":
    suspeita = suspeita + 1

trabalhou = input("Você já trabalhou com a vítima? (S/N) ")
if trabalhou == "S":
    suspeita = suspeita + 1

if suspeita < 2:
    print("Inocente")
elif suspeita == 2:
    print("Suspeita")
elif suspeita <= 4:
    print("Cúmplice")
elif suspeita == 5:
    print("Assassino")

