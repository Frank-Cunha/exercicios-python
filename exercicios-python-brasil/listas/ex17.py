'''
Em uma competição de salto em distância cada atleta tem direito a cinco saltos. O resultado do atleta será determinado pela média dos cinco valores restantes. Você deve fazer um programa que receba o nome e as cinco distâncias alcançadas pelo atleta em seus saltos e depois informe o nome, os saltos e a média dos saltos. O programa deve ser encerrado quando não for informado o nome do atleta. A saída do programa deve ser conforme o exemplo abaixo:
Atleta: Rodrigo Curvêllo
 
Primeiro Salto: 6.5 m
Segundo Salto: 6.1 m
Terceiro Salto: 6.2 m
Quarto Salto: 5.4 m
Quinto Salto: 5.3 m

Resultado final:
Atleta: Rodrigo Curvêllo
Saltos: 6.5 - 6.1 - 6.2 - 5.4 - 5.3
Média dos saltos: 5.9 m
'''
nomes = []
distancias = []
diantacias_atletas = []
saltos = ["Primeiro", "Sugundo", "Terceiro", "Quarto", "Quinto"]
cont = 0

while True:
    nomes.append((input("Atleta: ")))
    if nomes[cont] == "":
        nomes.pop()
        break
    print("")
    for i in range(5):
        print(saltos[i],"Salto: ", end="")
        distancias.append(float(input()))
    
    media_distancias = sum(distancias)/len(distancias)
    diantacias_atletas.append(media_distancias)

    print("\nResultado final: \nAtleta:", nomes[cont],"\nSaltos: ", end="")
    print(*distancias, sep = ' - ') #*lst, sep = ','
    print("Média dos saltos: %.2f"% media_distancias,"m\n")   
    distancias = []
    cont += 1

