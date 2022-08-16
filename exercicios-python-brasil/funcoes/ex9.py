#Reverso do número. Faça uma função que retorne o reverso de um número inteiro informado. Por exemplo: 127 -> 721.

def reverso_num(num):
    num = str(num)[::-1]
    return int(num)
    
n = int(input("Digite um número inteiro: "))

print("Reverso do número:", reverso_num(n))
