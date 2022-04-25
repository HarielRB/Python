# biblioteca que permite trabalhar com ips
import ipaddress


ip = '192.168.0.1'
# com a biblioteca é possivel transformar essa string em um endereço Ip e realizar operações com eles

# para printar a variavel como ip é necessario transformala com o metodo ip_address
endereco = ipaddress.ip_address(ip)
print(endereco + 256)

# para redes
ip_rede = '192.168.0.0/24'

rede = ipaddress.ip_network(ip_rede, strict=False)
print(rede)

# para imprimir todos os enderecos de uma rede
for ip_rede in rede:
    print(ip_rede)
