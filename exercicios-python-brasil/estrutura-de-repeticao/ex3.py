'''
Faça um programa que leia e valide as seguintes informações:
Nome: maior que 3 caracteres;
Idade: entre 0 e 150;
Salário: maior que zero;
Sexo: 'f' ou 'm';
Estado Civil: 's', 'c', 'v', 'd';
'''

while True:
    nome = input("Digite um nome (mais de 3 caracteres): ")
    idade = int(input("Digite sua idade: "))
    salario = int(input("Digite seu salário: R$"))
    sexo = input("Sexo: F/M ")
    estado_civil = input("Estado civil: S/C/V/D ")

    if len(nome) < 3 or (idade < 0 or idade > 150) or salario < 0 or (sexo != "F" and sexo !="M") or (estado_civil != "S" and estado_civil != "C" and estado_civil != "V" and estado_civil != "D"):
        print("Algo errado, digite as informações novamente")
    else:
        print("Informações validadas!")
        break