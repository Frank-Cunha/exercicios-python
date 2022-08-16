'''Faça um programa que simule um lançamento de dados. Lance o dado 100 vezes e armazene os resultados em um vetor . Depois, mostre quantas vezes cada valor foi conseguido. Dica: use um vetor de contadores(1-6) e uma função para gerar numeros aleatórios, simulando os lançamentos dos dados.'''
import random
dados_valores = []

for i in range(1,101):
    x = random.randint(1,6) #randint() gera aleatoriamente um número inteiro dentro de um intervalo dado
    dados_valores.append(x)

for i in range(1,6 + 1):
    print("Número de vezes que o número", i,"aparece:", dados_valores.count(i))