'''
Sua organização acaba de contratar um estagiário para trabalhar no Suporte de Informática, com a intenção de fazer um levantamento nas sucatas encontradas nesta área. A primeira tarefa dele é testar todos os cerca de 200 mouses que se encontram lá, testando e anotando o estado de cada um deles, para verificar o que se pode aproveitar deles.
Foi requisitado que você desenvolva um programa para registrar este levantamento. O programa deverá receber um número indeterminado de entradas, cada uma contendo: um número de identificação do mouse o tipo de defeito:
necessita da esfera;
necessita de limpeza; a.necessita troca do cabo ou conector; a.quebrado ou inutilizado Uma identificação igual a zero encerra o programa. Ao final o programa deverá emitir o seguinte relatório:
Quantidade de mouses: 100

Situação                        Quantidade              Percentual
1- necessita da esfera                  40                     40%
2- necessita de limpeza                 30                     30%
3- necessita troca do cabo ou conector  15                     15%
4- quebrado ou inutilizado              15                     15%
'''
numero_identificacao = []
tipo_defeito = []
cont = 0

print("Tipos de defeito: \n1- necessita da esfera\n2- necessita de limpeza\n3- necessita troca do cabo ou conector\n4- quebrado ou inutilizado\n")

while True:
    numero_identificacao.append(input("Número de identificação do mouse: "))
    if numero_identificacao[cont] == "0":
        numero_identificacao.pop()
        break
    tipo_defeito.append(int(input("Digite o número do defeito: ")))
    cont += 1

print("\nQuantidade de mouses:",len(numero_identificacao),"\n")

defeitos = ["Necessita da esfera", "Necessita de limpeza", "Necessita de troca do cabo ou conector", "Quebrado ou inutilizado"]

for i in range(len(defeitos)):
    quantidade = tipo_defeito.count(i+1)
    percentual = (tipo_defeito.count(i+1)/len(numero_identificacao))*100

    print(str(i+1) +"-", defeitos[i], "     ", quantidade, "     ", percentual,"%")

