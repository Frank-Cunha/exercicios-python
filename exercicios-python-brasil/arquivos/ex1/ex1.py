'''
Faça um programa que leia um arquivo texto contendo uma lista de endereços IP e gere um outro arquivo, contendo um relatório dos endereços IP válidos e inválidos.
O arquivo de entrada possui o seguinte formato:
200.135.80.9
192.168.1.1
8.35.67.74
257.32.4.5
85.345.1.2
1.2.3.4
9.8.234.5
192.168.0.256
O arquivo de saída possui o seguinte formato:
[Endereços válidos:]
200.135.80.9
192.168.1.1
8.35.67.74
1.2.3.4

[Endereços inválidos:]
257.32.4.5
85.345.1.2
9.8.234.5
192.168.0.256
'''
import re

def regex(pattern, string):
    capt = re.match(pattern, string)
    if bool(capt):
        return capt.group()
    else:
        return False

arquivo = open("exercicios-python-brasil/arquivos/ex1/ips.txt")

ips = arquivo.read()
ips = ips.split()

print(ips)

ip_i = []
ip_v = []

for ip in ips:
    if ip == "0.0.0.0":
        ip_v.append(ip)
    elif regex(r'\b((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)(\.|$)){4}\b', ip):
        ip_v.append(ip)
    else:
        ip_i.append(ip)

ips_v_i = open("exercicios-python-brasil/arquivos/ex1/ips_v_i.txt", "r+")

ips_v_i.write("[Endereços válidos:]\n")

for ip in ip_v:
    ips_v_i.write(ip+"\n")

ips_v_i.write("\n[Endereços inválidos:]\n")

for ip in ip_i:
    ips_v_i.write(ip+"\n")

print(ips_v_i.read())



