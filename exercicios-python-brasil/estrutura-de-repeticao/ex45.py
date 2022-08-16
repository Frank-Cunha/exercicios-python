'''
Desenvolver um programa para verificar a nota do aluno em uma prova com 10 questões, o programa deve perguntar ao aluno a resposta de cada questão e ao final comparar com o gabarito da prova e assim calcular o total de acertos e a nota (atribuir 1 ponto por resposta certa). Após cada aluno utilizar o sistema deve ser feita uma pergunta se outro aluno vai utilizar o sistema. Após todos os alunos terem respondido informar:
Maior e Menor Acerto;
Total de Alunos que utilizaram o sistema;
A Média das Notas da Turma.
Gabarito da Prova:

01 - A
02 - B
03 - C
04 - D
05 - E
06 - E
07 - D
08 - C
09 - B
10 - A
Após concluir isto você poderia incrementar o programa permitindo que o professor digite o gabarito da prova antes dos alunos usarem o programa.
'''

gabarito_prova = ["A", "B", "C", "D", "E", "E", "D", "C", "B", "A"]
respostas = []
alunos = []
pontos = 0
cont = 0

while True:
    for i in range(len(gabarito_prova)):
        print("Adicione a "+ str(i+1)+"a. reposta: ", end="")
        respostas.append(input())
        if respostas[i] == gabarito_prova[i]:
            pontos += 1

    alunos.append(pontos)
    
    print("\nGabarito Prova: \n")
    for item in range(len(gabarito_prova)):
        print(item+1,"-", gabarito_prova[item])

    print("\nTotal de acertos e nota: ", alunos[cont],"acertos,", alunos[cont],"pts")

    resposta = input("\nOutro aluno vai utilizar o sistema: S/N ")
    if resposta != "S":
        break
    pontos = 0
    cont += 1
    respostas = []

maior_acerto = max(alunos)
menor_acerto = min(alunos)
total_alunos = len(alunos)
media_notas = sum(alunos)/len(alunos)

print("\nMaior Acerto:", maior_acerto, "pts" "\nMenor Acerto:", menor_acerto,"pts", "\nTotal de Alunos que utilizaram o sistema:", total_alunos, "\nA Média das Notas da Turma:", media_notas,"pts")