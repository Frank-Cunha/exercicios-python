from bola import Bola

bola_1 = Bola("azul", 68, "couro")

print("bola 1\n")
print("Cor: ", bola_1.cor)
print("Circunferência: ", bola_1.circunferencia)
print("Material: ", bola_1.material)

bola_1.trocaCor("verde")
bola_1.mostraCor()