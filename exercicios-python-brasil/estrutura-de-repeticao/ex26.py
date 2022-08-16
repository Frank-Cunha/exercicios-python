#Numa eleição existem três candidatos. Faça um programa que peça o número total de eleitores. Peça para cada eleitor votar e ao final mostrar o número de votos de cada candidato.

num_eleitores = int(input("Digite o número de total eleitores: "))
votos = []

for i in range(1, num_eleitores+1):
    print("1 - primeiro candidato\n2 - segundo candidato\n3 - terceiro candidato\nDigite o número correspondente ao voto do "+ str(i) +"o. eleitor:")
    votos.append(input())

print("\n\nVotos para o primeiro candidato: ", votos.count("1"), "\nVotos para o segundo candidato: ", votos.count("2"), "\nVotos para o terceiro candidato: ", votos.count("3"))

