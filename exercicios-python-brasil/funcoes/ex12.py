#Embaralha palavra. Construa uma função que receba uma string como parâmetro e devolva outra string com os carateres embaralhados. Por exemplo: se função receber a palavra python, pode retornar npthyo, ophtyn ou qualquer outra combinação possível, de forma aleatória. Padronize em sua função que todos os caracteres serão devolvidos em caixa alta ou caixa baixa, independentemente de como foram digitados.
import random
def embaralha_palavra(palavra):
    posicoes = []
    while len(posicoes) < len(palavra):
        numero = random.randint(0,(len(palavra)-1))
        if False == (numero in posicoes):
            posicoes.append(numero)
    cont = 0
    palavra_nova = ""
    while len(palavra_nova) < len(palavra):
        palavra_nova = palavra_nova + palavra[posicoes[cont]]
        cont += 1
    return palavra_nova

p = input("Digite qualquer palavra: ")

print(embaralha_palavra(p))
