'''
Jogo de Craps. Faça um programa de implemente um jogo de Craps. O jogador lança um par de dados, obtendo um valor entre 2 e 12. Se, na primeira jogada, você tirar 7 ou 11, você um "natural" e ganhou. Se você tirar 2, 3 ou 12 na primeira jogada, isto é chamado de "craps" e você perdeu. Se, na primeira jogada, você fez um 4, 5, 6, 8, 9 ou 10,este é seu "Ponto". Seu objetivo agora é continuar jogando os dados até tirar este número novamente. Você perde, no entanto, se tirar um 7 antes de tirar este Ponto novamente.
'''
import random
def craps(dados):
    if dados == 7 or dados == 11:
        print("natural! \nVocê ganhou!")
    elif dados == 2 or dados == 3 or dados ==12:
        print("craps\nVocê perdeu")
    else:
        print("Ponto")
        ponto = dados
        while True:
            print("Girando os dados novamente...")
            dados = random.randint(2,12)
            print("Valor dos dados:", dados)
            if dados == ponto:
                print("Ganhou!")
                break
            elif dados == 7:
                print("Perdeu")
                break
            
print("Girando dados...")
dados = random.randint(2,12)
print("Valor dos dados:", dados)
craps(dados)