from retangulo import Retangulo

ladoA = int(input("Informe a medida do lado A metros: "))
ladoB = int(input("informe a medida do lado B em metros: "))

local1 = Retangulo(ladoA, ladoB)

print("Rodapés de 1m de largura necessários: ", local1.calcular_perimetro())
print("pisos de 1m² necessários: ", local1.calcular_area())


