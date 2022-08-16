import random
'''
Jogo de Forca. Desenvolva um jogo da forca. O programa terá uma lista de palavras lidas de um arquivo texto e escolherá uma aleatoriamente. O jogador poderá errar 6 vezes antes de ser enforcado.

Digite uma letra: A
-> Você errou pela 1ª vez. Tente de novo!

Digite uma letra: O
A palavra é: _ _ _ _ O

Digite uma letra: E
A palavra é: _ E _ _ O

Digite uma letra: S
-> Você errou pela 2ª vez. Tente de novo!
'''
arquivo = open("exercicios-python-brasil/strings/ex11/palavras.txt")

palavras = arquivo.read()
palavras = palavras.split() #metodo split: A função split() Python, que significa divisão, é um método utilizado para dividir o conteúdo de uma string. Ela contém alguns parâmetros para auxiliar a forma de separação de seu conteúdo. O resultado dessa divisão, que na opção padrão é feita sempre que a função encontrar um caractere de espaço, é retornado no formato de uma lista com uma ou mais substrings. fonte do texto: https://blog.betrybe.com/python/python-split/

numero_palavra = random.randint(0,len(palavras))
letras_corretas = []

erros = 0
while erros < 6:
    print("")
    letra = input("Digite uma letra: ")

    if letra in palavras[numero_palavra]:
        letras_corretas.append(letra)
        for l in palavras[numero_palavra]:
            if l in letras_corretas:
                print(l, end="")
            else:
                print("_", end="")
    else:
        erros += 1
        if erros == 6:
            print("Você errou pela "+str(erros)+"ª vez. Perdeu o Jogo!")
            
        else:
            print("Você errou pela "+str(erros)+"ª vez. Tente denovo!")

    p = 0
    for i in palavras[numero_palavra]:
        if False == (i in letras_corretas):
            p += 1
    if p == 0:
        print("\nForca! Fim de Jogo")
        break







    
