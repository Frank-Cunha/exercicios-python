'''O cardápio de uma lanchonete é o seguinte:
Especificação   Código  Preço
Cachorro Quente 100     R$ 1,20
Bauru Simples   101     R$ 1,30
Bauru com ovo   102     R$ 1,50
Hambúrguer      103     R$ 1,20
Cheeseburguer   104     R$ 1,30
Refrigerante    105     R$ 1,00
Faça um programa que leia o código dos itens pedidos e as quantidades desejadas. Calcule e mostre o valor a ser pago por item (preço * quantidade) e o total geral do pedido. Considere que o cliente deve informar quando o pedido deve ser encerrado.
'''
especificao = ["Cachorro Quente", "Bauru Simples", "Bauru com ovo", "Hambúrguer", "Cheeseburguer", "Refrigerante"]
codigo = ["100", "101", "102", "103", "104", "105"]
preco = [1.20, 1.30, 1.50, 1.20, 1.30, 1.00 ]
pedidos = []
quantidade = []
preco_total = 0

while True:
    pedidos.append(input("Digite o código do item que você deseja: "))
    quantidade.append(int(input("Digite a quantidade desse item: ")))

    contiuar = input("\nDeseja mais itens? S/N ")
    if contiuar != "S":
        break
print("\n")
for i in range(len(pedidos)):
    print(quantidade[i],"-", especificao[codigo.index(pedidos[i])], "         R$ {:0.2f}".format(quantidade[i]*preco[codigo.index(pedidos[i])]))

    preco_total += quantidade[i]*preco[codigo.index(pedidos[i])]
    
    
    

print("\nPreço total: R$ {:0.2f}".format(preco_total))

