'''
Conta espaços e vogais. Dado uma string com uma frase informada pelo usuário (incluindo espaços em branco), conte:

quantos espaços em branco existem na frase.
quantas vezes aparecem as vogais a, e, i, o, u.
'''
espaco_branco = 0
vogais_string = 0
vogais = ["a", "e", "i", "o", "u"]

string = input("Digite uma frase qualquer: ")
string = string.lower()

for i in string:
    if i == " ":
        espaco_branco +=1
    if i in vogais:
        vogais_string +=1

print("\nQuantidade de espaços em branco na frase:", espaco_branco,"\nQuantidade de vogais na frase:", vogais_string)