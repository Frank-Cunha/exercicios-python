'''
Tamanho de strings. Faça um programa que leia 2 strings e informe o conteúdo delas seguido do seu comprimento. Informe também se as duas strings possuem o mesmo comprimento e são iguais ou diferentes no conteúdo.

Compara duas strings
String 1: Brasil Hexa 2006
String 2: Brasil! Hexa 2006!
Tamanho de "Brasil Hexa 2006": 16 caracteres
Tamanho de "Brasil! Hexa 2006!": 18 caracteres
As duas strings são de tamanhos diferentes.
As duas strings possuem conteúdo diferente.
'''
string1 = input("String 1: ")
string2 = input("String 2: ")

print("Tamnho de \"" + string1 +"\":", len(string1), "caracteres\nTamnho de \"" + string2 +"\":", len(string2), "caracteres")

if len(string1) == len(string2):
    print("As duas strings são de tamanhos iguais.")
elif len(string1) != len(string2):
    print("As duas strings são de tamanhos diferentes.")

if string1 == string2:
    print("As duas strings possuem conteúdo igual.")
elif string1 != string2:
    print("As duas strings possuem conteúdo diferente.")


