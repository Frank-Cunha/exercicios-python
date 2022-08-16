#Altere o programa anterior permitindo ao usuário informar as populações e as taxas de crescimento iniciais. Valide a entrada e permita repetir a operação.

pais_a = int(input("Digite a população do pais A: "))
crescimento_pais_a = float(input("Digite a porcentagem de taxa de crescimento anual do pais A: "))
pais_b = int(input("Digite a população do pais B: "))
crescimento_pais_b = float(input("Digite a porcentagem taxa de crescimento anual do pais B: "))
anos = 0

while pais_a <= pais_b:
    pais_a = pais_a + (pais_a*(crescimento_pais_a/100))
    pais_b = pais_b + (pais_b*(crescimento_pais_b/100))
    anos = anos + 1
    
print("Serão necessários", anos, "anos para que o pais A ultrapasse a população do país B")