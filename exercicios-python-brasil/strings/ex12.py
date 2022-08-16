'''
Valida e corrige número de telefone. Faça um programa que leia um número de telefone, e corrija o número no caso deste conter somente 7 dígitos, acrescentando o '3' na frente. O usuário pode informar o número com ou sem o traço separador.

Valida e corrige número de telefone
Telefone: 461-0133
Telefone possui 7 dígitos. Vou acrescentar o digito três na frente.
Telefone corrigido sem formatação: 34610133
Telefone corrigido com formatação: 3461-0133
'''
print("Valida e corrige número de telefone")
numero = input("Telefone: ")

if numero[0] != "3" and (len(numero) <= 8 and len(numero) >= 7):
    numero = "3"+ numero
    if numero[4] != "-":
        print("Telefone possui: "+str(len(numero)-1)+" dígitos. Vou acrescentar o digito três na frente e o \"-\" no meio.")
        print("Telefone corrigido sem formatação: "+numero)
        print("Telefone corrigido com formatação: "+ numero[:4]+"-"+numero[4:])
    elif numero[4] == "-":
        print("Telefone possui: "+str(len(numero)-2)+" dígitos. Vou acrescentar o digito três na frente.")
        print("Telefone corrigido sem formatação: "+ numero[:4]+numero[5:])
        print("Telefone corrigido com formatação: "+ numero)

elif numero[0] == "3" and (len(numero) <= 9 and len(numero) >= 8):
    if numero[4] != "-":
        print("Telefone possui: "+str(len(numero))+" dígitos. Vou acrescentar o \"-\" no meio.")
        print("Telefone sem formatação: "+numero)
        print("Telefone com formatação: "+ numero[:4]+"-"+numero[4:])
    elif numero[4] == "-":
        print("Telefone possui: "+str(len(numero)-1)+" dígitos.")
        print("Telefone sem formatação: "+ numero[:4]+numero[5:])
        print("Telefone com formatação: "+ numero)

elif numero[0] == "3" and (len(numero) <= 8 or len(numero) >= 7):
    numero = "3"+ numero
    if numero[4] != "-":
        print("Telefone possui: "+str(len(numero)-1)+" dígitos. Vou acrescentar o digito três na frente e o \"-\" no meio.")
        print("Telefone corrigido sem formatação: "+numero)
        print("Telefone corrigido com formatação: "+ numero[:4]+"-"+numero[4:])
    elif numero[4] == "-":
        print("Telefone possui: "+str(len(numero)-2)+" dígitos. Vou acrescentar o digito três na frente.")
        print("Telefone corrigido sem formatação: "+ numero[:4]+numero[5:])
        print("Telefone corrigido com formatação: "+ numero)
else:
    print("Erro, telefone inválido")

