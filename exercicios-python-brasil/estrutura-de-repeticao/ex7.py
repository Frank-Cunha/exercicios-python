#Faça um programa que leia 5 números e informe o maior número.
maior_numero = 0
for i in range(5):
    numero = int(input("Dgite um número: "))
    if maior_numero < numero:
        maior_numero = numero

print(maior_numero)
