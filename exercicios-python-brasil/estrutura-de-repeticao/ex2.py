#Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações.

while True:
    usuario = input("Digite o nome de usuário: ")
    senha = input("Digite sua senha: ")
    if usuario == senha:
        print("[Erro] Usuário e senha iguais")
    else:
        print("Usuário e senha corretos!")
        break