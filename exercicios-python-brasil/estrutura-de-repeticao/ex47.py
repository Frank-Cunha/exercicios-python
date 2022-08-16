'''
Em uma competição de ginástica, cada atleta recebe votos de sete jurados. A melhor e a pior nota são eliminadas. A sua nota fica sendo a média dos votos restantes. Você deve fazer um programa que receba o nome do ginasta e as notas dos sete jurados alcançadas pelo atleta em sua apresentação e depois informe a sua média, conforme a descrição acima informada (retirar o melhor e o pior salto e depois calcular a média com as notas restantes). As notas não são informados ordenadas. Um exemplo de saída do programa deve ser conforme o exemplo abaixo:
Atleta: Aparecido Parente
Nota: 9.9
Nota: 7.5
Nota: 9.5
Nota: 8.5
Nota: 9.0
Nota: 8.5
Nota: 9.7

Resultado final:
Atleta: Aparecido Parente
Melhor nota: 9.9
Pior nota: 7.5
Média: 9,04
'''

notas = []
resultados = []
nomes_atletas = []
cont = 0

while True:
    nomes_atletas.append(input("Atleta: "))
    if nomes_atletas[cont] == "":
        nomes_atletas.pop()
        break

    for i in range(7):
        notas.append(float(input("Nota: ")))

    melhor_nota = max(notas)
    pior_nota = min(notas)
    media_notas = (sum(notas) - (max(notas) + min(notas)))/(len(notas) - 2)

    print("\nResultado final: \nAtleta: ", nomes_atletas[cont])
    print("Melhor nota:", melhor_nota)
    print("Pior salto:", pior_nota)
    print("Média: %.2f" % media_notas)
    resultados.append(media_notas)

    notas = []
    cont += 1