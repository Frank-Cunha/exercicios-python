'''Foi feita uma estatística em cinco cidades brasileiras para coletar dados sobre acidentes de trânsito. Foram obtidos os seguintes dados:
a. Código da cidade;
b. Número de veículos de passeio (em 1999);
c. Número de acidentes de trânsito com vítimas (em 1999). Deseja-se saber:
d. Qual o maior e menor índice de acidentes de transito e a que cidade pertence;
e. Qual a média de veículos nas cinco cidades juntas;
f. Qual a média de acidentes de trânsito nas cidades com menos de 2.000 veículos de passeio
'''
codigo_cidades = []
veiculos_passeio = []
acidentes_transito = []
soma_veiculos = 0
soma_veiculos_menos = 0
cidades_menos = 0

for i in range(5):
    print("\nDigite o código da "+ str(i+1)+"a. cidade: ", end="")
    codigo_cidades.append(input())
    print("Digite o número de veículos de passeio da "+ str(i+1)+"a. cidade (em 1999): ", end="")
    veiculos_passeio.append(int(input()))
    print("Digite o número de acidentes de trânsito com vítimas da "+ str(i+1)+"a. cidade (em 1999): ", end="")
    acidentes_transito.append(int(input()))
    if veiculos_passeio[i] < 2000:
        cidades_menos += 1
        soma_veiculos_menos += acidentes_transito[i]
    soma_veiculos += veiculos_passeio[i]

media_veiculos = soma_veiculos/len(codigo_cidades)
media_acidentes_menos = soma_veiculos_menos/cidades_menos

maior_acidentes = acidentes_transito.index(max(acidentes_transito))

print("\nMaior indice de acidentes de trânsito e código da cidade: ", max(acidentes_transito)/1000, " acidentes por 1000 veículos,", codigo_cidades[maior_acidentes])
print("Média de veículos das cinco cidades juntas:", media_veiculos)
print("Média de acidentes de trânsito nas cidades com menos de 2000 veículos de passeio: ", media_acidentes_menos)





