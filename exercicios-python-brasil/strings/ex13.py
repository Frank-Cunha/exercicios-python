#Jogo da palavra embaralhada. Desenvolva um jogo em que o usuário tenha que adivinhar uma palavra que será mostrada com as letras embaralhadas. O programa terá uma lista de palavras lidas de um arquivo texto e escolherá uma aleatoriamente. O jogador terá seis tentativas para adivinhar a palavra. Ao final a palavra deve ser mostrada na tela, informando se o usuário ganhou ou perdeu o jogo.

import random

arquivo = open("exercicios-python-brasil/strings/ex11/palavras.txt")

palavras = arquivo.read()
palavras = palavras.split()

numero_palavra = random.randint(0,len(palavras))
palavra_selecionada = palavras[numero_palavra]

numero_letras = []

while len(numero_letras) < len(palavra_selecionada):
    numero_aleatorio = random.randint(0,len(palavra_selecionada)-1)
    if (numero_aleatorio in numero_letras) == False:
        numero_letras.append(numero_aleatorio)

for i in numero_letras:
    print(palavra_selecionada[i], end="")

print("\n")

for i in range(6):
    tentativa_palavra = input("Adivinhe a palavra embaralhada: ")
    if tentativa_palavra == palavra_selecionada:
        print("Acertou!")
        break
    else:
        if i+1 == 6:
            print("Você errou pela "+ str(i+1)+"ª vez. Fim de jogo!")
        else:
            print("Você errou pela "+ str(i+1)+"ª vez. tente denovo!")



