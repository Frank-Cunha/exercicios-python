import re
'''
A ACME Inc., uma empresa de 500 funcionários, está tendo problemas de espaço em disco no seu servidor de arquivos. Para tentar resolver este problema, o Administrador de Rede precisa saber qual o espaço ocupado pelos usuários, e identificar os usuários com maior espaço ocupado. Através de um programa, baixado da Internet, ele conseguiu gerar o seguinte arquivo, chamado "usuarios.txt":
alexandre       456123789
anderson        1245698456
antonio         123456456
carlos          91257581
cesar           987458
rosemary        789456125
Neste arquivo, o nome do usuário possui 15 caracteres. A partir deste arquivo, você deve criar um programa que gere um relatório, chamado "relatório.txt", no seguinte formato:
ACME Inc.               Uso do espaço em disco pelos usuários
------------------------------------------------------------------------
Nr.  Usuário        Espaço utilizado     % do uso

1    alexandre       434,99 MB             16,85%
2    anderson       1187,99 MB             46,02%
3    antonio         117,73 MB              4,56%
4    carlos           87,03 MB              3,37%
5    cesar             0,94 MB              0,04%
6    rosemary        752,88 MB             29,16%

Espaço total ocupado: 2581,57 MB
Espaço médio ocupado: 430,26 MB
O arquivo de entrada deve ser lido uma única vez, e os dados armazenados em memória, caso sejam necessários, de forma a agilizar a execução do programa. A conversão da espaço ocupado em disco, de bytes para megabytes deverá ser feita através de uma função separada, que será chamada pelo programa principal. O cálculo do percentual de uso também deverá ser feito através de uma função, que será chamada pelo programa principal.
'''

usuarios = open("exercicios-python-brasil/listas/ex23/usuarios.txt", "r")

lista_nomes = []
lista_espaco = []

for linha in usuarios:
    nome = re.search(r"\D+", linha)
    lista_nomes.append(nome.group())
    espaco_ocupado = re.search(r"\d+", linha)
    lista_espaco.append(int(espaco_ocupado.group()))

relatorio = open("exercicios-python-brasil/listas/ex23/relatorio.txt", "w")

relatorio.write("ACME Inc.               Uso do espaço em disco pelos usuários\n------------------------------------------------------------------------\nNr.  Usuário        Espaço utilizado     % do uso\n")

def bytes_megabytes(b):
    mb = b/1000000
    return mb

for i in range(len(lista_nomes)):
    porcentagem = (float(lista_espaco[i])/float(sum(lista_espaco)))*100

    relatorio.write("\n"+ str(i+1)+("   ")+str(lista_nomes[i])+ str(bytes_megabytes(lista_espaco[i]))+"             "+str("%.2f"%porcentagem)+"%")

espaco_total = bytes_megabytes(sum(lista_espaco))

relatorio.write("\nEspaço total ocupado:"+ str(espaco_total) +"MB\nEspaço médio ocupado:"+ str(espaco_total/len(lista_espaco))+"MB")

relatorio = open("exercicios-python-brasil/listas/ex23/relatorio.txt", "r")
print(relatorio.read())







