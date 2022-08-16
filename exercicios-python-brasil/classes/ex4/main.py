from pessoa import Pessoa

pessoa1 = Pessoa("André", 15, 55, 1.69)

pessoa1.envelhecer(10)

print("%.2f"% pessoa1.altura, pessoa1.idade)