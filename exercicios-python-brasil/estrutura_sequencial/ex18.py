tamanho_arquivo = float(input("Digite o tamanho em MB do arquivo: "))
velocidade_internet = float(input("Digite a velocidade da internet em Mbps: "))
tempo_downl = tamanho_arquivo/(velocidade_internet/8) 

print("Tempo aproximado do download: ", tempo_downl, "segundos")