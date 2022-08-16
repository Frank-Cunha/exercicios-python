#Verificação de CPF. Desenvolva um programa que solicite a digitação de um número de CPF no formato xxx.xxx.xxx-xx e indique se é um número válido ou inválido através da validação dos dígitos verificadores e dos caracteres de formatação.

cpf = input("Insira seu CPF(formato xxx.xxx.xxx-xx): ")

try:
    cpfnum = int(cpf[:3] + cpf[4:7] + cpf[8:11] +cpf[12:14])
    if cpf[3] == "." and cpf[7] == "." and cpf[11] == "-" and len(cpfnum) == 14:
        print("CPF válido!")
    else:
        print("CPF inválido")
except:
    print("CPF inválido")