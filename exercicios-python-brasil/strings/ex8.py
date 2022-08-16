'''
Palíndromo. Um palíndromo é uma seqüência de caracteres cuja leitura é idêntica se feita da direita para esquerda ou vice−versa. Por exemplo: OSSO e OVO são palíndromos. Em textos mais complexos os espaços e pontuação são ignorados. A frase SUBI NO ONIBUS é o exemplo de uma frase palíndroma onde os espaços foram ignorados. Faça um programa que leia uma seqüência de caracteres, mostre−a e diga se é um palíndromo ou não.'''

string = input("Digite uma frase ou palavra qualquer: ")
string2 = ""

for i in string:
    if False == (i == " " or i == "." or i ==","):
        string2 += i

print("\nfrase: \""+string+"\"")

string = string2.lower()
string_invertida = string[::-1]

if string_invertida == string:
    print("A frase é um políndromo")
elif string_invertida != string:
    print("A frase não é um políndromo")