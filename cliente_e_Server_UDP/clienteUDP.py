# importar biblioteca socket
import socket


s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print('Cliente Socket Criado com Sucesso!')

host = 'localhost'
# localhost é a rede interna da maquina

porta = 5433

mensagem = "Olá, Servidor! Suave?"

try:
    print(f'Cliente:{mensagem}')
    s.sendto(mensagem.encode(), (host, porta))
    # encode empacota a mensagem e a envia para o servidor por meio dos pacotes UDP
    dados, servidor = s.recvfrom(4096)
    dados = dados.decode()
    # desempacotar os dados
    print(f'Cliente: {dados}')
finally:
    print('Cliente: Fechando a conexão...')
    s.close()
