'''
Uma empresa de pesquisas precisa tabular os resultados da seguinte enquete feita a um grande quantidade de organizações:
"Qual o melhor Sistema Operacional para uso em servidores?"

As possíveis respostas são:

1- Windows Server
2- Unix
3- Linux
4- Netware
5- Mac OS
6- Outro
Você foi contratado para desenvolver um programa que leia o resultado da enquete e informe ao final o resultado da mesma. O programa deverá ler os valores até ser informado o valor 0, que encerra a entrada dos dados. Não deverão ser aceitos valores além dos válidos para o programa (0 a 6). Os valores referentes a cada uma das opções devem ser armazenados num vetor. Após os dados terem sido completamente informados, o programa deverá calcular a percentual de cada um dos concorrentes e informar o vencedor da enquete. O formato da saída foi dado pela empresa, e é o seguinte:
Sistema Operacional     Votos   %
-------------------     -----   ---
Windows Server           1500   17%
Unix                     3500   40%
Linux                    3000   34%
Netware                   500    5%
Mac OS                    150    2%
Outro                     150    2%
-------------------     -----
Total                    8800

O Sistema Operacional mais votado foi o Unix, com 3500 votos, correspondendo a 40% dos votos.
'''

possiveis_respostas = ["Windows Server   ", "Unix             ", "Linux            ", "Netware          ", "Mac OS           ", "Outro            "]
numeros_respostas = []
votos = []
cont = 0
mais_votado_votos = 0

while True:
    votos.append(int(input("Digite o número correspondente ao voto: ")))
    if votos[cont] == 0:
        votos.pop()
        break
    elif votos[cont] < 0 or votos[cont] > 6:
        votos.pop()
        print("Voto inválido")
    else:
        if False == (votos[cont] in numeros_respostas):
            numeros_respostas.append(votos[cont])
        cont +=1
    
print("\nSistema Operacional        Votos    %")    
print("-------------------        -----    ---")    
for i in range(len(numeros_respostas)):
    numero_votos = votos.count(numeros_respostas[i])
    percentual = (votos.count(numeros_respostas[i])/len(votos))*100

    print(possiveis_respostas[numeros_respostas[i] - 1],"        ", numero_votos,  "       %.2f"% percentual,"%")
    if numero_votos > mais_votado_votos:
        mais_votado_votos = numero_votos
        mais_votado = possiveis_respostas[numeros_respostas[i] - 1]

print("-----------------     ---")
print("Total                ", len(votos))
print("\nO Sistema Operacional mais votado foi o "+ mais_votado.rstrip()+", com",mais_votado_votos,"votos, correspondendo a %.2f"% (mais_votado_votos/len(votos)*100),"% dos votos.")

#str.rstrip(): Retorna uma cópia da string com os espaços em branco à direita removidos.