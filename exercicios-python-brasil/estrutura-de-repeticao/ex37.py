#Uma academia deseja fazer um senso entre seus clientes para descobrir o mais alto, o mais baixo, a mais gordo e o mais magro, para isto você deve fazer um programa que pergunte a cada um dos clientes da academia seu código, sua altura e seu peso. O final da digitação de dados deve ser dada quando o usuário digitar 0 (zero) no campo código. Ao encerrar o programa também deve ser informados os códigos e valores do clente mais alto, do mais baixo, do mais gordo e do mais magro, além da média das alturas e dos pesos dos clientes

codigos = []
alturas = []
pesos = []
cont = 0
soma_alturas = 0
soma_pesos = 0

while True:
    codigos.append(input("Digite o seu código: "))
    if codigos[cont] == "0":
        break
    alturas.append(float(input("Digite sua altura em metros: ")))
    pesos.append(float(input("Digite seu peso em kg: ")))
    soma_alturas += alturas[cont]
    soma_pesos += pesos[cont]
    cont += 1

media_alturas = soma_alturas/len(alturas)
media_peso = soma_pesos/len(pesos)

cliente_alto = alturas.index(max(alturas))
cliente_baixo = alturas.index(min(alturas))
cliente_gordo = pesos.index(max(pesos))
cliente_magro = pesos.index(min(pesos))

print("\nCódigo e altura do cliente mais alto: ", codigos[cliente_alto], ", {:0.2f}".format(max(alturas)), "m")
print("Código e altura do cliente mais baixo: ", codigos[cliente_baixo], ", {:0.2f}".format(min(alturas)), "m")
print("Código e peso do cliente mais gordo: ", codigos[cliente_gordo], ", {:0.2f}".format(max(pesos)), "kg")
print("Código e peso do cliente mais magro: ", codigos[cliente_magro], ", {:0.2f}".format(min(pesos)), "kg")
print("Médias de altura e de peso dos clientes: {:0.2f}".format(media_alturas), "m, {:0.2f}".format(media_peso),"kg")

#{:0.2f}".format()

