#Número por extenso. Escreva um programa que solicite ao usuário a digitação de um número até 99 e imprima-o na tela por extenso.

unidades = ["Um", "Dois", "Três", "Quatro", "Cinco", "Seis", "Sete", "Oito", "Nove", "Dez", "Onze", "Doze", "Treze", "Quatorze", "Quinze", "Dezesseis", "Dezessete", "Dezoito", "Dezenove"]

dezenas = ["Vinte", "Trinta", "Quarenta", "Cinquenta", "Sessenta", "Setenta", "Oitenta", "Noventa"]

numero = int(input("Digite um número até 99: "))

print()
if numero < 20:
    print(unidades[numero-1])
elif numero <= 99:
    if str(numero)[1] == "0":
        numero_extenso = dezenas[int(str(numero)[0])-2]
        print(numero_extenso)
    else:
        numero_extenso = dezenas[int(str(numero)[0])-2] + " e " + unidades[int(str(numero)[1])-1]

        print(numero_extenso)
else:
    print("Erro, número inválido")
