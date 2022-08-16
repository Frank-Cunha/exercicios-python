'''
Faça um Programa que leia um número inteiro menor que 1000 e imprima a quantidade de centenas, dezenas e unidades do mesmo.
Observando os termos no plural a colocação do "e", da vírgula entre outros. Exemplo:
326 = 3 centenas, 2 dezenas e 6 unidades
12 = 1 dezena e 2 unidades Testar com: 326, 300, 100, 320, 310,305, 301, 101, 311, 111, 25, 20, 10, 21, 11, 1, 7 e 16
'''
import math

numero = int(input("Digite um número inteiro menor que 1000: "))

quant_cent = math.floor(numero/100) #Função math.floor(): arredonda sempre para baixo e quando o valor é 0.5 não arredonda para o valor par mais próximo.
quant_dez = math.floor((numero - quant_cent*100)/10)
quant_unid = numero - (quant_cent*100 + quant_dez*10)

if numero >= 1000:
    print("Número inválido")
else:
    if quant_cent == 1 and quant_dez == 1 and quant_unid == 1:
        print(numero, "=", quant_cent, "centena,", quant_dez,"dezena e", quant_unid,"unidade" )

    elif quant_cent == 1 and quant_dez == 1:
        print(numero, "=", quant_cent, "centena,", quant_dez,"dezena e", quant_unid,"unidades" )
    
    elif quant_cent == 1 and quant_unid == 1:
        print(numero, "=", quant_cent, "centena,", quant_dez,"dezenas e", quant_unid,"unidade" )
    
    elif quant_dez == 1 and quant_unid == 1:
        print(numero, "=", quant_cent, "centenas,", quant_dez,"dezena e", quant_unid,"unidade" )
    
    elif quant_cent == 1:
        print(numero, "=", quant_cent, "centena,", quant_dez,"dezenas e", quant_unid,"unidades" )

    elif quant_dez == 1:
        print(numero, "=", quant_cent, "centenas,", quant_dez,"dezena e", quant_unid,"unidades" )

    elif quant_unid == 1:
        print(numero, "=", quant_cent, "centenas,", quant_dez,"dezenas e", quant_unid,"unidade" )
    else: 
        print(numero, "=", quant_cent, "centenas,", quant_dez,"dezenas e", quant_unid,"unidades" )