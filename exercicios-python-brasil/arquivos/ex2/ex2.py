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

'''usuarios = open("exercicios-python-brasil/arquivos/ex2/usuarios.txt", "w")

usuarios.write("alexandre       456123789\nanderson        1245698456\nantonio         123456456\ncarlos          91257581\ncesar           987458\nrosemary        789456125")
'''
def byte_megabyte(bytes):
    return bytes/1000000

def percentual(bytes, espaco_tot):
    return bytes/espaco_tot*100
    

arquivo = open("exercicios-python-brasil/arquivos/ex2/usuarios.txt", "r")

conteudo = arquivo.read()
conteudo = conteudo.split()

usuarios = []
espaco_utilizado = []

cont = 0
for i in conteudo:
    if conteudo.index(i)%2 == 0:
        usuarios.append(i)
    else:
        espaco_utilizado.append(i)
    cont += 1

relatorio = open("exercicios-python-brasil/arquivos/ex2/relatorio.txt", "w")

relatorio.write("ACME Inc.               Uso do espaço em disco pelos usuários\n------------------------------------------------------------------------\nNr.  Usuário        Espaço utilizado     % do uso\n")

espaco_utilizado_int = []
for i in espaco_utilizado:
    espaco_utilizado_int.append(int(i))

espaco_total = sum(espaco_utilizado_int)
espaco_medio = espaco_total/len(usuarios)

for i in range(len(usuarios)):
    relatorio.write(usuarios[i] +"    " + str(byte_megabyte(espaco_utilizado_int[i])) +" MB    "+ str(percentual(espaco_utilizado_int[i], espaco_total))+"%\n")

relatorio.write("\nEspaço total ocupado: " + str(byte_megabyte(espaco_total)) +"\nEspaço médio ocupado: " + str(byte_megabyte(espaco_medio)))












